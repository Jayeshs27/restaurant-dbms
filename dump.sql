-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
-- Host: localhost    Database: final_restaurant
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `BRINGS`
--

DROP TABLE IF EXISTS `BRINGS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BRINGS` (
  `Waiter_ID` char(6) NOT NULL,
  `Order_Number` int NOT NULL,
  `Customer_Phone_No` char(10) NOT NULL,
  `Date` date NOT NULL,
  `Chef_ID` char(6) NOT NULL,
  `Table_Number` int NOT NULL,
  PRIMARY KEY (`Waiter_ID`,`Order_Number`,`Customer_Phone_No`,`Date`,`Chef_ID`,`Table_Number`),
  KEY `fk_brings_orderinfo1` (`Customer_Phone_No`,`Order_Number`,`Date`),
  KEY `fk_brings_chef` (`Chef_ID`),
  KEY `fk_brings_table` (`Table_Number`),
  CONSTRAINT `fk_brings_chef` FOREIGN KEY (`Chef_ID`) REFERENCES `CHEF` (`Chef_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_brings_orderinfo1` FOREIGN KEY (`Customer_Phone_No`, `Order_Number`, `Date`) REFERENCES `ORDER_INFO` (`Customer_Phone_No`, `Order_Number`, `Date`),
  CONSTRAINT `fk_brings_table` FOREIGN KEY (`Table_Number`) REFERENCES `TABLE_INFO` (`Table_Number`),
  CONSTRAINT `fk_brings_waiter` FOREIGN KEY (`Waiter_ID`) REFERENCES `WAITER` (`Waiter_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BRINGS`
--

LOCK TABLES `BRINGS` WRITE;
/*!40000 ALTER TABLE `BRINGS` DISABLE KEYS */;
INSERT INTO `BRINGS` VALUES ('W006',1,'1111111111','2023-11-23','C001',1),('W007',2,'1234567890','2023-11-24','C002',2),('W008',3,'5555555555','2023-11-25','C003',3),('W009',4,'9876543210','2023-11-26','C004',4),('W010',5,'9998887777','2023-11-27','C005',5);
/*!40000 ALTER TABLE `BRINGS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CHEF`
--

DROP TABLE IF EXISTS `CHEF`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CHEF` (
  `Chef_ID` char(6) NOT NULL,
  `Fname` varchar(25) DEFAULT NULL,
  `Mname` varchar(25) DEFAULT NULL,
  `Lname` varchar(25) DEFAULT NULL,
  `Date_of_join` date DEFAULT NULL,
  `Rating` int DEFAULT NULL,
  `Salary` int DEFAULT NULL,
  PRIMARY KEY (`Chef_ID`),
  CONSTRAINT `CHEF_chk_1` CHECK (((`Rating` >= 1) and (`Rating` <= 5)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CHEF`
--

LOCK TABLES `CHEF` WRITE;
/*!40000 ALTER TABLE `CHEF` DISABLE KEYS */;
INSERT INTO `CHEF` VALUES ('C001','Michael','A','Johnson','2010-03-15',4,60000),('C002','Emma','B','Smith','2012-08-10',3,55000),('C003','Alexander','C','Garcia','2015-01-20',5,70000),('C004','Sophia','D','Williams','2018-06-05',4,65000),('C005','Oliver','E','Brown','2020-02-18',4,62000);
/*!40000 ALTER TABLE `CHEF` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CHEF_SHIFT`
--

DROP TABLE IF EXISTS `CHEF_SHIFT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CHEF_SHIFT` (
  `Chef_ID` char(6) NOT NULL,
  `Shift_Start_time` time NOT NULL,
  `Shift_end_time` time NOT NULL,
  PRIMARY KEY (`Chef_ID`,`Shift_Start_time`,`Shift_end_time`),
  CONSTRAINT `fk_chefshift_chef` FOREIGN KEY (`Chef_ID`) REFERENCES `CHEF` (`Chef_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CHEF_SHIFT`
--

LOCK TABLES `CHEF_SHIFT` WRITE;
/*!40000 ALTER TABLE `CHEF_SHIFT` DISABLE KEYS */;
INSERT INTO `CHEF_SHIFT` VALUES ('C001','08:00:00','15:00:00'),('C002','10:00:00','17:00:00'),('C003','12:00:00','19:00:00'),('C004','14:00:00','21:00:00'),('C005','16:00:00','23:00:00');
/*!40000 ALTER TABLE `CHEF_SHIFT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CHEF_SPECIALISATION`
--

DROP TABLE IF EXISTS `CHEF_SPECIALISATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CHEF_SPECIALISATION` (
  `Chef_ID` char(6) NOT NULL,
  `Dish_name` varchar(25) NOT NULL,
  PRIMARY KEY (`Chef_ID`,`Dish_name`),
  KEY `fk_chefspec_dish` (`Dish_name`),
  CONSTRAINT `fk_chefspec_dish` FOREIGN KEY (`Dish_name`) REFERENCES `DISH` (`Name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_chefspecialisation_chef` FOREIGN KEY (`Chef_ID`) REFERENCES `CHEF` (`Chef_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CHEF_SPECIALISATION`
--

LOCK TABLES `CHEF_SPECIALISATION` WRITE;
/*!40000 ALTER TABLE `CHEF_SPECIALISATION` DISABLE KEYS */;
INSERT INTO `CHEF_SPECIALISATION` VALUES ('C001','Chicken Parmesan'),('C002','Margherita Pasta'),('C002','Margherita Pizza'),('C004','Masala Dosa'),('C001','Noodles Stir-Fry'),('C005','Paneer Butter Masala'),('C003','Schezwan Noodles'),('C005','Vegetable Biryani');
/*!40000 ALTER TABLE `CHEF_SPECIALISATION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `COMBO`
--

DROP TABLE IF EXISTS `COMBO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `COMBO` (
  `Name` varchar(25) NOT NULL,
  `Dish_Name` varchar(25) NOT NULL,
  `Price` int DEFAULT NULL,
  `Availability` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`Name`,`Dish_Name`),
  KEY `fk_combo_dish` (`Dish_Name`),
  CONSTRAINT `fk_combo_dish` FOREIGN KEY (`Dish_Name`) REFERENCES `DISH` (`Name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `COMBO`
--

LOCK TABLES `COMBO` WRITE;
/*!40000 ALTER TABLE `COMBO` DISABLE KEYS */;
INSERT INTO `COMBO` VALUES ('Asian Fusion','Noodles Stir-Fry',32,0),('Asian Fusion','Schezwan Noodles',32,0),('Classic Combo','Margherita Pizza',38,0),('Classic Combo','Masala Dosa',38,0),('Classic Combo','Vegetable Biryani',38,0),('Family Special','Chicken Parmesan',50,1),('Family Special','Paneer Butter Masala',50,1),('Family Special','Vegetable Biryani',50,1),('Italian Feast','Chicken Parmesan',40,1),('Italian Feast','Margherita Pasta',40,1),('Spicy Duo','Paneer Butter Masala',35,1),('Spicy Duo','Schezwan Noodles',35,1),('Veg Delight','Margherita Pizza',30,1),('Veg Delight','Masala Dosa',30,1);
/*!40000 ALTER TABLE `COMBO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `COMBO_TYPE`
--

DROP TABLE IF EXISTS `COMBO_TYPE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `COMBO_TYPE` (
  `Name` varchar(25) NOT NULL,
  `Dish_Name` varchar(25) NOT NULL,
  `Type` enum('Lunch Combo','Dinner Combo','Weekend Special') NOT NULL,
  PRIMARY KEY (`Name`,`Dish_Name`,`Type`),
  KEY `fk_combotype_combo2` (`Dish_Name`),
  CONSTRAINT `fk_combotype_combo` FOREIGN KEY (`Name`) REFERENCES `COMBO` (`Name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_combotype_combo2` FOREIGN KEY (`Dish_Name`) REFERENCES `COMBO` (`Dish_Name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `COMBO_TYPE`
--

LOCK TABLES `COMBO_TYPE` WRITE;
/*!40000 ALTER TABLE `COMBO_TYPE` DISABLE KEYS */;
INSERT INTO `COMBO_TYPE` VALUES ('Family Special','Chicken Parmesan','Weekend Special'),('Italian Feast','Chicken Parmesan','Dinner Combo'),('Italian Feast','Margherita Pasta','Dinner Combo'),('Classic Combo','Margherita Pizza','Lunch Combo'),('Veg Delight','Margherita Pizza','Lunch Combo'),('Veg Delight','Masala Dosa','Lunch Combo'),('Asian Fusion','Noodles Stir-Fry','Dinner Combo'),('Family Special','Paneer Butter Masala','Weekend Special'),('Spicy Duo','Paneer Butter Masala','Lunch Combo'),('Asian Fusion','Schezwan Noodles','Dinner Combo'),('Spicy Duo','Schezwan Noodles','Lunch Combo'),('Classic Combo','Vegetable Biryani','Lunch Combo'),('Family Special','Vegetable Biryani','Weekend Special');
/*!40000 ALTER TABLE `COMBO_TYPE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CUSTOMER`
--

DROP TABLE IF EXISTS `CUSTOMER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CUSTOMER` (
  `Fname` varchar(25) DEFAULT NULL,
  `Mname` varchar(25) DEFAULT NULL,
  `Lname` varchar(25) DEFAULT NULL,
  `Phone_No` char(10) NOT NULL,
  `Business_provided_till_now` int DEFAULT NULL,
  `Birthday` date DEFAULT NULL,
  `Table_Number` int DEFAULT NULL,
  PRIMARY KEY (`Phone_No`),
  KEY `fk_customer_table` (`Table_Number`),
  CONSTRAINT `fk_customer_table` FOREIGN KEY (`Table_Number`) REFERENCES `TABLE_INFO` (`Table_Number`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CUSTOMER`
--

LOCK TABLES `CUSTOMER` WRITE;
/*!40000 ALTER TABLE `CUSTOMER` DISABLE KEYS */;
INSERT INTO `CUSTOMER` VALUES ('Oliver','D','Williams','1111111111',600,'1989-11-30',4),('Emily','A','Johnson','1234567890',500,'1992-08-18',1),('Sophia','C','Anderson','5555555555',300,'1994-06-10',3),('James','B','Thompson','9876543210',800,'1987-03-22',2),('Ava','E','Davis','9998887777',400,'1991-02-25',5);
/*!40000 ALTER TABLE `CUSTOMER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DISH`
--

DROP TABLE IF EXISTS `DISH`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DISH` (
  `Name` varchar(25) NOT NULL,
  `Category` enum('Veg','Non-veg','Vegan') DEFAULT NULL,
  `Cuisine` enum('Indian','Italian','Chinese') DEFAULT NULL,
  `Description` varchar(255) DEFAULT NULL,
  `Price` int DEFAULT NULL,
  PRIMARY KEY (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DISH`
--

LOCK TABLES `DISH` WRITE;
/*!40000 ALTER TABLE `DISH` DISABLE KEYS */;
INSERT INTO `DISH` VALUES ('Chicken Parmesan','Non-veg','Italian','Breaded chicken topped with marinara sauce and cheese',25),('Margherita Pasta','Veg','Italian','Classic pasta with tomato sauce and mozzarella',18),('Margherita Pizza','Veg','Italian','Classic pizza with tomato, mozzarella, and basil',22),('Masala Dosa','Veg','Indian','Crispy dosa filled with spiced potato',12),('Noodles Stir-Fry','Vegan','Chinese','Stir-Fried noodles with mixed vegetables',18),('Paneer Butter Masala','Veg','Indian','Rich and creamy paneer curry',20),('Schezwan Noodles','Vegan','Chinese','Spicy noodles with vegetables in Schezwan sauce',15),('Vegetable Biryani','Veg','Indian','Aromatic rice dish with mixed vegetables',15);
/*!40000 ALTER TABLE `DISH` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DISH_REQUIREMENT`
--

DROP TABLE IF EXISTS `DISH_REQUIREMENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DISH_REQUIREMENT` (
  `Dish_Name` varchar(25) NOT NULL,
  `Ingredient` varchar(25) NOT NULL,
  PRIMARY KEY (`Dish_Name`,`Ingredient`),
  KEY `fk_dishreq_ing` (`Ingredient`),
  CONSTRAINT `fk_dishreq_dish` FOREIGN KEY (`Dish_Name`) REFERENCES `DISH` (`Name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_dishreq_ing` FOREIGN KEY (`Ingredient`) REFERENCES `INGREDIENT` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DISH_REQUIREMENT`
--

LOCK TABLES `DISH_REQUIREMENT` WRITE;
/*!40000 ALTER TABLE `DISH_REQUIREMENT` DISABLE KEYS */;
INSERT INTO `DISH_REQUIREMENT` VALUES ('Chicken Parmesan','Chicken Breast'),('Masala Dosa','Dosa Batter'),('Margherita Pasta','Mozzarella Cheese'),('Margherita Pizza','Mozzarella Cheese'),('Noodles Stir-Fry','Noodles'),('Schezwan Noodles','Noodles'),('Paneer Butter Masala','Paneer'),('Margherita Pasta','Pasta'),('Margherita Pizza','Pizza Dough'),('Vegetable Biryani','Rice'),('Margherita Pizza','Tomato Sauce');
/*!40000 ALTER TABLE `DISH_REQUIREMENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GIVES`
--

DROP TABLE IF EXISTS `GIVES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `GIVES` (
  `Phone_No` char(10) NOT NULL,
  `Order_Number` int NOT NULL,
  `Date` date NOT NULL,
  `Waiter_ID` char(6) NOT NULL,
  PRIMARY KEY (`Phone_No`,`Order_Number`,`Date`,`Waiter_ID`),
  KEY `fk_gives_waiter` (`Waiter_ID`),
  CONSTRAINT `fk_gives_orderinfo1` FOREIGN KEY (`Phone_No`, `Order_Number`, `Date`) REFERENCES `ORDER_INFO` (`Customer_Phone_No`, `Order_Number`, `Date`),
  CONSTRAINT `fk_gives_waiter` FOREIGN KEY (`Waiter_ID`) REFERENCES `WAITER` (`Waiter_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GIVES`
--

LOCK TABLES `GIVES` WRITE;
/*!40000 ALTER TABLE `GIVES` DISABLE KEYS */;
INSERT INTO `GIVES` VALUES ('1111111111',1,'2023-11-23','W006'),('1234567890',2,'2023-11-24','W007'),('5555555555',3,'2023-11-25','W008'),('9876543210',4,'2023-11-26','W009'),('9998887777',5,'2023-11-27','W010');
/*!40000 ALTER TABLE `GIVES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `INGREDIENT`
--

DROP TABLE IF EXISTS `INGREDIENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `INGREDIENT` (
  `Name` varchar(25) NOT NULL,
  `Quantity_in_hand` int DEFAULT NULL,
  `Supplier_ID` char(6) DEFAULT NULL,
  PRIMARY KEY (`Name`),
  KEY `fk_ing_sup` (`Supplier_ID`),
  CONSTRAINT `fk_ing_sup` FOREIGN KEY (`Supplier_ID`) REFERENCES `SUPPLIER` (`Supplier_ID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `INGREDIENT`
--

LOCK TABLES `INGREDIENT` WRITE;
/*!40000 ALTER TABLE `INGREDIENT` DISABLE KEYS */;
INSERT INTO `INGREDIENT` VALUES ('Aromatic Spices',50,'SUP010'),('Chicken Breast',50,'SUP001'),('Dosa Batter',40,'SUP011'),('Mozzarella Cheese',20,'SUP012'),('Noodles',60,'SUP005'),('Paneer',35,'SUP006'),('Pasta',30,'SUP002'),('Pizza Dough',25,'SUP011'),('Rice',100,'SUP007'),('Tomato Sauce',40,'SUP012');
/*!40000 ALTER TABLE `INGREDIENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ORDER_DISHES`
--

DROP TABLE IF EXISTS `ORDER_DISHES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ORDER_DISHES` (
  `Order_Number` int NOT NULL,
  `Date` date NOT NULL,
  `Customer_Phone_No` char(10) NOT NULL,
  `Dish_name` varchar(25) NOT NULL,
  PRIMARY KEY (`Order_Number`,`Date`,`Customer_Phone_No`,`Dish_name`),
  KEY `fk_orderdishes_orderinfo` (`Customer_Phone_No`,`Order_Number`,`Date`),
  KEY `fk_orderdishes_dish` (`Dish_name`),
  CONSTRAINT `fk_orderdishes_dish` FOREIGN KEY (`Dish_name`) REFERENCES `DISH` (`Name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_orderdishes_orderinfo` FOREIGN KEY (`Customer_Phone_No`, `Order_Number`, `Date`) REFERENCES `ORDER_INFO` (`Customer_Phone_No`, `Order_Number`, `Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ORDER_DISHES`
--

LOCK TABLES `ORDER_DISHES` WRITE;
/*!40000 ALTER TABLE `ORDER_DISHES` DISABLE KEYS */;
INSERT INTO `ORDER_DISHES` VALUES (1,'2023-11-23','1111111111','Chicken Parmesan'),(2,'2023-11-24','1234567890','Margherita Pasta'),(3,'2023-11-25','5555555555','Noodles Stir-Fry'),(4,'2023-11-26','9876543210','Masala Dosa'),(5,'2023-11-27','9998887777','Vegetable Biryani');
/*!40000 ALTER TABLE `ORDER_DISHES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ORDER_INFO`
--

DROP TABLE IF EXISTS `ORDER_INFO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ORDER_INFO` (
  `Order_Number` int NOT NULL,
  `Date` date NOT NULL,
  `Time` time DEFAULT NULL,
  `Total_price` int DEFAULT NULL,
  `Customer_Phone_No` char(10) NOT NULL,
  `Rating` int DEFAULT NULL,
  `Comment` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Order_Number`,`Customer_Phone_No`,`Date`),
  KEY `fk_orderinfo_customer` (`Customer_Phone_No`),
  CONSTRAINT `fk_orderinfo_customer` FOREIGN KEY (`Customer_Phone_No`) REFERENCES `CUSTOMER` (`Phone_No`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ORDER_INFO_chk_1` CHECK ((`Rating` between 1 and 10))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ORDER_INFO`
--

LOCK TABLES `ORDER_INFO` WRITE;
/*!40000 ALTER TABLE `ORDER_INFO` DISABLE KEYS */;
INSERT INTO `ORDER_INFO` VALUES (1,'2023-11-23','18:30:00',50,'1111111111',4,'Great service!'),(2,'2023-11-24','19:15:00',45,'1234567890',5,'Excellent experience'),(3,'2023-11-25','20:00:00',30,'5555555555',3,'Average food quality'),(4,'2023-11-26','18:45:00',70,'9876543210',4,'Enjoyed the meal'),(5,'2023-11-27','21:00:00',40,'9998887777',5,'Amazing flavors');
/*!40000 ALTER TABLE `ORDER_INFO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SUPPLIER`
--

DROP TABLE IF EXISTS `SUPPLIER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SUPPLIER` (
  `Supplier_ID` char(6) NOT NULL,
  `Fname` varchar(25) DEFAULT NULL,
  `Mname` varchar(25) DEFAULT NULL,
  `Lname` varchar(25) DEFAULT NULL,
  `House_No` varchar(25) DEFAULT NULL,
  `Street` varchar(127) DEFAULT NULL,
  `Pincode` int DEFAULT NULL,
  `Phone_No` char(10) DEFAULT NULL,
  `Transaction_Amount` int DEFAULT NULL,
  PRIMARY KEY (`Supplier_ID`),
  KEY `fk_pin_pin` (`Pincode`),
  CONSTRAINT `fk_pin_pin` FOREIGN KEY (`Pincode`) REFERENCES `SUPPLIER_PIN` (`Pincode`),
  CONSTRAINT `SUPPLIER_chk_1` CHECK (((`Pincode` >= 110001) and (`Pincode` <= 858434)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SUPPLIER`
--

LOCK TABLES `SUPPLIER` WRITE;
/*!40000 ALTER TABLE `SUPPLIER` DISABLE KEYS */;
INSERT INTO `SUPPLIER` VALUES ('SUP001','Ramesh','Kumar','Agarwal','12','Main Road',110001,'9876543210',5000),('SUP002','Sunita','Dev','Sharma','45','Market Street',560001,'8765432109',6000),('SUP005','Vijay','Kumar','Verma','78','Gandhi Nagar',500032,'7654321098',7000),('SUP006','Sangeeta','Singh','Chauhan','23','MG Road',400001,'6543210987',5500),('SUP007','Anand','Prakash','Joshi','56','Lajpat Nagar',110024,'5432109876',8000),('SUP010','Preeti','Rajesh','Verma','67','Viman Nagar',411014,'2109876543',7500),('SUP011','Sarika','Suresh','Mehra','89','Kormangala',560034,'4321098765',4500),('SUP012','Alok','Kumar','Sharma','34','Bandra',400050,'3210987654',9000);
/*!40000 ALTER TABLE `SUPPLIER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SUPPLIER_PIN`
--

DROP TABLE IF EXISTS `SUPPLIER_PIN`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SUPPLIER_PIN` (
  `Pincode` int NOT NULL,
  `City` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Pincode`),
  CONSTRAINT `SUPPLIER_PIN_chk_1` CHECK ((`Pincode` between 110001 and 858434))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SUPPLIER_PIN`
--

LOCK TABLES `SUPPLIER_PIN` WRITE;
/*!40000 ALTER TABLE `SUPPLIER_PIN` DISABLE KEYS */;
INSERT INTO `SUPPLIER_PIN` VALUES (110001,'Delhi'),(110024,'Delhi'),(400001,'Mumbai'),(400050,'Mumbai'),(411014,'Pune'),(500032,'Hyderabad'),(560001,'Bangalore'),(560034,'Bangalore');
/*!40000 ALTER TABLE `SUPPLIER_PIN` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TABLE_INFO`
--

DROP TABLE IF EXISTS `TABLE_INFO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TABLE_INFO` (
  `Table_Number` int NOT NULL,
  `Section_Type` enum('Private Room','Dining','Terrace') DEFAULT NULL,
  `Seating_Capacity` int DEFAULT NULL,
  `Status` enum('Occupied','Not occupied') DEFAULT 'Not occupied',
  PRIMARY KEY (`Table_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TABLE_INFO`
--

LOCK TABLES `TABLE_INFO` WRITE;
/*!40000 ALTER TABLE `TABLE_INFO` DISABLE KEYS */;
INSERT INTO `TABLE_INFO` VALUES (1,'Dining',4,'Occupied'),(2,'Dining',4,'Occupied'),(3,'Terrace',6,'Occupied'),(4,'Private Room',8,'Occupied'),(5,'Terrace',6,'Occupied'),(6,'Dining',4,'Not occupied'),(7,'Terrace',6,'Not occupied'),(8,'Dining',4,'Not occupied'),(9,'Private Room',8,'Not occupied'),(10,'Terrace',6,'Not occupied');
/*!40000 ALTER TABLE `TABLE_INFO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WAITER`
--

DROP TABLE IF EXISTS `WAITER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `WAITER` (
  `Fname` varchar(25) DEFAULT NULL,
  `Mname` varchar(25) DEFAULT NULL,
  `Lname` varchar(25) DEFAULT NULL,
  `Waiter_ID` char(6) NOT NULL,
  `Date_of_join` date DEFAULT NULL,
  `Rating` int DEFAULT NULL,
  `Number_of_tables_served_this_month` int DEFAULT NULL,
  `Salary` int DEFAULT NULL,
  `Mentor_ID` char(6) DEFAULT NULL,
  PRIMARY KEY (`Waiter_ID`),
  KEY `fk_waiter_waiterment` (`Mentor_ID`),
  CONSTRAINT `fk_waiter_waiterment` FOREIGN KEY (`Mentor_ID`) REFERENCES `WAITER` (`Waiter_ID`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `WAITER_chk_1` CHECK ((`Rating` between 1 and 5))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WAITER`
--

LOCK TABLES `WAITER` WRITE;
/*!40000 ALTER TABLE `WAITER` DISABLE KEYS */;
INSERT INTO `WAITER` VALUES ('Ryan','A','Johnson','W006','2013-05-20',4,28,58000,NULL),('Sophie','B','Miller','W007','2015-10-12',3,22,50000,NULL),('Lucas','C','Martinez','W008','2017-03-28',4,30,60000,NULL),('Isabella','D','Taylor','W009','2020-08-15',4,26,54000,NULL),('Elijah','E','White','W010','2022-02-10',3,35,62000,NULL);
/*!40000 ALTER TABLE `WAITER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WAITER_SHIFT`
--

DROP TABLE IF EXISTS `WAITER_SHIFT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `WAITER_SHIFT` (
  `Waiter_ID` char(6) NOT NULL,
  `Shift_Start_time` time NOT NULL,
  `Shift_end_time` time NOT NULL,
  PRIMARY KEY (`Waiter_ID`,`Shift_Start_time`,`Shift_end_time`),
  CONSTRAINT `fk_waitershift_waiter` FOREIGN KEY (`Waiter_ID`) REFERENCES `WAITER` (`Waiter_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WAITER_SHIFT`
--

LOCK TABLES `WAITER_SHIFT` WRITE;
/*!40000 ALTER TABLE `WAITER_SHIFT` DISABLE KEYS */;
INSERT INTO `WAITER_SHIFT` VALUES ('W006','08:00:00','16:00:00'),('W007','12:00:00','20:00:00'),('W008','16:00:00','00:00:00'),('W009','09:00:00','17:00:00'),('W010','14:00:00','22:00:00');
/*!40000 ALTER TABLE `WAITER_SHIFT` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-03  3:28:00
