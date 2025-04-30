#LibraApp – Library Management System

A Django-based web application for managing a library's book inventory, user records, and book issuing/returning process. Designed with role-based access for admins and users, LibraApp simplifies day-to-day library tasks using a clean, responsive interface.

## 🚀 Live Demo
Coming Soon

#Tools & Technologies
- **Backend**: Django Rest Framework (Python),Drf_spectacular
- **Database**: SQLite
- **Version Control**: Git, GitHub

##Features
- User authentication (Admin & User roles)
- Add, update, and delete books
- Manage user records
- Search books by title or author
- Filter books by availability
- Issue and return books with date tracking

##How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Niraj-commits/LibraApp.git
   cd LibraApp
2. Create annd activate a virtual environment
   -python -m venv env
   -source env/bin/activate   # For Linux/Mac
   -env\Scripts\activate      # For Windows
3. Install Dependencies
   -pip install -r requirements.txt
4. Apply Migrations
   -python manage.py makemigrations
   -python manage.py migrate
5. Create Superuser and Run the server
   -python manage.py createsuperuser
   -python manage.py runserver

