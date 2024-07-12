-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Počítač: 127.0.0.1
-- Vytvořeno: Stř 19. čen 2024, 16:28
-- Verze serveru: 10.4.32-MariaDB
-- Verze PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Databáze: `gramodesky`
--

-- --------------------------------------------------------

--
-- Struktura tabulky `gramodeska`
--

CREATE TABLE `gramodeska` (
  `IDdeska` int(200) NOT NULL,
  `nazev` varchar(200) NOT NULL,
  `autor` varchar(200) NOT NULL,
  `rok` int(200) DEFAULT NULL,
  `vydavatelstvi` varchar(200) NOT NULL,
  `cena` int(200) NOT NULL,
  `stav` int(200) DEFAULT NULL,
  `hlavni_obrazek` varchar(200) NOT NULL,
  `link` varchar(200) DEFAULT NULL,
  `obchod` int(200) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_czech_ci;

--
-- Vypisuji data pro tabulku `gramodeska`
--

INSERT INTO `gramodeska` (`IDdeska`, `nazev`, `autor`, `rok`, `vydavatelstvi`, `cena`, `stav`, `hlavni_obrazek`, `link`, `obchod`, `timestamp`) VALUES
(2, 'nazev2', 'autor2', 1902, 'vydavatelstvi2', 222, NULL, 'https://upload.wikimedia.org/wikipedia/commons/c/cd/Number_2_in_light_blue_rounded_square.svg', 'https://cs.wikipedia.org/', 2, '2024-06-19 12:57:32'),
(4, 'přednazevpo', 'autor4', 1904, 'vydavatelstvi4', 444, NULL, 'https://upload.wikimedia.org/wikipedia/commons/4/45/Eo_circle_blue_number-4.svg', 'https://cs.wikipedia.org/', 1, '2024-06-19 12:58:01'),
(5, 'nazev1', 'autor1', 1901, 'vydavatelstvi1', 111, NULL, 'https://upload.wikimedia.org/wikipedia/commons/f/fd/Eo_circle_blue_number-1.svg', 'https://cs.wikipedia.org/', 1, '2024-06-19 12:58:09'),
(8, 'nazev3', 'autor3', 1903, 'vadavatelstvi3', 333, NULL, 'https://upload.wikimedia.org/wikipedia/commons/3/3e/Eo_circle_blue_number-3.svg', 'https://cs.wikipedia.org/', 1, '2024-06-19 12:58:19'),
(9, 'názevžšč_', 'autor5', NULL, 'vydavatelstvi5', 555, NULL, 'https://upload.wikimedia.org/wikipedia/commons/d/db/Eo_circle_deep-orange_white_number-5.svg', 'https://cs.wikipedia.org/', 2, '2024-06-19 12:58:35'),
(16, 'muj nazev6', 'muj autor 6', 1906, 'mujm vydavatelstvi 6', 666, NULL, 'https://media.hornbach.cz/hb/packshot/as.47360528.jpg?dvid=7', 'https://cs.wikipedia.org/', 1, '2024-06-19 12:58:52');

-- --------------------------------------------------------

--
-- Struktura tabulky `obchod`
--

CREATE TABLE `obchod` (
  `IDobchod` int(200) NOT NULL,
  `jmeno` varchar(200) NOT NULL,
  `mesto` varchar(200) NOT NULL,
  `link` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_czech_ci;

--
-- Vypisuji data pro tabulku `obchod`
--

INSERT INTO `obchod` (`IDobchod`, `jmeno`, `mesto`, `link`) VALUES
(1, 'Čejka', 'Praha', 'http://www.antikvariat-cejka.com/info/contact'),
(2, 'Avion', 'Liberec', 'https://www.antikavion.cz/kontakt');

--
-- Indexy pro exportované tabulky
--

--
-- Indexy pro tabulku `gramodeska`
--
ALTER TABLE `gramodeska`
  ADD PRIMARY KEY (`IDdeska`),
  ADD KEY `obchod` (`obchod`);

--
-- Indexy pro tabulku `obchod`
--
ALTER TABLE `obchod`
  ADD PRIMARY KEY (`IDobchod`);

--
-- AUTO_INCREMENT pro tabulky
--

--
-- AUTO_INCREMENT pro tabulku `gramodeska`
--
ALTER TABLE `gramodeska`
  MODIFY `IDdeska` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT pro tabulku `obchod`
--
ALTER TABLE `obchod`
  MODIFY `IDobchod` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Omezení pro exportované tabulky
--

--
-- Omezení pro tabulku `gramodeska`
--
ALTER TABLE `gramodeska`
  ADD CONSTRAINT `gramodeska_ibfk_1` FOREIGN KEY (`obchod`) REFERENCES `obchod` (`IDobchod`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
