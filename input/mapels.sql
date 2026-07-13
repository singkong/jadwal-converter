-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 13, 2026 at 11:54 PM
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
-- Table structure for table `mapels`
--

CREATE TABLE `mapels` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `kode` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nama` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `deskripsi` text COLLATE utf8mb4_unicode_ci,
  `aktif` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `mapels`
--

INSERT INTO `mapels` (`id`, `kode`, `nama`, `deskripsi`, `aktif`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'F', 'Matematika', NULL, 1, '2026-07-01 03:28:23', '2026-07-12 00:21:34', NULL),
(2, 'C', 'Bahasa Indonesia', NULL, 1, '2026-07-01 03:28:23', '2026-07-12 00:20:22', NULL),
(3, 'G', 'Bahasa Inggris', NULL, 1, '2026-07-01 03:28:23', '2026-07-12 00:20:40', NULL),
(4, 'I', 'Projek Ilmu Pengetahuan Alam dan Sosial', NULL, 1, '2026-07-01 03:28:23', '2026-07-12 00:22:12', NULL),
(6, 'B', 'Pendidikan Pancasila', NULL, 1, '2026-07-01 03:28:23', '2026-07-12 00:20:07', NULL),
(7, 'A', 'Pendidikan Agama dan Budi Pekertai', NULL, 1, '2026-07-01 03:28:23', '2026-07-12 00:19:41', NULL),
(8, 'D', 'Pendidikan Jasmani, Olahraga, dan Kesehatan', NULL, 1, '2026-07-01 03:28:23', '2026-07-12 00:21:06', NULL),
(9, 'E', 'Seni Budaya', NULL, 1, '2026-07-01 03:28:23', '2026-07-12 00:21:21', NULL),
(10, 'J', 'Produk Kreatif dan Kewirausahaan', NULL, 1, '2026-07-01 03:28:23', '2026-07-12 00:22:46', NULL),
(11, 'T', 'Informatika', NULL, 1, '2026-07-01 03:28:23', '2026-07-12 00:30:47', NULL),
(12, 'U', 'Bahasa Daerah Lampung', NULL, 1, '2026-07-01 03:28:23', '2026-07-12 00:31:20', NULL),
(14, 'H', 'Sejarah Indonesia', '', 1, '2026-07-12 00:13:21', '2026-07-12 00:21:51', NULL),
(15, 'K', 'Pendidikan Antikorupsi', '', 1, '2026-07-12 00:15:08', '2026-07-12 00:23:46', NULL),
(16, 'P', 'Dasar Dasar Kejuruan Teknik Komputer dan Jaringan', '', 1, '2026-07-12 00:15:45', '2026-07-12 00:26:53', NULL),
(17, 'L', 'Dasar Dasar Kejuruan Manajemen Perkantoran', '', 1, '2026-07-12 00:16:07', '2026-07-12 00:25:16', NULL),
(18, 'N', 'Dasar Dasar Kejuruan Teknik Sepeda Motor', '', 1, '2026-07-12 00:16:24', '2026-07-12 00:29:02', NULL),
(19, 'R', 'Dasar Dasar Kejuruan Agribisnis Tanaman Pangan dan Hortikultura', '', 1, '2026-07-12 00:16:47', '2026-07-12 00:30:02', NULL),
(20, 'Q', 'Kompetensi Kejuruan Teknik Komputer dan Jaringan', '', 1, '2026-07-12 00:17:18', '2026-07-12 00:27:00', NULL),
(21, 'M', 'Kompetensi Kejuruan Manajemen Perkantoran', '', 1, '2026-07-12 00:17:36', '2026-07-12 00:25:28', NULL),
(22, 'O', 'Kompetensi Kejuruan Teknik Sepeda Motor', '', 1, '2026-07-12 00:17:56', '2026-07-12 00:25:58', NULL),
(23, 'S', 'Kompetensi Kejuruan Agribisnis Tanaman Pangan dan Hortikultura', '', 1, '2026-07-12 00:18:17', '2026-07-12 00:29:56', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mapels`
--
ALTER TABLE `mapels`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `mapels_kode_unique` (`kode`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mapels`
--
ALTER TABLE `mapels`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
