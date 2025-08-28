import random
import mysql.connector
from mysql.connector import Error

from main_menu import Main_menu

def test_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="e-market_place"
        )
        if conn.is_connected():
            print("Connection successful!")
            conn.close()
        else:
            print("Connection failed.")
    except Error as e:
        print(f"Error: {e}")

test_connection()
# -------------------: connect database :-------------------------------
class ShoppingApp:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="e-market_place"
            )
            self.cursor = self.conn.cursor()
            self.current_state = "welcome"
        except Error as e:
            print(f"Error while connecting to the database: {e}")
            exit()
# -----------------------------: Welcome Point :-----------------------------
    def welcome_point(self):
        try:
            print("= = = = = = = = = = = = Welcome to E-Market-Place = = = = = = = = = = = =")
            print("1. Sign up")
            print("2. Log in")
            print("3. Exit the Application")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.signup()
            elif choice == '2':
                self.login()
            elif choice == '3':
                print("Exiting...")
                self.conn.close()
                exit()
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
                self.welcome_point()
        except Exception as e:
            print(f"Error in welcome_point: {e}")
            self.rollback()
# -----------------------------: sign Up :---------------------------------------
    def signup(self):
        try:
            print("== // Sign Up // ==")
            print("1. Sign up using Gmail")
            print("2. Rollback")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.gmail_signup()
            elif choice == '2':
                self.rollback()
            else:
                print("Invalid input. Please enter 1 or 2.")
                self.signup()
        except Exception as e:
            print(f"Error in signup: {e}")
            self.rollback()

    def gmail_signup(self):
        try:
            name = input("Enter your Name: ")
            email = input("Enter your Gmail: ")
            password = input("Enter your Password: ")
            
            while(True):
                phonenumber = input("Enter your phone number: ")
                if len(phonenumber) == 10:
                    break
                else:
                    print("Enter 10 digit phone number!")

            if '@gmail.com' in email:
                self.cursor.execute("INSERT INTO signin (Name, Gmail, Password, Phonenumber) VALUES (%s, %s, %s, %s)", 
                                    (name, email, password, phonenumber))  
                self.conn.commit()
                print("--> Sign up Successful <--")
                self.welcome_point()
            else:
                print("Invalid Gmail address. Please use a valid Gmail address.")
                self.gmail_signup()
        except mysql.connector.Error as err:
            print(f"Error executing signup query: {err}")
            self.gmail_signup()
        except Exception as e:
            print(f"Error in gmail_signup: {e}")
            self.rollback()
# -------------------------: login :------------------------------
    def login(self):
        try:
            print("====================================================")
            print("= = = = = = = = = = = = Log in = = = = = = = = = = = =")
            print("1. Log in using Gmail")
            print("2. Rollback")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.gmail_login()
            elif choice == '2':
                self.rollback()
            else:
                print("Invalid input. Please enter 1 or 2.")
                self.login()
        except Exception as e:
            print(f"Error in login: {e}")
            self.rollback()

    def gmail_login(self):
        try:
            email = input("Enter your Gmail: ")
            password = input("Enter your Password: ")
            self.cursor.execute("SELECT * FROM signin WHERE Gmail = %s AND Password = %s", (email, password))
            user = self.cursor.fetchone()
            if user:
                print("--> Log in Successful <--")
                main_menu = Main_menu(self.conn,self.cursor,email)
                main_menu.print_options()

            else:
                print("Invalid Gmail or Password.")
                self.gmail_login()
        except mysql.connector.Error as err:
            print(f"Error executing login query: {err}")
            self.gmail_login()
        except Exception as e:
            print(f"Error in gmail_login: {e}")
            self.gmail_login()

    def rollback(self):
        try:
            print("Returning to the previous menu...")
            self.welcome_point()
        except Exception as e:
            print(f"Error in rollback: {e}")
            exit()


if __name__ == "__main__":
    try:
        app = ShoppingApp()
        app.welcome_point()
    except Exception as e:
        print(f"Error in main application: {e}")
