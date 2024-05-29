-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th5 12, 2024 lúc 05:24 PM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `project_dgmh`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `app_course`
--

-- CREATE TABLE `app_course` (
--   `id` bigint(20) NOT NULL,
--   `ma_mon_hoc` varchar(20) NOT NULL,
--   `ten_mon_hoc` varchar(100) NOT NULL,
--   `so_tin_chi` int(11) NOT NULL,
--   `ten_giang_vien` varchar(100) NOT NULL,
--   `so_luong_cmt` int(11) NOT NULL
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --
-- Đang đổ dữ liệu cho bảng `app_course`
--

INSERT INTO `app_course` (`id`, `ma_mon_hoc`, `ten_mon_hoc`, `so_tin_chi`, `ten_giang_vien`, `so_luong_cmt`) VALUES
(1, '4203003395', 'Logic Học', 3, 'Nguyễn Thị Thu Hà', 3),
(2, '4203014064', 'Đại Số Tuyến Tính', 3, 'Trịnh Thanh Sơn', 1),
(3, '4203015253', 'Tiếng Anh 1', 3, 'Đoàn Minh Huệ', 2),
(4, '4203000901', 'Cấu Trúc Rời Rạc', 3, 'Trịnh Thanh Sơn', 1),
(5, '4203014122', 'Xử Lý Ảnh', 3, 'Lê Phúc Lữ', 0),
(6, '4203002009', 'Nhập Môn Tin Học', 3, 'Nguyễn Chí Hiếu', 0),
(7, '4203003192', 'Kỹ Năng Làm Việc Nhóm', 3, 'Nguyễn Thị Hiền', 0),
(8, '4203014164', 'Triết Học Mác-Lênin', 2, 'Huỳnh Ngọc Bích', 0),
(9, '4203003848', 'Nhập Môn Lập Trình', 3, 'Nguyễn Hữu Tình', 0),
(10, '4203002137', 'Hệ Thống Máy Tính', 4, 'Lê Thị Thủy', 0),
(11, '4203000941', 'Kỹ Thuật Lập Trình', 3, 'Nguyễn Hữu Tình', 0),
(12, '4203000942', 'Cấu Trúc Dữ Liệu Và Giải Thuật', 4, 'Trương Văn Thông', 0),
(13, '4203001146', 'Hệ Cơ Sở Dữ Liệu', 4, 'Phan Thị Bảo Trân', 0),
(14, '4203003197', 'Kỹ Năng Xây Dựng Kế Hoạch', 3, 'Trần Thị Hiền', 0),
(15, '4203003259', 'Toán cao cấp 1', 2, 'Nguyễn Thị Thu Hà', 0),
(16, '4203014104', 'Nhập Môn Khoa Học Dữ Liệu', 3, 'Bùi Thanh Hùng', 0),
(17, '4203002422', 'Pháp Luật Đại Cương', 2, 'Trần Thị Ngọc Hết', 0),
(18, '4203003198', 'Phương Pháp Luận Nghiên Cứu Khoa Học', 2, 'Lý Thanh Bình', 0),
(19, '4203001058', 'Mạng Máy Tính', 4, 'Lê Thị Thủy', 0),
(20, '4203014061', 'Xác suất trong Khoa học Dữ liệu', 3, 'Lê Phúc Lữ', 0),
(21, '4203003659', 'An Toàn Thông Tin', 3, 'Nguyễn Thị Thanh Bình', 0),
(22, '4203002625', 'Hệ Thống Thông Tin Quản Lý', 3, 'Nguyễn Hữu Quang', 0),
(23, '4203003780', 'Marketing Số', 4, 'Nguyễn Thanh Bình', 0),
(24, '4203004137', 'Pháp Luật Thương Mại Điện Tử', 2, 'Võ Thị Thu Thủy', 0),
(25, '4203001295', 'Quản Trị Nguồn Nhân Lực', 3, 'Nguyễn Bình Phương Duy', 0),
(26, '4203003572', 'Thuật Ngữ TMĐT', 3, 'Phạm Thị Thùy Phương', 0),
(27, '4203003916', 'Cơ Sở Dữ Liệu', 3, 'Nguyễn Đức Cương', 0),
(28, '4203001018', 'Quản Trị Chiến Lược', 3, 'Đinh Văn Hưởng', 0),
(29, '4203001275', 'Marketing Căn Bản', 3, 'Nguyễn Thị Phương Chi', 0),
(30, '4203003867', 'Nguyên Lý TMDT', 3, 'Trần Khánh', 0);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `app_course`
--
ALTER TABLE `app_course`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ma_mon_hoc` (`ma_mon_hoc`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `app_course`
--
ALTER TABLE `app_course`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
