🛒 E-Market Place – Python & MySQL
A command-line based E-Market Place application built with Python and MySQL. This application provides a complete shopping experience, allowing users to sign up, log in, browse products, manage a shopping cart, and complete purchases.

✨ Features
👤 User Authentication: Secure sign-up and login system.

🛍️ Product Catalog: Browse products from categories like Fashion and Electronics.

🔍 Advanced Filtering: Filter products by price, color, brand, and rating.

🛒 Shopping Cart: Add, view, and remove items from a persistent cart.

💳 Checkout System: Purchase single items or the entire cart's contents.

🧾 Bill Generation: Generates a detailed bill in the console upon purchase.

🗃️ Relational Database: Uses MySQL to manage all application data.

🗂️ Project Structure
e-market-place/
│
├── signin_login.py         # Main entry point, handles user login/signup
├── main_menu.py            # Core application logic for shopping and cart
├── billing.py              # Classes for generating purchase bills
├── e-market_place.sql      # SQL script to set up the database schema and data
└── requirements.txt        # Python dependencies

✅ Prerequisites
Python 3.8 or newer

MySQL Server (It's recommended to use a local development server like XAMPP or WAMP)

Git for cloning the repository

🚀 Getting Started
Follow these steps to set up and run the project on your local machine.

1) Clone the Repository
git clone https://github.com/PATNI-CHIRAG/E-MARKET-PLACE_PYTHON.git
cd E-MARKET-PLACE_PYTHON

2) Set Up the Database
This project requires a MySQL database. The easiest way to set one up is with XAMPP.

Start Services: Open the XAMPP Control Panel and start the Apache and MySQL services.

Create Database: Open your browser and navigate to http://localhost/phpmyadmin/.

Click on the "Databases" tab.

Enter e-market_place as the database name and click "Create".

Import Data:

Select the e-market_place database from the left-hand sidebar.

Click on the "Import" tab.

Click "Choose File" and select the e-market_place.sql file from the project directory.

Click the "Import" button at the bottom of the page.

This will create all the necessary tables (signin, products, pending_cart) and populate them with sample data.

3) Install Dependencies
Install the required Python packages.

# Install dependencies
pip install -r requirements.txt

4) Configure the Database Connection
The Python script connects to the database using credentials specified in signin_login.py. The default configuration is set for a standard XAMPP installation with no password.

File to check: signin_login.py

# This block is inside the ShoppingApp class __init__ method
self.conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # <-- Update this if your root user has a password
    database="e-market_place"
)

If your MySQL setup has a password for the root user, you must update the password field.

5) Run the Application
Once the setup is complete, you can run the application from your terminal.

python signin_login.py

The application will start in the console, displaying the welcome screen with options to sign up or log in.

🛠️ Tech Stack
Backend Logic: Python

Database: MySQL (MariaDB via XAMPP)

Connector: mysql-connector-python

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.