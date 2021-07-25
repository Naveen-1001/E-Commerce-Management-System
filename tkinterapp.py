import tkinter
from tkinter.font import BOLD
import mysql.connector as mysql;
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("E-Commerce Management System")
#root.geometry("640x500")
buttonFont = ("Calibri", 17)
labelFont=("Georgia", 15)

testLabel=Label(root,text="E-Commerce Management System",font=("bold",22))
testLabel.pack(expand=True,fill="both")

db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
command_handler=db.cursor(buffered=True)

def queries():
    for child in mainFrame.winfo_children():
        child.destroy()

    def sq1():
        def sq1_helper():
            Label(mainFrame,font=labelFont,text="CustomerID---Name---PhoneNumber---Email").pack(expand=True)
            command_handler.execute("SELECT CustomerID,Name,PhoneNumber,Email FROM Customer WHERE Address LIKE %s;",("%"+city.get()+"%",))
            res=command_handler.fetchall()
            for x in res:
                Label(mainFrame,font=labelFont,text=x).pack(expand=True)

        for child in mainFrame.winfo_children():
            child.destroy()
        Label(mainFrame,font=labelFont,text="City:- ").pack(expand=True)
        city=Entry(mainFrame,width=40,font=("Arial",15))
        city.pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Find",command=sq1_helper).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=queries).pack(expand=True)
        
    def sq2():
        def sq2_helper():
            db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
            command_handler=db.cursor(buffered=True)
            command_handler.execute("UPDATE Product SET Cost=(Cost-%s*0.01*Cost) WHERE SellerID=%s;",(amount.get(),sellerID.get()))
            db.commit()
            amount.delete(0,'end')
            sellerID.delete(0,'end')

        for child in mainFrame.winfo_children():
            child.destroy()
        
        Label(mainFrame,font=labelFont,text="Seller ID:- ").pack(expand=True)
        sellerID=Entry(mainFrame,width=40,font=("Arial",15))
        sellerID.pack(expand=True)
        Label(mainFrame,font=labelFont,text="Amount(in %):- ").pack(expand=True)
        amount=Entry(mainFrame,width=40,font=("Arial",15))
        amount.pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Find",command=sq2_helper).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=queries).pack(expand=True)
        
    def sq3():
        for child in mainFrame.winfo_children():
            child.destroy()
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        command_handler.execute("SELECT DISTINCT PaymentType AS DifferentTypesOfPaymentsAccepted FROM Payment;")
        res=command_handler.fetchall()
        Label(mainFrame,font=labelFont,text="Different Types Of Payments Accepted",fg="Tomato").pack(expand=True)
        for x in res:
            Label(mainFrame,font=labelFont,text=x).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=queries).pack(expand=True)

    def sq4():
        for child in mainFrame.winfo_children():
            child.destroy()
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        command_handler.execute("SELECT DISTINCT Address FROM Seller;")
        res=command_handler.fetchall()
        Label(mainFrame,font=labelFont,text="Locations",fg="Tomato").pack(expand=True)
        for x in res:
            Label(mainFrame,font=labelFont,text=x).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=queries).pack(expand=True)

    def sq5():
        for child in mainFrame.winfo_children():
            child.destroy()
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        command_handler.execute("SELECT  * FROM Orders WHERE OrderDate > '2019-12-31';")
        res=command_handler.fetchall()
        Label(mainFrame,font=labelFont,text="Order ID---Customer ID---Product ID---Order Date",fg="Tomato").pack(expand=True)
        for x in res:
            Label(mainFrame,font=labelFont,text=x).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=queries).pack(expand=True)

    def sq6():
        for child in mainFrame.winfo_children():
            child.destroy()
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        command_handler.execute("SELECT ProductType, COUNT(*) AS NumberOfProducts FROM Product GROUP BY ProductType;")
        res=command_handler.fetchall()
        Label(mainFrame,font=labelFont,text="Product Type---Number of Products",fg="Tomato").pack(expand=True)
        for x in res:
            Label(mainFrame,font=labelFont,text=x).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=queries).pack(expand=True)

    def sq7():
        def sq7_helper():
            db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
            command_handler=db.cursor(buffered=True)
            command_handler.execute("SELECT O.OrderID,O.ProductID,O.OrderDate FROM Customer as C, Orders as O WHERE C.Name=%s and C.CustomerID=O.CustomerID;",(Name.get(),))
            res=command_handler.fetchall()
            Label(mainFrame,font=labelFont,text="Order ID---Product ID---Order Date",fg="Tomato").pack(expand=True)
            for x in res:
                Label(mainFrame,font=labelFont,text=x).pack(expand=True)
        for child in mainFrame.winfo_children():
            child.destroy()
        Label(mainFrame,font=labelFont,text="Name:- ").pack(expand=True)
        Name=Entry(mainFrame,width=40,font=("Arial",15))
        Name.pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Find",command=sq7_helper).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=queries).pack(expand=True)

    def sq8():
        for child in mainFrame.winfo_children():
            child.destroy()
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        command_handler.execute("SELECT * FROM Customer as C WHERE C.CustomerID IN(SELECT O.CustomerID From Orders AS O, CartItem as CI WHERE O.CustomerID=C.CustomerID AND C.CustomerID=CI.CustomerID);")
        res=command_handler.fetchall()
        Label(mainFrame,font=labelFont,text="Customer ID---Customer Password---Name---Address---Pincode---PhoneNumber---Email",fg="Tomato").pack(expand=True)
        for x in res:
            Label(mainFrame,font=labelFont,text=x).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=queries).pack(expand=True)

    def sq9():
        for child in mainFrame.winfo_children():
            child.destroy()
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        command_handler.execute("SELECT C.CustomerID, C.Name, O.OrderID, P.TotalAmount FROM Customer AS C, Orders AS O, Payment AS P WHERE O.CustomerID=C.CustomerID AND P.OrderID=O.OrderID AND P.TotalAmount=(SELECT MAX(P1.TotalAmount) FROM Payment AS P1, Orders AS O1 WHERE P1.OrderID=O1.OrderID AND O1.CustomerID=C.CustomerID);")
        res=command_handler.fetchall()
        Label(mainFrame,font=labelFont,text="Customer ID---Name---Order ID---Total Amount",fg="Tomato").pack(expand=True)
        for x in res:
            Label(mainFrame,font=labelFont,text=x).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=queries).pack(expand=True)

    def sq10():
        for child in mainFrame.winfo_children():
            child.destroy()
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        command_handler.execute("SELECT C.CustomerID, C.Name,COUNT(*) AS NoOfOrders FROM Customer C INNER JOIN Orders O ON O.CustomerID=C.CustomerID GROUP BY C.CustomerID HAVING NoOfOrders>=ALL(SELECT COUNT(*) FROM Orders GROUP BY CustomerID);")
        res=command_handler.fetchall()
        Label(mainFrame,font=labelFont,text="Customer ID---Name---No. of Orders",fg="Tomato").pack(expand=True)
        for x in res:
            Label(mainFrame,font=labelFont,text=x).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=queries).pack(expand=True)

    def sq11():
        for child in mainFrame.winfo_children():
            child.destroy()
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        command_handler.execute("SELECT * FROM Customer WHERE CustomerID!=ALL(SELECT CustomerID FROM Orders);")
        res=command_handler.fetchall()
        Label(mainFrame,font=labelFont,text="Customer ID---Customer Password---Name---Address---Pincode---PhoneNumber---Email",fg="Tomato").pack(expand=True)
        for x in res:
            Label(mainFrame,font=labelFont,text=x).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=queries).pack(expand=True)

    def sq12():
        def sq12_helper():
            db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
            command_handler=db.cursor(buffered=True)
            command_handler.execute("CALL GetSellerProducts(%s);",(sellerID.get(),))
            Label(mainFrame,font=labelFont,text="Product ID---Product Type---Product Name---Cost---Quantity---Seller ID",fg="Tomato").pack(expand=True)
            res=command_handler.fetchall()
            for x in res:
                Label(mainFrame,font=labelFont,text=x).pack(expand=True)

        for child in mainFrame.winfo_children():
            child.destroy()
        Label(mainFrame,font=labelFont,text="Seller ID:- ").pack(expand=True)
        sellerID=Entry(mainFrame,width=40,font=("Arial",15))
        sellerID.pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Find",command=sq12_helper).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=queries).pack(expand=True)     

    def sq13():
        def sq13_helper():
            db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
            command_handler=db.cursor(buffered=True)
            command_handler.execute("CALL GetCustomersCartItems(%s);",(CustomerID.get(),))
            res=command_handler.fetchall()
            Label(mainFrame,font=labelFont,text="Customer ID---Product ID---Quantity---Total Amount",fg="Tomato").pack(expand=True)
            for x in res:
                Label(mainFrame,font=labelFont,text=x).pack(expand=True)

        for child in mainFrame.winfo_children():
            child.destroy()
        Label(mainFrame,font=labelFont,text="Customer ID:- ").pack(expand=True)
        CustomerID=Entry(mainFrame,width=40,font=("Arial",15))
        CustomerID.pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Find",command=sq13_helper).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=queries).pack(expand=True)     

    def sq14():
        def sq14_helper():
            db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
            command_handler=db.cursor(buffered=True)
            command_handler.execute("CALL GetCustomersOrders(%s);",(CustomerID.get(),))
            res=command_handler.fetchall()
            Label(mainFrame,font=labelFont,text="Order ID---Product ID---Order Date",fg="Tomato").pack(expand=True)
            for x in res:
                Label(mainFrame,font=labelFont,text=x).pack(expand=True)

        for child in mainFrame.winfo_children():
            child.destroy()
        Label(mainFrame,font=labelFont,text="Customer ID:- ").pack(expand=True)
        CustomerID=Entry(mainFrame,width=40,font=("Arial",15))
        CustomerID.pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Find",command=sq14_helper).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=queries).pack(expand=True)     

    def sq15():
        def sq15_helper():
            db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
            command_handler=db.cursor(buffered=True)
            command_handler.execute("SELECT GetStock(%s);",(ProductID.get(),))
            res=command_handler.fetchall()
            Label(mainFrame,font=labelFont,text="Stock",fg="Tomato").pack(expand=True)
            for x in res:
                Label(mainFrame,font=labelFont,text=x).pack(expand=True)

        for child in mainFrame.winfo_children():
            child.destroy()
        Label(mainFrame,font=labelFont,text="Product ID:- ").pack(expand=True)
        ProductID=Entry(mainFrame,width=40,font=("Arial",15))
        ProductID.pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Find",command=sq15_helper).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=queries).pack(expand=True)

    def sq16():
        def sq16_helper():
            db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
            command_handler=db.cursor(buffered=True)
            Label(mainFrame,font=labelFont,text="Phone Number",fg="Tomato").pack(expand=True)
            command_handler.execute("SELECT GetContactDetailOfSeller(%s)",(ProductID.get(),))
            res=command_handler.fetchall()
            for x in res:
                Label(mainFrame,font=labelFont,text=x).pack(expand=True)

        for child in mainFrame.winfo_children():
            child.destroy()
        Label(mainFrame,font=labelFont,text="Product ID:- ").pack(expand=True)
        ProductID=Entry(mainFrame,width=40,font=("Arial",15))
        ProductID.pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Find",command=sq16_helper).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=queries).pack(expand=True)

    Button(mainFrame,font=buttonFont,text="Get the details of all the customers of a particular city",command=sq1).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Decrease the price of all products of a seller by a certain amount",command=sq2).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Get the different types of payment accepted",command=sq3).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Find all the distinct locations where the various sellers are located",command=sq4).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Get the details of all orders placed after 2019",command=sq5).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Get the count of different types of products available along with their count",command=sq6).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Get the details of orders of a particular customer",command=sq7).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Find customers who have placed orders as well as have items in their cart",command=sq8).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Find the highest order of all customers",command=sq9).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Find the customer with maximum orders placed",command=sq10).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Find Customers who have not purchased anything",command=sq11).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Get Sellers products of a particular seller",command=sq12).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Get cart items of a particular customer",command=sq13).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Customers orders",command=sq14).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Find the stock of a particular product",command=sq15).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Find the phone number of seller of a Product",command=sq16).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Back",command=admin_menu).pack(expand=True)

def view_tables():
    for child in mainFrame.winfo_children():
        child.destroy()
    def customer_details():
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        for child in mainFrame.winfo_children():
            child.destroy()
        command_handler.execute("SELECT * FROM Customer")
        allCustomers=command_handler.fetchall()
        Label(mainFrame,font=labelFont,text="Customer ID---Customer Password---Name---Address---Pincode---PhoneNumber---Email",fg="Tomato").pack(expand=True)
        for customer in allCustomers:
            Label(mainFrame,font=labelFont,text=customer).pack(expand=True)
        Button(mainFrame,font=buttonFont, text="Back",command=view_tables).pack(expand=True)
        
    def seller_details():
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        for child in mainFrame.winfo_children():
            child.destroy()
        command_handler.execute("SELECT * FROM Seller")
        Label(mainFrame,font=labelFont,text="Seller ID---Seller Password---Name---Address---Phone Number",fg="Tomato").pack(expand=True)
        allSellers=command_handler.fetchall()
        for seller in allSellers:
            Label(mainFrame,font=labelFont,text=seller).pack(expand=True)
        Button(mainFrame,font=buttonFont, text="Back",command=view_tables).pack(expand=True)
    
    def product_details():
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        for child in mainFrame.winfo_children():
            child.destroy()
        command_handler.execute("SELECT * FROM Product")
        Label(mainFrame,font=labelFont,text="Product ID---Product Type---Product Name---Cost---Quantity---Seller ID",fg="Tomato").pack(expand=True)
        allProducts=command_handler.fetchall()
        for product in allProducts:
            Label(mainFrame,font=labelFont,text=product).pack(expand=True)
        Button(mainFrame,font=buttonFont, text="Back",command=view_tables).pack(expand=True)
    

    def cart_details():
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        for child in mainFrame.winfo_children():
            child.destroy()
        command_handler.execute("SELECT * FROM CartItem")
        Label(mainFrame,font=labelFont,text="Customer ID---Product ID---Quantity---Total Amount",fg="Tomato").pack(expand=True)
        allCartItems=command_handler.fetchall()
        for cartItem in allCartItems:
            Label(mainFrame,font=labelFont,text=cartItem).pack(expand=True)
        Button(mainFrame,font=buttonFont, text="Back",command=view_tables).pack(expand=True)

    def order_details():
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        for child in mainFrame.winfo_children():
            child.destroy()
        command_handler.execute("SELECT * FROM Orders")
        Label(mainFrame,font=labelFont,text="Order ID---Customer ID---Product ID---Order Date",fg="Tomato").pack(expand=True)
        allOrders=command_handler.fetchall()
        for order in allOrders:
            Label(mainFrame,font=labelFont,text=order).pack(expand=True)
        Button(mainFrame,font=buttonFont, text="Back",command=view_tables).pack(expand=True)

    def payment_details():
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        for child in mainFrame.winfo_children():
            child.destroy()
        command_handler.execute("SELECT * FROM Payment")
        Label(mainFrame,font=labelFont,text="Payment ID---Payment Type---Total Amount",fg="Tomato").pack(expand=True)
        allPayments=command_handler.fetchall()
        for payment in allPayments:
            Label(mainFrame,font=labelFont,text=payment).pack(expand=True)
        Button(mainFrame,font=buttonFont, text="Back",command=view_tables).pack(expand=True)

    Label(mainFrame,font=labelFont,text="All Entity Details")
    Button(mainFrame,font=buttonFont,text="Customer Details",command=customer_details).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Seller Details",command=seller_details).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Product Details",command=product_details).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Cart Details",command=cart_details).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Order Details",command=order_details).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Payment Details",command=payment_details).pack(expand=True)
    Button(mainFrame,font=buttonFont, text="Back",command=admin_menu).pack(expand=True)
    
def admin_menu():
    for child in mainFrame.winfo_children():
        child.destroy()
    Label(mainFrame,font=labelFont,text="Admin Menu:- ").pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Tables",command=view_tables).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Queries",command=queries).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Back",command=login_auth).pack(expand=True)

def seller_menu(Seller_ID):
    db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
    db.cursor(buffered=True)
    for child in mainFrame.winfo_children():
        child.destroy()
    
    def back_helper():
        seller_menu(Seller_ID)

    def view_products():
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        for child in mainFrame.winfo_children():
            child.destroy()
        command_handler.execute("SELECT * FROM Product WHERE SellerID=%s;",(Seller_ID,))
        res=command_handler.fetchall()
        Label(mainFrame,font=labelFont,text="Product ID---Product Type---Product Name---Cost---Quantity---Seller ID",fg="Tomato").pack(expand=True)
        for x in res:
            Label(mainFrame,font=labelFont,text=x).pack(expand=True)  
        Button(mainFrame,font=buttonFont,text="Back",command=back_helper).pack(expand=True)      
    
    def view_orders():
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        for child in mainFrame.winfo_children():
            child.destroy()
        command_handler.execute("SELECT O.OrderID,O.CustomerID,O.ProductID,P.ProductType,P.ProductName, P.Cost, P.Quantity from Orders O,Product P WHERE O.ProductID=P.ProductID AND P.SellerID=%s;",(Seller_ID,))
        res=command_handler.fetchall()
        Label(mainFrame,font=labelFont,text="Order ID---Customer ID---Product ID---Product Type---Product Name---Cost---Quantity",fg="Tomato").pack(expand=True)
        for x in res:
            Label(mainFrame,font=labelFont,text=x).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=back_helper).pack(expand=True)
    
    def add_product():
        for child in mainFrame.winfo_children():
            child.destroy()
        def validate_product():
            db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
            command_handler=db.cursor(buffered=True)
            command_handler.execute("SELECT * from Product WHERE ProductID=%s",(product_id.get(),))
            match=command_handler.fetchall()
            if len(match)==0:
                row=(product_id.get(),product_type.get(), product_name.get(),int(cost.get()),int(stock.get()),Seller_ID)
                command_handler.execute("INSERT INTO Product VALUES (%s,%s,%s,%s,%s,%s);",row)
                db.commit()
                messagebox.showinfo(message="Product Added to Database!")
                product_id.delete(0,'end')
                product_name.delete(0,'end')
                product_type.delete(0,'end')
                cost.delete(0,'end')
                stock.delete(0,'end')
            else:
                messagebox.showerror(message="Product Id already exists!")
                product_id.delete(0,'end')

        for child in mainFrame.winfo_children():
            child.destroy()
        Label(mainFrame,font=labelFont,text="Product Type:- ").pack(expand=True)
        product_type=Entry(mainFrame,width=40,font=("Arial",15))
        product_type.pack(expand=True)
        Label(mainFrame,font=labelFont,text="Product Name:- ").pack(expand=True)
        product_name=Entry(mainFrame,width=40,font=("Arial",15))
        product_name.pack(expand=True)
        Label(mainFrame,font=labelFont,text="Product Cost:- ").pack(expand=True)
        cost=Entry(mainFrame,width=40,font=("Arial",15))
        cost.pack(expand=True)
        Label(mainFrame,font=labelFont,text="Product Stock:- ").pack(expand=True)
        stock=Entry(mainFrame,width=40,font=("Arial",15))
        stock.pack(expand=True)
        Label(mainFrame,font=labelFont,text="Product Id:- ").pack(expand=True)
        product_id=Entry(mainFrame,width=40,font=("Arial",15))
        product_id.pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Submit",bg='MediumSeaGreen',command=validate_product).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=login_auth).pack(expand=True)

    def delete_product():
        for child in mainFrame.winfo_children():
            child.destroy()
        def delete_product_helper():
            db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
            command_handler=db.cursor(buffered=True)
            command_handler.execute("DELETE FROM Product WHERE SellerID=%s and ProductID=%s ;",(Seller_ID,product_id.get()))
            db.commit()
            messagebox.showinfo(message="Product deleted successfully!")
            product_id.delete(0,'end')
        
        Label(mainFrame,font=labelFont,text="Product Id:- ").pack(expand=True)
        product_id=Entry(mainFrame,width=40,font=("Arial",15))
        product_id.pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Submit",bg='MediumSeaGreen',command=delete_product_helper).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=back_helper).pack(expand=True)

    Label(mainFrame,font=labelFont,text="Seller Menu:-").pack(expand=True)
    Button(mainFrame,font=buttonFont,text="View Products",command=view_products).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="View Orders",command=view_orders).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Add Product",command=add_product).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Delete Product",command=delete_product).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Back",command=back_helper).pack(expand=True)


def customer_menu(Customer_ID):
    db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
    db.cursor(buffered=True)
    for child in mainFrame.winfo_children():
        child.destroy()
    
    def back_helper():
        customer_menu(Customer_ID)
    
    def check_cart():
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        command_handler.execute("SELECT * FROM CartItem WHERE CustomerID=%s;",(Customer_ID,))
        res=command_handler.fetchall()
        for child in mainFrame.winfo_children():
            child.destroy()
        Label(mainFrame,font=labelFont,text="Customer ID---Product ID---Quantity---Total Amount",fg="Tomato").pack(expand=True)
        for x in res:
            Label(mainFrame,font=labelFont,text=x).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=back_helper).pack(expand=True)

    def check_orders():
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        command_handler.execute("SELECT * FROM Orders WHERE CustomerID=%s;",(Customer_ID,))
        res=command_handler.fetchall()
        for child in mainFrame.winfo_children():
            child.destroy()
        Label(mainFrame,font=labelFont,text="Order ID---Customer ID---Product ID---Order Date",fg="Tomato").pack(expand=True)
        for x in res:
            Label(mainFrame,font=labelFont,text=x).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=back_helper).pack(expand=True)

    def check_payments():
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        command_handler.execute("SELECT * FROM Payment P, Orders O WHERE O.OrderID=P.OrderID and O.CustomerID=%s;",(Customer_ID,))
        res=command_handler.fetchall()
        for child in mainFrame.winfo_children():
            child.destroy()
        Label(mainFrame,font=labelFont,text="Payment ID---Payment Type---Total Amount",fg="Tomato").pack(expand=True)
        for x in res:
            Label(mainFrame,font=labelFont,text=x).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=back_helper).pack(expand=True)

    def add_to_cart():
        for child in mainFrame.winfo_children():
            child.destroy()
        def add_to_cart_helper():
            db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
            command_handler=db.cursor(buffered=True)
            command_handler.execute("CALL AddToCart(%s,%s,%s);",(Product_ID.get(),Customer_ID,Quantity.get()))
            Product_ID.delete(0,'end')
            Quantity.delete(0,'end')
            db.commit()
            messagebox.showinfo(message="Product added to Cart!")

        Label(mainFrame,font=labelFont,text="Enter Product_ID:- ").pack(expand=True)
        Product_ID=Entry(mainFrame,width=40,font=("Arial",15))
        Product_ID.pack(expand=True)
        Label(mainFrame,font=labelFont,text="Enter Quantity:- ").pack(expand=True)
        Quantity=Entry(mainFrame,width=40,font=("Arial",15))
        Quantity.pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Submit",bg='MediumSeaGreen',command=add_to_cart_helper).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=back_helper).pack(expand=True)

    def remove_from_cart():
        for child in mainFrame.winfo_children():
            child.destroy()
        def remove_from_cart_helper():
            db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
            command_handler=db.cursor(buffered=True)
            command_handler.execute("CALL RemoveFromCart(%s,%s,%s);",(Product_ID.get(),Customer_ID,Quantity.get()))
            Product_ID.delete(0,'end')
            Quantity.delete(0,'end')
            messagebox.showwarning(message="Product removed from Cart!")
            db.commit()

        Label(mainFrame,font=labelFont,text="Enter Product_ID:- ").pack(expand=True)
        Product_ID=Entry(mainFrame,width=40,font=("Arial",15))
        Product_ID.pack(expand=True)
        Label(mainFrame,font=labelFont,text="Enter Quantity:- ").pack(expand=True)
        Quantity=Entry(mainFrame,width=40,font=("Arial",15))
        Quantity.pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Submit",bg='MediumSeaGreen',command=remove_from_cart_helper).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=back_helper).pack(expand=True)

    def buy_product_from_cart():
        for child in mainFrame.winfo_children():
            child.destroy()
        def buy_product_from_cart_helper():
            db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
            command_handler=db.cursor(buffered=True)
            command_handler.execute("CALL BuyProduct(%s,%s,%s);",(Customer_ID,Product_ID.get(),PaymentType.get()))
            Product_ID.delete(0,'end')
            PaymentType.delete(0,'end')
            messagebox.showinfo(message="Order has been Placed!")

        Label(mainFrame,font=labelFont,text="Enter Product_ID:- ").pack(expand=True)
        Product_ID=Entry(mainFrame,width=40,font=("Arial",15))
        Product_ID.pack(expand=True)
        Label(mainFrame,font=labelFont,text="Enter Payment Type:- ").pack(expand=True)
        PaymentType=Entry(mainFrame,width=40,font=("Arial",15))
        PaymentType.pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Submit",bg='MediumSeaGreen',command=buy_product_from_cart_helper).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=back_helper).pack(expand=True)

    def return_item():
        for child in mainFrame.winfo_children():
            child.destroy()
        def return_item_helper():
            db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
            command_handler=db.cursor(buffered=True)
            command_handler.execute("CALL ReturnOrder(%s);",(Order_ID.get(),))
            db.commit()
            Order_ID.delete(0,'end')
            messagebox.showinfo(message="Item will be recieved from your location shortly.")
        Label(mainFrame,font=labelFont,text="Enter Order_ID:- ").pack(expand=True)
        Order_ID=Entry(mainFrame,width=40,font=("Arial",15))
        Order_ID.pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Submit",bg='MediumSeaGreen',command=return_item_helper).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=back_helper).pack(expand=True)

    def check_available_items():
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        for child in mainFrame.winfo_children():
            child.destroy()
        Label(mainFrame,font=labelFont,text="Available Products:- ").pack(expand=True)

        command_handler.execute("SELECT * FROM Product")
        allProducts=command_handler.fetchall()
        Label(mainFrame,font=labelFont,text="Product ID---Product Type---Product Name---Cost---Quantity---Seller ID",fg="Tomato").pack(expand=True)
        for x in allProducts:
            Label(mainFrame,font=labelFont,text=x).pack(expand=True)
        Button(mainFrame,font=buttonFont,text="Back",command=back_helper).pack(expand=True)

    Label(mainFrame,font=labelFont,text="Customer Menu:-").pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Check Cart",command=check_cart).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Check Orders",command=check_orders).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Check Payments",command=check_payments).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Add to Cart",command=add_to_cart).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Remove from Cart",command=remove_from_cart).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Buy Item from Cart",command=buy_product_from_cart).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Return Item",command=return_item).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Check Available Items",command=check_available_items).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Back",command=login_auth).pack(expand=True)

def customer_login():
    db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
    command_handler=db.cursor(buffered=True)
    for child in mainFrame.winfo_children():
        child.destroy()
    def validate_customer():
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        authenticate=(username.get(),password.get())
        command_handler.execute("SELECT UserID,UserPassword,TypeOfUser FROM UserIDandPasswords WHERE UserID=%s AND UserPassword=%s and TypeOfUser='Customer';",authenticate)
        user=command_handler.fetchall()
        if len(user): 
            customer_menu(username.get())
        else:
            messagebox.showwarning(message="Invalid username/password")
            username.delete(0,'end')
            password.delete(0,'end')
    Label(mainFrame,font=labelFont,text="Enter username:- ").pack(expand=True)
    username=Entry(mainFrame,width=40,font=("Arial",15))
    username.pack(expand=True)
    Label(mainFrame,font=labelFont,text="Enter password:- ").pack(expand=True)
    password=Entry(mainFrame,width=40,font=("Arial",15))
    password.pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Submit",bg='MediumSeaGreen',command=validate_customer).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Back",command=login_auth).pack(expand=True)

def seller_login():
    db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
    command_handler=db.cursor(buffered=True)
    for child in mainFrame.winfo_children():
        child.destroy()
    def validate_seller():
        db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
        command_handler=db.cursor(buffered=True)
        authenticate=(username.get(),password.get())
        command_handler.execute("SELECT UserID,UserPassword,TypeOfUser FROM UserIDandPasswords WHERE UserID=%s AND UserPassword=%s and TypeOfUser='Seller';",authenticate)
        user=command_handler.fetchall()
        if len(user): 
            seller_menu(username.get())
        else:
            messagebox.showwarning(message="Invalid username/password")
            username.delete(0,'end')
            password.delete(0,'end')
    Label(mainFrame,font=labelFont,text="Enter username:- ").pack(expand=True)
    username=Entry(mainFrame,width=40,font=("Arial",15))
    username.pack(expand=True)
    Label(mainFrame,font=labelFont,text="Enter password:- ").pack(expand=True)
    password=Entry(mainFrame,width=40,font=("Arial",15))
    password.pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Submit",bg='MediumSeaGreen',command=validate_seller).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Back",command=login_auth).pack(expand=True)

def admin_login():
    db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
    db.cursor(buffered=True)
    for child in mainFrame.winfo_children():
        child.destroy()
    def validate_admin():
        if username.get()=="admin" and password.get()=="admin":
            admin_menu()
        else:
            messagebox.showwarning(message="Invalid username/password")
            username.delete(0,'end')
            password.delete(0,'end')
    Label(mainFrame,font=labelFont,text="Enter username:- ").pack(expand=True)
    username=Entry(mainFrame,width=40,font=("Arial",15))
    username.pack(expand=True)
    Label(mainFrame,font=labelFont,text="Enter password:- ").pack(expand=True)
    password=Entry(mainFrame,width=40,font=("Arial",15))
    password.pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Submit",bg='MediumSeaGreen',command=validate_admin).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Back",command=login_auth).pack(expand=True)

def login_auth():
    db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
    db.cursor(buffered=True)
    for child in mainFrame.winfo_children():
        child.destroy()
    Button(mainFrame,font=buttonFont,text="Customer",command=customer_login).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Seller",command=seller_login).pack(expand=True)
    Button(mainFrame,font=buttonFont, text="Admin",command=admin_login).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Back",command=main).pack(expand=True)

def register_customer():
    db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
    command_handler=db.cursor(buffered=True)
    for child in mainFrame.winfo_children():
        child.destroy()

    def clickSubmit():
        command_handler.execute("SELECT * FROM UserIDandPasswords WHERE UserID=%s AND TypeOfUser='Customer'",(username.get(),))
        match=command_handler.fetchall()
        if len(match):
            
            messagebox.showwarning(message="username already taken. Try something else")
            username.delete(0,'end')
        elif password.get()!=re_password.get():
            messagebox.showwarning(message="Passwords do not match. Try again")
            
            re_password.delete(0,'end')
        else :
            new_customer=(username.get(),password.get(),name.get(),address.get(),pincode.get(),phoneNumber.get(),email.get())
            command_handler.execute("INSERT INTO Customer VALUES (%s,%s,%s,%s,%s,%s,%s)",new_customer)
            db.commit()
            command_handler.execute("INSERT INTO UserIDandPasswords VALUES (%s,%s,'Customer')",(username.get(), password.get()))
            db.commit()
            messagebox.showinfo(message="Registered Successfully!")
            name.delete(0,'end')
            address.delete(0,'end')
            pincode.delete(0,'end')
            phoneNumber.delete(0,'end')
            email.delete(0,'end')
            username.delete(0,'end')
            password.delete(0,'end')
            re_password.delete(0,'end')
            
    Label(mainFrame,font=labelFont,text="Name:- ").pack(expand=True)
    name=Entry(mainFrame,width=40,font=("Arial",15))
    name.pack(expand=True)
    Label(mainFrame,font=labelFont,text="Address:- ").pack(expand=True)
    address=Entry(mainFrame,width=40,font=("Arial",15))
    address.pack(expand=True)
    Label(mainFrame,font=labelFont,text="PinCode:- ").pack(expand=True)
    pincode=Entry(mainFrame,width=40,font=("Arial",15))
    pincode.pack(expand=True)
    Label(mainFrame,font=labelFont,text="Phone Number:- ").pack(expand=True)
    phoneNumber=Entry(mainFrame,width=40,font=("Arial",15))
    phoneNumber.pack(expand=True)
    Label(mainFrame,font=labelFont,text="Email:- ").pack(expand=True)
    email=Entry(mainFrame,width=40,font=("Arial",15))
    email.pack(expand=True)
    Label(mainFrame,font=labelFont,text="Username:- ").pack(expand=True)
    username=Entry(mainFrame,width=40,font=("Arial",15))
    username.pack(expand=True)
    Label(mainFrame,font=labelFont,text="Password:- ").pack(expand=True)
    password=Entry(mainFrame,width=40,font=("Arial",15))
    password.pack(expand=True)
    Label(mainFrame,font=labelFont,text="Confirm Password:- ").pack(expand=True)
    re_password=Entry(mainFrame,width=40,font=("Arial",15))
    re_password.pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Submit",bg='MediumSeaGreen',command=clickSubmit).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Back",command=register_auth).pack(expand=True)

def register_seller():
    db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
    command_handler=db.cursor(buffered=True)
    for child in mainFrame.winfo_children():
        child.destroy()

    def clickSubmit():
        command_handler.execute("SELECT * FROM UserIDandPasswords WHERE UserID=%s AND TypeOfUser='Seller'",(username.get(),))
        match=command_handler.fetchall()
        if len(match):
            messagebox.showwarning(message="username already taken. Try something else")
            username.delete(0,'end')
        elif password.get()!=re_password.get():
            messagebox.showwarning(message="Passwords do not match. Try again")
            re_password.delete(0,'end')
        else :
            new_seller=(username.get(),password.get(),name.get(),address.get(),phoneNumber.get())
            command_handler.execute("INSERT INTO Seller VALUES (%s,%s,%s,%s,%s)",new_seller)
            db.commit()
            command_handler.execute("INSERT INTO UserIDandPasswords VALUES (%s,%s,'Seller')",(username.get(), password.get()))
            db.commit()
            messagebox.showinfo(message="Registered Successfully!")
            name.delete(0,'end')
            address.delete(0,'end')
            phoneNumber.delete(0,'end')
            username.delete(0,'end')
            password.delete(0,'end')
            re_password.delete(0,'end')
            
    Label(mainFrame,font=labelFont,text="Name:- ").pack(expand=True)
    name=Entry(mainFrame,width=40,font=("Arial",15))
    name.pack(expand=True)
    Label(mainFrame,font=labelFont,text="Address:- ").pack(expand=True)
    address=Entry(mainFrame,width=40,font=("Arial",15))
    address.pack(expand=True)
    Label(mainFrame,font=labelFont,text="Phone Number:- ").pack(expand=True)
    phoneNumber=Entry(mainFrame,width=40,font=("Arial",15))
    phoneNumber.pack(expand=True)
    Label(mainFrame,font=labelFont,text="Username:- ").pack(expand=True)
    username=Entry(mainFrame,width=40,font=("Arial",15))
    username.pack(expand=True)
    Label(mainFrame,font=labelFont,text="Password:- ").pack(expand=True)
    password=Entry(mainFrame,width=40,font=("Arial",15))
    password.pack(expand=True)
    Label(mainFrame,font=labelFont,text="Confirm Password:- ").pack(expand=True)
    re_password=Entry(mainFrame,width=40,font=("Arial",15))
    re_password.pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Submit",bg='MediumSeaGreen',command=clickSubmit).pack(expand=True)
    Button(mainFrame,font=buttonFont,text="Back",command=register_auth).pack(expand=True)

def register_auth():
    for child in mainFrame.winfo_children():
        child.destroy()
    Label(mainFrame,text="Register Menu:- ",font=(BOLD,18)).pack(side=TOP,expand=True,fill="both")
    Button(mainFrame,font=buttonFont,text="Customer ",command=register_customer).pack(side=TOP,expand=True,fill="both")
    Button(mainFrame,font=buttonFont,text="Seller",command=register_seller).pack(side=TOP,expand=True,fill="both")
    Button(mainFrame,font=buttonFont,text="Back",command=main).pack(side=TOP,expand=True,fill="both")

def main():
    for child in mainFrame.winfo_children():
        child.destroy()
    db=mysql.connect(host="localhost", user="root", password="password", database="ECOMMERCE",autocommit=True)
    db.cursor(buffered=True)
    regLabel=Button(mainFrame,font=buttonFont,text="Register:- ",command=register_auth)
    regLabel.pack(side=LEFT,expand=True,fill="both")
    lLabel=Button(mainFrame,font=buttonFont,text="Login:- ",command=login_auth)
    lLabel.pack(side=LEFT,expand=True,fill="both")

mainFrame=Frame(root)
mainFrame.pack(expand=True,fill="both")
main()
root.mainloop()