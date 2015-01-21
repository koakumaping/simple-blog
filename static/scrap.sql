# Host: 127.0.0.1  (Version: 5.6.21-log)
# Date: 2015-01-20 13:06:35
# Generator: MySQL-Front 5.3  (Build 4.191)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "scrap"
#

DROP TABLE IF EXISTS `scrap`;
CREATE TABLE `scrap` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `file_type` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `archive` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tag` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `is_deleted` tinyint(3) unsigned DEFAULT '0',
  `content` text COLLATE utf8_unicode_ci,
  `counter` varchar(32) COLLATE utf8_unicode_ci DEFAULT '0',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
