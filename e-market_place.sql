-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 28, 2025 at 06:52 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `e-market_place`
--

-- --------------------------------------------------------

--
-- Table structure for table `pending_cart`
--

CREATE TABLE `pending_cart` (
  `pending_cart_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `brand` varchar(30) NOT NULL,
  `colour` varchar(20) NOT NULL,
  `size` varchar(11) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `product_name`, `brand`, `colour`, `size`, `rating`, `price`) VALUES
(1, 'Tshirt', 'BrandA', 'Red', 'M', 4, 500),
(2, 'Shirt', 'BrandB', 'Blue', 'L', 4, 800),
(3, 'Jacket', 'BrandC', 'Black', 'XL', 5, 1500),
(4, 'Jeans', 'BrandD', 'Denim', '32', 4, 1200),
(5, 'Sneakers', 'BrandE', 'White', '10', 5, 2000),
(6, 'Tshirt', 'BrandF', 'Green', 'S', 4, 450),
(7, 'Shirt', 'BrandG', 'Gray', 'M', 4, 850),
(8, 'Jacket', 'BrandH', 'Brown', 'L', 5, 1600),
(9, 'Jeans', 'BrandI', 'Black', '34', 4, 1300),
(10, 'Sneakers', 'BrandJ', 'Blue', '11', 4, 2200),
(11, 'Tshirt', 'BrandK', 'Yellow', 'L', 4, 550),
(12, 'Shirt', 'BrandL', 'Purple', 'S', 5, 900),
(13, 'Jacket', 'BrandM', 'Gray', 'M', 4, 1700),
(14, 'Jeans', 'BrandN', 'Navy', '36', 5, 1400),
(15, 'Sneakers', 'BrandO', 'Red', '9', 4, 2100),
(16, 'Tshirt', 'BrandP', 'White', 'XL', 4, 500),
(17, 'Shirt', 'BrandQ', 'Pink', 'L', 4, 800),
(18, 'Jacket', 'BrandR', 'Beige', 'S', 5, 1550),
(19, 'Jeans', 'BrandS', 'Charcoal', '30', 4, 1250),
(20, 'Sneakers', 'BrandT', 'Gray', '8', 5, 2300),
(21, 'Mobile', 'Apple', 'Black', NULL, 5, 75000),
(22, 'Mobile', 'Samsung', 'White', NULL, 5, 70000),
(23, 'TV', 'Sony', 'Black', NULL, 4, 60000),
(24, 'TV', 'LG', 'Silver', NULL, 4, 55000),
(25, 'Fridge', 'Samsung', 'Grey', NULL, 5, 45000),
(26, 'Fridge', 'LG', 'White', NULL, 5, 50000),
(27, 'Speaker', 'Bose', 'Black', NULL, 4, 18000),
(28, 'Speaker', 'JBL', 'Blue', NULL, 4, 20000),
(29, 'Washing Machine', 'Bosch', 'White', NULL, 5, 35000),
(30, 'Washing Machine', 'LG', 'Silver', NULL, 5, 30000),
(31, 'Mobile', 'Google', 'Black', NULL, 4, 65000),
(32, 'Mobile', 'OnePlus', 'Red', NULL, 5, 60000),
(33, 'TV', 'Samsung', 'Black', NULL, 5, 70000),
(34, 'TV', 'Panasonic', 'Grey', NULL, 4, 55000),
(35, 'Fridge', 'Whirlpool', 'Silver', NULL, 4, 48000),
(36, 'Fridge', 'Godrej', 'White', NULL, 5, 47000),
(37, 'Speaker', 'Sony', 'Black', NULL, 4, 19000),
(38, 'Speaker', 'Marshall', 'Brown', NULL, 4, 22000),
(39, 'Washing Machine', 'IFB', 'White', NULL, 5, 36000),
(40, 'Washing Machine', 'Whirlpool', 'Silver', NULL, 5, 31000),
(43, 'Sneakers', 'nike', 'red', '7', 5, 8500);

--
-- Triggers `products`
--
DELIMITER $$
CREATE TRIGGER `delete_fro_bestseller` BEFORE DELETE ON `products` FOR EACH ROW BEGIN
    -- Delete the product from the bestseller table if it exists there
    DELETE FROM bestseller
    WHERE product_id = OLD.product_id;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `signin`
--

CREATE TABLE `signin` (
  `user_id` int(11) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Gmail` varchar(30) DEFAULT NULL,
  `Password` varchar(30) DEFAULT NULL,
  `phonenumber` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `signin`
--

INSERT INTO `signin` (`user_id`, `Name`, `Gmail`, `Password`, `phonenumber`) VALUES
(14, 'dharmesh', 'dharmesh@gmail.com', 'dharmesh1234', 8511469392),
(21, 'kavya ', 'kavya@gmail.com', '1234', 1234512345),
(23, 'ansh', 'ansh@gmail.com', '1234', 1111122222),
(25, 'chirag', 'chirag@gmail.com', '1234', 1234512340);

--
-- Triggers `signin`
--
DELIMITER $$
CREATE TRIGGER `before_insert_signoin` BEFORE INSERT ON `signin` FOR EACH ROW BEGIN
    -- Check for duplicate gmail
    IF EXISTS (SELECT 1 FROM signin WHERE gmail = NEW.gmail) THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Email already exists.';
    END IF;

    -- Check for duplicate phonenumber
    IF EXISTS (SELECT 1 FROM signin WHERE phonenumber = NEW.phonenumber) THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Phone number already exists.';
    END IF;
END
$$
DELIMITER ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pending_cart`
--
ALTER TABLE `pending_cart`
  ADD PRIMARY KEY (`pending_cart_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `signin`
--
ALTER TABLE `signin`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pending_cart`
--
ALTER TABLE `pending_cart`
  MODIFY `pending_cart_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT for table `signin`
--
ALTER TABLE `signin`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
