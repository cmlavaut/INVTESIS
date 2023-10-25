-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 192.168.50.254
-- Generation Time: Oct 25, 2023 at 10:36 PM
-- Server version: 11.1.2-MariaDB-1:11.1.2+maria~ubu2204
-- PHP Version: 8.2.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `invernadero`
--

-- --------------------------------------------------------

--
-- Table structure for table `clientes`
--

CREATE TABLE `clientes` (
  `id` int(10) UNSIGNED NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `curp` varchar(100) NOT NULL,
  `user` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL,
  `id_plantacion` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `clientes`
--

INSERT INTO `clientes` (`id`, `nombre`, `curp`, `user`, `password`, `creado`, `actualizado`, `id_plantacion`) VALUES
(1, 'Annie', 'ONPA970105MNERNN02', 'annieo', 'annieop.97', '0000-00-00 00:00:00', '2023-10-25 22:29:19', 3),
(2, 'Pilar', 'MOPP961003MNERVR02', 'pili', 'pilis', '0000-00-00 00:00:00', '2023-10-25 04:35:21', 2),
(3, 'Leo', 'GUDL960605HNERPN25', 'leoguty', 'leo@123', '0000-00-00 00:00:00', '2023-10-25 04:34:14', 1),
(4, 'Alejandro', 'BOSA961012HNERGL10', 'borges', 'borges*96', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 3),
(5, 'Lianne', 'CEPL960228MNERRN03', 'lianne', 'lianne@lquizar', '0000-00-00 00:00:00', '2023-10-25 04:20:52', 4);

--
-- Triggers `clientes`
--
DELIMITER $$
CREATE TRIGGER `update_field_clientes` BEFORE UPDATE ON `clientes` FOR EACH ROW SET NEW.actualizado = NOW()
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `end_device`
--

CREATE TABLE `end_device` (
  `id` int(10) UNSIGNED NOT NULL,
  `esp_serial` varchar(50) NOT NULL,
  `ubicacion` varchar(50) NOT NULL,
  `protocolo_cx` varchar(50) NOT NULL,
  `id_servidor` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `end_device`
--

INSERT INTO `end_device` (`id`, `esp_serial`, `ubicacion`, `protocolo_cx`, `id_servidor`) VALUES
(1, 'esp47', 'parcela1', 'mqtt', 2),
(2, 'esp78', 'parcela2', 'mqtt', 1),
(3, 'esp20', 'casa1', 'mqtt', 2),
(4, 'esp67', 'casa2', 'mqtt', 1),
(5, 'esp12', 'casa3', 'mqtt', 2);

-- --------------------------------------------------------

--
-- Table structure for table `plantacion`
--

CREATE TABLE `plantacion` (
  `id` int(10) UNSIGNED NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `ubicacion` varchar(50) NOT NULL,
  `fecha_cultivo` datetime NOT NULL,
  `cantidad_plantas` bigint(10) NOT NULL,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `plantacion`
--

INSERT INTO `plantacion` (`id`, `nombre`, `ubicacion`, `fecha_cultivo`, `cantidad_plantas`, `creado`, `actualizado`) VALUES
(1, 'Cafe', 'Cicata Legaria', '2023-10-24 18:44:48', 450, '0000-00-00 00:00:00', '2023-10-25 22:26:19'),
(2, 'Jitomate', 'Demet Toreo', '2023-10-24 18:44:48', 4700, '0000-00-00 00:00:00', '2023-10-25 22:26:31'),
(3, 'Cempasuchil', 'Loma Hermosa', '2023-10-24 18:45:21', 9800, '0000-00-00 00:00:00', '2023-10-25 22:25:44'),
(4, 'Jitomate', 'Bosque de Chapultepec', '2023-10-24 18:45:21', 980789, '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(5, 'Cafe de Altura', 'Puebla', '2023-10-24 18:46:44', 74170, '0000-00-00 00:00:00', '0000-00-00 00:00:00');

--
-- Triggers `plantacion`
--
DELIMITER $$
CREATE TRIGGER `update_field_plantacion` BEFORE UPDATE ON `plantacion` FOR EACH ROW SET NEW.actualizado = NOW()
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `sensores`
--

CREATE TABLE `sensores` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `valor` decimal(10,0) NOT NULL,
  `hora_medicion` datetime NOT NULL,
  `id_endevice` int(10) UNSIGNED NOT NULL,
  `creado` datetime NOT NULL,
  `actualizado` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Triggers `sensores`
--
DELIMITER $$
CREATE TRIGGER `update_field_sensores` BEFORE UPDATE ON `sensores` FOR EACH ROW SET NEW.actualizado = NOW()
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `servidores`
--

CREATE TABLE `servidores` (
  `id` int(10) UNSIGNED NOT NULL,
  `rasp_serial` varchar(50) NOT NULL,
  `id_plantacion` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `servidores`
--

INSERT INTO `servidores` (`id`, `rasp_serial`, `id_plantacion`) VALUES
(1, '10000000620194e6', 3),
(2, '10000000de97ad98', 1),
(3, '1000000005f2b79b', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `curp` (`curp`),
  ADD UNIQUE KEY `user` (`user`),
  ADD KEY `id_clientes_plantacion` (`id_plantacion`);

--
-- Indexes for table `end_device`
--
ALTER TABLE `end_device`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_endevice_server` (`id_servidor`);

--
-- Indexes for table `plantacion`
--
ALTER TABLE `plantacion`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sensores`
--
ALTER TABLE `sensores`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_sensores_endevice` (`id_endevice`);

--
-- Indexes for table `servidores`
--
ALTER TABLE `servidores`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_servidores_plantacion` (`id_plantacion`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `end_device`
--
ALTER TABLE `end_device`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `plantacion`
--
ALTER TABLE `plantacion`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `sensores`
--
ALTER TABLE `sensores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `servidores`
--
ALTER TABLE `servidores`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `clientes`
--
ALTER TABLE `clientes`
  ADD CONSTRAINT `id_clientes_plantacion` FOREIGN KEY (`id_plantacion`) REFERENCES `plantacion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `end_device`
--
ALTER TABLE `end_device`
  ADD CONSTRAINT `id_endevice_server` FOREIGN KEY (`id_servidor`) REFERENCES `servidores` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `sensores`
--
ALTER TABLE `sensores`
  ADD CONSTRAINT `id_sensores_endevice` FOREIGN KEY (`id_endevice`) REFERENCES `end_device` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `servidores`
--
ALTER TABLE `servidores`
  ADD CONSTRAINT `id_servidores_plantacion` FOREIGN KEY (`id_plantacion`) REFERENCES `plantacion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
