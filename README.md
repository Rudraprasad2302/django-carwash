# 🚗 Django Car Wash Management System

A web-based Car Wash Management System built using **Django** that allows customers to book car wash services online and enables administrators to manage bookings efficiently.

---

## 📌 Project Overview

The Django Car Wash Management System simplifies appointment scheduling and service management.  
It includes user authentication, booking management, and an admin dashboard to control operations.

---

## ✨ Features

- 🔐 User Registration & Login
- 📅 Book Car Wash Appointment
- 📋 View Booking History
- 🛠 Admin Dashboard for Managing Services
- 📊 Booking Status Management
- 💾 SQLite Database Integration
- 🎨 Clean UI using HTML & CSS

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Authentication:** Django Built-in Auth System

---

## 📂 Project Structure

```
django-carwash/
│
├── carwash/          # Main project configuration
├── bookings/         # Booking application
├── templates/        # HTML templates
├── static/           # CSS & static files
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/Rudraprasad2302/django-carwash.git
cd django-carwash
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate environment:

**Windows**
```
venv\Scripts\activate
```

**Mac/Linux**
```
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```
python manage.py migrate
```

### 5️⃣ Run Development Server

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🔑 Admin Panel Access

Create superuser:

```
python manage.py createsuperuser
```

Then visit:

```
http://127.0.0.1:8000/admin
```

---

## 🚀 Future Improvements

- 💳 Payment Gateway Integration
- 📧 Email Notifications
- 📱 Responsive UI Improvements
- 🌐 Deployment (Render / Railway)
- 📊 Service Pricing Module

---

## 🎯 Learning Outcomes

- Django project architecture
- Model-View-Template (MVT) pattern
- Authentication system
- CRUD operations
- Form handling
- Database migrations

---

## 👤 Author

**Rudra Prasad**  
📧 rudraprasad2302@gmail.com  
🔗 GitHub: https://github.com/Rudraprasad2302  

---

⭐ If you like this project, consider giving it a star!
