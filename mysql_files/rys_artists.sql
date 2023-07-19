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
-- Table structure for table `artists`
--

DROP TABLE IF EXISTS `artists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artists` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `popularity` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artists`
--

LOCK TABLES `artists` WRITE;
/*!40000 ALTER TABLE `artists` DISABLE KEYS */;
INSERT INTO `artists` VALUES ('00FQb4jTyendYWaN8pK0wa','Lana Del Rey',91),('01C9OoXDvCKkGcf735Tcfo','Serge Gainsbourg',56),('053q0ukIDRgzwTr4vNSwab','Grimes',68),('066X20Nz7iquqkkCW6Jxy6','LCD Soundsystem',58),('09hVIj6vWgoCDtT03h8ZCa','A Tribe Called Quest',67),('09xj0S68Y1OU1vHMCZAIvz','Café Tacvba',69),('0b3fYxnG6tlR0zLtBJd8DF','DANGERDOOM',52),('0epOFNiUfyON9EYx7Tpr6V','The Strokes',76),('0IVcLMMbm05VIjnzPkGCyp','J Dilla',59),('0KDbBK1pnCWEL33tRNwDhD','Catherine O\'Hara',37),('0LVrQUinPUBFvVD5pLqmWY','Doves',47),('0LyfQWJT6nXafLPZqxe9Of','Various Artists',0),('0oSGxfWSnnOXhD2fKuz2Gy','David Bowie',77),('0wNZvrIMNUCs24G0wFg2D6','Jeff Rosenstock',49),('0x8J72N9ilqcIZbWEKB8T2','Mychael Danna',52),('164hs3x1Tsp3FgJWNHee1r','The Citizens of Halloween',43),('168dgYui7ExaU612eooDF1','Brand New',57),('16tbi6bWXBzJ9pOMZ5gIC7','Life Without Buildings',35),('1aSxMhuvixZ8h9dK9jIDwL','Kate Bush',70),('1gIa65d5ICT2xVWiUJ3u27','Tom Zé',45),('1GImnM7WYVp95431ypofy9','Caifanes',69),('1gR0gsQYfi6joyO1dlp76N','Justice',58),('1HVwzNriKEjaeE06okqSpx','Carla Bruni',60),('1KHydwFySZY3YcWyo2q2dF','Neurosis',32),('1KsASRNugxU85T0u6zSg32','Tori Amos',55),('1LBMTH4i180mwTLvTW84H3','Cast - The Nightmare Before Christmas',30),('1LxdCpPSFpzNBKyQI22aDz','Les Rallizes Dénudés',29),('1lYT0A0LV5DUfxr6doRP3d','The Stone Roses',61),('1nJvji2KIlWSseXRSlNYsC','The Velvet Underground',63),('1R84VlXnFFULOsWWV8IrCQ','Panda Bear',51),('1tqZaCwM57UFKjWoYwMLrw','The Cardigans',67),('1W8TbFzNS15VwsempfY12H','Charles Mingus',47),('1ZwdS5xdxEREPySFridCfh','2Pac',80),('20JZFwl6HVl6yg8a4H3ZqK','Panic! At The Disco',77),('2ApaG60P4r0yhBoDCGD8YG','Elliott Smith',64),('2cUnvdrMWIMACo3fSxCrWW','Mumm-ra',35),('2d0hyoQ5ynDBnkvAbJKORj','Rage Against The Machine',71),('2DaxqgrOhkeH0fpeiQq2f4','Oasis',76),('2Iv9xUxQZyMxknah773Sdw','Ed Ivory',35),('2lZkXWxkZsZzBocxMjN1or','Sunny Day Real Estate',45),('2MRBDr0crHWE5JwPceFncq','Juan Gabriel',74),('2ooIqOf4X2uz4mMptXCtie','Neutral Milk Hotel',56),('2QoU3awHVdcHS8LrZEKvSM','Wilco',60),('2uH0RyPcX7fnCcT90HFDQX','Manic Street Preachers',54),('2VAvhf61GgLYmC6C8anyX1','Boards of Canada',58),('2VYQTNDsvvKN9wmU5W7xpj','Marilyn Manson',69),('2yQf6b8hxahZaT5dHlWaB1','Raekwon',69),('2YZyLoL8N0Wb9xBt1NhZWg','Kendrick Lamar',89),('2zRt0sfxNnqI8gLR7d8gWt','She Wants Revenge',54),('31TPClRtHm23RisEBtV3X7','Justin Timberlake',79),('33ZXBbTDWd3gX0Wd0ewwxC','Le Volume Courbe',16),('34EP7KEpOjXcM2TCat1ISk','Wu-Tang Clan',69),('35C0NSLogAwImm8HAMqEmG','Black Lips',42),('36E7oYfz3LLRto6l2WmDcD','Pulp',60),('3Ayl7mCk0nScecqOzvNp6s','Jimmy Eat World',67),('3CIRif6ZAedT7kZSPvj2A4','She & Him',44),('3CjlHNtplJyTf9npxaPl5w','CHVRCHES',64),('3EgMK920cIH5aLxFnJ6zSi','Boris',40),('3g2kUQ6tHLLbmkV7T4GPtL','Fiona Apple',62),('3iTsJGG39nMg9YiolUgLMQ','Morrissey',59),('3KH6DLHeoFZgVbtKiLXb6L','The Field Mice',27),('3kjuyTCjPG1WMFCiyc5IuB','Arcade Fire',65),('3nFkdlSjzX9mRTtwJOzDYB','JAY-Z',84),('3oDbviiivRWhXwIE8hxkVV','The Beach Boys',72),('3qwabfaWewpfli7hMNM3O8','Róisín Murphy',55),('3WaJSfKnzc65VDgmj2zU8B','Interpol',64),('3WrFJ7ztbogyGnTHbHJFl2','The Beatles',84),('3yEnArbNHyTCwMRvD9SBy4','Wolfmother',60),('3yY2gUcIsjMr8hjo51PoJ8','The Smiths',76),('3z6Gk257P9jNcZbBXJNX5i','Regina Spektor',61),('40Yq4vzPs9VNUrIBG5Jr2i','The Smashing Pumpkins',72),('47QqI0kuVSCrV0KVRBZ3km','Meaghan Smith',25),('4aaBjq7VqqQvpSF69GglvO','Moloko',54),('4I2BJf80C0skQpp1sQmA0h','Belle and Sebastian',57),('4IwOItqRhsIoRuD5HP4vyC','Slint',41),('4kwxTgCKMipBKhSnEstNKj','Animal Collective',50),('4MXUO7sVCaFgFjoTI5ox5c','Sufjan Stevens',71),('4PtVXWSOmF4Tox1jj6ctSq','Plastilina Mosh',52),('4qwv0DPSYiEZvWwclqubKE','maudlin of the Well',23),('4svpOyfmQKuWpHLjgy4cdK','Godspeed You! Black Emperor',43),('4tZwfgrHOc3mvqYlEYSvVi','Daft Punk',82),('4UXqAaa6dQYAk18Lv7PEgX','Fall Out Boy',79),('4V8LLVI7PbaPR0K2TGSxFF','Tyler, The Creator',88),('4W48hZAnAHVOC2c8WH8pcq','The Temper Trap',66),('4wLIbcoqmqI4WZHDiBxeCB','Sleater-Kinney',44),('4XYH5Be5pn1qkxhfaID3J5','Jane Birkin',46),('4Z8W4fKeB5YxbusRsdQVPb','Radiohead',80),('50NoVNy9GU1lCrDV8iGpyu','Ol\' Dirty Bastard',66),('54QMjE4toDfiCryzYWCpXX','Metronomy',62),('56ZTgzPBDge0OvCGgMO3OY','Beach House',73),('5BvJzeQpmsdsFp4HGUYUEx','Vampire Weekend',66),('5CE2IfdYZEQGIDsfiRm8SI','DJ Shadow',63),('5CG9X521RDFWCuAhlo6QoR','Fela Kuti',48),('5E2rtn57BM2WPjwak4kGd5','At the Drive-In',45),('5gInJ5P5gQnOKPM3SUEVFt','Camera Obscura',43),('5INjqkS1o8h1imAzPqGZBb','Tame Impala',80),('5K4W6rqBFWDnAN6FQUkS6x','Kanye West',90),('5l8VQNuIg0turYE1VtM9zV','Leonard Cohen',64),('5me0Irg2ANcsgc93uaYrpb','The Notorious B.I.G.',78),('5qBZETtyzfYnXOobDXbmcD','Danny Elfman',60),('5UqTO8smerMvxHYA5xsXb6','Sonic Youth',58),('5Wabl1lPdNOeIn0SQ5A1mp','Cocteau Twins',63),('5xeBMeW0YzWIXSVzAxhM8O','of Montreal',51),('63LljpkL9zSFiMggvYQKnh','Patrick Stewart',20),('6awzBEyEEwWHOjLox1DkLr','Girl Talk',50),('6bYFkBNvayh3nGqxcPp7Sv','Ulver',41),('6CWTBjOJK75cTE8Xv8u1kj','Feist',61),('6J7biCazzYhU3gM9j1wfid','Jamiroquai',67),('6kBDZFXuLrZgHnvmPu9NsG','Aphex Twin',65),('6liAMWkVf5LH7YR9yfFy1Y','Portishead',61),('6nS5roXSAGhTGr34W6n7Et','Disclosure',72),('6ns6XAOsw4B0nDUIovAOUO','GZA',63),('6RWjTQqILL7a1tQ0VapyLK','The Magnetic Fields',50),('6sFIWsNpZYqfjUpaCgueju','Carly Rae Jepsen',72),('6UUrUCIZtQeOf8tC0WuzRy','Sigur Rós',54),('6vbY3hOaCAhC7VjucswgdS','Twista',65),('6WH1V41LwGDGmlPUhSZLHO','Autechre',41),('6zvul52xwTWzilBZl6BUbT','Pixies',71),('70cRZdQywnSFp9pnc2WTCE','Simon & Garfunkel',72),('72X6FHxaShda0XeQw3vbeF','Slowdive',59),('75U40yZLLPglFgXbDVnmVs','The Mars Volta',54),('77tT1kLj6mCWtFNqiOmP9H','Daryl Hall & John Oates',72),('7bu3H8JO7d0UbMoVzbo70s','The Cure',76),('7CyeXFnOrfC1N6z4naIpgo','The Ronettes',57),('7FIoB5PHdrMZVC3q2HE5MS','George Harrison',67),('7hJcb9fa4alzcOq3EaNPoG','Snoop Dogg',83),('7L6u6TyhjuwubrcojPeNgf','Burzum',47),('7lbSsjYACZHn1MSDXPxNF2','Hikaru Utada',66),('7M1FPw29m5FbicYzS2xdpi','King Crimson',55),('7oEkUINVIj1Nr3Wnj8tzqr','Gilberto Gil',63),('7vX3cMVyW8gtDA4y855ynF','Rodrigo y Gabriela',51),('7w29UYBi0qsHi5RTcv3lmA','Björk',62);
/*!40000 ALTER TABLE `artists` ENABLE KEYS */;
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
