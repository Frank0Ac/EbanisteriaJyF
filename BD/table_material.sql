SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Base de datos: 
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materiales_ebanisteria`
--

CREATE TABLE IF NOT EXISTS `materiales_ebanisteria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `material_nombre` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `detalle` text COLLATE utf8_unicode_ci,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=101;

--
-- Volcado de datos para la tabla `materiales_ebanisteria`
--

INSERT INTO `materiales_ebanisteria` (`id`, `material_nombre`, `detalle`) VALUES
(1, 'Roble', 'Madera dura y resistente con un grano distintivo.'),
(2, 'Cerezo', 'Madera de grano fino con tonalidad rojiza.'),
(3, 'Caoba', 'Madera de grano fino y color rojizo a marrón oscuro.'),
(4, 'Nogal', 'Madera oscura y duradera con un grano distintivo.'),
(5, 'Ébano', 'Madera extremadamente densa y oscura, ideal para detalles finos.'),
(6, 'Palisandro', 'Madera tropical con un grano veteado y colores ricos.'),
(7, 'Arce', 'Madera clara y dura con un grano uniforme.'),
(8, 'Pino', 'Madera blanda y liviana, ideal para proyectos más ligeros.'),
(9, 'Haya', 'Madera dura con un grano uniforme y color claro.'),
(10, 'Teca', 'Madera resistente al agua, ideal para muebles de exterior.'),
(11, 'Sipo', 'Madera similar a la caoba con un tono marrón.'),
(12, 'Abedul', 'Madera clara con un grano fino y uniforme.'),
(13, 'Cedro', 'Madera aromática, ligera y resistente a las plagas.'),
(14, 'Fresno', 'Madera dura con un grano distintivo y color claro.'),
(15, 'Koa', 'Madera hawaiana con colores ricos y variados.'),
(16, 'Mogno', 'Madera tropical con tonos rojizos y grano hermoso.'),
(17, 'Palo de Rosa', 'Madera tropical con un tono rosado y aroma agradable.'),
(18, 'Sándalo', 'Madera aromática con un grano fino y color dorado.'),
(19, 'Tejo', 'Madera duradera con un tono rojizo y grano único.'),
(20, 'Zebrano', 'Madera con un distintivo patrón de rayas, ideal para detalles decorativos.'),
(21, 'Cocobolo', 'Madera tropical con colores vibrantes y gran dureza.'),
(22, 'Castaño', 'Madera resistente con un tono marrón claro a medio.'),
(23, 'Abeto', 'Madera liviana y fácil de trabajar, común en construcción de muebles.'),
(24, 'Iroko', 'Madera africana resistente y duradera.'),
(25, 'Aguacate', 'Madera reciclada de árboles de aguacate, sostenible y única.'),
(26, 'Olmo', 'Madera con un grano distintivo y tono marrón claro.'),
(27, 'Caoba Africana', 'Madera similar a la caoba, pero de origen africano.'),
(28, 'Níspero', 'Madera dura y pesada con un grano hermoso.'),
(29, 'Avellano', 'Madera de grano fino y color claro, ideal para detalles.'),
(30, 'Bubinga', 'Madera africana con tonos rosados y veteado atractivo.'),
(31, 'Aliso', 'Madera ligera con grano uniforme y color claro.'),
(32, 'Chapapote', 'Madera oscura y densa, utilizada para detalles decorativos.'),
(33, 'Ciprés', 'Madera aromática con un grano distintivo y duradera.'),
(34, 'Ébano de Macasar', 'Madera de ébano con patrón veteado y tonalidad oscura.'),
(35, 'Granadillo', 'Madera dura y pesada con tonalidad rojiza.'),
(36, 'Louro Preto', 'Madera brasileña con un color oscuro y grano atractivo.'),
(37, 'Madera de Serbal', 'Madera clara y duradera con grano hermoso.'),
(38, 'Makoré', 'Madera africana con tonalidades rosadas y marrones.'),
(39, 'Nogal Americano', 'Variedad de nogal con tonalidades marrones y grano elegante.'),
(40, 'Olivo', 'Madera de olivo con patrones únicos y colores cálidos.'),
(41, 'Naranjo', 'Madera de árboles de naranja con tono claro y aroma cítrico.'),
(42, 'Tornillo', 'Madera sudamericana con grano atractivo y tono claro a medio.'),
(43, 'Palo de Golf', 'Madera densa y resistente con tono marrón oscuro.'),
(44, 'Nogal Inglés', 'Madera noble con tono marrón oscuro y grano elegante.'),
(45, 'Algarrobo', 'Madera sudamericana con tono marrón oscuro y duradera.'),
(46, 'Mara', 'Madera sudamericana con grano distintivo y color claro.'),
(47, 'Tamarindo', 'Madera tropical con tono dorado y grano atractivo.'),
(48, 'Ziricote', 'Madera mexicana con patrón veteado y colores oscuros.'),
(49, 'Rosa Morada', 'Madera peruana con tono morado y grano hermoso.'),
(50, 'Limba', 'Madera africana con grano recto y tono claro.'),
(51, 'Chicozapote', 'Madera mexicana con tonalidades marrones y grano interesante.'),
(52, 'Madreperla', 'Madera con tono perlado y brillo natural.'),
(53, 'Padouk', 'Madera africana con tonos rojizos intensos.'),
(54, 'Roble Blanco', 'Variedad de roble con color más claro y grano atractivo.'),
(55, 'Ipe', 'Madera brasileña extremadamente resistente y duradera.'),
(56, 'Sucupira', 'Madera sudamericana con grano veteado y tono marrón oscuro.'),
(57, 'Tali', 'Madera africana con tono marrón y grano atractivo.'),
(58, 'Zapote', 'Madera tropical con tonalidades marrones y grano distintivo.'),
(59, 'Nogal Negro', 'Variedad de nogal con tonalidades más oscuras.'),
(60, 'Catalox', 'Madera mexicana con tono oscuro y grano hermoso.'),
(61, 'Andiroba', 'Madera sudamericana con tono marrón claro y duradera.'),
(62, 'Bálsamo', 'Madera con aroma agradable y color claro a medio.'),
(63, 'Birch', 'Madera con grano fino y tono claro.'),
(64, 'Caucho', 'Madera resistente y sostenible, ideal para muebles modernos.'),
(65, 'Cupiúba', 'Madera sudamericana con grano veteado y tono claro.'),
(66, 'Guanacaste', 'Madera tropical con tonalidades marrones y grano distintivo.'),
(67, 'Gumwood', 'Madera ligera y fácil de trabajar.'),
(68, 'Jatobá', 'Madera brasileña con tono marrón oscuro y grano atractivo.'),
(69, 'Karri', 'Madera australiana con tono marrón claro y grano recto.'),
(70, 'Kempas', 'Madera asiática con tono rojo y grano distintivo.'),
(71, 'Lingue', 'Madera sudamericana con tono amarillo y grano hermoso.'),
(72, 'Makassar', 'Madera con patrón veteado y tonalidades oscuras.'),
(73, 'Nance', 'Madera tropical con tono claro y grano atractivo.'),
(74, 'Nióbi', 'Madera sudamericana con tonalidades marrones y grano interesante.'),
(75, 'Pernambuco', 'Madera brasileña con tono naranja y grano distintivo.'),
(76, 'Quina', 'Madera sudamericana con tonalidades marrones y grano hermoso.'),
(77, 'Rosa Amarilla', 'Madera brasileña con tono amarillo y grano recto.'),
(78, 'Rubio', 'Madera sudamericana con tonalidades marrones y grano atractivo.'),
(79, 'Sassafras', 'Madera con aroma agradable y tono marrón claro.'),
(80, 'Satinwood', 'Madera con brillo satinado y tono claro.'),
(81, 'Tanimbuca', 'Madera sudamericana con tonalidades marrones y grano distintivo.'),
(82, 'Tarara', 'Madera sudamericana con tono marrón oscuro y grano hermoso.'),
(83, 'Tatajuba', 'Madera brasileña con tono amarillo y grano recto.'),
(84, 'Tauari', 'Madera sudamericana con tono marrón claro y grano atractivo.'),
(85, 'Thuya', 'Madera con aroma agradable y patrón veteado.'),
(86, 'Tola', 'Madera sudamericana con tonalidades marrones y grano distintivo.'),
(87, 'Ulin', 'Madera asiática con tono oscuro y grano atractivo.'),
(88, 'Vera', 'Madera sudamericana con tono marrón claro y grano recto.'),
(89, 'Virola', 'Madera sudamericana con tonalidades marrones y grano hermoso.'),
(90, 'Wamara', 'Madera brasileña con tono naranja y grano atractivo.'),
(91, 'Xixia', 'Madera asiática con tono marrón claro y grano distintivo.'),
(92, 'Yacal', 'Madera sudamericana con tono marrón oscuro y grano recto.'),
(93, 'Zapote Amarillo', 'Madera tropical con tono amarillo y grano hermoso.'),
(94, 'Zarza', 'Madera sudamericana con tonalidades marrones y grano atractivo.'),
(95, 'Zein', 'Madera asiática con tono claro y grano hermoso.'),
(96, 'Ziruma', 'Madera sudamericana con tonalidades marrones y grano recto.'),
(97, 'Zirumo', 'Madera sudamericana con tono marrón claro y grano atractivo.'),
(98, 'Zopilote', 'Madera tropical con tonalidades marrones y grano distintivo.'),
(99, 'Zumaque', 'Madera sudamericana con tono marrón oscuro y grano hermoso.'),
(100, 'Zuruma', 'Madera con tonalidades marrones y grano recto.');
