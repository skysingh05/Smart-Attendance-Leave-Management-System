# Smart Attendance & Leave Management System

A backend system built using **Django** and **Django REST Framework** to manage employee attendance, leave workflows, and role-based access control.

This project demonstrates real-world backend development concepts including **authentication, authorization, reporting, and scalable API design**.

---

## 🚀 Features

### 🔐 Authentication & Authorization
- JWT-based authentication using **Django REST Framework SimpleJWT**
- Role-based access control using **Django Groups**
- Secure API access with permission checks

### ⏱ Attendance Management
- Employee check-in and check-out
- Prevention of duplicate daily check-ins
- Daily attendance tracking
- Dynamic calculation of total working hours

### 🏖 Leave Management
- Leave application with date-range validation
- Prevention of overlapping leave requests
- Leave approval and rejection workflow
- Role-based access (Employee, Manager, HR)

### 📊 Attendance Reports
- Daily attendance report (Admin/HR)
- Monthly attendance summary (Employee)
- Total working hours calculation
- SQL-style aggregation using Django ORM

### 🧑‍💼 Admin Panel
- User and group management
- Role assignment (Employee / Manager / HR)
- Attendance and leave monitoring

---

## 🛠 Tech Stack

- **Backend:** Python, Django  
- **API Framework:** Django REST Framework  
- **Authentication:** JWT (SimpleJWT)  
- **Database:** SQLite (upgradeable to PostgreSQL)  
- **Authorization:** Django Groups & Permissions  
- **Tools:** Django Admin, Postman  

---

## 📁 Project Structure
saams/
├── api/                # API views and URLs
├── attendance/         # Attendance & Leave models
├── users/              # Custom user model
├── reports/            # Attendance reports logic
├── saams/              # Project settings
├── manage.py
├── requirements.txt
└── README.md

---

## 🔑 User Roles & Access

| Role     | Capabilities |
|----------|-------------|
| Employee | Check-in/out, apply leave, view own reports |
| Manager  | Approve/reject leave, view attendance |
| HR       | Manage attendance, approve leaves, view users |
| Admin    | Full system access |

---

## 📡 API Endpoints

### 🔐 Authentication
- `POST /api/token/`
- `POST /api/token/refresh/`

### ⏱ Attendance
- `POST /api/check-in/`
- `POST /api/check-out/`
- `GET /api/attendance/my/monthly/?month=YYYY-MM`
- `GET /api/attendance/my/hours/`
- `GET /api/attendance/admin/daily/?date=YYYY-MM-DD`

### 🏖 Leave Management
- `POST /api/leave/apply/`
- `GET /api/leave/my/`
- `GET /api/leave/all/`
- `POST /api/leave/update/{leave_id}/`

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone <repository-url>
cd saams

###2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

###3️⃣ Install Dependencies
pip install -r requirements.txt

###4️⃣ Run Migrations
python manage.py migrate

###5️⃣Create Superuser
python manage.py createsuperuser

###6️⃣ Start Development Server
python manage.py runserver

## 🧪 Testing

- Performed functional testing of REST APIs using **Django REST Framework Browsable API** during development.
- Validated API request/response flows, authentication, and authorization using **Postman**.
- Conducted **role-based permission testing** by verifying access for Employee, Manager, and HR users.
- Tested edge cases including:
  - Duplicate attendance check-ins
  - Overlapping leave requests
  - Unauthorized access to restricted APIs

---

## 📈 Scalability & Improvements

- Designed the system to support migration from **SQLite to PostgreSQL** for production environments.
- Can integrate **Redis caching** to improve performance of frequently accessed attendance reports.
- CI/CD pipelines can be implemented for automated testing and deployment.
- Additional security enhancements such as **rate limiting, audit logging, and monitoring** can be added for production readiness.

---

## 🧠 Interview Highlights

- Implemented **JWT-based authentication** to enable secure, stateless API communication.
- Designed **role-based access control** using Django Groups for Employee, Manager, and HR roles.
- Built attendance analytics using **Django ORM aggregation** instead of raw SQL queries.
- Followed **clean code practices** and a modular Django app architecture.

---

## 👨‍💻 Author

**Akash Singh**  
Backend Developer (Django / REST APIs)


---

## ✅ Why this looks professional now
- Proper **headings**
- Clean **bullet spacing**
- Code blocks formatted correctly
- Tables for roles
- GitHub-friendly Markdown

This README now looks like it belongs to a **real company project**, not a tutorial.

---

### Next (optional but powerful)
If you want, I can:
1️⃣ Review your **GitHub repo before publishing**  
2️⃣ Optimize this README for **ATS keywords**  
3️⃣ Prepare **one-minute project explanation** for interviews  

Just tell me 👍



