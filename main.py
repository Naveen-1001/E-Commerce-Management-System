import mysql.connector as mysql;

db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
command_handler=db.cursor(buffered=True)

print("Welcome to E-Commerce Database Management System")

def view_tables():
    while 1:
        print("1. Customer Details")
        print("2. Seller Details")
        print("3. Product Details")
        print("4. Cart Details")
        print("5. Order Details")
        print("6. Payment Details")
        print("back/exit")
        option=input(str("Choose 1-6/back/exit"))
        if option=="1":
            command_handler.execute("SELECT * FROM Customer")
            allCustomers=command_handler.fetchall()
            for customer in allCustomers:
                print(customer)
        elif option=="2":
            command_handler.execute("SELECT * FROM Seller")
            allSellers=command_handler.fetchall()
            for seller in allSellers:
                print(seller)
        elif option=="3":
            command_handler.execute("SELECT * FROM Product")
            allProducts=command_handler.fetchall()
            for product in allProducts:
                print(product)
        elif option=="4":
            command_handler.execute("SELECT * FROM CartItem")
            allCartItems=command_handler.fetchall()
            for cartItem in allCartItems:
                print(cartItem)
        elif option=="5":
            command_handler.execute("SELECT * FROM Orders")
            allOrders=command_handler.fetchall()
            for order in allOrders:
                print(order)
        elif option=="6":
            command_handler.execute("SELECT * FROM Payment")
            allPayments=command_handler.fetchall()
            for payment in allPayments:
                print(payment)
        elif option=="back":
            admin_menu()
        elif option=="exit":
            break
        else:
            print("Invalid Choice")

def sq1(city):
    command_handler.execute("SELECT CustomerID,Name,PhoneNumber,Email FROM Customer WHERE Address LIKE %s;",("%"+city+"%",))
    res=command_handler.fetchall()
    for x in res:
        print(x)

def sq2(sellerID,amount):
    amount=int(amount)
    command_handler.execute("UPDATE Product SET Cost=(Cost-%s*0.01*Cost) WHERE SellerID=%s;",(amount,sellerID))
    db.commit()

def sq3():
    command_handler.execute("SELECT DISTINCT PaymentType AS DifferentTypesOfPaymentsAccepted FROM Payment;")
    res=command_handler.fetchall()
    for x in res:
        print(x)

def sq4():
    command_handler.execute("SELECT DISTINCT Address FROM Seller;")
    res=command_handler.fetchall()
    for x in res:
        print(x)

def sq5():
    command_handler.execute("SELECT  * FROM Orders WHERE OrderDate > '2019-12-31';")
    res=command_handler.fetchall()
    for x in res:
        print(x)

def sq6():
    command_handler.execute("SELECT ProductType, COUNT(*) AS NumberOfProducts FROM Product GROUP BY ProductType;")
    res=command_handler.fetchall()
    for x in res:
        print(x)

def sq7(Name):
    command_handler.execute("SELECT O.OrderID,O.ProductID,O.OrderDate FROM Customer as C, Orders as O WHERE C.Name=%s and C.CustomerID=O.CustomerID;",(Name,))
    res=command_handler.fetchall()
    for x in res:
        print(x)

def sq8():
    command_handler.execute("SELECT * FROM Customer as C WHERE C.CustomerID IN(SELECT O.CustomerID From Orders AS O, CartItem as CI WHERE O.CustomerID=C.CustomerID AND C.CustomerID=CI.CustomerID);")
    res=command_handler.fetchall()
    for x in res:
        print(x)

def sq9():
    command_handler.execute("SELECT C.CustomerID, C.Name, O.OrderID, P.TotalAmount FROM Customer AS C, Orders AS O, Payment AS P WHERE O.CustomerID=C.CustomerID AND P.OrderID=O.OrderID AND P.TotalAmount=(SELECT MAX(P1.TotalAmount) FROM Payment AS P1, Orders AS O1 WHERE P1.OrderID=O1.OrderID AND O1.CustomerID=C.CustomerID);")
    res=command_handler.fetchall()
    for x in res:
        print(x)

def sq10():
    command_handler.execute("SELECT C.CustomerID, C.Name,COUNT(*) AS NoOfOrders FROM Customer C INNER JOIN Orders O ON O.CustomerID=C.CustomerID GROUP BY C.CustomerID HAVING NoOfOrders>=ALL(SELECT COUNT(*) FROM Orders GROUP BY CustomerID);")
    res=command_handler.fetchall()
    for x in res:
        print(x)

def sq11():
    command_handler.execute("SELECT * FROM Customer WHERE CustomerID!=ALL(SELECT CustomerID FROM Orders);")
    res=command_handler.fetchall()
    for x in res:
        print(x)

def sq12(sellerID):
    command_handler.execute("CALL GetSellerProducts(%s);",(sellerID,))
    res=command_handler.fetchall()
    for x in res:
        print(x)

def sq13(CustomerID):
    command_handler.execute("CALL GetCustomersCartItems(%s);",(CustomerID,))
    res=command_handler.fetchall()
    for x in res:
        print(x)

def sq14(CustomerID):
    command_handler.execute("CALL GetCustomersOrders(%s);",(CustomerID,))
    res=command_handler.fetchall()
    for x in res:
        print(x)

def sq15(ProductID):
    command_handler.execute("SELECT GetStock(%s);",(ProductID,))
    res=command_handler.fetchall()
    for x in res:
        print(x)

def sq16(ProductID):
    command_handler.execute("SELECT GetContactDetailOfSeller(%s)",(ProductID,))
    res=command_handler.fetchall()
    for x in res:
        print(x)

def specific_queries():
    print("1. Get the details of all the customers of a particular city 'Mumbai")
    print("2. To decrease the price of all products of seller with SellerID 'sid101' by 10%")
    print("3. To get the different types of payment accepted")
    print("4. To Find all the distinct locations where the various sellers are located")
    print("5. To get the details of all orders placed after 2019")
    print("6. To get the count of different types of products available along with their count")
    print("7. To get the details of orders of a particular customer with name Rajesh")
    print("8. To find customers who have placed orders as well as have items in their cart")
    print("9. To find the highest order of all customers")
    print("10. To find the customer with maximum orders placed")
    print("11. To find Customers who have not purchased anything")
    print("12. Get Sellers products of a particular seller")
    print("13. Get cart items of a particular customer")
    print("14. Customers orders")
    print("15. Find the stock of a particular product")
    print("16. Find the phone number of seller of a Product")
    option=input(str("Choose 1-30"))
    if option=="1":
        city=input(str("Enter city:- "))
        sq1(city)
    elif option=="2":
        sellerID=input(str("Enter Seller ID"))
        amount=input(str("Enter percentage amount"))
        amount=int(amount)
        sq2(sellerID,amount)
    elif option=="3":
        sq3()
    elif option=="4":
        sq4()
    elif option=="5":
        sq5()
    elif option=="6":
        sq6()
    elif option=="7":
        Name=input(str("Enter Name:- "))
        sq7(Name)
    elif option=="8":
        sq8()
    elif option=="9":
        sq9()
    elif option=="10":
        sq10()
    elif option=="11":
        sq11()
    elif option=="12":
        sellerID=input(str("Seller ID:- "))
        sq12(sellerID)
    elif option=="13":
        customerID=input(str("Customer ID:- "))
        sq13(customerID)
    elif option=="14":
        customerID=input(str("Customer ID:- "))
        sq14(customerID)
    elif option=="15":
        productID=input(str("Enter Product ID"))
        sq15(productID)
    elif option=="16":
        productID=input(str("Enter Product ID"))
        sq16(productID)
    
def admin_menu():
    print("Admin Menu:- ")
    while 1:
        print("1. Tables")
        print("2. Specific Queries")
        print("exit")
        option=input(str("Choose 1/2/exit"))
        if option=="1":
            view_tables()
        elif option=="2":
            specific_queries()
        elif option=="exit":
            break
        else:
            print("Invalid Choice")

def check_cart(Customer_ID):
    command_handler.execute("SELECT * FROM CartItem WHERE CustomerID=%s;",(Customer_ID,))
    res=command_handler.fetchall()
    for x in res:
        print(x)

def check_orders(Customer_ID):
    command_handler.execute("SELECT * FROM Orders WHERE CustomerID=%s;",(Customer_ID,))
    res=command_handler.fetchall()
    for x in res:
        print(x)

def check_payments(Customer_ID):
    command_handler.execute("SELECT * FROM Payment P, Orders O WHERE O.OrderID=P.OrderID and O.CustomerID=%s;",(Customer_ID,))
    res=command_handler.fetchall()
    for x in res:
        print(x)

def add_to_cart(Customer_ID,Product_ID, Quantity):
    command_handler.execute("CALL AddToCart(%s,%s,%s);",(Product_ID,Customer_ID,Quantity))
    db.commit()

def remove_from_cart(Product_ID, Customer_ID,Quantity):
    command_handler.execute("CALL RemoveFromCart(%s,%s,%s);",(Product_ID,Customer_ID,Quantity))
    db.commit()

def buy_product_from_cart(Customer_ID,Product_ID,PaymentType):
    command_handler.execute("CALL BuyProduct(%s,%s,%s);",(Customer_ID,Product_ID,PaymentType))

def return_item(Order_ID):
    command_handler.execute("CALL ReturnOrder(%s);",(Order_ID,))
    db.commit()

def customer_menu(Customer_ID):
    print("Customer Menu:-")
    print("1. Check Cart")
    print("2. Check Orders")
    print("3. Check Payments")
    print("4. Add to Cart")
    print("5. Remove from Cart")
    print("6. Buy Item from Cart")
    print("7. Return Item")
    print("8. Check Available Products")
    while 1:
        option=input(str("Choose 1-7/exit"))
        if option=="1":
            check_cart(Customer_ID)
        elif option=="2":
            check_orders(Customer_ID)
        elif option=="3":
            check_payments(Customer_ID)
        elif option=="4":
            product_ID=input(str("Enter Product ID- "))
            quantity=input(str("Enter Quantity:- "))
            add_to_cart(Customer_ID,product_ID,quantity)
        elif option=="5":
            product_ID=input(str("Enter Product ID- "))
            quantity=input(str("Enter Quantity:- "))
            remove_from_cart(product_ID,Customer_ID,quantity)
        elif option=="6":
            product_ID=input(str("Enter Product ID- "))
            type_of_payment=input(str("Enter payment type:- "))
            buy_product_from_cart(Customer_ID,product_ID,type_of_payment)
        elif option=="7":
            order_id=input(str("Enter order id:- "))
            return_item(order_id)
        elif option=="8":
            command_handler.execute("SELECT * FROM Product")
            allProducts=command_handler.fetchall()
            for product in allProducts:
                print(product)
        elif option=="exit":
            break
        else:
            print("Invalid option")

def seller_menu(Seller_ID):
    print("Seller Menu:-")
    print("1. View All products")
    print("2. View Orders")
    print("3. Add Product")
    print("4. Delete Product")
    while 1:
        option=input(str("Choose 1-4/exit"))
        if option=="1":
            command_handler.execute("SELECT * FROM Product WHERE SellerID=%s;",(Seller_ID,))
            res=command_handler.fetchall()
            for x in res:
                print(x)
        elif option=="2":
            command_handler.execute("SELECT O.OrderID,O.CustomerID,O.ProductID,P.ProductType,P.ProductName, P.Cost, P.Quantity from Orders O,Product P WHERE O.ProductID=P.ProductID AND P.SellerID=%s;",(Seller_ID,))
            res=command_handler.fetchall()
            for x in res:
                print(x)
        elif option=="3":
            product_type=input(str("Product Type:- "))
            product_name=input(str("Product Name:- "))
            cost=input(str("Enter Product Cost:- "))
            stock=input(str("Enter stock available:- "))
            while 1:
                product_id=input(str("Enter Product ID:- "))
                command_handler.execute("SELECT * from Product WHERE ProductID=%s",(product_id,))
                match=command_handler.fetchall()
                if len(match)==0:
                    row=(product_id,product_type, product_name,int(cost),int(stock),Seller_ID)
                    command_handler.execute("INSERT INTO Product VALUES (%s,%s,%s,%s,%s,%s);",row)
                    db.commit()
                    break
                else:
                    print("Product id already exists")
        elif option=="4":
            product_id=input(str("Product ID:- "))
            command_handler.execute("DELETE FROM Product WHERE SellerID=%s and ProductID=%s ;",(Seller_ID,product_id))
            db.commit()
        elif option=="exit":
            break
        else:
            print("Invalid Choice!")

def login_auth():
    print("Login Menu:-")
    while 1:
        print("1. Admin")
        print("2. Customer")
        print("3. Seller")
        print("back/exit")
        option=input(str("Select (1-3):- "))
        if option=="1":
            username=input(str("Enter username:- "))
            password=input(str("Enter password:- "))
            if (username, password)==("admin","admin"):
                admin_menu()
            else:
                print("Invalid username/password")
        elif option=="2":
            username=input(str("Enter username:- "))
            password=input(str("Enter password:- "))
            authenticate=(username, password)
            command_handler.execute("SELECT UserID,UserPassword,TypeOfUser FROM UserIDandPasswords WHERE UserID=%s AND UserPassword=%s and TypeOfUser='Customer';",authenticate)
            user=command_handler.fetchall()
            if len(user): 
                customer_menu(username)
            else:
                print("Invalid username/password")
        elif option=="3":
            username=input(str("Enter username:- "))
            password=input(str("Enter password:- "))
            authenticate=(username, password)
            command_handler.execute("SELECT UserID,UserPassword,TypeOfUser FROM UserIDandPasswords WHERE UserID=%s AND UserPassword=%s and TypeOfUser='Seller';",authenticate)
            user=command_handler.fetchall()
            if len(user):
                seller_menu(username)
            else:
                print("Invalid username/password")
        elif option=="back":
            main()
        elif option=="exit":
            break
        else:
            print("Invalid Choice")

def register_auth():
    print("Register Menu")
    while 1:
        print("1. Customer")
        print("2. Seller")
        print("back/exit")
        option=input(str("Select 1/2:- "))
        if option=="1":
            name=input(str("Name:- "))
            address=input(str("Address:- "))
            pincode=input(str("PinCode:- "))
            phoneNumber=input(str("Phone No.:- "))
            email=input(str("Email:- "))
            while 1: 
                username=input(str("Enter username:- "))
                command_handler.execute("SELECT * FROM UserIDandPasswords WHERE UserID=%s AND TypeOfUser='Customer'",(username,))
                match=command_handler.fetchall()
                if len(match):
                    print("username already taken. Try something else")
                else: 
                    break
            while 1:
                password=input(str("Enter password:- "))
                re_password=input(str("Confirm password:- "))
                if password!=re_password:
                    print("Passwords do not match. Try again")
                else:
                    break
            new_customer=(username,password,name,address,pincode,phoneNumber,email)
            command_handler.execute("INSERT INTO Customer VALUES (%s,%s,%s,%s,%s,%s,%s)",new_customer)
            db.commit()
            command_handler.execute("INSERT INTO UserIDandPasswords VALUES (%s,%s,'Customer')",(username, password))
            db.commit()
        elif option=="2":
            name=input(str("Name:- "))
            address=input(str("Address:- "))
            phoneNumber=input(str("Phone No.:- "))
            while 1: 
                username=input(str("Enter username:- "))
                command_handler.execute("SELECT * FROM UserIDandPasswords WHERE TypeOfUser='Seller' AND UserID=%s",(username,))
                match=command_handler.fetchall()
                if len(match):
                    print("username already taken. Try something else")
                else:
                    break
            while 1:
                password=input(str("Enter password:- "))
                re_password=input(str("Confirm password:- "))
                if password!=re_password:
                    print("Passwords do not match. Try again")
                else:
                    break
            new_seller=(username,password,name,address,phoneNumber)
            command_handler.execute("INSERT INTO Seller VALUES (%s,%s,%s,%s,%s)",new_seller)
            db.commit()
            command_handler.execute("INSERT INTO UserIDandPasswords VALUES (%s,%s,'Seller')",(username, password))
            db.commit()
        elif option=="back":
            main()
        elif option=="exit":
            break
        else:
            print("Invalid Choice")

def main():
    while 1:
        print("1. Register")
        print("2. Login")
        option=input(str("Select 1/2:- "))
        if option=="1":
            register_auth()
        elif option=="2":
            login_auth()
        elif option=="3":
            break
        else:
            print("Invalid Choice")
            
main()