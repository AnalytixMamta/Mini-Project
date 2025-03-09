# Library Management System

##  Project Overview
This is a **Library Management System** that enables users to manage books and members efficiently. The system allows users to add books, register members, issue or buy books, and display book and member details. The project is built using **Python** and **MySQL**.

##  Database Schema
The system uses a MySQL database with the following tables:
- **members**: Stores member details (ID, Name, Email, Phone)
- **books**: Stores book details (ID, Title, Author, Quantity, Price)
- **transactions**: Records book transactions (Member ID, Book ID, Transaction Type, Date)

##  Features
1. **Add Member**: Register a new library member.
2. **Add Book**: Add new books to the library.
3. **Issue Book**: Borrow a book from the library (reduces quantity by 1).
4. **Buy Book**: Purchase a book (reduces quantity by 1).
5. **Display Members**: View all registered members.
6. **Display Books**: View all available books.
7. **Exit**: Close the system.

##  Technologies Used
- **Python**  (MySQL Connector for database interactions)
- **MySQL** 🗄️ (Database management)



## 🛠️ Installation & Setup
### 1️⃣ Set up MySQL Database
1. Install MySQL Server.
2. Open MySQL and create a database by running:
   ```sql
   CREATE DATABASE library_db;
   ```
3. Import the provided **Library.sql** file to create tables.

### 2️⃣ Install Required Python Packages
Run the following command to install MySQL Connector:
```bash
pip install mysql-connector-python
```

### 3️⃣ Run the Application
Execute the Python script:
```bash
python library_management.py
```

## 📜 How to Use
1️⃣ **Run the script** and select an option from the menu.

2️⃣ **Add books and members** before issuing or buying books.

3️⃣ **Issue/Buy books**, and transactions will be recorded in the database.


---
🔗 **Connect with me**: [LinkedIn](https://www.linkedin.com/in/mamata-sawant-87330b2a6) 

