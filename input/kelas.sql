-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 13, 2026 at 10:00 PM
-- Server version: 5.7.44-log
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sijuma`
--

-- --------------------------------------------------------

--
-- Table structure for table `kelas`
--

CREATE TABLE `kelas` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `kode` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nama` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tingkat` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `kapasitas` int(10) UNSIGNED NOT NULL DEFAULT '30',
  `aktif` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `kelas`
--

INSERT INTO `kelas` (`id`, `kode`, `nama`, `tingkat`, `kapasitas`, `aktif`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'XTKJ1', 'X TKJ 1', '10', 36, 1, '2026-07-01 03:28:24', '2026-07-03 00:22:23', NULL),
(2, 'XTKJ2', 'X TKJ 2', '10', 36, 1, '2026-07-01 03:28:24', '2026-07-01 03:28:24', NULL),
(3, 'XMP1', 'X MP 1', '10', 36, 1, '2026-07-01 03:28:24', '2026-07-01 03:28:24', NULL),
(4, 'XMP2', 'X MP 2', '10', 36, 1, '2026-07-01 03:28:24', '2026-07-01 03:28:24', NULL),
(5, 'XTSM1', 'X TSM 1', '10', 36, 1, '2026-07-01 03:28:24', '2026-07-01 03:28:24', NULL),
(6, 'XTSM2', 'X TSM 2', '10', 36, 1, '2026-07-01 03:28:24', '2026-07-01 03:28:24', NULL),
(7, 'XATPH', 'X ATPH', '10', 36, 1, '2026-07-01 03:28:24', '2026-07-01 03:28:24', NULL),
(8, 'XITKJ1', 'XI TKJ 1', '11', 36, 1, '2026-07-01 03:28:24', '2026-07-01 03:28:24', NULL),
(9, 'XITKJ2', 'XI TKJ 2', '11', 36, 1, '2026-07-01 03:28:24', '2026-07-01 03:28:24', NULL),
(11, 'XIMP', 'XI MP', '11', 36, 1, '2026-07-03 00:31:30', '2026-07-12 00:48:29', NULL),
(12, 'XIMP2', 'XI MP 2', '11', 36, 1, '2026-07-03 00:32:06', '2026-07-12 00:48:07', '2026-07-12 00:48:07'),
(13, 'XITSM1', 'XI TSM 1', '11', 36, 1, '2026-07-03 00:32:22', '2026-07-03 00:32:22', NULL),
(14, 'XITSM2', 'XI TSM 2', '11', 36, 1, '2026-07-03 00:32:39', '2026-07-03 00:32:39', NULL),
(15, 'XIATPH', 'XI ATPH', '11', 36, 1, '2026-07-03 00:32:57', '2026-07-03 00:32:57', NULL),
(16, 'XIITKJ1', 'XII TKJ 1', '12', 36, 1, '2026-07-03 00:33:18', '2026-07-03 00:33:18', NULL),
(17, 'XIITKJ2', 'XII TKJ 2', '12', 36, 1, '2026-07-03 00:33:29', '2026-07-03 00:33:29', NULL),
(18, 'XIITSM1', 'XII TSM 1', '12', 36, 1, '2026-07-03 00:34:06', '2026-07-03 00:34:06', NULL),
(19, 'XIITSM2', 'XII TSM 2', '12', 36, 1, '2026-07-03 00:34:17', '2026-07-03 00:34:17', NULL),
(20, 'XIIATPH', 'XII ATPH', '12', 36, 1, '2026-07-03 00:34:33', '2026-07-03 00:34:33', NULL),
(21, 'XIIMP', 'XII MP', '12', 36, 1, '2026-07-03 00:35:16', '2026-07-03 00:35:16', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `kelas`
--
ALTER TABLE `kelas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kelas_kode_unique` (`kode`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `kelas`
--
ALTER TABLE `kelas`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
