import mysql
from billing import Billing_Purchase,Billing_Cart_purchase
class Main_menu:
    def __init__(self,conn,cursor,email):
        self.conn = conn
        self.cursor = cursor
        self.email = email
        pass
# --------------------------------: main menu:-------------------------------
    def print_options(self):
        try:
            continue_running = True
            while continue_running:
                print("\n---------------------- Main Menu ----------------------")
                print("1. Shopping")
                print("2. View Cart")
                print("3. Exit")
                choice = int(input("Please select an option: "))

                if choice == 1:
                    self.shopping_menu()  
                elif choice == 2:
                    self.view_cart()
                elif choice == 3:
                    continue_running = False
                    print("\nExiting the application. Thank you for using our service!")
                else:
                    print("\nInvalid input. Please select a valid option.")
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.conn.rollback()
        except Exception as e:
            print(f"Error in print option: {e}")
            self.conn.rollback()

    
    # ----------------------------: View Cart :------------------------------
    def view_cart(self):
        try:
            # Step 1: Retrieve user_id based on the logged-in email
            self.cursor.execute("SELECT user_id FROM signin WHERE Gmail = %s", (self.email,))
            user = self.cursor.fetchone()

            if user:
                user_id = user[0]

                # Step 2: Retrieve cart details (product_id and quantity) for the user
                self.cursor.execute(
                    "SELECT p.product_id, p.product_name, p.price, pc.quantity "
                    "FROM pending_cart pc "
                    "JOIN products p ON pc.product_id = p.product_id "
                    "WHERE pc.user_id = %s", (user_id,)
                )
                cart_items = self.cursor.fetchall()

                # Step 3: Check if the cart is empty
                if len(cart_items) == 0:
                    print("\nYour cart is empty.")
                else:
                    print("\n------------------- Your Cart -------------------")
                    print("Product ID | Name | Quantity | Price | Total")
                    print("---------------------------------------------------")

                    # Display cart items
                    total_price = 0
                    for item in cart_items:
                        product_id, product_name, price, quantity = item
                        total_item_price = price * quantity
                        total_price += total_item_price
                        print(f"{product_id} | {product_name} | {quantity} | ${price} | ${total_item_price}")

                    print(f"\nTotal Price: ${total_price}")
                    
                    # Step 4: Options for the user
                    print("\n1. Purchase cart Item")
                    print("2. Remove Item from Cart")
                    print("3. Back")

                    option = input("Please select an option: ")

                    if option == '1':
                        self.purchase_cart_item(user_id)
                    elif option == '2':
                        self.remove_item_from_cart(user_id)
                        self.view_cart()
                    elif option == '3':
                        return
                    else:
                        print("\nInvalid input. Please select a valid option.")
                        self.view_cart()

            else:
                print("User not found. Please sign in first.")
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.conn.rollback()
        except Exception as e:
            print(f"Error in view_cart: {e}")
            self.conn.rollback()
    

    def purchase_cart_item(self, user_id):
        try:
            # Step 1: Retrieve cart items for the user (product_id, quantity)
            self.cursor.execute(
                "SELECT p.product_id, p.product_name, p.price, pc.quantity "
                "FROM pending_cart pc "
                "JOIN products p ON pc.product_id = p.product_id "
                "WHERE pc.user_id = %s", (user_id,)
            )
            cart_items = self.cursor.fetchall()

            if len(cart_items) == 0:
                print("\nYour cart is empty. Cannot proceed with purchase.")
                return

            total_price = 0
            billing = Billing_Cart_purchase(user_name="", contact="")

            # Step 2: Collect cart details and calculate total price
            for item in cart_items:
                product_id, product_name, price, quantity = item
                total_item_price = price * quantity
                total_price += total_item_price
                billing.add_item(product_name, price, quantity)

            # Step 3: Ask user for details to complete the purchase (only once)
            user_name = input("Enter your name: ")
            user_contact = input("Enter your 10-digit contact number: ")

            while len(user_contact) != 10 or not user_contact.isdigit():
                print("Invalid phone number. Please enter a 10-digit number.")
                user_contact = input("Enter your 10-digit contact number: ")

            # Step 4: Ask user to choose a payment method
            payment_method = self.pyment_method()

            # Set user details in billing object
            billing.user_name = user_name
            billing.contact = user_contact

            # Step 5: Generate consolidated bill for all cart items
            billing.generate_consolidated_bill(payment_method)

            # Step 6: Now, after generating the bill, delete all items from the cart
            self.cursor.execute("DELETE FROM pending_cart WHERE user_id = %s", (user_id,))
            self.conn.commit()

            print(f"\nSuccessfully removed all items from your cart.")

            # Step 7: Thank the user for the purchase
            print("\nThank you for your purchase! Your items have been purchased and removed from the cart.")

        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.conn.rollback()
        except Exception as e:
            print(f"Error in purchase_cart_item: {e}")
            self.conn.rollback()
    # ---------------------------: difine payment method :---------------------
    def pyment_method(self):
        try:
            print("\nChoose your payment method:")
            print("1. Credit Card")
            print("2. PayPal")
            print("3. Cash")
            payment_choice = input("Enter the number corresponding to your payment method: ")

            if payment_choice == "1":
                return "Credit Card"
            elif payment_choice == "2":
                return "PayPal"
            elif payment_choice == "3":
                return "Cash"
            else:
                print("Invalid choice. Defaulting to 'Cash'.")
                return "Cash"
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.conn.rollback()
        except Exception as e:
            print(f"Error in pyment_method: {e}")
            self.conn.rollback()

    # ----------------------------: Remove Item from Cart :------------------------
    def remove_item_from_cart(self, user_id):
        try:
            # Step 1: Retrieve cart items to show to the user
            self.cursor.execute(
                "SELECT p.product_id, p.product_name, pc.quantity "
                "FROM pending_cart pc "
                "JOIN products p ON pc.product_id = p.product_id "
                "WHERE pc.user_id = %s", (user_id,)
            )
            cart_items = self.cursor.fetchall()

            if len(cart_items) == 0:
                print("\nYour cart is empty. No items to remove.")
                return

            print("\n------------------- Items in Cart -------------------")
            for index, item in enumerate(cart_items):
                product_id, product_name, quantity = item
                print(f"{index + 1}. {product_name} | Quantity: {quantity} | Product ID: {product_id}")
            
            # Step 2: Ask the user to select the item to remove
            item_to_remove = int(input("\nEnter the number of the item you want to remove: "))
            
            if 1 <= item_to_remove <= len(cart_items):
                product_id = cart_items[item_to_remove - 1][0]

                # Step 3: Remove the item from the cart
                self.cursor.execute("DELETE FROM pending_cart WHERE user_id = %s AND product_id = %s", (user_id, product_id))
                self.conn.commit()

                print(f"\nSuccessfully removed the product from your cart.")
            else:
                print("Invalid option. Please try again.")
                self.remove_item_from_cart(user_id)

        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.conn.rollback()
        except Exception as e:
            print(f"Error in remove_item_from_cart: {e}")
            self.conn.rollback()

# -------------------------------: shopping menu :-----------------------
    def shopping_menu(self):
        try:
            while True:
                print("\n------------------- Shopping Menu -------------------")
                print("1. Fashion")
                print("2. Electronics")
                print("3. Back")
                choice = input("Please select an option: ")

                if choice == '1':
                    self.clothing_menu()  
                elif choice == '2':
                    self.electronic_menu()  
                elif choice == '3':
                    break
                else:
                    print("\nInvalid input. Please select a valid option.")
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.conn.rollback()
        except Exception as e:
            print(f"Error in shopping_menu: {e}")
            self.conn.rollback()
# ---------------------------:clothing deatails :---------------------
    def clothing_menu(self):
        try:
            clothing_options = {
                1: "Tshirt",
                2: "Shirt",
                3: "Jacket",
                4: "Jeans",
                5: "Sneakers"
                }
            
            print("\n------------------ Clothing Menu -------------------")
            print("1. Tshirt")
            print("2. Shirt")
            print("3. Jacket")
            print("4. Jeans")
            print("5. Sneakers")
            print("6. Back")
        
            try:
                choice = int(input("Please select an option: "))
                item = clothing_options.get(choice)

                if item:
                    query = f"product_name = '{item}'"
                    self.show_details(query)

                elif choice == 6:
                    return
                else:
                    print("\nInvalid input. Please select a number between 1 and 6.")
                    self.clothing_menu()
            except ValueError:
                print("Please enter a valid number.")
                self.clothing_menu()
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.conn.rollback()
        except Exception as e:
            print(f"Error in  clothing_menu: {e}")
            self.conn.rollback()

# --------------------------: Electronics Details :------------------------
    def electronic_menu(self):
        try:
            electronic_options = {
                1: "Mobile",
                2: "TV",
                3: "Fridge",
                4: "Speaker",
                5: "Washing Machine"
                }
            
            print("\n------------------ Electronic Menu -------------------")
            print("1. Mobile")
            print("2. TV")
            print("3. Fridge")
            print("4. Speaker")
            print("5. Washing Machine")
            print("6. Back")
        
            try:
                choice = int(input("Please select an option: "))
                item = electronic_options.get(choice)

                if item:
                    query = f"product_name = '{item}'"
                    self.show_details(query)

                elif choice == 6:
                    return
                else:
                    print("\nInvalid input. Please select a number between 1 and 6.")
                    self.electronic_menu()
            except ValueError:
                print("Please enter a valid number.")
                self.electronic_menu()
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.conn.rollback()
        except Exception as e:
            print(f"Error in electronic_menu: {e}")
            self.conn.rollback()

# -----------------------------:show details:--------------------
    def show_details(self,query):
        sql_query = f"SELECT * FROM products WHERE {query}"
        self.cursor.execute(sql_query)
        products = self.cursor.fetchall()
        
        if len(products) == 0:
            print("\nNo products found.")
            return
        else:
            print("\n------------------ Product Details ------------------")
            print("Product ID | Name | Brand | Colour | Size | Rating | Price")
            print("--------------------------------------------------------")
            
            # i = 0
            # id_map = {}
            for product in products:
                print(f"{product[0]} | {product[1]} | {product[2]} | {product[3]} | {product[4]} | {product[5]} | ${product[6]}")
                # id_map[i] = product[0]
                # i += 1
            
            print("\n1. Purchase")
            print("2. Add to cart")
            print("3. View cart")
            print("4. Filter Products")
            print("5. Back")
            
            try:
                option = int(input("Please select an option: "))
                
                if option == 1:
                    self.purchase(product[1])
                    self.show_details(query)
                elif option == 2:
                    self.add_to_cart(product[1])
                    self.show_details(query)
                elif option == 3:
                    self.view_cart()
                    self.show_details(query)
                elif option == 4:
                    query = self.filter_products(query)
                    self.show_details(query)
                elif option == 5:
                    return
                else:
                    print("\nInvalid input. Please select a number between 1 and 3.")
                    self.show_details(query)
            except ValueError:
                print("Please enter a valid number.")
                self.show_details(query)
            except mysql.connector.Error as err:
                print(f"MySQL Error: {err}")
                self.conn.rollback()
            except Exception as e:
                print(f"Error in show_details: {e}")
                self.conn.rollback()

    # ----------------------------: purchase :-------------------------
    def purchase(self,product_name):
        try:

            # Fetch product_id correctly
            self.cursor.execute("SELECT product_id FROM products WHERE product_name = %s", (product_name,))
            product = self.cursor.fetchall()

            if product:
                print(f"Available Product IDs: {[p[0] for p in product]}")

                product_id = int(input("Enter product id: "))

                # Validate product_id selection
                product_ids = [p[0] for p in product]
                if product_id in product_ids:
                    print(f"Product ID: {product_id}")
                
            
                    query = "SELECT product_name, brand, price FROM products WHERE product_id = %s"
                    self.cursor.execute(query, (product_id,))
                    item = self.cursor.fetchone()

                    if item:
                        product_name, brand, price = item  # Extracting product details
                        quantity = int(input("\nHow many items do you want: "))
                        if (quantity > 10 or quantity < 1):
                            print("Quantity must be at least 1 or at most 10 . Please try again.")
                            return

                        user_name = input("Enter your name: ")
                        user_contact = input("Enter your 10-digit contact number: ")

                        while len(user_contact) != 10 or not user_contact.isdigit():
                            print("Invalid phone number. Please enter a 10-digit number.")
                            user_contact = input("Enter your 10-digit contact number: ")

                        payment_method = self.pyment_method()

                        print("\nProduct purchase successful! Generating bill...")

                        # Pass actual product details instead of placeholder values
                        billing = Billing_Purchase(product_name, brand, price, quantity, user_name, user_contact)
                        billing.generate_bill(payment_method)
                    else:
                        print("\nProduct ID not found. Please try again.")
                        self.purchase()
                else:
                    print(f"Product ID '{product_id}' in '{product_name}' is not Available.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            self.purchase()
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.conn.rollback()
        except Exception as e:
            print(f"Error in purchase_cart_item: {e}")
            self.conn.rollback()


    # ----------------------------: Add to cart  :-------------------------------
    def add_to_cart(self, product_name):
        try:
            self.cursor.execute("SELECT user_id FROM signin WHERE Gmail = %s", (self.email,))
            user = self.cursor.fetchone()

            if user:
                user_id = user[0]
                print(f"User ID: {user_id}")

                # Fetch product_id correctly
                self.cursor.execute("SELECT product_id FROM products WHERE product_name = %s", (product_name,))
                product = self.cursor.fetchall()

                if product:
                    print(f"Available Product IDs: {[p[0] for p in product]}")

                    product_id = int(input("Enter product id: "))

                    # Validate product_id selection
                    product_ids = [p[0] for p in product]
                    if product_id in product_ids:
                        print(f"Product ID: {product_id}")

                        # Get quantity from the user
                        while True:
                            quantity = int(input("Enter quantity (must be 10 or less): "))
                            if quantity <= 10:
                                break
                            else:
                                print("Quantity must be 10 or less. Please try again.")

                        # Insert into cart
                        self.cursor.execute(
                            "INSERT INTO pending_cart (user_id, product_id, quantity) VALUES (%s, %s, %s)",
                            (user_id, product_id, quantity)
                        )
                        self.conn.commit()

                        print(f"Successfully added {quantity} of {product_name} to your cart.")
                    else:
                        print(f"Product ID '{product_id}' in '{product_name}' is  not valid.")
                else:
                    print(f"Product with name '{product_name}' not found.")
            else:
                print("User not found. Please sign up or log in first.")

        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.conn.rollback()
        except Exception as e:
            print(f"Error in add_to_cart: {e}")
            self.conn.rollback()



    # ----------------------------: Filter Products :-----------------------------
    def filter_products(self, query):
        try:
            print("\n------------------ Filter Products ------------------")
            print("1. By Price")
            print("2. By Colour")
            print("3. By Brand")
            print("4. By Rating")
            print("5. Back")
            n = input("Please select an option: ")
            if n == '1':
                start_price = int(input("Enter starting price range: "))
                end_price = int(input("Enter ending price range: "))
                query += f" AND price BETWEEN {start_price} AND {end_price+1}"
            elif n == '2':
                colour = input("Enter Colour: ")
                query += f" AND colour = '{colour}'"
            elif n == '3':
                brand = input("Enter Brand: ")
                query += f" AND brand = '{brand}'"
            elif n == '4':
                start_rating = int(input("Enter starting rating range: "))
                end_rating = int(input("Enter ending rating range: "))
                query += f" AND rating BETWEEN {start_rating} AND {end_rating+0.1}"
            elif n == '5':
                pass
            else:
                print("\nInvalid input. Please select a number between 1 and 5.")
                query = self.filter_products(query)
            return query
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.conn.rollback()
        except Exception as e:
            print(f"Error in filter_products: {e}")
            self.conn.rollback()

        