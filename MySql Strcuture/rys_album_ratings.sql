-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: rys
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `album_ratings`
--

DROP TABLE IF EXISTS `album_ratings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album_ratings` (
  `id_user` int NOT NULL,
  `id_album` varchar(22) NOT NULL,
  `simple_avg_rating` decimal(2,2) DEFAULT NULL,
  `more_than_nine_rating` decimal(2,2) DEFAULT NULL,
  `weight_rating` decimal(2,2) DEFAULT NULL,
  `suggested_rating_a` decimal(2,2) DEFAULT NULL,
  `suggested_rating_b` decimal(2,2) DEFAULT NULL,
  `user_final_rating` decimal(2,2) DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_user`,`id_album`),
  KEY `album_ratings_ibfk_2` (`id_album`),
  CONSTRAINT `album_ratings_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id`),
  CONSTRAINT `album_ratings_ibfk_2` FOREIGN KEY (`id_album`) REFERENCES `albums` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album_ratings`
--

LOCK TABLES `album_ratings` WRITE;
/*!40000 ALTER TABLE `album_ratings` DISABLE KEYS */;
INSERT INTO `album_ratings` VALUES (1,'05J8PFXdYKeYNb8YjqqJYr',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:06:04','2023-06-01 23:06:04'),(1,'0CA2EVHhRPR5VPV78KZw89',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:01:34','2023-06-01 23:01:34'),(1,'0CoNLgOwcZGBUSwd9fAZuy',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:03:13','2023-06-01 23:03:13'),(1,'0DQyTVcDhK9wm0f6RaErWO',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:58:18','2023-06-01 22:58:18'),(1,'0ETFjACtuP2ADo6LFhL6HN',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:13:11','2023-06-01 23:13:11'),(1,'0hB42ZAD897hziy7Jfe6Si',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:01:40','2023-06-01 23:01:40'),(1,'0HHmJpwOXXRJu9HI9iQiEO',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:17:52','2023-06-01 23:17:52'),(1,'0Hre57CORsiZN5rwHunPQu',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:36:01','2023-06-01 22:36:01'),(1,'0JfCEzWgcuUxrAUZw5eUT4',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:41:55','2023-06-01 22:41:55'),(1,'0jTGHV5xqHPvEcwL8f6YU5',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:13:43','2023-06-01 23:13:43'),(1,'0kL3TYRsSXnu0iJvFO3rud',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:45:57','2023-06-01 22:45:57'),(1,'0nZUgRGeIf1YcKmAK6F5yq',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:50:56','2023-06-01 22:50:56'),(1,'0PT5m6hwPRrpBwIHVnvbFX',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:13:22','2023-06-01 23:13:22'),(1,'0Pv5bdtwTTBSHy9GyUe9um',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:23:05','2023-06-01 20:23:05'),(1,'0SeTonJJPjy57LqiCDmeEM',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:39:24','2023-06-01 22:39:24'),(1,'0um9FI6BLBldL5POP4D4Cw',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:14:45','2023-06-01 23:14:45'),(1,'0vVekV45lOaVKs6RZQQNob',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:47:12','2023-06-01 22:47:12'),(1,'0w0jXq1fLPMPCNsVmmxNnc',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:34:32','2023-06-01 22:34:32'),(1,'0xawWBAjFaa8dk7IJJsIFH',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:09:18','2023-06-01 23:09:18'),(1,'13dGZzRzFoejmyVXAbTPAH',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:49:51','2023-06-01 22:49:51'),(1,'14gI3ml0wxlgVrX1ve8zyJ',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:00:54','2023-06-01 23:00:54'),(1,'15Fb7HPHdy42No0l9KnXAZ',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:55:18','2023-06-01 22:55:18'),(1,'1aYdiJk6XKeHWGO3FzHHTr',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:13:46','2023-06-01 23:13:46'),(1,'1B5Lwt0D1ZetRreaCBYobP',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:36:19','2023-06-01 22:36:19'),(1,'1c7eigkoEcDAKKhkajY3Br',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:51:52','2023-06-01 22:51:52'),(1,'1DMMv1Kmoli3Y9fVEZDUVC',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:07:03','2023-06-01 23:07:03'),(1,'1GXMNFfoHF4sN7lG8gZq1j',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:19:30','2023-06-01 23:19:30'),(1,'1HrMmB5useeZ0F5lHrMvl0',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:56:45','2023-06-01 22:56:45'),(1,'1j57Q5ntVi7crpibb0h4sv',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:14:52','2023-06-01 23:14:52'),(1,'1klALx0u4AavZNEvC4LrTL',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:13:16','2023-06-01 23:13:16'),(1,'1lM5IfaqcIsXd6UCV3aDSs',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:33:34','2023-06-01 22:33:34'),(1,'1Lr3IdIToxtcNiCLcf04MB',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:05:35','2023-06-01 23:05:35'),(1,'1p12OAWwudgMqfMzjMvl2a',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:21:29','2023-06-01 20:21:29'),(1,'1pOl0KEC1iQnA6F0XxV4To',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:12:02','2023-06-01 23:12:02'),(1,'1td0hx7C7mdZGvekzMD1CL',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:46:35','2023-06-01 22:46:35'),(1,'1Tf6V7olrJ32d4DhqWVTgM',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:06:44','2023-06-01 23:06:44'),(1,'1vANZV20H5B4Fk6yf7Ot9a',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:14:03','2023-06-01 23:14:03'),(1,'1vdQ5t7iO2gC3OX7j2GFCt',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:56:52','2023-06-01 22:56:52'),(1,'1VW1MFNstaJuygaoTPkdCk',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:55:03','2023-06-01 22:55:03'),(1,'1WBZyULtlANBKed7Zf9cDP',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:21:15','2023-06-01 20:21:15'),(1,'1WrK98KVZxkTgMD3a9Kpnl',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:31:54','2023-06-01 20:31:54'),(1,'1zOxlHQGGV6EH7n4OIFTyh',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:34:26','2023-06-01 22:34:26'),(1,'20IklXmkirz07Lpv6jnLNB',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:35:04','2023-06-01 22:35:04'),(1,'20r762YmB5HeofjMCiPMLv',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:43:51','2023-06-01 22:43:51'),(1,'25mCHdzcOvPkKjMOnbjgtK',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:03:37','2023-06-01 23:03:37'),(1,'277GP8d3KlBSQwMZJza6pe',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:30:43','2023-06-01 20:30:43'),(1,'29U9LtzSF0ftWiLNNw1CP6',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:38:24','2023-06-01 22:38:24'),(1,'2Aiv0ThDpFa7lqHphR6MN5',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:52:46','2023-06-01 22:52:46'),(1,'2BRqfk8jL7y3egZqlc5MkU',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:30:24','2023-06-01 20:30:24'),(1,'2BtE7qm1qzM80p9vLSiXkj',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:13:51','2023-06-01 23:13:51'),(1,'2BwbUYJeuUsv6LUA6GZHB4',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:50:17','2023-06-01 22:50:17'),(1,'2cGrlR3OJwtQXUa4aQJRCV',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:31:57','2023-06-01 20:31:57'),(1,'2CNEkSE8TADXRT2AzcEt1b',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:06:18','2023-06-01 23:06:18'),(1,'2dR2ZmzPqVoBK9vxHNjEUo',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:44:56','2023-06-01 22:44:56'),(1,'2GuROKcqyHdpIDcgxml1C7',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:01:20','2023-06-01 23:01:20'),(1,'2HOf3Nb44Us8U9oEtKLSrX',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:17:45','2023-06-01 23:17:45'),(1,'2ix8vWvvSp2Yo7rKMiWpkg',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:57:03','2023-06-01 22:57:03'),(1,'2jOgajtpXNsinBpwg2dUjH',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:17:13','2023-06-01 23:17:13'),(1,'2JR65ppK6Z6h1lfV5fy7Fr',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:39:41','2023-06-01 22:39:41'),(1,'2mPZNQNgW1zrkIPyL9XJcf',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:31:46','2023-06-01 20:31:46'),(1,'2n5AOB0lGse7qp38HvVROB',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:08:15','2023-06-01 23:08:15'),(1,'2nkto6YNI4rUYTLqEwWJ3o',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:19:06','2023-06-01 23:19:06'),(1,'2NnkLRaeX33d1Mn8ZLgTo8',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:09:44','2023-06-01 23:09:44'),(1,'2noRn2Aes5aoNVsU6iWThc',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:42:43','2023-06-01 20:42:43'),(1,'2oj3FG6fos7zAQJxLQGzou',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:33:53','2023-06-01 20:33:53'),(1,'2Om4oR7plGGub1aYe5uB7B',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:52:51','2023-06-01 22:52:51'),(1,'2P2Xwvh2xWXIZ1OWY9S9o5',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:39:58','2023-06-01 22:39:58'),(1,'2qIu18hUz5c6BzY3Rh6fIJ',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:10:02','2023-06-01 23:10:02'),(1,'2Qs2SpclDToB087fLolhCN',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:00:31','2023-06-01 23:00:31'),(1,'2scB1uhcCI1TSf6b9TCZK3',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:44:18','2023-06-01 22:44:18'),(1,'2tA6VFMIQuSF3KpXsrulw9',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:37:00','2023-06-01 22:37:00'),(1,'2VHpCS4RKmaIHoaIBZFeip',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:23:08','2023-06-01 20:23:08'),(1,'2wA3MvoZFWXgOJqoY5ebyK',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:50:13','2023-06-01 22:50:13'),(1,'2wa3NSRvKgsUqIuEgRcl6K',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:48:31','2023-06-01 22:48:31'),(1,'2Xbd3EI9auhlw5WOKnNX3H',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:28:51','2023-06-01 20:28:51'),(1,'2xkZV2Hl1Omi8rk2D7t5lN',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:15:26','2023-06-01 23:15:26'),(1,'2YJo8wNg6DLNM5HnvKscxJ',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:52:26','2023-06-01 22:52:26'),(1,'2ymwUMeW3BySLhKNp8UQZ3',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:02:25','2023-06-01 23:02:25'),(1,'2yNaksHgeMQM9Quse463b5',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:15:30','2023-06-01 23:15:30'),(1,'2zcMgU6PAlLUDQMqZcxxUU',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:19:34','2023-06-01 23:19:34'),(1,'30iqYID1JMBXLVFfErwTSd',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:01:37','2023-06-01 23:01:37'),(1,'32hXKuDkMnpQaOI67xQj86',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:44:11','2023-06-01 20:44:11'),(1,'3539EbNgIdEDGBKkUf4wno',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:58:34','2023-06-01 22:58:34'),(1,'35UJLpClj5EDrhpNIi4DFg',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:56:31','2023-06-01 22:56:31'),(1,'3AOI0WbFQWOvgRZQrMPGXG',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:47:35','2023-06-01 22:47:35'),(1,'3BYlBcND6PeKoW6ZODjZO3',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:11:48','2023-06-01 23:11:48'),(1,'3C2MFZ2iHotUQOSBzdSvM7',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:04:13','2023-06-01 23:04:13'),(1,'3FR8CV7OSyZDnxneavnh8t',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:07:06','2023-06-01 23:07:06'),(1,'3gBVdu4a1MMJVMy6vwPEb8',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:56:24','2023-06-01 22:56:24'),(1,'3GmCXW10kLxmZrEY0JpRlw',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:14:08','2023-06-01 23:14:08'),(1,'3HFbH1loOUbqCyPsLuHLLh',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:15:38','2023-06-01 23:15:38'),(1,'3jRLyc2t1tExfVpdB88EUm',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:05:13','2023-06-01 23:05:13'),(1,'3k8xoyOXkGgZxUKgpmxz4P',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:37:56','2023-06-01 22:37:56'),(1,'3knDOJUQBAATXsKYLWO4k8',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:27:21','2023-06-01 20:27:21'),(1,'3KzAvEXcqJKBF97HrXwlgf',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:13:19','2023-06-01 23:13:19'),(1,'3ly9T2L4pqTZijFgQssd3x',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:58:57','2023-06-01 22:58:57'),(1,'3NcGNYXKiHeygdXXL7czL1',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:33:07','2023-06-01 20:33:07'),(1,'3p7WXDBxhC5KS9IFXnwae7',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:27:28','2023-06-01 20:27:28'),(1,'3PRoXYsngSwjEQWR5PsHWR',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:13:55','2023-06-01 23:13:55'),(1,'3QTmNqASavj7H8DPhFss1r',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:47:16','2023-06-01 22:47:16'),(1,'3tshnNFNhHrO6NUQ0BHw42',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:10:37','2023-06-01 23:10:37'),(1,'3wdD2PQkm8N4ezZf732Oxv',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:12:27','2023-06-01 23:12:27'),(1,'48D1hRORqJq52qsnUYZX56',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:52:45','2023-06-01 20:52:45'),(1,'4BnNSzOWadogStvyYshJIo',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:58:37','2023-06-01 22:58:37'),(1,'4DILWb0ZQcBYBfmtJTSfpJ',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:08:50','2023-06-01 23:08:50'),(1,'4eLPsYPBmXABThSJ821sqY',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:45:14','2023-06-01 22:45:14'),(1,'4eMxaP2VDkK8yKP38Q8fkY',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:48:05','2023-06-01 22:48:05'),(1,'4GGazqHvuKwxBjWLFaJkDL',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:43:39','2023-06-01 22:43:39'),(1,'4GqinDAWUcJ20wfCaie6f8',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:56:48','2023-06-01 22:56:48'),(1,'4hm0QL0lk1Cp7hcq0GU0UZ',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:52:23','2023-06-01 22:52:23'),(1,'4k61t42VwBmNE7zmlZi0yJ',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:03:52','2023-06-01 23:03:52'),(1,'4L4tcx3itXbtx5kuchKhFE',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:08:19','2023-06-01 23:08:19'),(1,'4LaRYkT4oy47wEuQgkLBul',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:07:33','2023-06-01 23:07:33'),(1,'4m2880jivSbbyEGAKfITCa',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:42:37','2023-06-01 20:42:37'),(1,'4mTFNkSq63GHT8i1HKC0nZ',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:39:43','2023-06-01 20:39:43'),(1,'4RzYS74QxvpqTDVwKbhuSg',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:35:30','2023-06-01 22:35:30'),(1,'4sW8Eql2e2kdRP1A1R1clG',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:38:38','2023-06-01 22:38:38'),(1,'4tI4WJdTN5MzDMRMl2i7VR',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:55:41','2023-06-01 22:55:41'),(1,'4tUVkNYSFrrEqqrxBQW9PN',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:34:05','2023-06-01 22:34:05'),(1,'4TyyZazCkju7vwioaV1KyE',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:21:46','2023-06-01 20:21:46'),(1,'4u3MPfHM60rFFULJebZIay',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:27:24','2023-06-01 20:27:24'),(1,'4usPTyIIgnAZ9eiItfEYSK',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:25:50','2023-06-01 20:25:50'),(1,'4Uv86qWpGTxf7fU7lG5X6F',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:44:00','2023-06-01 22:44:00'),(1,'4xbivyNgO8FTIfxnzBtr5j',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:18:30','2023-06-01 23:18:30'),(1,'4xwx0x7k6c5VuThz5qVqmV',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:17:42','2023-06-01 23:17:42'),(1,'50o7kf2wLwVmOTVYJOTplm',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:13:29','2023-06-01 23:13:29'),(1,'51AxfjN2gEt5qeJqPY5w0e',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:25:33','2023-06-01 20:25:33'),(1,'53eHm1f3sFiSzWMaKOl98Z',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:10:53','2023-06-01 23:10:53'),(1,'55RhFRyQFihIyGf61MgcfV',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:00:24','2023-06-01 23:00:24'),(1,'5DM1qCdgGt2zbknnsVn1Ca',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:15:03','2023-06-01 23:15:03'),(1,'5fedTyx7AnXeyxLL0giq6x',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:19:27','2023-06-01 23:19:27'),(1,'5fMlysqhFE0itGn4KezMBW',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:38:50','2023-06-01 22:38:50'),(1,'5G5UwqPsxDKpxJLX4xsyuh',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:44:42','2023-06-01 22:44:42'),(1,'5hryhrT7wEdLnZCbJX9F6L',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:34:23','2023-06-01 22:34:23'),(1,'5HSUjEYLmSEsAo4DrkMxSE',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:03:45','2023-06-01 23:03:45'),(1,'5IFOummNcGXY3qCBWRchqP',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:11:08','2023-06-01 23:11:08'),(1,'5IO0ppb7WMdyanUnnBCR0M',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:59:15','2023-06-01 22:59:15'),(1,'5JLKZcOSNXcm6xaX1vI7nB',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:04:37','2023-06-01 23:04:37'),(1,'5lEphbceIgaK1XxWeSrC9E',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:42:15','2023-06-01 20:42:15'),(1,'5lKYNLYykoFAVRAeV5EqPE',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:48:14','2023-06-01 22:48:14'),(1,'5ll74bqtkcXlKE7wwkMq4g',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:43:55','2023-06-01 22:43:55'),(1,'5mzoI3VH0ZWk1pLFR6RoYy',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:56:41','2023-06-01 22:56:41'),(1,'5NKTuBLCYhN0OwqFiGdXd1',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:44:47','2023-06-01 22:44:47'),(1,'5OEz7YwAQyYvaSl1pmkPCI',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:18:55','2023-06-01 23:18:55'),(1,'5TiPpuwLSWSJl98yTyE8BK',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:24:49','2023-06-01 20:24:49'),(1,'5vkqYmiPBYLaalcmjujWxK',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:56:34','2023-06-01 22:56:34'),(1,'5WsCU95SaumguegxnC87TV',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:54:48','2023-06-01 22:54:48'),(1,'5XpEKORZ4y6OrCZSKsi46A',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:53:12','2023-06-01 22:53:12'),(1,'5Y0p2XCgRRIjna91aQE8q7',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:14:56','2023-06-01 23:14:56'),(1,'5y5Qnze6BJUbON6FxndO9c',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:00:17','2023-06-01 23:00:17'),(1,'5zfhhKXHK0YQdvacCs1ErM',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:54:40','2023-06-01 22:54:40'),(1,'5zi7WsKlIiUXv09tbGLKsE',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:19:10','2023-06-01 23:19:10'),(1,'64TDaAbxgO0TmKZrIavdLg',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:58:08','2023-06-01 22:58:08'),(1,'6acGx168JViE5LLFR1rGRE',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:20:25','2023-06-01 23:20:25'),(1,'6aSk2vxoY3xtz7cXKuY9EL',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:53:40','2023-06-01 22:53:40'),(1,'6aZ07R6mxyg52G9TEKCvKw',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:42:38','2023-06-01 22:42:38'),(1,'6BRq5g6CWiFgN3NrjLGAYq',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:21:42','2023-06-01 20:21:42'),(1,'6cI1XoZsOhkyrCwtuI70CN',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:14:59','2023-06-01 23:14:59'),(1,'6dVIqQ8qmQ5GBnJ9shOYGE',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:56:28','2023-06-01 22:56:28'),(1,'6fQElzBNTiEMGdIeY0hy5l',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:52:55','2023-06-01 20:52:55'),(1,'6GjwtEZcfenmOf6l18N7T7',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:56:37','2023-06-01 22:56:37'),(1,'6LZiNXaDvhzvnXUubVOmNU',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:28:10','2023-06-01 20:28:10'),(1,'6nzpuAXn43S5FwBrzxFsna',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:05:30','2023-06-01 23:05:30'),(1,'6PanEvuo9ZNvGT39v50xp6',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:21:09','2023-06-01 23:21:09'),(1,'6PBZN8cbwkqm1ERj2BGXJ1',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:45:18','2023-06-01 22:45:18'),(1,'6QaVfG1pHYl1z15ZxkvVDW',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:13:58','2023-06-01 23:13:58'),(1,'6Sts4Yh7KsDFwq2yTWrGGV',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:34:21','2023-06-01 20:34:21'),(1,'6t4LdKTNWIOr2PZIB8tiZF',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:48:10','2023-06-01 22:48:10'),(1,'6TgkNOiJxeSkVVbXV720B1',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:43:29','2023-06-01 20:43:29'),(1,'6tVg2Wl9hVKMpHYcAl2V2M',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:49:39','2023-06-01 22:49:39'),(1,'6wCttLq0ADzkPgtRnUihLV',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:13:26','2023-06-01 23:13:26'),(1,'6ZB8qaR9JNuS0Q0bG1nbcH',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:22:34','2023-06-01 20:22:34'),(1,'6ZiwdJgvbvWILwuObZc8wS',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:40:16','2023-06-01 22:40:16'),(1,'6zTAW5oRuOmxJuUHhcQope',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:56:58','2023-06-01 22:56:58'),(1,'716fnrS2qXChPC3J2X73pK',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:50:43','2023-06-01 22:50:43'),(1,'748dZDqSZy6aPXKcI9H80u',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:45:43','2023-06-01 22:45:43'),(1,'79dL7FLiJFOO0EoehUHQBv',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:04:10','2023-06-01 23:04:10'),(1,'7aNclGRxTysfh6z0d8671k',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:22:09','2023-06-01 20:22:09'),(1,'7aPolrSqVawIhC7iTo2b5F',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:37:41','2023-06-01 22:37:41'),(1,'7btiyhWzUfzxN3ijSiBpC8',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:07:51','2023-06-01 23:07:51'),(1,'7d7WtcAp4qNtfwOqzAPQMJ',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:24:45','2023-06-01 20:24:45'),(1,'7EJ5pXrSqqfybKyfbvlz84',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:30:58','2023-06-01 20:30:58'),(1,'7FiPNXyrCGGWFqO4btxPEe',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:51:32','2023-06-01 22:51:32'),(1,'7glwer1Pzyns4h32fHbl53',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:00:41','2023-06-01 23:00:41'),(1,'7gsWAHLeT0w7es6FofOXk1',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:43:48','2023-06-01 22:43:48'),(1,'7HNrDkHNFopKBXGWf0UZML',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:25:55','2023-06-01 20:25:55'),(1,'7J84ixPVFehy6FcLk8rhk3',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:37:44','2023-06-01 22:37:44'),(1,'7jfexk2w5aDI25njkN0UGg',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:15:07','2023-06-01 23:15:07'),(1,'7oNSmwtmqu8EvnD3cv2HOr',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:31:43','2023-06-01 20:31:43'),(1,'7pBPB9vwqCMLKNmUCK4k62',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:42:18','2023-06-01 20:42:18'),(1,'7pi7cx7tlpJWQwoWYpvlZk',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:54:17','2023-06-01 22:54:17'),(1,'7u6zL7kqpgLPISZYXNTgYk',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 20:42:53','2023-06-01 20:42:53'),(1,'7uUltiwqvVn8Uy23Hdf1kE',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:04:34','2023-06-01 23:04:34'),(1,'7ycBtnsMtyVbbwTfJwRjSP',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 22:45:48','2023-06-01 22:45:48'),(1,'7ysKTnHt4ve0MvIWm3vPdz',NULL,NULL,NULL,NULL,NULL,NULL,'2023-06-01 23:00:34','2023-06-01 23:00:34');
/*!40000 ALTER TABLE `album_ratings` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-01 23:24:49