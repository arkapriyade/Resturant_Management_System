CREATE DATABASE  IF NOT EXISTS `rms_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `rms_db`;
-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: rms_db
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `rms_book_table`
--

LOCK TABLES `rms_book_table` WRITE;
/*!40000 ALTER TABLE `rms_book_table` DISABLE KEYS */;
INSERT INTO `rms_book_table` VALUES (1,NULL),(2,'sun'),(3,NULL),(4,'astha'),(5,'astha'),(6,NULL),(7,'astha'),(8,NULL),(9,'astha'),(10,NULL);
/*!40000 ALTER TABLE `rms_book_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `rms_feedback_table`
--

LOCK TABLES `rms_feedback_table` WRITE;
/*!40000 ALTER TABLE `rms_feedback_table` DISABLE KEYS */;
INSERT INTO `rms_feedback_table` VALUES (3,'arkapriya','good food'),(4,'shreya','nice food'),(5,'arnabdey93@gmail.com','Hi this was good'),(6,'','ghjkl;'),(7,'','lkj\n');
/*!40000 ALTER TABLE `rms_feedback_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `rms_menu_table`
--

LOCK TABLES `rms_menu_table` WRITE;
/*!40000 ALTER TABLE `rms_menu_table` DISABLE KEYS */;
INSERT INTO `rms_menu_table` VALUES (1,'pizza','pizza is one of the most special food item of our resturant',300,'yes'),(2,'spring roll','spring roll is also a famous dishes of our resturant',150,'yes'),(3,'biryani','most popular dish of our resturant',300,'yes'),(4,'chilli chicken','4 pcs chicken with extra spice',100,'yes'),(5,'Butter Chicen','4 pcs chicken without bone',150,'yes'),(6,'Idli dhosa','2 pcs idli,1 pcs dhosa',100,'yes'),(7,'Mutton biryani','1 pcs Mutton with free pepsi',250,'yes'),(8,'Paneer masala','8 pcs paneer with spicy masala',120,'yes'),(9,'Roti','1 pcs roti',20,'yes'),(10,'Burger','Extra large',100,'yes'),(11,'Patis','veg patis',50,'yes'),(12,'Pepsi','coco cola',50,'yes');
/*!40000 ALTER TABLE `rms_menu_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `rms_order_table`
--

LOCK TABLES `rms_order_table` WRITE;
/*!40000 ALTER TABLE `rms_order_table` DISABLE KEYS */;
INSERT INTO `rms_order_table` VALUES (1,'16',1,'pizza',300,1,'Order ready',84,1,'2020-10-21 11:07:45'),(1,'16',2,'spring roll',150,1,'Order ready',84,1,NULL),(2,'16',1,'pizza',300,2,'Order ready',81,1,NULL),(3,'5',1,'pizza',300,2,'Bill Generated',83,4,NULL),(3,'5',2,'spring roll',150,1,'Bill Generated',83,NULL,NULL),(5,'16',1,'pizza',300,3,'Order ready',88,NULL,NULL),(6,'16',3,'biryani',300,2,'Order ready',89,NULL,NULL),(8,'16',2,'spring roll',150,2,'Order ready',92,10,NULL),(9,'16',3,'biryani',300,1,'Order ready',87,NULL,NULL),(10,'16',3,'biryani',300,1,'Order ready',91,10,'2020-10-21 11:18:44'),(11,'16',2,'spring roll',150,2,'Order ready',90,10,'2020-10-21 11:20:52'),(12,'16',12,'Pepsi',50,1,'Order ready',93,NULL,'2020-10-24 22:26:19'),(13,'16',11,'Patis',50,1,'Order ready',94,NULL,'2020-10-24 22:29:12'),(14,'16',12,'Pepsi',50,1,'Order ready',95,NULL,'2020-10-24 22:31:33'),(15,'16',6,'Idli dhosa',100,2,'Order ready',96,9,'2020-10-24 23:26:11'),(16,'25',12,'Pepsi',50,3,'Bill Generated',97,1,'2020-10-26 17:23:32'),(17,'25',9,'Roti',20,1,'Bill Generated',98,1,'2020-10-26 17:44:15'),(18,'6',12,'Pepsi',50,2,'Food is preparing',99,NULL,'2020-10-26 18:29:55'),(19,'6',12,'Pepsi',50,2,'Food is preparing',100,NULL,'2020-10-26 19:07:23'),(20,'6',12,'Pepsi',50,1,'Food is preparing',101,NULL,'2020-10-26 19:36:40'),(21,'16',12,'Pepsi',50,1,'Order ready',102,4,'2020-10-26 19:52:28'),(22,'16',12,'Pepsi',50,1,'Order ready',103,5,'2020-10-26 19:57:03'),(23,'6',12,'Pepsi',50,1,'Food is preparing',104,NULL,'2020-10-26 20:10:32'),(24,'16',12,'Pepsi',50,1,'Bill Generated',106,7,'2020-10-26 22:21:29'),(25,'16',11,'Patis',50,1,'Bill Generated',107,5,'2020-10-26 23:09:05'),(26,'6',10,'Burger',100,1,'Bill Generated',105,NULL,'2020-10-26 23:17:03'),(27,'6',8,'Paneer masala',120,1,'Bill Generated',108,NULL,'2020-10-26 23:19:39'),(28,'16',11,'Patis',50,1,'Bill Generated',109,5,'2020-10-27 10:36:49'),(29,'16',7,'Mutton biryani',250,1,'Bill Generated',110,5,'2020-10-27 10:46:39'),(30,'16',9,'Roti',20,1,'Bill Generated',111,5,'2020-10-27 10:48:23'),(31,'16',9,'Roti',20,1,'Bill Generated',112,5,'2020-10-27 10:53:32'),(32,'16',8,'Paneer masala',120,1,'Bill Generated',113,5,'2020-10-27 10:57:39'),(33,'16',10,'Burger',100,1,'Bill Generated',114,4,'2020-10-27 10:58:34'),(34,'6',9,'Roti',20,1,'Bill Generated',115,NULL,'2020-10-27 11:04:59'),(35,'16',9,'Roti',20,1,'Bill Generated',116,4,'2020-10-27 17:06:16'),(36,'16',10,'Burger',100,1,'Bill Generated',117,5,'2020-10-27 17:38:27'),(37,'16',11,'Patis',50,1,'Bill Generated',118,5,'2020-10-27 17:39:59'),(38,'16',11,'Patis',50,1,'Bill Generated',119,5,'2020-10-27 17:43:58'),(39,'16',10,'Burger',100,1,'Bill Generated',120,5,'2020-10-27 17:45:58'),(40,'16',10,'Burger',100,1,'Bill Generated',121,5,'2020-10-27 17:47:35'),(41,'16',9,'Roti',20,1,'Bill Generated',122,5,'2020-10-27 17:49:10'),(42,'16',11,'Patis',50,1,'Bill Generated',123,4,'2020-10-27 17:50:41'),(43,'16',10,'Burger',100,1,'Bill Generated',124,5,'2020-10-27 18:00:30'),(44,'16',11,'Patis',50,1,'Bill Generated',125,7,'2020-10-27 18:03:43'),(45,'16',11,'Patis',50,1,'Bill Generated',126,4,'2020-10-27 18:26:37'),(46,'16',9,'Roti',20,1,'Bill Generated',127,5,'2020-10-27 18:42:48'),(47,'16',11,'Patis',50,1,'Bill Generated',128,4,'2020-10-27 18:44:27'),(48,'16',11,'Patis',50,1,'Bill Generated',129,5,'2020-10-27 18:47:43'),(49,'16',12,'Pepsi',50,1,'Bill Generated',130,5,'2020-10-27 19:04:21'),(50,'16',9,'Roti',20,1,'Bill Generated',131,5,'2020-10-27 19:06:36'),(51,'16',10,'Burger',100,1,'Bill Generated',132,4,'2020-10-27 19:08:35'),(52,'16',11,'Patis',50,1,'Bill Generated',133,4,'2020-10-27 19:14:26'),(53,'16',9,'Roti',20,2,'Bill Generated',134,5,'2020-10-27 19:44:50'),(54,'16',9,'Roti',20,1,'Bill Generated',138,5,'2020-10-27 19:49:03'),(55,'16',9,'Roti',20,1,'Bill Generated',135,7,'2020-10-27 19:50:05'),(56,'16',9,'Roti',20,1,'Bill Generated',136,5,'2020-10-27 19:51:23'),(57,'16',11,'Patis',50,1,'Bill Generated',137,4,'2020-10-27 20:06:12'),(58,'16',7,'Mutton biryani',250,2,'Bill Generated',139,5,'2020-10-27 21:44:54'),(58,'16',8,'Paneer masala',120,2,'Bill Generated',139,5,'2020-10-27 21:44:54'),(59,'16',9,'Roti',20,1,'Bill Generated',140,5,'2020-10-27 23:14:26'),(60,'16',4,'chilli chicken',100,1,'Bill Generated',141,7,'2020-10-28 21:56:03'),(61,'16',5,'Butter Chicen',150,1,'Bill Generated',142,7,'2020-10-28 21:56:50'),(62,'16',4,'chilli chicken',100,1,'Bill Generated',143,NULL,'2020-10-28 22:00:13'),(62,'16',5,'Butter Chicen',150,1,'Bill Generated',143,NULL,'2020-10-28 22:00:13'),(63,'16',4,'chilli chicken',100,1,'Bill Generated',144,7,'2020-10-28 23:13:34'),(64,'16',4,'chilli chicken',100,3,'Bill Generated',145,5,'2020-10-29 07:30:13'),(66,'16',5,'Butter Chicen',150,3,'Order Placed',NULL,7,'2020-10-29 07:43:27'),(67,'16',6,'Idli dhosa',100,1,'Order Placed',NULL,NULL,'2020-10-29 09:25:27'),(68,'6',12,'Pepsi',50,1,'Order Placed',NULL,NULL,'2020-10-29 09:29:16');
/*!40000 ALTER TABLE `rms_order_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `rms_user_details`
--

LOCK TABLES `rms_user_details` WRITE;
/*!40000 ALTER TABLE `rms_user_details` DISABLE KEYS */;
INSERT INTO `rms_user_details` VALUES (2,'de','moon','customer','de','moon89@gmail.com','5678954378'),(3,'oil','arnab','Customer','','arnab34@gmail.com','6789065434'),(4,'arka','priya','manager','de','dear23@gmail.com','8348117410'),(5,'tom','arkapriya','customer','de','dearka01@gmail.com','8348117410'),(6,'tom','goutam','customer','de','goutam4@gmail.com',''),(10,'priya','shreya','cook','sharma','sharma34@gmail.com','8348117410'),(11,'de','sun','Customer','','srf56@gmail.com','8348117410'),(12,'tom','arnab','Customer','','akslk@gmail.com','9620500396'),(19,'tom','ashish','customer','','ash01@gmail.com','9876543214'),(20,'tom','Arkapriya de','customer','','dearkapriya01@gmail.com','8348117410'),(21,'Tom$jerry','Arkapriya','manager','','dearkapriya01@gmail.com','9620500396'),(25,'Tom$jerry@123','arnabdey93','customer','','arnabdey93@gmail.com','9620500396'),(26,'Tom$jerry','arnabdey934','manager','','arnabdey93@gmail.com','9820500396'),(27,'Tom$jerry','arnabdey9344','usertype','','arnabdey93@gmail.com','9620500396'),(28,'Tom$jerry','arnabdey9345','cook','','arnabdey93@gmail.com','9620500396');
/*!40000 ALTER TABLE `rms_user_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `temp_astha_cart`
--

LOCK TABLES `temp_astha_cart` WRITE;
/*!40000 ALTER TABLE `temp_astha_cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `temp_astha_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `temp_goutam_cart`
--

LOCK TABLES `temp_goutam_cart` WRITE;
/*!40000 ALTER TABLE `temp_goutam_cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `temp_goutam_cart` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-29  9:46:42
