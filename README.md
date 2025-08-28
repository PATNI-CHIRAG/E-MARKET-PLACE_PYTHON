# 🛒 E-Market Place – Python & MySQL

A **command-line based E-Market Place application** built with Python and MySQL.  
This application provides a complete shopping experience with user authentication, product browsing, cart management, and billing features.

---

## ✨ Features

- 👤 **User Authentication** – Secure sign-up and login system.  
- 🛍️ **Product Catalog** – Browse products from categories like *Fashion* and *Electronics*.  
- 🔍 **Advanced Filtering** – Filter products by **price, color, brand, and rating**.  
- 🛒 **Shopping Cart** – Add, view, and remove items from a persistent cart.  
- 💳 **Checkout System** – Purchase single items or the entire cart's contents.  
- 🧾 **Bill Generation** – Generates a detailed bill in the console upon purchase.  
- 🗃️ **Relational Database** – Uses **MySQL** to manage all application data.  

---

## 🗂️ Project Structure

```
e-market-place/
│
├── signin_login.py         # Main entry point, handles user login/signup
├── main_menu.py            # Core application logic for shopping and cart
├── billing.py              # Classes for generating purchase bills
├── e-market_place.sql      # SQL script to set up the database schema and data
└── requirements.txt        # Python dependencies
```

---

## ✅ Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)  
- [MySQL Server](https://www.apachefriends.org/) (recommended: XAMPP/WAMP)  
- [Git](https://git-scm.com/downloads)  

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine:

### 1) Clone the Repository
```bash
git clone https://github.com/PATNI-CHIRAG/E-MARKET-PLACE_PYTHON.git
cd E-MARKET-PLACE_PYTHON
```

### 2) Set Up the Database

1. Start **XAMPP Control Panel** and enable **Apache** and **MySQL**.  
2. Open [phpMyAdmin](http://localhost/phpmyadmin/).  
3. Create a new database named `e-market_place`.  
4. Import the SQL script:  
   - Select the `e-market_place` database.  
   - Go to the **Import** tab.  
   - Choose the file `e-market_place.sql` from the project folder.  
   - Click **Import**.  

This will create all required tables (`signin`, `products`, `pending_cart`) with sample data.

### 3) Install Dependencies
```bash
pip install -r requirements.txt
```

### 4) Configure the Database Connection

In `signin_login.py`, update your MySQL credentials if needed:  

```python
self.conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Update if your MySQL root user has a password
    database="e-market_place"
)
```

### 5) Run the Application
```bash
python signin_login.py
```

The console will display the welcome screen with options to **Sign Up** or **Log In**.

---

## 🛠️ Tech Stack

- **Backend Logic**: Python  
- **Database**: MySQL (MariaDB via XAMPP)  
- **Connector**: mysql-connector-python  

---

## 📦 requirements.txt

Ensure the following dependencies are installed:

```
mysql-connector-python
tabulate
colorama
```

(You can add more packages here if your project uses them.)  

---

## 🤝 Contributing

Contributions are always welcome!  

- Fork the repository  
- Create your feature branch (`git checkout -b feature-xyz`)  
- Commit your changes (`git commit -m "Add feature xyz"`)  
- Push to the branch (`git push origin feature-xyz`)  
- Open a Pull Request  

---

## 📜 License

This project is open-source and available under the **MIT License**.
