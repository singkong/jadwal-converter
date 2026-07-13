-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 13, 2026 at 09:59 PM
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
-- Table structure for table `gurus`
--

CREATE TABLE `gurus` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `user_id` bigint(20) UNSIGNED DEFAULT NULL,
  `nip` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nama` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `jenis_kelamin` enum('L','P') COLLATE utf8mb4_unicode_ci NOT NULL,
  `tempat_lahir` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tanggal_lahir` date DEFAULT NULL,
  `alamat` text COLLATE utf8mb4_unicode_ci,
  `telepon` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pendidikan_terakhir` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tanggal_masuk` date DEFAULT NULL,
  `aktif` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `gurus`
--

INSERT INTO `gurus` (`id`, `user_id`, `nip`, `nama`, `jenis_kelamin`, `tempat_lahir`, `tanggal_lahir`, `alamat`, `telepon`, `pendidikan_terakhir`, `tanggal_masuk`, `aktif`, `created_at`, `updated_at`, `deleted_at`) VALUES
(35, 2, '198401062010012019', 'ARLIYANTI, S.Pi., M.M.', 'P', 'Lampung', '1984-06-01', NULL, NULL, 'S2', '1975-01-01', 1, '2026-07-01 03:28:26', '2026-07-05 05:38:05', NULL),
(8, 3, '198207042024211004', 'SUMARNO, S.P.', 'L', 'Lampung', '1982-04-07', NULL, NULL, 'S1', '1978-01-01', 1, '2026-07-01 03:28:27', '2026-07-05 05:39:51', NULL),
(19, 4, '198409262024211006', 'SUBIRMAN, S.Pd.', 'L', 'Lampung', '1984-09-26', NULL, NULL, 'S1', '1980-01-01', 1, '2026-07-01 03:28:28', '2026-07-05 05:41:09', NULL),
(24, 33, '198307012024212019', 'EVI ANDRIANI, S.Pd.', 'P', 'Bandung', '1983-07-12', NULL, NULL, 'S1', '1982-01-01', 1, '2026-07-01 03:28:29', '2026-07-05 05:43:35', NULL),
(3, 6, '198510082024212012', 'SULAMI, S.Pd.', 'P', 'Lampung', '1985-10-08', NULL, NULL, 'S2', '1984-01-01', 1, '2026-07-01 03:28:30', '2026-07-05 05:46:55', NULL),
(30, 5, '198506062025212039', 'YUNITA SOPHIA, S.Pd.', 'P', 'Lampung', '1985-06-06', NULL, NULL, 'S1', '1986-01-01', 1, '2026-07-01 03:28:30', '2026-07-05 05:44:37', NULL),
(22, 8, '198608072024211011', 'ANANG KRISTIANTO, S.Pd.', 'L', 'Bogor', '1988-12-05', NULL, NULL, 'S1', '1988-01-01', 1, '2026-07-01 03:28:31', '2026-07-05 05:51:42', NULL),
(1, 9, '198810042024212015', 'SITI NURYATI, S.Pd.', 'P', 'Lampung', '1990-02-14', NULL, NULL, 'S1', '1990-01-01', 1, '2026-07-01 03:28:32', '2026-07-05 05:52:21', NULL),
(7, 10, '198505282022211007', 'MEI RAHMAT, S.Kom', 'L', 'Sumber Agung', '1985-05-28', 'Banjar Agung', '081379812540', 'S1', '2022-01-03', 1, '2026-07-04 06:24:09', '2026-07-05 05:52:59', NULL),
(13, 11, '198904072024211007', 'MARYADI, S.Kom', 'L', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 05:54:42', '2026-07-05 05:54:42', NULL),
(18, 12, '199012242024212020', 'SUPRAPTI, S.P.', 'P', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 05:55:31', '2026-07-05 05:55:31', NULL),
(20, 13, '199108062024211012', 'AGUS SALIM, S.P.', 'L', 'Bandung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 05:56:29', '2026-07-05 05:56:29', NULL),
(2, 14, '199108202023211013', 'NICO RIANTINO, S.Pd', 'L', 'Lampung', '2026-07-05', '', '082185535658', 'S1', '2026-07-05', 1, '2026-07-05 05:57:04', '2026-07-06 00:00:56', NULL),
(11, 15, '199110152024212026', 'SITI AMINAH, S.Pd.', 'P', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 05:57:41', '2026-07-05 05:57:41', NULL),
(32, 16, '199110152025212052', 'NUR MAULEVA SARI, S.Pd.', 'P', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 05:58:29', '2026-07-05 05:58:29', NULL),
(5, 17, '199209242024211010', 'GUNAWAN, S.Pd.', 'L', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 05:59:06', '2026-07-05 05:59:06', NULL),
(4, 18, '199305052020122029', 'FLOSIA ROSIANI, S.Pd', 'P', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 06:08:11', '2026-07-05 06:08:11', NULL),
(31, 19, '199404052025212027', 'MARDIANA, S.Pd.', 'P', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 06:08:47', '2026-07-05 06:08:47', NULL),
(16, 20, '199410202024211014', 'DAWUD KURNIAWAN, S.Kom', 'L', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 06:09:39', '2026-07-05 06:09:39', NULL),
(25, 21, '199410222024211013', 'MUHAMMAD ANDI FIRMAN, S.Pd.', 'L', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 06:14:21', '2026-07-05 06:14:21', NULL),
(26, 22, '199411242025212020', 'ZAIDAH NUR AINI, S.Pd.', 'P', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 06:50:38', '2026-07-05 06:51:24', NULL),
(12, 23, '199505082024212022', 'RENI WIDIYANTI, S.Pd.', 'P', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 06:51:15', '2026-07-05 06:51:15', NULL),
(6, 24, '199507252024212026', 'YUSY IRALISA, S.Pd.', 'P', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 06:53:00', '2026-07-05 06:53:00', NULL),
(17, 25, '199510302024212032', 'SHELLA INDRIANI, S.Pd.', 'P', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 06:53:35', '2026-07-05 06:53:35', NULL),
(9, 26, '199604302022211002', 'HANGGORO MUKTI, S.Pd', 'L', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 06:54:12', '2026-07-05 06:54:12', NULL),
(14, 27, '199605102024212032', 'IRDYA MEILANISA, S.Pd.', 'P', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 06:54:53', '2026-07-05 06:54:53', NULL),
(15, 28, '199607292024212024', 'DEWI JUNITA, S.Pd.', 'P', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 06:55:26', '2026-07-05 06:55:26', NULL),
(21, 29, '199712092024211006', 'AMIRUL ANAM, S.Pd.', 'L', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 06:55:53', '2026-07-05 06:55:53', NULL),
(23, 30, '199802182024211009', 'ANAS ROSYID DIAN, S.Kom.', 'L', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 06:56:23', '2026-07-05 06:56:23', NULL),
(28, 31, '199905282025212074', 'NONA MEYANA, S.Pd.', 'P', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 06:56:53', '2026-07-05 06:56:53', NULL),
(10, 7, '198601292023212018', 'JERI YANA, S.Pd.', 'P', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 06:57:26', '2026-07-05 06:57:26', NULL),
(29, 32, '1805082', 'RUSLINA WATI, S.Pd.', 'P', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 06:58:04', '2026-07-05 07:01:38', NULL),
(27, 34, '1805081', 'AGUS SUTOPO, S.Kom.', 'L', 'Lampung', '2026-07-05', '', '', 'S1', '2026-07-05', 1, '2026-07-05 07:00:21', '2026-07-05 07:01:47', NULL),
(33, 35, '1805083', 'RUBEN, S.Pd', 'L', 'Lampung', '2026-07-01', 'Lampung', '', 'S1', '2026-07-01', 1, '2026-07-12 00:11:49', '2026-07-12 00:11:49', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `gurus`
--
ALTER TABLE `gurus`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `gurus_nip_unique` (`nip`),
  ADD KEY `gurus_user_id_foreign` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `gurus`
--
ALTER TABLE `gurus`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `gurus`
--
ALTER TABLE `gurus`
  ADD CONSTRAINT `gurus_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
