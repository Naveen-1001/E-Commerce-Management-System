CREATE DATABASE ECOMMERCE;
use ECOMMERCE;
drop table Orders;
drop table UserIDandPasswords;
drop table CartItem;
drop table Product;
drop table Seller;
drop table Payment;
drop table Customer;

CREATE TABLE UserIDandPasswords
(
    UserID VARCHAR(6) NOT NULL PRIMARY KEY,
    UserPassword VARCHAR(10) NOT NULL,
    TypeOfUser VARCHAR(10) NOT NULL
);

CREATE TABLE Customer
(
    CustomerID VARCHAR(6) NOT NULL PRIMARY KEY,
    CustomerPassword VARCHAR(10) NOT NULL,
    Name VARCHAR(30) NOT NULL,
    Address VARCHAR(50) NOT NULL,
    Pincode VARCHAR(10) NOT NULL,
    PhoneNumber VARCHAR(10) NOT NULL,
    Email VARCHAR(255)
);

CREATE TABLE Seller
(
    SellerID VARCHAR(6) NOT NULL PRIMARY KEY,
    SellerPassword VARCHAR(10) NOT NULL,
    Name VARCHAR(20) NOT NULL,
    Address VARCHAR(50) NOT NULL,
    PhoneNumber VARCHAR(10) NOT NULL
);

CREATE TABLE Payment
(
  OrderID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  PaymentType VARCHAR(20) NOT NULL,
  TotalAmount INT
)AUTO_INCREMENT=1000001;

CREATE TABLE Product
(
  ProductID VARCHAR(7) NOT NULL PRIMARY KEY,
  ProductType VARCHAR(20) NOT NULL,
  ProductName VARCHAR(20) NOT NULL,
  Cost INT NOT NULL,
  Quantity INT NOT NULL,
  SellerID VARCHAR(6),
  FOREIGN KEY (SellerID) REFERENCES Seller(SellerID)
  ON DELETE SET NULL
);

CREATE TABLE CartItem
(
    CustomerID VARCHAR(7) NOT NULL,
    ProductID VARCHAR(7) NOT NULL,
    Quantity INT NOT NULL,
    TotalAmount INT NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    PRIMARY KEY(CustomerID,ProductID)
 );

 CREATE TABLE Orders
 (
   OrderID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
   CustomerID VARCHAR(7) NOT NULL,
   ProductID VARCHAR(7) NOT NULL,
   OrderDate DATE NOT NULL,
   FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
   FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
   FOREIGN KEY (OrderID) REFERENCES Payment(OrderID)
 )AUTO_INCREMENT=1000001;

INSERT INTO UserIDandPasswords VALUES
(10001,'abvpwd123','Customer'),
(10002,'axxcvpd3','Customer'),
(10003,'bbvxwd123','Customer'),
(10004,'abbcvp245','Customer'),
(10005,'abvpwd123','Customer'),
(10006,'abvdgd1675','Customer'),
(10007,'lskvpds79','Customer'),
(10008,'bbvpwd320','Customer'),
(10009,'ab1234psh','Customer'),
(10010,'xxv123pqr','Customer'),
('sid101','hwevbf','Seller'),
('sid102','fwgihi','Seller'),
('sid103','bbweuhww','Seller'),
('sid104','wbdfbh','Seller'),
('sid105','uiewbibi','Seller'),
('sid106','ebfiwbef','Seller'),
('sid107','bbwewu','Seller'),
('sid108','feydfuwu','Seller'),
('sid109','iueouow','Seller');

INSERT INTO Customer VALUES
(10001,'abvpwd123','Rajesh','East Phase New Delhi',661023,'8456712345','rajesh@gmail.com'),
(10002,'axxcvpd3','Ajit','Juhu Mumbai',681023,'8456652345','ajit@gmail.com'),
(10003,'bbvxwd123','Rahul','Lions Road Bangalore',661323,'8126712345','rahul@gmail.com'),
(10004,'abbcvp245','Arjun','New Delhi',661023,'8456712345','arjun@gmail.com'),
(10005,'abvpwd123','Raheem','Old City Lucknow',781023,'8456719845','raheem@gmail.com'),
(10006,'abvdgd1675','Charu','Kings Road Chandigarh',661723,'8106712345','charu@gmail.com'),
(10007,'lskvpds79','Sonam','New Delhi',661023,'8456719785','sonam@gmail.com'),
(10008,'bbvpwd320','Priya','Rajeshwari Kolkata',721023,'8896714345','priya@gmail.com'),
(10009,'ab1234psh','Anil','Colaba Mumbai',661093,'8456719845','anil@gmail.com'),
(10010,'xxv123pqr','Riya','Rajouri NewDelhi',760823,'8419812345','riya@gmail.com');

INSERT INTO Seller VALUES
('sid100','bfhbfj','Aman','At post Delhi','9923657432'),
('sid101','hwevbf','Zaad','At post Mumbai','9923657433'),
('sid102','fwgihi','Nazir','At post Bhiwandi','9923657434'),
('sid103','bbweuhww','Aadil','At post Pune','9923657435'),
('sid104','wbdfbh','Anil','At post Bhopal','9923657436'),
('sid105','uiewbibi','Yogesh','At post Mumbai','9923657437'),
('sid106','ebfiwbef','Kiran','At post Delhi','9923657438'),
('sid107','bbwewu','Himanshu','At post Bhiwandi','9923657439'),
('sid108','feydfuwu','Mohan','At post Chennai','9923657440'),
('sid109','iueouow','Bhanupriya','At post Banglore','9923657430');

INSERT INTO Product VALUES
('pid1001','Book','Harry Potter',600,10,'sid101'),
('pid1002','Fashion','Makeup',800,18,'sid105'),
('pid1003','Electronics','iPhone X',100000,40,'sid109'),
('pid1004','Eatables','Ice Cream',30,15,'sid104'),
('pid1005','Book','Rich Dad Poor Dad',200,15,'sid101'),
('pid1006','Electronics','Sony Bravia',75000,7,'sid106'),
('pid1007','Footwear','Adidas Predator',5000,20,'sid108'),
('pid1008','Vehicle','TVS Jupiter',45000,5,'sid102'),
('pid1009','Eatables','Coke',40,50,'sid101'),
('pid1010','Eatables','Bread',20,100,'sid103'),
('pid1011','Eatables','Bisleri',10,100,'sid103'),
('pid1012','Book','Tinkle',120,18,'sid101');

INSERT INTO CartItem VALUES
(10001,'pid1001',2,1200),
(10002,'pid1004',3,90),
(10007,'pid1005',1,200),
(10004,'pid1009',5,200), 
(10008,'pid1011',10,100),
(10009,'pid1003',1,100000),
(10008,'pid1009',3,120),
(10002,'pid1005',2,400),
(10006,'pid1002',1,800),
(10004,'pid1006',1,75000);

INSERT INTO Payment(PaymentType,TotalAmount) VALUES
('Net Banking',800),
('Credit/Debit',100000),
('Net Banking',75000),
('UPI',600),
('COD',45000),
('COD',600),
('UPI',200),
('Credit/Debit',40),
('COD',5000),
('UPI',120),
('UPI',10),
('COD',10),
('Net Banking',200),
('COD',30),
('UPI',30);

INSERT INTO Orders(CustomerID,ProductID,OrderDate) VALUES
(10003,'pid1002','2020-10-12'),
(10001,'pid1003','2019-10-23'),
(10005,'pid1006','2018-10-15'),
(10003,'pid1001','2019-10-05'),
(10006,'pid1008','2020-10-06'),
(10007,'pid1001','2019-10-08'),
(10005,'pid1005','2020-10-12'),
(10003,'pid1009','2019-10-02'),
(10001,'pid1007','2019-10-14'),
(10009,'pid1012','2018-10-02'),
(10004,'pid1011','2020-10-13'),
(10007,'pid1011','2018-10-02'),
(10005,'pid1005','2018-10-17'),
(10001,'pid1004','2018-10-18'),
(10003,'pid1004','2020-10-02');

/*
SELECT CustomerID,Name,PhoneNumber,Email
FROM Customer
WHERE Address LIKE '%Mumbai%';

SELECT * FROM Product;
UPDATE Product SET cost=0.9*cost
WHERE SellerID='sid101';

SELECT * FROM Product;
SELECT DISTINCT PaymentType AS DifferentTypesOfPaymentsAccepted
FROM Payment;
*/
SET sql_mode = '';
/*
SELECT P.ProductID,P.ProductName,S.SellerID,S.Name,P.Cost
FROM Product P,Seller S
WHERE P.SellerID=S.SellerID
GROUP BY P.SellerID
HAVING Cost=MAX(Cost);

SELECT DISTINCT Address
FROM Seller;

SELECT C.CustomerID, C.Name, COUNT(*) AS NumberOfItems
FROM Customer C,CartItem CI
WHERE C.CustomerID=CI.CustomerID
GROUP BY C.CustomerID
ORDER BY NumberOfItems desc;

SELECT  * FROM Orders
WHERE OrderDate > '2019-12-31';

SELECT ProductType, COUNT(*) AS NumberOfProducts
FROM Product
GROUP BY ProductType;

SELECT ProductType,AVG(COST) AS AverageCost
FROM Product
GROUP BY ProductType;

SELECT C.Name,O.OrderID,O.ProductID,O.OrderDate
FROM Customer as C, Orders as O
WHERE C.Name='Rajesh' and C.CustomerID=O.CustomerID;

SELECT * FROM Customer as C
WHERE C.CustomerID IN(SELECT O.CustomerID
                      From Orders AS O, CartItem as CI 
                      WHERE O.CustomerID=C.CustomerID AND C.CustomerID=CI.CustomerID);

SELECT P.PaymentType,COUNT(*) AS NumberOfPayments
FROM Payment P, Orders O 
WHERE P.OrderID=O.OrderID AND
O.CustomerID IN(SELECT CustomerID 
                FROM Customer 
                WHERE CustomerID=O.CustomerID AND 
                Address LIKE '%Mumbai%' OR Address LIKE '%Delhi%') 
GROUP BY P.PaymentType;

SELECT C.CustomerID, C.Name, O.OrderID, P.TotalAmount 
FROM Customer AS C, Orders AS O, Payment AS P 
WHERE O.CustomerID=C.CustomerID AND P.OrderID=O.OrderID
AND P.TotalAmount=(SELECT MAX(P1.TotalAmount) 
                   FROM Payment AS P1, Orders AS O1  
                   WHERE P1.OrderID=O1.OrderID AND O1.CustomerID=C.CustomerID);

SELECT C.CustomerID, C.Name,COUNT(*) AS NoOfOrders FROM Customer C 
INNER JOIN Orders O 
ON O.CustomerID=C.CustomerID 
GROUP BY C.CustomerID 
HAVING NoOfOrders>=ALL(SELECT COUNT(*) FROM
                       Orders 
                       GROUP BY CustomerID);

SELECT DISTINCT C.CustomerID, C.Name FROM Customer C,Orders O, Product P,Seller S 
WHERE O.CustomerID=C.CustomerID AND O.ProductID=P.ProductID AND P.SellerID=S.SellerID AND 
P.SellerID IN(SELECT SellerID 
              FROM Product 
              GROUP BY SellerID 
              HAVING COUNT(*)>1);

SELECT O.CustomerID, O.OrderID, O.ProductID, O.OrderDate FROM Orders AS O 
WHERE O.CustomerID = (SELECT CustomerID 
                      FROM Orders 
                      GROUP BY CustomerID 
                      ORDER BY COUNT(CustomerID) DESC LIMIT 1); 

SELECT * FROM Customer 
WHERE CustomerID!=ALL(SELECT CustomerID 
                      FROM Orders);

*/
                      
DROP VIEW OrderDet;
CREATE VIEW OrderDet AS
SELECT O.OrderID, C.Name AS CustomerName, S.Name AS SellerName
FROM Orders AS O, Customer AS C, Product AS P, Seller AS S 
WHERE O.CustomerID=C.CustomerID AND O.ProductID=P.ProductID AND P.SellerID=S.SellerID;

/*SELECT * FROM OrderDet;*/

DROP VIEW ProductsWithPriceLessThanRs1000;
CREATE VIEW ProductsWithPriceLessThanRs1000 AS
SELECT * FROM Product 
WHERE Cost<1000
ORDER BY Cost;

/*SELECT * FROM ProductsWithPriceLessThanRs1000;*/

DROP VIEW HighestPurchaseOfDay;
CREATE VIEW HighestPurchaseOfDay AS 
SELECT C.CustomerID, C.Name, MAX(P.Cost) as PurchaseAmount, O.OrderDate 
FROM Customer C, Orders O, Product P
WHERE O.CustomerID=C.CustomerID AND O.ProductID=P.ProductID 
GROUP BY O.OrderDate;
SET sql_mode = '';

/*SELECT * FROM HighestPurchaseOfDay;*/

DROP VIEW CheapestProductOfSeller;
CREATE VIEW CheapestProductOfSeller AS
SELECT S.SellerID, P.ProductID, P.ProductName, P.Cost 
FROM Product AS P, Seller AS S
WHERE P.SellerID=S.SellerID AND P.ProductID = (SELECT ProductID 
                                               FROM Product 
                                               WHERE SellerID=S.SellerID 
                                               ORDER BY COST LIMIT 1);

/*SELECT * FROM CheapestProductOfSeller;*/

DROP VIEW HighestPayType;
CREATE VIEW HighestPayType AS 
SELECT PaymentType,Max(TotalAmount) 
FROM Payment 
GROUP BY PaymentType ;

/*SELECT * FROM HighestPayType;*/

DROP PROCEDURE IF EXISTS AddToCart;
DELIMITER //
CREATE PROCEDURE AddToCart(IN ProductID VARCHAR(7), IN CustomerID VARCHAR(7), IN Quantity INT)
BEGIN
    DECLARE TotalAmount int;
    DECLARE Stock int;
    DECLARE ErrorMessage VARCHAR(255);
    SET ErrorMessage = 'Not Enough Stock Available';
    SELECT P.Quantity INTO Stock FROM Product AS P WHERE P.ProductID=ProductID; 
    IF Quantity<=Stock THEN
        SELECT P.Cost*Quantity INTO TotalAmount From Product as P WHERE P.ProductID=ProductID;
        INSERT INTO CartItem VALUES(CustomerID,ProductID,Quantity,TotalAmount);
        IF Quantity=Stock THEN 
          DELETE FROM Product P WHERE ProductID=P.ProductID;
        ELSE 
          UPDATE Product P SET P.Quantity=Stock-Quantity WHERE ProductID=P.ProductID;
        END IF;
    ELSE 
        SIGNAL SQLSTATE '45000' SET message_text = ErrorMessage;
    END IF;
END//
DELIMITER ;
/*
SELECT * FROM CartItem;
CALL AddToCart('pid1011','10001',20);
SELECT * FROM CartItem;
*/

DROP PROCEDURE IF EXISTS RemoveFromCart;
DELIMITER //
CREATE PROCEDURE RemoveFromCart(IN ProductID VARCHAR(7),IN CustomerID VARCHAR(7),IN NoOfItems INT)
BEGIN
  DECLARE Quan INT;
  DECLARE QLeft INT;
  SELECT C.Quantity INTO Quan 
  FROM CartItem C
  WHERE C.CustomerID=CustomerID AND C.ProductID=ProductID;
  IF NoOfItems<Quan THEN SET QLeft=Quan-NoOfItems;
  ELSE SET QLeft=0;
  END IF;
  UPDATE CartItem C
  SET C.Quantity=QLeft
  WHERE C.ProductID=ProductID AND C.CustomerID=CustomerID;
END //
DELIMITER;
/*
SELECT * FROM CartItem;
CALL RemoveFromCart('pid1011','10001',5);
SELECT * FROM CartItem;
*/

DROP PROCEDURE IF EXISTS GetSellerProducts;
DELIMITER //
CREATE PROCEDURE GetSellerProducts(IN SellerID VARCHAR(6))
BEGIN
  SELECT * FROM Product AS P
  WHERE P.SellerID=SellerID;
END//
DELIMITER ;
/*
CALL GetSellerProducts('sid101');
*/

DROP PROCEDURE IF EXISTS GetCustomersCartItems;
DELIMITER //
CREATE PROCEDURE GetCustomersCartItems(IN CustomerID VARCHAR(6))
BEGIN
  SELECT * FROM CartItem AS CI 
  WHERE CI.CustomerID=CustomerID;
END//
DELIMITER ;
/*
CALL GetCustomersCartItems('10001');
*/

DROP PROCEDURE IF EXISTS GetCustomersOrders;
DELIMITER //
CREATE PROCEDURE GetCustomersOrders(IN CustomerID VARCHAR(6))
BEGIN
  SELECT OrderID,ProductID,OrderDate FROM Orders AS O 
  WHERE O.CustomerID=CustomerID;
END//
DELIMITER ;
/*
CALL GetCustomersOrders('10003');
*/

DROP FUNCTION IF EXISTS GetCartCost;
DELIMITER //
CREATE FUNCTION GetCartCost(customerID VARCHAR(7))
RETURNS INT
DETERMINISTIC
BEGIN
  DECLARE TotalCost INT DEFAULT 0;
  SELECT SUM(TotalAmount) INTO TotalCost 
  FROM CartItem AS CI 
  WHERE CI.CustomerID=customerID;
  RETURN TotalCost;
END //
DELIMITER ;
/*
SELECT GetCartCost('10002') AS TotalAmountInCart;
SELECT GetCartCost('10008') AS TotalAmountInCart;
*/

DROP FUNCTION IF EXISTS GetProductLevel;
DELIMITER //
CREATE FUNCTION GetProductLevel(PName VARCHAR(20))
RETURNS VARCHAR(15)
DETERMINISTIC
BEGIN
  DECLARE val INT DEFAULT 0;
  DECLARE level varchar(15);
  SELECT Cost INTO val FROM Product WHERE ProductName=PName;
  IF val<10000 THEN
  SET level='AFFORDABLE';
  ELSEIF val<=70000 THEN
  SET level='MID-RANGE';
  ELSE
  SET level='EXPENSIVE';
  END IF;
  RETURN (level);
END //
DELIMITER ;
/*
SELECT GetProductLevel('Sony Bravia') AS ProductLevel;
SELECT GetProductLevel('Bisleri') AS ProductLevel;
*/
DROP FUNCTION IF EXISTS GetExpensiveProduct;
DELIMITER //
CREATE FUNCTION GetExpensiveProduct()
RETURNS varchar(20)
DETERMINISTIC
BEGIN
  DECLARE val varchar(20);
  SELECT ProductName INTO val FROM Product WHERE Cost=(SELECT MAX(Cost) FROM Product P) ;
  RETURN val;
END //
DELIMITER ;
SELECT GetExpensiveProduct() AS ExpensiveProduct;

DROP FUNCTION IF EXISTS GetStock;
DELIMITER //
CREATE FUNCTION GetStock(ProductID VARCHAR(7))
RETURNS INT
DETERMINISTIC
BEGIN
  DECLARE Stock INT;
  SELECT Quantity INTO Stock FROM Product P
  WHERE P.ProductID=ProductID;
  RETURN Stock;
END //
DELIMITER ;
/*
SELECT GetStock('pid1003') AS Stock;
SELECT GetStock('pid1006') AS Stock;
*/

DROP FUNCTION IF EXISTS GetContactDetailOfSeller;
DELIMITER //
CREATE FUNCTION GetContactDetailOfSeller(ProductID VARCHAR(7))
RETURNS VARCHAR(10)
DETERMINISTIC
BEGIN
  DECLARE ContactNo VARCHAR(10);
  SELECT S.PhoneNumber INTO ContactNo FROM Product P, Seller S
  WHERE P.ProductID=ProductID AND S.SellerID=P.SellerID;
  RETURN ContactNo;
END //
DELIMITER ;
/*
SELECT GetContactDetailOfSeller('pid1005') AS ContactNo;
SELECT GetContactDetailOfSeller('pid1011') AS ContactNo;
*/

DROP TRIGGER IF EXISTS BuyProductTrigger;
DELIMITER //
CREATE TRIGGER BuyProductTrigger
AFTER DELETE ON CartItem
FOR EACH ROW
BEGIN
  DECLARE Quantity INT;
  DECLARE Total INT;
  DECLARE Price INT;
  DECLARE PaymentID VARCHAR(7);
  SELECT Cost INTO Price FROM Product WHERE ProductID=old.ProductID;
  SET Total=Price*old.Quantity; 
  INSERT INTO Payment(PaymentType,TotalAmount) VALUES ('COD',Total);
  SELECT OrderID INTO PaymentID FROM Payment ORDER BY OrderID DESC LIMIT 1;
  INSERT INTO Orders VALUES (PaymentID,old.CustomerID,old.ProductID,CURDATE());
  UPDATE Product P SET P.Quantity=P.Quantity-old.Quantity
  WHERE P.ProductID=old.ProductID;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS BuyProduct;
DELIMITER //
CREATE PROCEDURE BuyProduct(IN CustomerID VARCHAR(7),IN ProductID VARCHAR(7),IN PaymentType VARCHAR(7))
BEGIN
  DECLARE PaymentID VARCHAR(7);
  DELETE FROM CartItem C 
  WHERE C.CustomerID=CustomerID AND C.ProductID=ProductID;
  SELECT OrderID INTO PaymentID FROM Payment ORDER BY OrderID DESC LIMIT 1;
  UPDATE Payment P SET P.PaymentType=PaymentType WHERE P.OrderID=PaymentID;
END //
DELIMITER ;
/*
SELECT * FROM CartItem;
SELECT * FROM Product;
SELECT * FROM Orders;
SELECT * FROM Payment;

CALL BuyProduct(10008,'pid1009','Net Banking');
SELECT * FROM CartItem;
SELECT * FROM Product;
SELECT * FROM Orders;
SELECT * FROM Payment;
*/

DROP TRIGGER IF EXISTS ApplyDiscount;
DELIMITER //
CREATE TRIGGER ApplyDiscount
BEFORE INSERT ON Payment  
FOR EACH ROW
BEGIN
  IF new.TotalAmount>=75000 THEN
  SET new.TotalAmount=0.9*new.TotalAmount;
END IF;
END//
DELIMITER ;
/*
SELECT * FROM CartItem;
SELECT * FROM Product;
CALL BuyProduct(10009,'pid1003','COD');
SELECT * FROM Payment;
*/
DROP TRIGGER IF EXISTS Refund;
DELIMITER //
CREATE TRIGGER Refund
AFTER DELETE ON Orders
FOR EACH ROW
BEGIN
  DELETE FROM Payment
  WHERE OrderID=old.OrderID;
END//
DELIMITER ;

DROP PROCEDURE IF EXISTS ReturnOrder;
DELIMITER //
CREATE PROCEDURE ReturnOrder(IN OrderID VARCHAR(7))
BEGIN
  DELETE FROM Orders AS O
  WHERE O.OrderID = OrderID;
END//
DELIMITER ;
/*
SELECT * FROM Orders;
SELECT * FROM Payment;
CALL ReturnOrder('1000004');
SELECT * FROM Orders;
SELECT * FROM Payment;
*/