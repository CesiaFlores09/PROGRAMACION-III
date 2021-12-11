-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.6.4-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para clinica
CREATE DATABASE IF NOT EXISTS `clinica` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `clinica`;

-- Volcando estructura para tabla clinica.citas
CREATE TABLE IF NOT EXISTS `citas` (
  `idConsulta` int(11) NOT NULL,
  `idPaciente` int(11) DEFAULT NULL,
  `idPersonal` int(11) DEFAULT NULL,
  `FechaCita` datetime DEFAULT NULL,
  `Detalles` text DEFAULT NULL,
  PRIMARY KEY (`idConsulta`),
  KEY `FKPacienteCita` (`idPaciente`),
  KEY `FKPersonalCita` (`idPersonal`),
  CONSTRAINT `FKPacienteCita` FOREIGN KEY (`idPaciente`) REFERENCES `pacientes` (`idPaciente`) ON UPDATE CASCADE,
  CONSTRAINT `FKPersonalCita` FOREIGN KEY (`idPersonal`) REFERENCES `personal` (`idPersonal`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.citas: ~14 rows (aproximadamente)
DELETE FROM `citas`;
/*!40000 ALTER TABLE `citas` DISABLE KEYS */;
INSERT INTO `citas` (`idConsulta`, `idPaciente`, `idPersonal`, `FechaCita`, `Detalles`) VALUES
	(0, 2, 0, '2021-12-15 20:30:00', ''),
	(2, 5, 2, '2021-12-15 13:30:00', 'La roca B|'),
	(3, 1, 2, '2021-12-14 20:00:00', ''),
	(4, 1, 0, '2021-12-14 03:00:00', 'dcs'),
	(5, 2, 2, '2021-12-15 18:30:00', 'asas'),
	(6, 0, 0, '2021-12-14 03:30:00', 'xc'),
	(7, 2, 2, '2021-12-14 14:30:00', 'dfdf'),
	(8, 0, 0, '2021-12-13 05:00:00', 'sd'),
	(9, 0, 0, '2021-12-14 09:30:00', ''),
	(10, 0, 0, '2021-12-14 03:30:00', 'df'),
	(11, 0, 1, '2021-12-14 03:30:00', 'ds'),
	(12, 0, 0, '2021-12-13 05:00:00', 'ds'),
	(13, 0, 0, '2021-12-14 16:00:00', 'sdds'),
	(14, 0, 0, '2021-12-14 04:00:00', 'fd');
/*!40000 ALTER TABLE `citas` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.detalle_cita
CREATE TABLE IF NOT EXISTS `detalle_cita` (
  `idCita` int(11) DEFAULT NULL,
  `idSintoma` int(11) DEFAULT NULL,
  KEY `FKCitaDetalle` (`idCita`),
  KEY `FKSintomaDetalleCita` (`idSintoma`),
  CONSTRAINT `FKCitaDetalle` FOREIGN KEY (`idCita`) REFERENCES `citas` (`idConsulta`) ON UPDATE CASCADE,
  CONSTRAINT `FKSintomaDetalleCita` FOREIGN KEY (`idSintoma`) REFERENCES `sintomas` (`idSintoma`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.detalle_cita: ~23 rows (aproximadamente)
DELETE FROM `detalle_cita`;
/*!40000 ALTER TABLE `detalle_cita` DISABLE KEYS */;
INSERT INTO `detalle_cita` (`idCita`, `idSintoma`) VALUES
	(0, 0),
	(0, 1),
	(2, 0),
	(2, 10),
	(3, 1),
	(3, 2),
	(4, 1),
	(5, 0),
	(5, 2),
	(6, 0),
	(7, 1),
	(8, 9),
	(10, 7),
	(10, 8),
	(12, 1),
	(13, 0),
	(13, 1),
	(13, 2),
	(13, 3),
	(13, 4),
	(13, 5),
	(13, 6),
	(14, 0);
/*!40000 ALTER TABLE `detalle_cita` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.detalle_examenes
CREATE TABLE IF NOT EXISTS `detalle_examenes` (
  `idExamen` int(11) DEFAULT NULL,
  `idEnfermedad` int(11) DEFAULT NULL,
  `Estado` int(11) DEFAULT NULL,
  KEY `FKExamenDetalle` (`idExamen`),
  KEY `FKEnfermedadExamen` (`idEnfermedad`),
  CONSTRAINT `FKEnfermedadExamen` FOREIGN KEY (`idEnfermedad`) REFERENCES `enfermedades` (`idEnfermedad`) ON UPDATE CASCADE,
  CONSTRAINT `FKExamenDetalle` FOREIGN KEY (`idExamen`) REFERENCES `examenes` (`idExamen`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.detalle_examenes: ~6 rows (aproximadamente)
DELETE FROM `detalle_examenes`;
/*!40000 ALTER TABLE `detalle_examenes` DISABLE KEYS */;
INSERT INTO `detalle_examenes` (`idExamen`, `idEnfermedad`, `Estado`) VALUES
	(0, 0, 2),
	(0, 1, 0),
	(1, 1, 1),
	(2, 0, 1),
	(3, 0, 1),
	(4, 0, 0);
/*!40000 ALTER TABLE `detalle_examenes` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.detalle_recetas
CREATE TABLE IF NOT EXISTS `detalle_recetas` (
  `idReceta` int(11) NOT NULL,
  `idMedicamento` int(11) DEFAULT NULL,
  KEY `FKMedicamentoReceta` (`idMedicamento`),
  KEY `FKRecetaDetalle` (`idReceta`),
  CONSTRAINT `FKMedicamentoReceta` FOREIGN KEY (`idMedicamento`) REFERENCES `medicamentos` (`idMedicamento`) ON UPDATE CASCADE,
  CONSTRAINT `FKRecetaDetalle` FOREIGN KEY (`idReceta`) REFERENCES `recetas` (`idReceta`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.detalle_recetas: ~2 rows (aproximadamente)
DELETE FROM `detalle_recetas`;
/*!40000 ALTER TABLE `detalle_recetas` DISABLE KEYS */;
INSERT INTO `detalle_recetas` (`idReceta`, `idMedicamento`) VALUES
	(0, 2),
	(1, 0);
/*!40000 ALTER TABLE `detalle_recetas` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.detalle_tratamientos
CREATE TABLE IF NOT EXISTS `detalle_tratamientos` (
  `idTratamiento` int(11) DEFAULT NULL,
  `idExamen` int(11) DEFAULT NULL,
  KEY `FKTratamientoDetalle` (`idTratamiento`),
  KEY `FKExamenTratamientoDetalle` (`idExamen`),
  CONSTRAINT `FKExamenTratamientoDetalle` FOREIGN KEY (`idExamen`) REFERENCES `examenes` (`idExamen`) ON UPDATE CASCADE,
  CONSTRAINT `FKTratamientoDetalle` FOREIGN KEY (`idTratamiento`) REFERENCES `tratamientos` (`idTratamiento`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.detalle_tratamientos: ~5 rows (aproximadamente)
DELETE FROM `detalle_tratamientos`;
/*!40000 ALTER TABLE `detalle_tratamientos` DISABLE KEYS */;
INSERT INTO `detalle_tratamientos` (`idTratamiento`, `idExamen`) VALUES
	(0, 0),
	(1, 0),
	(2, 1),
	(3, 2),
	(4, 3);
/*!40000 ALTER TABLE `detalle_tratamientos` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.enfermedades
CREATE TABLE IF NOT EXISTS `enfermedades` (
  `idEnfermedad` int(11) NOT NULL,
  `Nombre` varchar(70) DEFAULT NULL,
  `Detalles` text DEFAULT NULL,
  PRIMARY KEY (`idEnfermedad`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.enfermedades: ~2 rows (aproximadamente)
DELETE FROM `enfermedades`;
/*!40000 ALTER TABLE `enfermedades` DISABLE KEYS */;
INSERT INTO `enfermedades` (`idEnfermedad`, `Nombre`, `Detalles`) VALUES
	(0, 'Fiebre Común', 'Ase calor'),
	(1, 'Gonorrea', 'Vomita pero no por la boca');
/*!40000 ALTER TABLE `enfermedades` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.especialidad
CREATE TABLE IF NOT EXISTS `especialidad` (
  `idEspecialidad` int(11) NOT NULL,
  `Nombre` varchar(150) NOT NULL DEFAULT '',
  PRIMARY KEY (`idEspecialidad`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.especialidad: ~5 rows (aproximadamente)
DELETE FROM `especialidad`;
/*!40000 ALTER TABLE `especialidad` DISABLE KEYS */;
INSERT INTO `especialidad` (`idEspecialidad`, `Nombre`) VALUES
	(0, 'Enfermero'),
	(1, 'Doctor'),
	(2, 'Gerente'),
	(3, 'Intendente'),
	(4, 'Cirujano');
/*!40000 ALTER TABLE `especialidad` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.examenes
CREATE TABLE IF NOT EXISTS `examenes` (
  `idExamen` int(11) NOT NULL,
  `idTipoExamen` int(11) DEFAULT NULL,
  `idCita` int(11) DEFAULT NULL,
  `FechaRealizacion` date DEFAULT NULL,
  `FechaResultados` date DEFAULT NULL,
  `Estado` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`idExamen`),
  KEY `FKTipoExamen` (`idTipoExamen`),
  KEY `FKCitaExamen` (`idCita`),
  CONSTRAINT `FKCitaExamen` FOREIGN KEY (`idCita`) REFERENCES `citas` (`idConsulta`) ON UPDATE CASCADE,
  CONSTRAINT `FKTipoExamen` FOREIGN KEY (`idTipoExamen`) REFERENCES `tipo_examen` (`idTipo`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.examenes: ~5 rows (aproximadamente)
DELETE FROM `examenes`;
/*!40000 ALTER TABLE `examenes` DISABLE KEYS */;
INSERT INTO `examenes` (`idExamen`, `idTipoExamen`, `idCita`, `FechaRealizacion`, `FechaResultados`, `Estado`) VALUES
	(0, 2, 2, '2021-12-15', '2021-12-23', 2),
	(1, 1, 0, '2021-12-15', '2021-12-23', 1),
	(2, 4, 8, '2021-12-13', '2021-12-16', 1),
	(3, 1, 10, '2021-12-14', '2021-12-15', 1),
	(4, 2, 12, '2021-12-13', '2021-12-13', 0);
/*!40000 ALTER TABLE `examenes` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.medicamentos
CREATE TABLE IF NOT EXISTS `medicamentos` (
  `idMedicamento` int(11) NOT NULL,
  `idProveedor` int(11) NOT NULL,
  `Nombre` varchar(150) NOT NULL DEFAULT '',
  `Precio` float NOT NULL DEFAULT 0,
  `Cantidad` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`idMedicamento`),
  KEY `FKProveedor` (`idProveedor`),
  CONSTRAINT `FKProveedor` FOREIGN KEY (`idProveedor`) REFERENCES `proveedores` (`idProveedor`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.medicamentos: ~3 rows (aproximadamente)
DELETE FROM `medicamentos`;
/*!40000 ALTER TABLE `medicamentos` DISABLE KEYS */;
INSERT INTO `medicamentos` (`idMedicamento`, `idProveedor`, `Nombre`, `Precio`, `Cantidad`) VALUES
	(0, 1, 'Tapsin', 1, 500),
	(1, 1, 'Dolocrin', 1.5, 300),
	(2, 0, 'Dfdgdfg', 7.2, 44);
/*!40000 ALTER TABLE `medicamentos` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.pacientes
CREATE TABLE IF NOT EXISTS `pacientes` (
  `idPaciente` int(11) NOT NULL,
  `DUI` varchar(10) NOT NULL DEFAULT '',
  `NIT` varchar(17) NOT NULL DEFAULT '',
  `Nombre` varchar(150) NOT NULL DEFAULT '',
  `Sexo` varchar(150) NOT NULL DEFAULT '',
  `Telefono` varchar(9) NOT NULL DEFAULT '',
  `Correo` varchar(150) NOT NULL DEFAULT '',
  `Direccion` varchar(150) NOT NULL DEFAULT '',
  `FechaNacimiento` date NOT NULL DEFAULT '0000-00-00',
  `Foto` text NOT NULL,
  PRIMARY KEY (`idPaciente`),
  UNIQUE KEY `DUI` (`DUI`),
  UNIQUE KEY `NIT` (`NIT`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.pacientes: ~9 rows (aproximadamente)
DELETE FROM `pacientes`;
/*!40000 ALTER TABLE `pacientes` DISABLE KEYS */;
INSERT INTO `pacientes` (`idPaciente`, `DUI`, `NIT`, `Nombre`, `Sexo`, `Telefono`, `Correo`, `Direccion`, `FechaNacimiento`, `Foto`) VALUES
	(0, '06142428-3', '1234-123456-123-1', 'David José Hernandez Martinez', 'F', '2222-2222', 'e@gmail.com', 'Casa x Calle x Colonia x', '2021-12-04', 'icon/pacientes/perfil0.jpg'),
	(1, '42356781-9', '4862-579135-915-5', 'William Alexander Amaya García', 'M', '7272-7272', 'william@gmail.com', 'Colonia X Barrio X casa #X', '2021-12-04', 'icon/pacientes/perfil1.jpg'),
	(2, '98653214-7', '5784-986573-986-9', 'Will Smith', 'M', '7272-7272', 'willsmith@gmail.com', 'Colonia X calle #2 AV 12 casa #3', '2021-12-04', 'icon/pacientes/perfil2.jpg'),
	(3, '12345678-9', '1234-567890-123-4', 'Riven La Exiliada', 'F', '2222-2222', 'riven@gmail.com', 'Exiliada de noxus', '2021-12-14', 'icon/pacientes/perfil3.jpg'),
	(4, '45612378-9', '7894-123456-790-2', 'Vicha Más Tarada', 'F', '2222-2222', 'tdetarada@gmail.com', 'Debajo de un puente', '2021-12-14', 'icon/pacientes/perfil4.jpg'),
	(5, '64591372-8', '6497-583126-648-6', 'La Roca', 'M', '2222-2222', 'laroca@gmail.com', 'Colonia X calle #2 AV 12 casa #1', '2002-06-12', 'icon/pacientes/perfil5.jpg'),
	(6, '24657982-3', '5621-648531-324-8', 'William Alexander Amaya García', 'F', '2222-2222', 'william@gmail.com', 'Casa x Calle x Colonia x', '2021-12-09', 'icon/pacientes/perfil6.jpg'),
	(7, '92432148-5', '1123-150900-109-3', 'Elías Mauricio Parada Lozano', 'F', '2331-4590', 'olaf@olaf.olaf', 'Colonia X calle #2 AV 12 casa #3', '2021-12-11', 'icon/pacientes/perfil7.jpg'),
	(8, '02495046-3', '0614-051286-129-4', 'Elías Mauricio Parada Lozano', 'F', '2222-2222', 'e@gmail.com', 'Casa x Calle x Colonia x', '2021-12-11', 'icon/pacientes/perfil8.jpg');
/*!40000 ALTER TABLE `pacientes` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.personal
CREATE TABLE IF NOT EXISTS `personal` (
  `idPersonal` int(11) NOT NULL,
  `DUI` varchar(10) NOT NULL DEFAULT '',
  `NIT` varchar(17) NOT NULL DEFAULT '',
  `Nombre` varchar(150) NOT NULL DEFAULT '',
  `Sexo` varchar(150) NOT NULL DEFAULT '',
  `Telefono` varchar(9) NOT NULL DEFAULT '',
  `Correo` varchar(150) NOT NULL DEFAULT '',
  `Direccion` varchar(150) NOT NULL DEFAULT '',
  `FechaNacimiento` date NOT NULL DEFAULT '0000-00-00',
  `Foto` text NOT NULL,
  `idEspecialidad` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`idPersonal`),
  UNIQUE KEY `DUI` (`DUI`),
  UNIQUE KEY `NIT` (`NIT`),
  KEY `FKEspecialidad` (`idEspecialidad`),
  CONSTRAINT `FKEspecialidad` FOREIGN KEY (`idEspecialidad`) REFERENCES `especialidad` (`idEspecialidad`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.personal: ~6 rows (aproximadamente)
DELETE FROM `personal`;
/*!40000 ALTER TABLE `personal` DISABLE KEYS */;
INSERT INTO `personal` (`idPersonal`, `DUI`, `NIT`, `Nombre`, `Sexo`, `Telefono`, `Correo`, `Direccion`, `FechaNacimiento`, `Foto`, `idEspecialidad`) VALUES
	(0, '12345678-9', '1234-123456-123-1', 'Carlos Jose Jose Jose', 'M', '7777 7777', 'j@gmail.com', 'Casa', '2021-11-28', 'icon/personal/personal0.jpg', 0),
	(1, '32165498-7', '1234-123456-123-2', 'María María María María', 'M', '7777 7777', 'm@gmail.com', 'Casa', '2021-11-28', 'icon/personal/personal1.jpg', 0),
	(2, '54632146-8', '1234-123456-123-3', 'María María María María', 'F', '7777 7777', 'm@gmail.com', 'Casa', '2021-11-28', 'icon/personal/personal2.jpg', 4),
	(3, '58761348-5', '6482-357816-555-6', 'María María María María', 'M', '7777 7777', 'j@gmail.com', 'Casa', '2021-12-09', 'icon/personal/personal3.jpg', 4),
	(5, '06142428-3', '1123-150900-108-5', 'Carlos Jose Jose Jose', 'M', '7777 7777', 'j@gmail.com', 'Casa', '2021-12-11', 'icon/personal/personal5.jpg', 1),
	(6, '45455375-8', '1121-120100-109-1', 'María María María María', 'M', '7777 7777', 'j@gmail.com', 'Casa', '2021-12-11', 'icon/personal/personal6.jpg', 1);
/*!40000 ALTER TABLE `personal` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.proveedores
CREATE TABLE IF NOT EXISTS `proveedores` (
  `idProveedor` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL DEFAULT '',
  `Telefono` varchar(10) NOT NULL DEFAULT '',
  `Direccion` varchar(150) NOT NULL DEFAULT '',
  PRIMARY KEY (`idProveedor`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.proveedores: ~3 rows (aproximadamente)
DELETE FROM `proveedores`;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
INSERT INTO `proveedores` (`idProveedor`, `Nombre`, `Telefono`, `Direccion`) VALUES
	(0, 'Baller', '2244 2444', '2da calle, 6ta AV N, Edificio #20'),
	(1, 'Alcaslser', '2444 2444', '4ta calle, 6ta AV N, Edificio #20'),
	(2, 'Baller', '2444 2444', '4ta calle, 6ta AV N, Edificio #20');
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.recetas
CREATE TABLE IF NOT EXISTS `recetas` (
  `idReceta` int(11) NOT NULL,
  `idPaciente` int(11) DEFAULT NULL,
  `idPersonal` int(11) DEFAULT NULL,
  `Detalles` text DEFAULT NULL,
  PRIMARY KEY (`idReceta`),
  KEY `FKPacienteReceta` (`idPaciente`),
  KEY `FKPersonalReceta` (`idPersonal`),
  CONSTRAINT `FKPacienteReceta` FOREIGN KEY (`idPaciente`) REFERENCES `pacientes` (`idPaciente`) ON UPDATE CASCADE,
  CONSTRAINT `FKPersonalReceta` FOREIGN KEY (`idPersonal`) REFERENCES `personal` (`idPersonal`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.recetas: ~2 rows (aproximadamente)
DELETE FROM `recetas`;
/*!40000 ALTER TABLE `recetas` DISABLE KEYS */;
INSERT INTO `recetas` (`idReceta`, `idPaciente`, `idPersonal`, `Detalles`) VALUES
	(0, 1, 1, 'Tomar porque si'),
	(1, 3, 0, 'Tomatelas y ya no preguntes');
/*!40000 ALTER TABLE `recetas` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.sintomas
CREATE TABLE IF NOT EXISTS `sintomas` (
  `idSintoma` int(11) NOT NULL,
  `Nombre` varchar(70) DEFAULT NULL,
  `Detalles` text DEFAULT NULL,
  PRIMARY KEY (`idSintoma`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.sintomas: ~11 rows (aproximadamente)
DELETE FROM `sintomas`;
/*!40000 ALTER TABLE `sintomas` DISABLE KEYS */;
INSERT INTO `sintomas` (`idSintoma`, `Nombre`, `Detalles`) VALUES
	(0, 'Dolor De Cabeza', 'Lele cabecha'),
	(1, 'Fiebre Lebe', 'Se pone caliente'),
	(2, 'Dolor De Articulaciones', 'No siento mis piernas!!!'),
	(3, 'Vomito', 'ki asco'),
	(4, 'Pierna Amputada', 'Am'),
	(5, 'Descorazanación', 'Cuando la persona extrañamente vive sin corazón'),
	(6, 'Vertigo', 'Mareo o miedo al encontrase en la sima... del exito'),
	(7, 'Buscando Al Nemos', 'Un film animado de un pez payaso que busca a su hijo porque el invecil fue capturado'),
	(8, 'Tos', 'Cuando toces'),
	(9, 'Dolor De Ojos', 'Que le duelen los ojos :y'),
	(10, 'Migraña', 'Migración a las arañas');
/*!40000 ALTER TABLE `sintomas` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.sintoma_enfermedad
CREATE TABLE IF NOT EXISTS `sintoma_enfermedad` (
  `idEnfermedad` int(11) DEFAULT NULL,
  `idSintoma` int(11) DEFAULT NULL,
  KEY `FKSintomaEnfermedadEnfermedad` (`idEnfermedad`),
  KEY `FKSintomaEnfermedadSintoma` (`idSintoma`),
  CONSTRAINT `FKSintomaEnfermedadEnfermedad` FOREIGN KEY (`idEnfermedad`) REFERENCES `enfermedades` (`idEnfermedad`) ON UPDATE CASCADE,
  CONSTRAINT `FKSintomaEnfermedadSintoma` FOREIGN KEY (`idSintoma`) REFERENCES `sintomas` (`idSintoma`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.sintoma_enfermedad: ~4 rows (aproximadamente)
DELETE FROM `sintoma_enfermedad`;
/*!40000 ALTER TABLE `sintoma_enfermedad` DISABLE KEYS */;
INSERT INTO `sintoma_enfermedad` (`idEnfermedad`, `idSintoma`) VALUES
	(0, 0),
	(0, 1),
	(0, 2),
	(1, 3);
/*!40000 ALTER TABLE `sintoma_enfermedad` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.tipo_examen
CREATE TABLE IF NOT EXISTS `tipo_examen` (
  `idTipo` int(11) NOT NULL,
  `Nombre` varchar(75) DEFAULT NULL,
  `Detalles` text DEFAULT NULL,
  PRIMARY KEY (`idTipo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.tipo_examen: ~4 rows (aproximadamente)
DELETE FROM `tipo_examen`;
/*!40000 ALTER TABLE `tipo_examen` DISABLE KEYS */;
INSERT INTO `tipo_examen` (`idTipo`, `Nombre`, `Detalles`) VALUES
	(1, 'Examen de sangre', 'Para los vampiros'),
	(2, 'Examen de orina', 'Miados'),
	(3, 'Examen de eces', 'kk'),
	(4, 'Radiografia', 'Rachos lasers');
/*!40000 ALTER TABLE `tipo_examen` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.tipo_tratamiento
CREATE TABLE IF NOT EXISTS `tipo_tratamiento` (
  `idTratamiento` int(11) NOT NULL,
  `Nombre` varchar(75) DEFAULT NULL,
  `Detalles` text DEFAULT NULL,
  PRIMARY KEY (`idTratamiento`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.tipo_tratamiento: ~2 rows (aproximadamente)
DELETE FROM `tipo_tratamiento`;
/*!40000 ALTER TABLE `tipo_tratamiento` DISABLE KEYS */;
INSERT INTO `tipo_tratamiento` (`idTratamiento`, `Nombre`, `Detalles`) VALUES
	(0, 'Tratamiento Algo', 'No se, que tratamientos tiene una clinica, una quimio, nah eso pa un hospital.'),
	(1, 'Reposo B)', 'No se, algui tengo que poenr para probar que esto srive');
/*!40000 ALTER TABLE `tipo_tratamiento` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.tratamientos
CREATE TABLE IF NOT EXISTS `tratamientos` (
  `idTratamiento` int(11) NOT NULL,
  `idTipo` int(11) DEFAULT NULL,
  `FechaIniciar` date DEFAULT NULL,
  `FechaFinalizar` date DEFAULT NULL,
  `Estado` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`idTratamiento`),
  KEY `FKTratamientoTipo` (`idTipo`),
  CONSTRAINT `FKTratamientoTipo` FOREIGN KEY (`idTipo`) REFERENCES `tipo_tratamiento` (`idTratamiento`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.tratamientos: ~5 rows (aproximadamente)
DELETE FROM `tratamientos`;
/*!40000 ALTER TABLE `tratamientos` DISABLE KEYS */;
INSERT INTO `tratamientos` (`idTratamiento`, `idTipo`, `FechaIniciar`, `FechaFinalizar`, `Estado`) VALUES
	(0, 0, '2021-12-09', '2021-12-09', 0),
	(1, 0, '2021-12-09', '2021-12-09', 1),
	(2, 1, '2021-12-09', '2021-12-09', 0),
	(3, 1, '2021-12-09', '2021-12-09', 0),
	(4, 0, '2021-12-09', '2021-12-09', 0);
/*!40000 ALTER TABLE `tratamientos` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.turnos
CREATE TABLE IF NOT EXISTS `turnos` (
  `idTurno` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL DEFAULT '',
  `HoraInicio` time DEFAULT NULL,
  `HoraSalida` time DEFAULT NULL,
  `DiaInicio` varchar(10) DEFAULT NULL,
  `DiaSalida` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`idTurno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.turnos: ~5 rows (aproximadamente)
DELETE FROM `turnos`;
/*!40000 ALTER TABLE `turnos` DISABLE KEYS */;
INSERT INTO `turnos` (`idTurno`, `Nombre`, `HoraInicio`, `HoraSalida`, `DiaInicio`, `DiaSalida`) VALUES
	(0, 'Turno Vespertino', '14:53:00', '15:53:00', 'Martes', 'Miercoles'),
	(1, 'Turno Matutino', '03:09:00', '05:09:00', 'Lunes', 'Martes'),
	(2, 'Turno Vespertino Sala De Espera', '13:50:00', '20:50:00', 'Martes', 'Miercoles'),
	(3, 'Ajio', '21:06:00', '22:06:00', 'Miercoles', 'Jueves'),
	(4, 'Ajio', '02:04:00', '18:04:00', 'Lunes', 'Lunes');
/*!40000 ALTER TABLE `turnos` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.turnos_personal
CREATE TABLE IF NOT EXISTS `turnos_personal` (
  `idTurno` int(11) DEFAULT NULL,
  `idPersonal` int(11) DEFAULT NULL,
  KEY `FKHorario` (`idTurno`),
  KEY `FKHorarioPersonal` (`idPersonal`),
  CONSTRAINT `FKHorario` FOREIGN KEY (`idTurno`) REFERENCES `turnos` (`idTurno`) ON UPDATE CASCADE,
  CONSTRAINT `FKHorarioPersonal` FOREIGN KEY (`idPersonal`) REFERENCES `personal` (`idPersonal`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.turnos_personal: ~12 rows (aproximadamente)
DELETE FROM `turnos_personal`;
/*!40000 ALTER TABLE `turnos_personal` DISABLE KEYS */;
INSERT INTO `turnos_personal` (`idTurno`, `idPersonal`) VALUES
	(0, 0),
	(1, 0),
	(1, 1),
	(0, 2),
	(2, 2),
	(4, 2),
	(1, 3),
	(3, 3),
	(4, 3),
	(2, 5),
	(4, 5),
	(0, 6);
/*!40000 ALTER TABLE `turnos_personal` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
