-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-12-2023 a las 23:13:38
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tutorias`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `agenda_tutores_aprendices`
--

CREATE TABLE `agenda_tutores_aprendices` (
  `ID_TUTOR` varchar(10) NOT NULL,
  `FECHA` date NOT NULL,
  `ID_APRENDIZ` varchar(10) NOT NULL,
  `TIEMPO` int(11) NOT NULL,
  `ID_AREA_CONOCIMIENTO` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `agenda_tutores_aprendices`
--

INSERT INTO `agenda_tutores_aprendices` (`ID_TUTOR`, `FECHA`, `ID_APRENDIZ`, `TIEMPO`, `ID_AREA_CONOCIMIENTO`) VALUES
('5478951', '2023-03-09', '1000666777', 30, 'FILO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `aprendices`
--

CREATE TABLE `aprendices` (
  `CEDULA_APRENDICES` varchar(10) NOT NULL,
  `NOMBRES_APRENDICES` varchar(30) NOT NULL,
  `APELLIDOS_APRENDICES` varchar(30) NOT NULL,
  `CORREO_ELECTRONICO_APRENDICES` varchar(50) NOT NULL,
  `PÁIS_APRENDICES` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `aprendices`
--

INSERT INTO `aprendices` (`CEDULA_APRENDICES`, `NOMBRES_APRENDICES`, `APELLIDOS_APRENDICES`, `CORREO_ELECTRONICO_APRENDICES`, `PÁIS_APRENDICES`) VALUES
('1000222333', 'Veronica', 'Robles Aguas', 'lavero@a.a', 'COL'),
('1000456123', 'Santiago', 'Bonilla Urueña', 'elsanti@a.a', 'COL'),
('1000478963', 'David Steven', 'Niño Matos', 'eldavid@a.a', 'COL'),
('1000666777', 'Kevin Sebastian', 'Patiño España', 'skqweq@gmail.bla', 'COL');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `areas_conocimiento`
--

CREATE TABLE `areas_conocimiento` (
  `ID_AREA_CONOCIMIENTO` varchar(10) NOT NULL,
  `NOMBRE_AREA_CONOCIMIENTO` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `areas_conocimiento`
--

INSERT INTO `areas_conocimiento` (`ID_AREA_CONOCIMIENTO`, `NOMBRE_AREA_CONOCIMIENTO`) VALUES
('DER', 'Derecho privado'),
('FILO', 'Filosofia'),
('PROG', 'Programacion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paises`
--

CREATE TABLE `paises` (
  `ID_PAIS` varchar(3) NOT NULL,
  `NOMBRE_PAIS` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `paises`
--

INSERT INTO `paises` (`ID_PAIS`, `NOMBRE_PAIS`) VALUES
('ARG', 'Argentina'),
('COL', 'Colombia'),
('MEX', 'Mexico');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tutores`
--

CREATE TABLE `tutores` (
  `ID_TUTORES` varchar(10) NOT NULL,
  `NOMBRES_TUTORES` varchar(30) NOT NULL,
  `APELLIDOS_TUTORES` varchar(30) NOT NULL,
  `CORREO_ELECTRONICO_TUTORES` varchar(50) NOT NULL,
  `PAIS_TUTOR` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tutores`
--

INSERT INTO `tutores` (`ID_TUTORES`, `NOMBRES_TUTORES`, `APELLIDOS_TUTORES`, `CORREO_ELECTRONICO_TUTORES`, `PAIS_TUTOR`) VALUES
('1000887998', 'Karl', 'Marx', 'a@a.a', 'COL'),
('5478951', 'Federico', 'Engels', 'blabla@bla.bla', 'COL');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tutores_areas_conocimiento`
--

CREATE TABLE `tutores_areas_conocimiento` (
  `ID_TUTOR` varchar(10) NOT NULL,
  `ID_AREA_CONOCIMIENTO` varchar(10) NOT NULL,
  `TARIFA` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tutores_areas_conocimiento`
--

INSERT INTO `tutores_areas_conocimiento` (`ID_TUTOR`, `ID_AREA_CONOCIMIENTO`, `TARIFA`) VALUES
('1000887998', 'FILO', 5000),
('5478951', 'FILO', 1000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tutorias`
--

CREATE TABLE `tutorias` (
  `ID_APRENDIZ_TUTORIA` varchar(10) NOT NULL,
  `ID_TUTOR_TUTORIA` varchar(10) NOT NULL,
  `ID_AREA_CONOCIMIENTO_TUTORIA` varchar(10) NOT NULL,
  `FECHA_TUTORIA` date NOT NULL,
  `TIEMPO_TUTORIA` int(11) NOT NULL,
  `CALIFICACION_TUTOR` int(11) NOT NULL,
  `CALIFICACION_ESTUDIANTE` int(11) NOT NULL,
  `VALOR_TUTORIA` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tutorias`
--

INSERT INTO `tutorias` (`ID_APRENDIZ_TUTORIA`, `ID_TUTOR_TUTORIA`, `ID_AREA_CONOCIMIENTO_TUTORIA`, `FECHA_TUTORIA`, `TIEMPO_TUTORIA`, `CALIFICACION_TUTOR`, `CALIFICACION_ESTUDIANTE`, `VALOR_TUTORIA`) VALUES
('1000666777', '5478951', 'FILO', '2023-03-09', 30, 5, 5, 1000);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `agenda_tutores_aprendices`
--
ALTER TABLE `agenda_tutores_aprendices`
  ADD PRIMARY KEY (`ID_TUTOR`,`FECHA`,`ID_APRENDIZ`),
  ADD KEY `FK_AGENDA_ID_APREDIZ` (`ID_APRENDIZ`),
  ADD KEY `FK_AGENDA_ID_PAIS` (`ID_AREA_CONOCIMIENTO`);

--
-- Indices de la tabla `aprendices`
--
ALTER TABLE `aprendices`
  ADD PRIMARY KEY (`CEDULA_APRENDICES`),
  ADD KEY `FK_APRENDICES_PAIS` (`PÁIS_APRENDICES`);

--
-- Indices de la tabla `areas_conocimiento`
--
ALTER TABLE `areas_conocimiento`
  ADD PRIMARY KEY (`ID_AREA_CONOCIMIENTO`);

--
-- Indices de la tabla `paises`
--
ALTER TABLE `paises`
  ADD PRIMARY KEY (`ID_PAIS`),
  ADD KEY `ID_PAIS` (`ID_PAIS`);

--
-- Indices de la tabla `tutores`
--
ALTER TABLE `tutores`
  ADD PRIMARY KEY (`ID_TUTORES`),
  ADD KEY `FK_TUTORES_PAISES` (`PAIS_TUTOR`);

--
-- Indices de la tabla `tutores_areas_conocimiento`
--
ALTER TABLE `tutores_areas_conocimiento`
  ADD PRIMARY KEY (`ID_TUTOR`,`ID_AREA_CONOCIMIENTO`),
  ADD KEY `FK_AREA_CONOCIMIENTO` (`ID_AREA_CONOCIMIENTO`);

--
-- Indices de la tabla `tutorias`
--
ALTER TABLE `tutorias`
  ADD KEY `FK_ID_APRENDIZ` (`ID_APRENDIZ_TUTORIA`),
  ADD KEY `FK_ID_TUTOR` (`ID_TUTOR_TUTORIA`),
  ADD KEY `FK_ID_AREA_CONOCIMIENTO` (`ID_AREA_CONOCIMIENTO_TUTORIA`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `agenda_tutores_aprendices`
--
ALTER TABLE `agenda_tutores_aprendices`
  ADD CONSTRAINT `FK_AGENDA_ID_APREDIZ` FOREIGN KEY (`ID_APRENDIZ`) REFERENCES `aprendices` (`CEDULA_APRENDICES`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `FK_AGENDA_ID_PAIS` FOREIGN KEY (`ID_AREA_CONOCIMIENTO`) REFERENCES `areas_conocimiento` (`ID_AREA_CONOCIMIENTO`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `FK_AGENDA_ID_TUTOR` FOREIGN KEY (`ID_TUTOR`) REFERENCES `tutores` (`ID_TUTORES`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `aprendices`
--
ALTER TABLE `aprendices`
  ADD CONSTRAINT `FK_APRENDICES_PAIS` FOREIGN KEY (`PÁIS_APRENDICES`) REFERENCES `paises` (`ID_PAIS`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `tutores`
--
ALTER TABLE `tutores`
  ADD CONSTRAINT `FK_TUTORES_PAISES` FOREIGN KEY (`PAIS_TUTOR`) REFERENCES `paises` (`ID_PAIS`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `tutores_areas_conocimiento`
--
ALTER TABLE `tutores_areas_conocimiento`
  ADD CONSTRAINT `FK_AREA_CONOCIMIENTO` FOREIGN KEY (`ID_AREA_CONOCIMIENTO`) REFERENCES `areas_conocimiento` (`ID_AREA_CONOCIMIENTO`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `FK_TUTORES` FOREIGN KEY (`ID_TUTOR`) REFERENCES `tutores` (`ID_TUTORES`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `tutorias`
--
ALTER TABLE `tutorias`
  ADD CONSTRAINT `FK_ID_APRENDIZ` FOREIGN KEY (`ID_APRENDIZ_TUTORIA`) REFERENCES `aprendices` (`CEDULA_APRENDICES`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `FK_ID_AREA_CONOCIMIENTO` FOREIGN KEY (`ID_AREA_CONOCIMIENTO_TUTORIA`) REFERENCES `areas_conocimiento` (`ID_AREA_CONOCIMIENTO`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `FK_ID_TUTOR` FOREIGN KEY (`ID_TUTOR_TUTORIA`) REFERENCES `tutores` (`ID_TUTORES`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
