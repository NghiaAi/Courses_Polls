Để cài đặt và chạy dự án Courses-Polls, bạn cần thực hiện theo các bước sau:

Bước 1: Tải và cài đặt XAMPP
1. Tải XAMPP từ trang web chính thức xampp.apachefriends.org.
2. Cài đặt XAMPP và khởi động ứng dụng.
3. Mở XAMPP Control Panel và khởi động các dịch vụ Apache và MySQL bằng cách nhấp vào nút Start.
4. Nhấp vào nút Admin bên cạnh MySQL để mở phpMyAdmin.
5. Trong phpMyAdmin, tạo một cơ sở dữ liệu mới với tên là project_dgmh.
   
Bước 2: Cài đặt các gói cần thiết cho Django
Mở terminal hoặc command prompt và thực hiện các lệnh sau để cài đặt các gói cần thiết:
1. Cài đặt Django:
- pip install django
2. Cài đặt Django REST framework:
- pip install djangorestframework
3. Cài đặt MySQL client:
- pip install mysqlclient
4. Cài đặt Python dateutil:
- pip install python-dateutil
  
Bước 3: Thiết lập cơ sở dữ liệu và chạy server
1. Thực hiện di chuyển cơ sở dữ liệu:
- python manage.py makemigrations
2. Áp dụng các thay đổi vào cơ sở dữ liệu:
- python manage.py migrate
3. Khởi động server:
- python manage.py runserver
Sau khi hoàn tất các bước trên, bạn có thể truy cập vào ứng dụng Courses-Polls bằng cách mở trình duyệt web và nhập địa chỉ http://127.0.0.1:8000/. Chúc bạn thành công!
