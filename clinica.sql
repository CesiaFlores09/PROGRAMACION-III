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

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla clinica.detalle_examenes
CREATE TABLE IF NOT EXISTS `detalle_examenes` (
  `idExamen` int(11) DEFAULT NULL,
  `idPaciente` int(11) DEFAULT NULL,
  `idConsulta` int(11) DEFAULT NULL,
  `FechaRealizacion` date DEFAULT NULL,
  `FechaResultado` date DEFAULT NULL,
  `Estado` tinyint(4) DEFAULT NULL,
  KEY `FKExamenDetalle` (`idExamen`),
  KEY `FKPacienteExamenDetalle` (`idPaciente`),
  KEY `FKCitaExamenDetalle` (`idConsulta`),
  CONSTRAINT `FKCitaExamenDetalle` FOREIGN KEY (`idConsulta`) REFERENCES `citas` (`idConsulta`) ON UPDATE CASCADE,
  CONSTRAINT `FKExamenDetalle` FOREIGN KEY (`idExamen`) REFERENCES `examenes` (`idExamen`) ON UPDATE CASCADE,
  CONSTRAINT `FKPacienteExamenDetalle` FOREIGN KEY (`idPaciente`) REFERENCES `pacientes` (`idPaciente`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla clinica.detalle_recetas
CREATE TABLE IF NOT EXISTS `detalle_recetas` (
  `idReceta` int(11) NOT NULL,
  `idMedicamento` int(11) DEFAULT NULL,
  PRIMARY KEY (`idReceta`),
  KEY `FKMedicamentoReceta` (`idMedicamento`),
  CONSTRAINT `FKMedicamentoReceta` FOREIGN KEY (`idMedicamento`) REFERENCES `medicamentos` (`idMedicamento`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla clinica.detalle_tratamientos
CREATE TABLE IF NOT EXISTS `detalle_tratamientos` (
  `idTratamiento` int(11) DEFAULT NULL,
  `idPaciente` int(11) DEFAULT NULL,
  `idExamen` int(11) DEFAULT NULL,
  `FechaInicio` date DEFAULT NULL,
  `FechaFinalizacion` date DEFAULT NULL,
  `Estado` tinyint(4) DEFAULT NULL,
  KEY `FKTratamientoDetalle` (`idTratamiento`),
  KEY `FKPacienteTratamientoDetalle` (`idPaciente`),
  KEY `FKExamenTratamientoDetalle` (`idExamen`),
  CONSTRAINT `FKExamenTratamientoDetalle` FOREIGN KEY (`idExamen`) REFERENCES `examenes` (`idExamen`) ON UPDATE CASCADE,
  CONSTRAINT `FKPacienteTratamientoDetalle` FOREIGN KEY (`idPaciente`) REFERENCES `pacientes` (`idPaciente`) ON UPDATE CASCADE,
  CONSTRAINT `FKTratamientoDetalle` FOREIGN KEY (`idTratamiento`) REFERENCES `tratamientos` (`idTratamiento`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla clinica.especialidad
CREATE TABLE IF NOT EXISTS `especialidad` (
  `idEspecialidad` int(11) NOT NULL,
  `Nombre` varchar(150) NOT NULL DEFAULT '',
  PRIMARY KEY (`idEspecialidad`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla clinica.examenes
CREATE TABLE IF NOT EXISTS `examenes` (
  `idExamen` int(11) NOT NULL,
  `idTipoExamen` int(11) DEFAULT NULL,
  PRIMARY KEY (`idExamen`),
  KEY `FKTipoExamen` (`idTipoExamen`),
  CONSTRAINT `FKTipoExamen` FOREIGN KEY (`idTipoExamen`) REFERENCES `tipo_examen` (`idTipo`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla clinica.medicamentos
CREATE TABLE IF NOT EXISTS `medicamentos` (
  `idMedicamento` int(11) NOT NULL,
  `idProveedor` int(11) NOT NULL,
  `Nombre` varchar(150) NOT NULL DEFAULT '',
  `Cantidad` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`idMedicamento`),
  KEY `FKProveedor` (`idProveedor`),
  CONSTRAINT `FKProveedor` FOREIGN KEY (`idProveedor`) REFERENCES `proveedores` (`idProveedor`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla clinica.pacientes
CREATE TABLE IF NOT EXISTS `pacientes` (
  `idPaciente` int(11) NOT NULL,
  `DUI` varchar(10) NOT NULL DEFAULT '',
  `Nombre` varchar(150) NOT NULL DEFAULT '',
  `Telefono` varchar(9) NOT NULL DEFAULT '',
  `Correo` varchar(150) NOT NULL DEFAULT '',
  `Direccion` varchar(150) NOT NULL DEFAULT '',
  `FechaNacimiento` date NOT NULL DEFAULT '0000-00-00',
  `Foto` text NOT NULL,
  PRIMARY KEY (`idPaciente`),
  UNIQUE KEY `DUI` (`DUI`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla clinica.personal
CREATE TABLE IF NOT EXISTS `personal` (
  `idPersonal` int(11) NOT NULL,
  `DUI` varchar(10) NOT NULL DEFAULT '',
  `Nombre` varchar(150) NOT NULL DEFAULT '',
  `Telefono` varchar(9) NOT NULL DEFAULT '',
  `Correo` varchar(150) NOT NULL DEFAULT '',
  `Direccion` varchar(150) NOT NULL DEFAULT '',
  `FechaNacimiento` date NOT NULL DEFAULT '0000-00-00',
  `Foto` text NOT NULL,
  `idEspecialidad` int(11) NOT NULL DEFAULT 0,
  `idTurno` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`idPersonal`),
  UNIQUE KEY `DUI` (`DUI`),
  KEY `FKEspecialidad` (`idEspecialidad`),
  KEY `FKTurno` (`idTurno`),
  CONSTRAINT `FKEspecialidad` FOREIGN KEY (`idEspecialidad`) REFERENCES `especialidad` (`idEspecialidad`) ON UPDATE CASCADE,
  CONSTRAINT `FKTurno` FOREIGN KEY (`idTurno`) REFERENCES `turnos` (`idTurno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla clinica.proveedores
CREATE TABLE IF NOT EXISTS `proveedores` (
  `idProveedor` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL DEFAULT '',
  `Telefono` varchar(10) NOT NULL DEFAULT '',
  `Dirección` varchar(150) NOT NULL DEFAULT '',
  PRIMARY KEY (`idProveedor`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

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

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla clinica.tipo_examen
CREATE TABLE IF NOT EXISTS `tipo_examen` (
  `idTipo` int(11) NOT NULL,
  `Nombre` varchar(75) DEFAULT NULL,
  `Detalles` text DEFAULT NULL,
  PRIMARY KEY (`idTipo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla clinica.tipo_tratamiento
CREATE TABLE IF NOT EXISTS `tipo_tratamiento` (
  `idTratamiento` int(11) NOT NULL,
  `Detalle` text DEFAULT NULL,
  PRIMARY KEY (`idTratamiento`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla clinica.tratamientos
CREATE TABLE IF NOT EXISTS `tratamientos` (
  `idTratamiento` int(11) NOT NULL,
  `idTipo` int(11) DEFAULT NULL,
  PRIMARY KEY (`idTratamiento`),
  KEY `FKTratamientoTipo` (`idTipo`),
  CONSTRAINT `FKTratamientoTipo` FOREIGN KEY (`idTipo`) REFERENCES `tipo_tratamiento` (`idTratamiento`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla clinica.turnos
CREATE TABLE IF NOT EXISTS `turnos` (
  `idTurno` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL DEFAULT '',
  PRIMARY KEY (`idTurno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla clinica.turnos_hora
CREATE TABLE IF NOT EXISTS `turnos_hora` (
  `idTurno` int(11) DEFAULT NULL,
  `Hora` time DEFAULT NULL,
  KEY `FKHorario` (`idTurno`),
  CONSTRAINT `FKHorario` FOREIGN KEY (`idTurno`) REFERENCES `turnos` (`idTurno`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
