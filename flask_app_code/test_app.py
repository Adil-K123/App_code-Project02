import pytest
import os
import mysql.connector
from app import app

@pytest.fixture(scope='module')
def test_db():
    # Connect to the test database using environment variables
    db = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE'),
        autocommit=False  # Disable autocommit for transaction management
    )
    cursor = db.cursor()
    
    # Begin transaction
    cursor.execute("START TRANSACTION")

    # Yield the database connection and cursor to the test
    yield db, cursor

    # Rollback any changes made during the test
    db.rollback()
    
    # Clean up: close cursor and database connection
    cursor.close()
    db.close()

@pytest.fixture
def client():
    # Set up the Flask app in testing mode
    app.config['TESTING'] = True
    
    # Use Flask's test client for making requests
    with app.test_client() as client:
        yield client

def test_index_route(test_db, client):
    # Unpack the test_db fixture to get the database connection and cursor
    db, cursor = test_db

    try:
        # Insert test data into the database
        cursor.execute("INSERT INTO reviews (name, product_name, review) VALUES ('Test User', 'Test Product', 'Test Review')")
        db.commit()  # Commit the transaction to make the data visible to the Flask app

        # Use the Flask test client to access the route being tested
        response = client.get('/')

        # Assert that the response contains the inserted review data
        assert b'Test User' in response.data
        assert b'Test Product' in response.data
        assert b'Test Review' in response.data

    finally:
        # Clean up: delete the test data from the database, regardless of assertions pass or fail
        cursor.execute("DELETE FROM reviews WHERE name = 'Test User'")
        db.commit()  # Commit the transaction to remove the test data from the databa
