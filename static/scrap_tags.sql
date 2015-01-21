# Host: 127.0.0.1  (Version: 5.6.21-log)
# Date: 2015-01-19 17:47:08
# Generator: MySQL-Front 5.3  (Build 4.191)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "scrap_tags"
#

DROP TABLE IF EXISTS `scrap_tags`;
CREATE TABLE `scrap_tags` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `tag` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

#
# Data for table "scrap_tags"
#

INSERT INTO `scrap_tags` VALUES (1,'Python'),(2,'c'),(3,'c++'),(4,'Hadoop');
