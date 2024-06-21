import pytest
import os
import mysql.connector
from app import app

@pytest.fixture
def test_db():
    # Connect to the test database
    db = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),          # Use environment variable for sql host
        user=os.getenv('MYSQL_USER'),          # Use environment variable for sql username
        password=os.getenv('MYSQL_PASSWORD'),  # Use environment variable for sql password
        database=os.getenv('MYSQL_DATABASE')   # Use environment variable for database name
    )

    # Create a cursor
    cursor = db.cursor()

    # Yield the database connection and cursor to the test
    yield db, cursor

    # Teardown: close the cursor and database connection
    cursor.close()
    db.close()

def test_index_route(test_db):
    # Unpack the test_db fixture to get the database connection and cursor
    db, cursor = test_db

    # Use the database connection and cursor to interact with the database
    # For example, you can insert test data into the test database and test your Flask routes
    cursor.execute("INSERT INTO reviews (name, product_name, review) VALUES ('Test User', 'Test Product', 'Test Review')")
    db.commit()

    # Use the Flask test client to test your routes
    client = app.test_client()
    response = client.get('/')
    
    # Assert that the response contains the inserted review
    assert b'Test User' in response.data
    assert b'Test Product' in response.data
    assert b'Test Review' in response.data
