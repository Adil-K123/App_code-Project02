from flask import Flask, request, render_template, redirect, url_for
import os
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host=os.getenv('MYSQL_HOST'),  # Use environment variable for host
    user=os.getenv('MYSQL_USER'),  # Use environment variable for username
    password=os.getenv('MYSQL_PASSWORD'),  # Use environment variable for password
    database=os.getenv('MYSQL_DATABASE'),  # Use environment variable for database
)

cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name'].capitalize()
        product_name = request.form['product_name'].capitalize()
        review = request.form['review']
        
        # Insert the data into the database
        cursor.execute("INSERT INTO reviews (name, product_name, review) VALUES (%s, %s, %s)", (name, product_name, review))
        db.commit()

        # Redirect to avoid form resubmission on refresh
        return redirect(url_for('index'))
    
    # Fetch all reviews from the database
    cursor.execute("SELECT name, product_name, review FROM reviews")
    reviews = cursor.fetchall()
    
    # Render the HTML template with the reviews data
    return render_template('index.html', reviews="hello")

if __name__ == '__main__':
    app.run(debug=True)
