-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 25, 2019 at 04:46 PM
-- Server version: 10.1.29-MariaDB
-- PHP Version: 7.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `instacatch`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`) VALUES
(1, 'aadeezgauravatif');

-- --------------------------------------------------------

--
-- Table structure for table `user_follower`
--

CREATE TABLE `user_follower` (
  `user_id` int(11) NOT NULL,
  `follower_username` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `follower_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `user_follower`
--

INSERT INTO `user_follower` (`user_id`, `follower_username`, `follower_name`) VALUES
(1, 'ayomide_lexxy', 'ayomide'),
(1, 'minute.snippet', ''),
(1, 'insta_official_puru19', '____P U R U S H O T T A M____👈'),
(1, 'pratiksha.dave', 'Pr@t¡k$/-/a  👑'),
(1, 'brajrajsinghrawat', 'Brajraj Singh Rawat'),
(1, 'ovac4u', 'OVAC ™🌐💻'),
(1, 'vikarmsinghratho', 'vikarm singh rathore'),
(1, 'narendra_nk5060', 'Narendra Kumawat'),
(1, 'bsallu43362', 'bharat parashar'),
(1, 'frenzy.arts', 'We <3 Programming'),
(1, 'idiotprogrammer', 'The Programmer'),
(1, 'herbalife_nutrition995', ''),
(1, '122mohit_baba', 'Mohit Sen'),
(1, 'vickypushkar', 'Vicky Parashar'),
(1, 'ashraf.ansari9', 'Ashraf AnsaRi'),
(1, 'gaurang_sharma11', 'Gaurang Sharma'),
(1, 'code.community', 'Code.community'),
(1, 'developerjokes', 'Developer Jokes'),
(1, 'i.am_prady', 'PRADHYUMN AGRAWAL💥'),
(1, 'electronicsenthusiasts', 'Electronics Inside'),
(1, 'longnightstudio', 'Longnight Studio'),
(1, 'sourabh1931', 'sourabh parashar'),
(1, 'en34147', 'en3'),
(1, 'isha2464', '💙i$hA 💟vE®mA💙'),
(1, 'freelanceleads', 'Freelance Leads'),
(1, 'nerd4lifestudio', 'Nerd4life store for developers'),
(1, 'codemagister', ''),
(1, 'muraliparashar', 'Murali Parashar'),
(1, 'programmerschillzone', ''),
(1, 'heart_to_heart___', 'H To H'),
(1, 'swenson_he', 'Swenson He'),
(1, 'reena5981', 'Reena Soni'),
(1, 'saksham_agroya', 'Sãkshám Agrøyä'),
(1, 'lendenbd', 'lenden'),
(1, 'laserpai1.ru', 'Лазер Паи'),
(1, 'abhiesheksoni', 'abhishek'),
(1, 'manou_jb_m_', 'Manou Jbebli'),
(1, 'vaibhavr10', 'vaibhav ranjan'),
(1, 'nerdexplainsitall', 'Nerd Explains It All !'),
(1, 'gardo_suave', 'Gardo Suave'),
(1, 'ajay_hindoniya', 'Ajay Hindoniya'),
(1, 'mg.software', 'Mark Gerard'),
(1, 'global_project_makers_official', 'Global Project Makers Official'),
(1, 'poojasoni_', 'Pooja Soni'),
(1, 'moobido', 'Moobido'),
(1, 'aadi_78692', 'aadilkhanpathan'),
(1, 'sugary_pie_shweta', 'shweta upadhyay'),
(1, 'codebrewlabs', 'Code Brew Labs'),
(1, 'winds.of.wander', 'Emily & Zane\'s #Adventures'),
(1, 'vishnukraman', 'Vishnu K.Raman'),
(1, 'bmxstyle.collective', 'Collective of BMX Style'),
(1, 'sandeep.2548', 'sandeep soni'),
(1, 'emmanuelowenez', 'Emmanuel Owen'),
(1, 'devminds', 'DEVMINDS'),
(1, 'dyanablinks', 'Diana Blinks'),
(1, '_the.programmers_', 'the programmers'),
(1, 'isha9751', 'Isha verma'),
(1, 'prashant_miishra', 'Prashant Mishra'),
(1, 'cosmic_mans', 'cosmic mans'),
(1, 'join_codex', 'codeX'),
(1, 'computer_programmer', 'Computer Programmer 👍💻'),
(1, 'aboutdevelopers', 'Developers'),
(1, 'dct_shoots', 'dct_photography'),
(1, 'this.mayank', 'Mayank Sharma'),
(1, 'aestheticstartup', 'Startup Design 🖥️🍥'),
(1, 'bhanu_11_pratap', 'Rawat Bhanu Pratap Singh'),
(1, 'programmers404', 'programmers404'),
(1, 'jsimankur586', 'Ankush jain'),
(1, 'mrr_goms', 'gome goms'),
(1, 'fx_data_cloud', 'F(x) Data Cloud'),
(1, 'priyank_udai', 'Priyank'),
(1, 'ravikumar_1997', 'Ravi kumar'),
(1, 'timothymarois', 'Timothy Marois ™'),
(1, 'for_geek', 'For Geek'),
(1, 'adityasoni2104', 'Aditya Soni'),
(1, 'pankaj_lakhani_04', 'PanKaj ##😉😉😉'),
(1, 'parasharhemant', 'Hemant Parashar'),
(1, 'upgrademydatabase', 'Upgrade My Database'),
(1, 'games_for_developers', 'Games For Developers'),
(1, 'killerappdev', 'Patricia Reynolds'),
(1, 'techiegirls', 'TechieGirls ✨'),
(1, 'gogiger', 'GoGiger Or Gogigger'),
(1, 'raviparsoya', 'Ravi Parsoya'),
(1, 'yazilimkulturucom', 'Yazilim Kulturu'),
(1, 'programmers_code', 'Programmers_Code'),
(1, 'agenciadw3', 'Agência DW3'),
(1, 'i_am_apurba_', 'Apurba Biswas'),
(1, '2dakikadaprogramlama', 'Umut Sinav'),
(1, 'pratiksha_dave1', ''),
(1, 'iran_sanat_negar', 'ایران صنعت نگار'),
(1, 'chicco.abdullai', 'chicco abdullai'),
(1, 'mr_rathore_kpbanna', 'Kr. Krishna Singh Rathore'),
(1, 'mohammadjaved7669', 'Mohammad Javed'),
(1, 'gamingmemesus', ''),
(1, 'fashion_sense_the_replica', 'FASHION SenSe'),
(1, 'mr.radhey', 'saurav radhey'),
(1, 'pankaj__parashar', 'pankaj parashar'),
(1, 'gunwantiparashar', 'Gunwanti parashar'),
(1, 'sharmapriyanka5542', 'Sharma Priyanka'),
(1, 'grayowldev', 'GrayOwlDev'),
(1, 'blovesterxd98', '☆BlovesterXD☆'),
(1, 'aakash6188', 'aakash solanki'),
(1, 'sleepgurusbeds', 'Sleep Gurus'),
(1, 'kirankashyap03', 'kiran kashyap mehra'),
(1, 'ajayparashar80', 'ajay parashar'),
(1, 'mediadriver', 'Media Driver'),
(1, 'wpformers', 'WPformers'),
(1, 'mr.silentfighter4545', 'aniket sharma'),
(1, 'engineer.magazines', 'Engineer Magazine'),
(1, 'yash_pal_parashar', 'yp'),
(1, 'netflixandcode', 'Netflix & Code'),
(1, 'nikhil_raj99', 'Nikhil Raj');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_follower`
--
ALTER TABLE `user_follower`
  ADD KEY `user_id_frg` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `user_follower`
--
ALTER TABLE `user_follower`
  ADD CONSTRAINT `user_id_frg` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
