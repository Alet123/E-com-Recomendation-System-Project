-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 24, 2021 at 06:39 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `dbshopping`
--

-- --------------------------------------------------------

--
-- Table structure for table `tblbrand`
--

CREATE TABLE IF NOT EXISTS `tblbrand` (
  `bid` int(11) NOT NULL AUTO_INCREMENT,
  `brand` varchar(50) NOT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `tblbrand`
--

INSERT INTO `tblbrand` (`bid`, `brand`) VALUES
(1, 'Samsung'),
(2, 'Toshiba'),
(3, 'Sandisk'),
(4, 'Sony'),
(5, 'Hp'),
(6, 'Amaze');

-- --------------------------------------------------------

--
-- Table structure for table `tblcart`
--

CREATE TABLE IF NOT EXISTS `tblcart` (
  `cartid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `cdate` datetime NOT NULL,
  `qty` int(11) NOT NULL,
  `rate` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`cartid`),
  KEY `rid` (`rid`),
  KEY `pid` (`pid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `tblcart`
--

INSERT INTO `tblcart` (`cartid`, `rid`, `pid`, `cdate`, `qty`, `rate`, `status`) VALUES
(1, 1, 4, '2021-05-22 17:16:46', 1, 2500, 'purchased');

-- --------------------------------------------------------

--
-- Table structure for table `tblcategory`
--

CREATE TABLE IF NOT EXISTS `tblcategory` (
  `catid` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(50) NOT NULL,
  PRIMARY KEY (`catid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `tblcategory`
--

INSERT INTO `tblcategory` (`catid`, `category`) VALUES
(1, 'Electronics'),
(2, 'Clothings'),
(3, 'Fashion accessories');

-- --------------------------------------------------------

--
-- Table structure for table `tbllogin`
--

CREATE TABLE IF NOT EXISTS `tbllogin` (
  `uname` varchar(50) NOT NULL,
  `pwd` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbllogin`
--

INSERT INTO `tbllogin` (`uname`, `pwd`, `utype`, `status`) VALUES
('tarun@gmail.com', 'tarun', 'customer', '1'),
('admin@gmail.com', 'admin', 'admin', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tblproduct`
--

CREATE TABLE IF NOT EXISTS `tblproduct` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `subid` int(11) NOT NULL,
  `bid` int(11) NOT NULL,
  `product` varchar(50) NOT NULL,
  `description` varchar(100) NOT NULL,
  `rate` int(11) NOT NULL,
  `img` varchar(100) NOT NULL,
  PRIMARY KEY (`pid`),
  KEY `subid` (`subid`,`bid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `tblproduct`
--

INSERT INTO `tblproduct` (`pid`, `subid`, `bid`, `product`, `description`, `rate`, `img`) VALUES
(1, 1, 5, 'Hp 32 gb silver pendrive', 'hjvnn', 750, 'static/media/hp-32gb-usb-20-pendrive_Pe4UH5C.jpg'),
(2, 1, 2, 'Toshiba 16 gb pendrive', 'jhwvnjsh', 350, 'static/media/41g8qWL2z-L._AC_SS450_.jpg'),
(3, 1, 3, 'Sandisk 16 gb pendrive', 'ajbhv', 700, 'static/media/61PVIzk6ALL._SL1104_.jpg'),
(4, 2, 6, 'Full flared kids frock', 'jhbfvhj', 2500, 'static/media/3434121141_1994964681.jpg'),
(5, 2, 6, 'Kids frock', 'ijnk', 1500, 'static/media/61o9b8KupZL._UL1000_.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `tblregistration`
--

CREATE TABLE IF NOT EXISTS `tblregistration` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `contact` varchar(50) NOT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `tblregistration`
--

INSERT INTO `tblregistration` (`rid`, `name`, `email`, `contact`) VALUES
(1, 'Tarun', 'tarun@gmail.com', '8596471023');

-- --------------------------------------------------------

--
-- Table structure for table `tblreview`
--

CREATE TABLE IF NOT EXISTS `tblreview` (
  `revid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `rdate` datetime NOT NULL,
  `feedback` varchar(100) NOT NULL,
  `rating` int(11) NOT NULL,
  PRIMARY KEY (`revid`),
  KEY `rid` (`rid`,`pid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `tblreview`
--

INSERT INTO `tblreview` (`revid`, `rid`, `pid`, `rdate`, `feedback`, `rating`) VALUES
(1, 1, 4, '2021-05-22 18:05:33', 'Good product', 3);

-- --------------------------------------------------------

--
-- Table structure for table `tblsubcategory`
--

CREATE TABLE IF NOT EXISTS `tblsubcategory` (
  `subid` int(11) NOT NULL AUTO_INCREMENT,
  `catid` int(11) NOT NULL,
  `subcategory` varchar(50) NOT NULL,
  PRIMARY KEY (`subid`),
  KEY `catid` (`catid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `tblsubcategory`
--

INSERT INTO `tblsubcategory` (`subid`, `catid`, `subcategory`) VALUES
(1, 1, 'Gadget'),
(2, 2, 'Kids wear');

-- --------------------------------------------------------

--
-- Table structure for table `tblview`
--

CREATE TABLE IF NOT EXISTS `tblview` (
  `vid` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) NOT NULL,
  `vdate` date NOT NULL,
  `pid` int(11) NOT NULL,
  PRIMARY KEY (`vid`),
  KEY `rid` (`rid`,`pid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `tblview`
--

INSERT INTO `tblview` (`vid`, `rid`, `vdate`, `pid`) VALUES
(1, 1, '2021-05-24', 1),
(2, 1, '2021-05-24', 1),
(3, 1, '2021-05-24', 4);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tblcart`
--
ALTER TABLE `tblcart`
  ADD CONSTRAINT `tblcart_ibfk_2` FOREIGN KEY (`pid`) REFERENCES `tblproduct` (`pid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tblcart_ibfk_1` FOREIGN KEY (`rid`) REFERENCES `tblregistration` (`rid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tblsubcategory`
--
ALTER TABLE `tblsubcategory`
  ADD CONSTRAINT `tblsubcategory_ibfk_1` FOREIGN KEY (`catid`) REFERENCES `tblsubcategory` (`subid`) ON DELETE CASCADE ON UPDATE CASCADE;
