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
  `FechaCita` date DEFAULT NULL,
  `Detalles` text DEFAULT NULL,
  PRIMARY KEY (`idConsulta`),
  KEY `FKPacienteCita` (`idPaciente`),
  KEY `FKPersonalCita` (`idPersonal`),
  CONSTRAINT `FKPacienteCita` FOREIGN KEY (`idPaciente`) REFERENCES `pacientes` (`idPaciente`) ON UPDATE CASCADE,
  CONSTRAINT `FKPersonalCita` FOREIGN KEY (`idPersonal`) REFERENCES `personal` (`idPersonal`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.citas: ~0 rows (aproximadamente)
DELETE FROM `citas`;
/*!40000 ALTER TABLE `citas` DISABLE KEYS */;
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

-- Volcando datos para la tabla clinica.detalle_cita: ~0 rows (aproximadamente)
DELETE FROM `detalle_cita`;
/*!40000 ALTER TABLE `detalle_cita` DISABLE KEYS */;
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

-- Volcando datos para la tabla clinica.detalle_examenes: ~0 rows (aproximadamente)
DELETE FROM `detalle_examenes`;
/*!40000 ALTER TABLE `detalle_examenes` DISABLE KEYS */;
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

-- Volcando datos para la tabla clinica.detalle_recetas: ~1 rows (aproximadamente)
DELETE FROM `detalle_recetas`;
/*!40000 ALTER TABLE `detalle_recetas` DISABLE KEYS */;
INSERT INTO `detalle_recetas` (`idReceta`, `idMedicamento`) VALUES
	(0, 0),
	(0, 1);
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

-- Volcando datos para la tabla clinica.detalle_tratamientos: ~0 rows (aproximadamente)
DELETE FROM `detalle_tratamientos`;
/*!40000 ALTER TABLE `detalle_tratamientos` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_tratamientos` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.enfermedades
CREATE TABLE IF NOT EXISTS `enfermedades` (
  `idEnfermedad` int(11) NOT NULL,
  `Detalles` int(11) DEFAULT NULL,
  PRIMARY KEY (`idEnfermedad`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.enfermedades: ~0 rows (aproximadamente)
DELETE FROM `enfermedades`;
/*!40000 ALTER TABLE `enfermedades` DISABLE KEYS */;
/*!40000 ALTER TABLE `enfermedades` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.especialidad
CREATE TABLE IF NOT EXISTS `especialidad` (
  `idEspecialidad` int(11) NOT NULL,
  `Nombre` varchar(150) NOT NULL DEFAULT '',
  PRIMARY KEY (`idEspecialidad`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.especialidad: ~4 rows (aproximadamente)
DELETE FROM `especialidad`;
/*!40000 ALTER TABLE `especialidad` DISABLE KEYS */;
INSERT INTO `especialidad` (`idEspecialidad`, `Nombre`) VALUES
	(0, 'Enfermero'),
	(1, 'Doctor'),
	(2, 'Gerente'),
	(3, 'Intendente');
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

-- Volcando datos para la tabla clinica.examenes: ~0 rows (aproximadamente)
DELETE FROM `examenes`;
/*!40000 ALTER TABLE `examenes` DISABLE KEYS */;
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

-- Volcando datos para la tabla clinica.medicamentos: ~2 rows (aproximadamente)
DELETE FROM `medicamentos`;
/*!40000 ALTER TABLE `medicamentos` DISABLE KEYS */;
INSERT INTO `medicamentos` (`idMedicamento`, `idProveedor`, `Nombre`, `Precio`, `Cantidad`) VALUES
	(0, 1, 'Tapsin', 1, 500),
	(1, 1, 'Dolocrin', 1.5, 300);
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

-- Volcando datos para la tabla clinica.pacientes: ~4 rows (aproximadamente)
DELETE FROM `pacientes`;
/*!40000 ALTER TABLE `pacientes` DISABLE KEYS */;
INSERT INTO `pacientes` (`idPaciente`, `DUI`, `NIT`, `Nombre`, `Sexo`, `Telefono`, `Correo`, `Direccion`, `FechaNacimiento`, `Foto`) VALUES
	(0, '98765432-2', '1234-123456-123-1', 'Carlos Antonio Amaya Carranza', 'M', '2222-2222', 'e@gmail.com', 'Su casa', '2021-11-28', 'icon/pacientes/perfil0.jpg'),
	(1, '98765432-5', '1231-123451-123-1', 'Carlos Antonio Amaya Carranza', 'M', '2222-2222', 'e@gmail.com', 'Su casa', '2021-11-28', 'icon/pacientes/perfil1.jpg'),
	(2, '98765432-3', '9876-987654-987-5', 'Carlos Antonio Amaya Carranza', 'M', '2222-2222', 'e@gmail.com', 'Casa x Calle x Colonia x', '2021-11-28', 'icon/pacientes/perfil2.jpg'),
	(4, '98765432-4', '1231-123456-123-1', 'Carlos Antonio Amaya Carranza', 'M', '2222-2222', 'e@gmail.com', 'Mi casa', '2021-11-28', 'icon/pacientes/perfil4.jpg');
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

-- Volcando datos para la tabla clinica.personal: ~2 rows (aproximadamente)
DELETE FROM `personal`;
/*!40000 ALTER TABLE `personal` DISABLE KEYS */;
INSERT INTO `personal` (`idPersonal`, `DUI`, `NIT`, `Nombre`, `Sexo`, `Telefono`, `Correo`, `Direccion`, `FechaNacimiento`, `Foto`, `idEspecialidad`) VALUES
	(0, '12345678-9', '1234-123456-123-1', 'Carlos Jose Jose Jose', 'M', '7777 7777', 'j@gmail.com', 'Casa', '2021-11-28', 'icon/personal/perfil0.jpg', 1),
	(1, '32165498-7', '1234-123456-123-2', 'María María María María', 'M', '7777 7777', 'm@gmail.com', 'Casa', '2021-11-28', 'icon/personal/perfil1.jpg', 0);
/*!40000 ALTER TABLE `personal` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.proveedores
CREATE TABLE IF NOT EXISTS `proveedores` (
  `idProveedor` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL DEFAULT '',
  `Telefono` varchar(10) NOT NULL DEFAULT '',
  `Direccion` varchar(150) NOT NULL DEFAULT '',
  PRIMARY KEY (`idProveedor`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.proveedores: ~2 rows (aproximadamente)
DELETE FROM `proveedores`;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
INSERT INTO `proveedores` (`idProveedor`, `Nombre`, `Telefono`, `Direccion`) VALUES
	(0, 'Baller', '2244 2444', '2da calle, 6ta AV N, Edificio #20'),
	(1, 'Alcaslser', '2444 2444', '4ta calle, 6ta AV N, Edificio #20');
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

-- Volcando datos para la tabla clinica.recetas: ~1 rows (aproximadamente)
DELETE FROM `recetas`;
/*!40000 ALTER TABLE `recetas` DISABLE KEYS */;
INSERT INTO `recetas` (`idReceta`, `idPaciente`, `idPersonal`, `Detalles`) VALUES
	(0, 1, 0, 'dsdsdss');
/*!40000 ALTER TABLE `recetas` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.sintomas
CREATE TABLE IF NOT EXISTS `sintomas` (
  `idSintoma` int(11) NOT NULL,
  `Detalles` text DEFAULT NULL,
  PRIMARY KEY (`idSintoma`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.sintomas: ~0 rows (aproximadamente)
DELETE FROM `sintomas`;
/*!40000 ALTER TABLE `sintomas` DISABLE KEYS */;
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

-- Volcando datos para la tabla clinica.sintoma_enfermedad: ~0 rows (aproximadamente)
DELETE FROM `sintoma_enfermedad`;
/*!40000 ALTER TABLE `sintoma_enfermedad` DISABLE KEYS */;
/*!40000 ALTER TABLE `sintoma_enfermedad` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.tipo_examen
CREATE TABLE IF NOT EXISTS `tipo_examen` (
  `idTipo` int(11) NOT NULL,
  `Nombre` varchar(75) DEFAULT NULL,
  `Detalles` text DEFAULT NULL,
  PRIMARY KEY (`idTipo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.tipo_examen: ~0 rows (aproximadamente)
DELETE FROM `tipo_examen`;
/*!40000 ALTER TABLE `tipo_examen` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_examen` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.tipo_tratamiento
CREATE TABLE IF NOT EXISTS `tipo_tratamiento` (
  `idTratamiento` int(11) NOT NULL,
  `Detalle` text DEFAULT NULL,
  PRIMARY KEY (`idTratamiento`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.tipo_tratamiento: ~0 rows (aproximadamente)
DELETE FROM `tipo_tratamiento`;
/*!40000 ALTER TABLE `tipo_tratamiento` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_tratamiento` ENABLE KEYS */;

-- Volcando estructura para tabla clinica.tratamientos
CREATE TABLE IF NOT EXISTS `tratamientos` (
  `idTratamiento` int(11) NOT NULL,
  `idTipo` int(11) DEFAULT NULL,
  `idReceta` int(11) DEFAULT NULL,
  `FechaIniciar` date DEFAULT NULL,
  `FechaFinalizar` date DEFAULT NULL,
  `Estado` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`idTratamiento`),
  KEY `FKTratamientoTipo` (`idTipo`),
  KEY `FKRecetaTratamiento` (`idReceta`),
  CONSTRAINT `FKRecetaTratamiento` FOREIGN KEY (`idReceta`) REFERENCES `recetas` (`idReceta`) ON UPDATE CASCADE,
  CONSTRAINT `FKTratamientoTipo` FOREIGN KEY (`idTipo`) REFERENCES `tipo_tratamiento` (`idTratamiento`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla clinica.tratamientos: ~0 rows (aproximadamente)
DELETE FROM `tratamientos`;
/*!40000 ALTER TABLE `tratamientos` DISABLE KEYS */;
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

-- Volcando datos para la tabla clinica.turnos: ~2 rows (aproximadamente)
DELETE FROM `turnos`;
/*!40000 ALTER TABLE `turnos` DISABLE KEYS */;
INSERT INTO `turnos` (`idTurno`, `Nombre`, `HoraInicio`, `HoraSalida`, `DiaInicio`, `DiaSalida`) VALUES
	(0, 'Turno Vespertino', '14:53:00', '15:53:00', 'Martes', 'Miercoles'),
	(1, 'Turno Matutino', '03:09:00', '05:09:00', 'Lunes', 'Martes');
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

-- Volcando datos para la tabla clinica.turnos_personal: ~3 rows (aproximadamente)
DELETE FROM `turnos_personal`;
/*!40000 ALTER TABLE `turnos_personal` DISABLE KEYS */;
INSERT INTO `turnos_personal` (`idTurno`, `idPersonal`) VALUES
	(0, 0),
	(1, 0),
	(1, 1);
/*!40000 ALTER TABLE `turnos_personal` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
