# Full-Stack Task Management System (React + Flask)


A fully functional and responsive **TODO List application** built using modern full-stack technologies.

* 🤳 **Frontend:** React (Vite)
* 🐍 **Backend:** Python (Flask)
* 🗄️ **Database:** MySQL

This project demonstrates a simple **CRUD-based task manager** where users can **Create**, **Read**, **Update**, and **Delete** tasks using a clean UI and RESTful API integration.

---

## 🔧 Tech Stack

| Layer    | Technology                         |
| -------- | ---------------------------------- |
| Frontend | React + Vite                       |
| Backend  | Python + Flask + Flask-CORS        |
| Database | MySQL (mysql-connector-python)     |

---

## 📄 Features

* ✅ Add new tasks  
* ✅ View all tasks  
* ✅ Edit / update tasks  
* ✅ Delete tasks  
* ✅ REST API integration  
* ✅ Clean and maintainable folder structure  
* ✅ Frontend–backend separation  

---

## 🛁 Folder Structure

```
ToDO-App/
├── client/        # React Vite frontend
│   └── ...
├── server/        # Flask backend
│   ├── app.py
│   ├── routes.py
│   ├── models.py
│   ├── db.py
│   └── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/rudranisingh100/ToDO-App.git
cd ToDO-App
```

---

### 2️⃣ Run the Backend (Python + Flask)

```bash
cd server
python -m venv venv
```

Activate the virtual environment:

**Linux / macOS**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

Install dependencies and start server:

```bash
pip install -r requirements.txt
python app.py
```

Backend will run at:
```
http://localhost:5000
```

---

### 3️⃣ Run the Frontend (React + Vite)

```bash
cd client
npm install
npm run dev
```

Frontend will run at:
```
http://localhost:5173
```

---

## 🔗 API Overview

| Method | Endpoint       | Description        |
|------:|---------------|--------------------|
| GET   | `/tasks`       | Fetch all tasks    |
| POST  | `/tasks`       | Create a task      |
| PUT   | `/tasks/<id>`  | Update a task      |
| DELETE| `/tasks/<id>`  | Delete a task      |

---

## 📝 Project Notes

This project was developed to practice full-stack development concepts, REST API design, and frontend–backend integration using lightweight and scalable technologies.

---

## 📖 License

This project is licensed under the **MIT License**.

---


