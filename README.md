# E-commerce Application

This project is a mini e-commerce application with a Django backend and a Vue.js frontend. The application includes functionality for managing products with filtering, pagination, and basic CRUD operations.

---

## 1. Prerequisites

Before you start, ensure you have the following installed:

- **Python**: Version 3.8 or higher
- **Node.js**: Version 14 or higher
- **npm** or **yarn**
- **Git**

---

## 2. Setup Instructions

### 2.1 Backend Setup

1. **Clone the Repository**:
   bash
   git clone <https://github.com/AlmiaGhassenn/Mini-Application-E-Commerce.git>
   cd <Mini-Application-E-Commerce>

2.**Create a Virtual Environment:**

**For Windows:**

python -m venv venv
venv\Scripts\activate

**For macOS/Linux:**

python3 -m venv venv
source venv/bin/activate
Install Dependencies: Install the required Python packages:

pip install -r requirements.txt
Run Migrations: Apply database migrations:

python manage.py migrate
Start the Backend Server: Launch the Django development server:

**python manage.py runserver**
The backend will be available at: http://127.0.0.1:8000/

2.1 **Frontend Setup**
Navigate to the Frontend Directory:

cd ecommerce-frontend
Install Frontend Dependencies: Install the necessary packages:

npm install
Start the Frontend Development Server: Run the Vue.js application:

npm run serve
The frontend will be available at: http://localhost:8080/



