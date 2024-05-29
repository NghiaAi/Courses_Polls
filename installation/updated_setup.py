import subprocess
import sys
import mysql.connector
import os
from mysql.connector import errorcode

def install_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# Danh sách các package cần cài đặt
packages = [
    "django",
    "djangorestframework",
    "mysqlclient",
    "python-dateutil",
    "mysql-connector-python"
]

# Cài đặt các package
for package in packages:
    print(f"Installing {package}...")
    install_package(package)
    print(f"{package} installed successfully!")

# Thông tin kết nối MySQL
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'project_dgmh',
}

# Kết nối đến cơ sở dữ liệu để đảm bảo thông tin cấu hình là đúng
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connected to the database")
    cursor.close()
    conn.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")
    sys.exit(1)

# Đường dẫn đến tệp dump SQL
# sql_file = 'app_course.sql'
current_directory = os.path.dirname(os.path.abspath(__file__))

# Đường dẫn tới file SQL
sql_file = os.path.join(current_directory, 'app_course.sql')

# Cấu hình lệnh để thực thi MySQL
command = f"C:/xampp/mysql/bin/mysql -u root -h localhost project_dgmh < \"{sql_file}\""


# Lệnh để thực thi tệp SQL
command = f"C:/xampp/mysql/bin/mysql -u root -h localhost project_dgmh < app_course.sql"

# Thực thi lệnh
try:
    subprocess.run(command, shell=True, check=True)
    print("Database loaded successfully from app_course.sql")
except subprocess.CalledProcessError as err:
    print(f"Error: {err}")
