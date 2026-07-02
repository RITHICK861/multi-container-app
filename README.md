# 🚀 Automated Multi-Container CI/CD Application

## 📌 Overview

This project demonstrates a complete DevOps CI/CD pipeline for a multi-container web application using Jenkins, Docker, Docker Compose, GitHub, and Flask.

The application consists of:

- Frontend (HTML, CSS, JavaScript served using Nginx)
- Backend (Python Flask REST API)
- Docker containers
- Docker Compose orchestration
- Jenkins Pipeline for Continuous Integration and Continuous Deployment
- GitHub as Source Code Repository

Whenever code is pushed to GitHub, Jenkins automatically pulls the latest code, builds new Docker images, and deploys the updated application.

---

# 🏗 Project Architecture

```
                    Developer
                        │
                  VS Code Development
                        │
                  git add / commit
                        │
                    git push
                        │
                     GitHub
                        │
                Jenkins Pipeline
                        │
        ┌───────────────┴───────────────┐
        │                               │
  Docker Build                     Docker Compose
        │                               │
        └───────────────┬───────────────┘
                        │
              Multi-Container Deployment
                        │
        ┌───────────────┴───────────────┐
        │                               │
   Frontend (Nginx)              Backend (Flask)
```

---

# ✨ Features

- Responsive frontend
- Flask REST API
- Live API communication
- Dockerized frontend
- Dockerized backend
- Docker Compose orchestration
- Jenkins CI/CD Pipeline
- GitHub integration
- Automatic deployment
- Container verification

---

# 🛠 Technologies Used

## Frontend

- HTML5
- CSS3
- JavaScript

## Backend

- Python
- Flask
- Flask-CORS

## DevOps

- Docker
- Docker Compose
- Jenkins
- Git
- GitHub

## Editor

- Visual Studio Code

---

# 📂 Project Structure

```
multi-container-app/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── Dockerfile
│
├── docker-compose.yml
├── Jenkinsfile
├── README.md
└── .gitignore
```

---

# ⚙ Docker Workflow

Build and deploy everything

```bash
docker compose up --build
```

Stop the application

```bash
docker compose down
```

---

# ⚙ Jenkins Pipeline Stages

1. Checkout Source Code
2. Stop Existing Containers
3. Build Docker Images
4. Deploy Containers
5. Verify Deployment

---

# 🌐 Application URLs

Frontend

```
http://localhost:8085
```

Backend API

```
http://localhost:5000/api
```

---

# 📦 Sample API Response

```json
{
    "company": "TechNova Solutions",
    "project": "Automated Multi-Container Deployment",
    "status": "Running Successfully",
    "version": "1.0.0",
    "technology": [
        "Flask",
        "Docker",
        "Docker Compose",
        "Jenkins",
        "GitHub"
    ]
}
```

---

# 🔄 CI/CD Workflow

```
Developer
    │
    ▼
VS Code
    │
git commit
git push
    │
    ▼
GitHub Repository
    │
    ▼
Jenkins Pipeline
    │
Checkout
    │
Build Docker Images
    │
Deploy Containers
    │
Verify Deployment
    │
Application Running
```

---

# 📈 Skills Demonstrated

- CI/CD Pipeline Development
- Docker Containerization
- Docker Compose Orchestration
- Jenkins Automation
- Git Version Control
- GitHub Integration
- Flask REST API Development
- Frontend Development
- Container Networking

---

# 🎯 Learning Outcomes

This project demonstrates practical experience in:

- Building Docker images
- Running multi-container applications
- Writing Jenkins pipelines
- Automating deployments
- Integrating GitHub with Jenkins
- Developing REST APIs using Flask
- Working with Nginx containers
- Continuous Integration and Continuous Deployment

---

# 👨‍💻 Author

**Rithick KM**

GitHub: https://github.com/RITHICK861