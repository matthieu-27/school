/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

DROP DATABASE IF EXISTS `school`;
CREATE DATABASE IF NOT EXISTS `school` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin */;
USE `school`;

DROP TABLE IF EXISTS `address`;
CREATE TABLE IF NOT EXISTS `address` (
  `id_address` int(11) NOT NULL AUTO_INCREMENT,
  `street` varchar(80) NOT NULL,
  `city` varchar(50) NOT NULL,
  `postal_code` smallint(6) NOT NULL,
  PRIMARY KEY (`id_address`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

DROP TABLE IF EXISTS `course`;
CREATE TABLE IF NOT EXISTS `course` (
  `id_course` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `id_teacher` int(11) NOT NULL,
  PRIMARY KEY (`id_course`),
  KEY `id_teacher` (`id_teacher`),
  CONSTRAINT `course_ibfk_1` FOREIGN KEY (`id_teacher`) REFERENCES `teacher` (`id_teacher`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

DROP TABLE IF EXISTS `person`;
CREATE TABLE IF NOT EXISTS `person` (
  `id_person` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `age` tinyint(4) NOT NULL,
  `id_address` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_person`),
  UNIQUE KEY `id_address` (`id_address`),
  CONSTRAINT `person_ibfk_1` FOREIGN KEY (`id_address`) REFERENCES `address` (`id_address`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

DROP TABLE IF EXISTS `student`;
CREATE TABLE IF NOT EXISTS `student` (
  `student_nbr` int(11) NOT NULL,
  `id_person` int(11) NOT NULL,
  PRIMARY KEY (`student_nbr`),
  UNIQUE KEY `id_person` (`id_person`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`id_person`) REFERENCES `person` (`id_person`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


DROP TABLE IF EXISTS `takes`;
CREATE TABLE IF NOT EXISTS `takes` (
  `student_nbr` int(11) NOT NULL,
  `id_course` int(11) NOT NULL,
  PRIMARY KEY (`student_nbr`,`id_course`),
  KEY `id_course` (`id_course`),
  CONSTRAINT `takes_ibfk_1` FOREIGN KEY (`student_nbr`) REFERENCES `student` (`student_nbr`),
  CONSTRAINT `takes_ibfk_2` FOREIGN KEY (`id_course`) REFERENCES `course` (`id_course`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


DROP TABLE IF EXISTS `teacher`;
CREATE TABLE IF NOT EXISTS `teacher` (
  `id_teacher` int(11) NOT NULL AUTO_INCREMENT,
  `hiring_date` date NOT NULL,
  `id_person` int(11) NOT NULL,
  PRIMARY KEY (`id_teacher`),
  UNIQUE KEY `id_person` (`id_person`),
  CONSTRAINT `teacher_ibfk_1` FOREIGN KEY (`id_person`) REFERENCES `person` (`id_person`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

INSERT INTO `address` (`id_address`, `street`, `city`, `postal_code`) VALUES
	(1, '12 rue des Pinsons', 'Castanet', 31320),
	(2, '43 avenue Jean Zay', 'Toulouse', 31200),
	(3, '7 impasse des Coteaux', 'Cornebarrieu', 31150);

INSERT INTO `person` (`id_person`, `first_name`, `last_name`, `age`, `id_address`) VALUES
	(1, 'Paul', 'Dubois', 12, 1),
	(2, 'Valérie', 'Dumont', 13, 2),
	(3, 'Louis', 'Berthot', 11, 3),
	(4, 'Victor', 'Hugo', 23, NULL),
	(5, 'Jules', 'Michelet', 32, NULL),
	(6, 'Sophie', 'Germain', 25, NULL),
	(7, 'Marie', 'Curie', 31, NULL),
	(8, 'William', 'Shakespeare', 34, NULL),
	(9, 'Michel', 'Platini', 42, NULL);
INSERT INTO `teacher` (`id_teacher`, `hiring_date`, `id_person`) VALUES
	(1, '2023-09-04', 4),
	(2, '2023-09-04', 5),
	(3, '2023-09-04', 6),
	(4, '2023-09-04', 7),
	(5, '2023-09-04', 8),
	(6, '2023-09-04', 9);
INSERT INTO `student` (`student_nbr`, `id_person`) VALUES
	(1, 1),
	(2, 2),
	(3, 3);
INSERT INTO `course` (`id_course`, `name`, `start_date`, `end_date`, `id_teacher`) VALUES
	(1, 'Français', '2024-01-29', '2024-02-16', 1),
	(2, 'Histoire', '2024-02-05', '2024-02-16', 2),
	(3, 'Géographie', '2024-02-05', '2024-02-16', 2),
	(4, 'Mathématiques', '2024-02-12', '2024-03-08', 3),
	(5, 'Physique', '2024-02-19', '2024-03-08', 4),
	(6, 'Chimie', '2024-02-26', '2024-03-15', 4),
	(7, 'Anglais', '2024-02-12', '2024-02-24', 5),
	(8, 'Sport', '2024-03-04', '2024-03-15', 6);
INSERT INTO `takes` (`student_nbr`, `id_course`) VALUES
	(2, 1),
	(2, 2),
	(1, 3),
	(3, 3),
	(3, 4),
	(1, 5),
	(3, 5),
	(2, 6),
	(1, 7),
	(3, 8);


/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
