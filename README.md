# 🛡️ KAVACHAR-WEB

### AI-Powered Industrial Safety Training & Management Platform

> **KAVACHAR** is a digital industrial safety ecosystem designed to make workplace safety training more interactive, accessible, and effective for industrial workers.
> This repository contains the **web-based backend and administration platform** built with Django for managing workers, training modules, safety content, assessments, certificates, and platform data.

---

## 📌 Table of Contents

* [About the Project](#-about-the-project)
* [Problem Statement](#-problem-statement)
* [Our Solution](#-our-solution)
* [Key Features](#-key-features)
* [System Architecture](#-system-architecture)
* [Technology Stack](#-technology-stack)
* [Project Structure](#-project-structure)
* [Getting Started](#-getting-started)
* [Installation](#-installation)
* [Database Setup](#-database-setup)
* [Running the Project](#-running-the-project)
* [Django Admin Panel](#-django-admin-panel)
* [Team Collaboration](#-team-collaboration)
* [Git Workflow](#-git-workflow)
* [Production Deployment](#-production-deployment)
* [Security](#-security)
* [Future Scope](#-future-scope)
* [Contributing](#-contributing)
* [License](#-license)

---

# 🌟 About the Project

Industrial workers often receive safety training through traditional classroom sessions, printed manuals, and theoretical demonstrations. These approaches can be difficult to retain and may not adequately prepare workers for real-world hazards.

**KAVACHAR** aims to transform industrial safety education through a combination of:

* 📱 Interactive mobile learning
* 🥽 Augmented Reality (AR)
* 🤖 AI/ML-based hazard detection
* 🧠 Interactive safety training modules
* 📝 Assessments and quizzes
* 🏆 Training completion and certification
* 👨‍💼 Administrative management

The **KAVACHAR-WEB** application provides the web-based management layer of this ecosystem.

---

# 🚨 Problem Statement

Industrial environments contain numerous hazards, including:

* 🔥 Fire and flammable materials
* ⚡ Electrical hazards
* 🏭 Industrial machinery
* ☣️ Hazardous substances
* 🧯 Improper emergency response
* 🦺 Improper use of Personal Protective Equipment (PPE)
* 🚧 Unsafe working environments

Traditional safety training can be:

* Passive
* Difficult to personalize
* Difficult to monitor
* Operationally disruptive
* Less engaging for younger workers

KAVACHAR aims to make safety education **interactive, measurable, and technology-driven**.

---

# 💡 Our Solution

KAVACHAR combines a mobile safety-learning experience with a centralized web platform.

```text
                 ┌──────────────────────┐
                 │      KAVACHAR        │
                 │   Safety Ecosystem   │
                 └──────────┬───────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
      ┌───────────────┐          ┌────────────────┐
      │ Mobile / AR   │          │ KAVACHAR-WEB   │
      │ Application   │          │ Django Platform │
      └───────┬───────┘          └───────┬────────┘
              │                          │
              │                          ▼
              │                  ┌────────────────┐
              │                  │   PostgreSQL   │
              │                  │    Database    │
              │                  └────────────────┘
              │
              ▼
       AI / ML / AR Features
```

The web platform provides the administrative infrastructure required to manage the ecosystem.

---

# ✨ Key Features

## 👨‍💼 Admin Dashboard

A centralized dashboard for administrators to manage the platform.

Possible administrative operations include:

* View platform statistics
* Manage workers
* Manage users
* Manage training modules
* Manage safety content
* Monitor assessments
* Manage certificates
* View training progress
* Manage permissions

---

## 👷 Worker Management

Administrators can manage worker information such as:

* Worker identity
* Contact information
* Organization information
* Training status
* Assessment status
* Certification status

---

## 📚 Training Module Management

The platform can support multiple safety-training modules.

Examples:

* 🦺 PPE Safety
* 🔥 Fire Safety
* ⚡ Electrical Safety
* 🧯 Emergency Response
* 🏭 Machinery Safety
* ☣️ Hazardous Material Safety
* 🚧 Workplace Hazard Awareness

---

## 📝 Assessment Management

The system can be extended to manage:

* Questions
* Answers
* Quizzes
* Scores
* Attempts
* Passing criteria
* Training completion

---

## 🏆 Certification

The platform can support digital certification based on:

```text
Training
    ↓
Assessment
    ↓
Passing Score
    ↓
Completion
    ↓
Certificate
```

Certificates can later be integrated with QR-code or verification systems.

---

# 🧠 AI / ML Integration

KAVACHAR is designed to work alongside AI/ML-powered safety features.

The mobile application can use on-device machine-learning models to identify relevant objects or hazards.

Potential detection categories include:

* 🔥 Fire
* 🧯 Fire extinguisher
* ⚡ Electrical equipment
* 🧪 Hazardous objects
* 🦺 PPE
* 🚧 Safety barriers
* 🏭 Industrial equipment

The Django web platform can provide the management and data layer for these features.

---

# 🥽 AR Integration

The KAVACHAR mobile application can use Augmented Reality to provide interactive safety experiences.

Possible AR functionality includes:

* Hazard visualization
* Safety instructions
* Object-based safety information
* Emergency guidance
* Interactive industrial scenarios
* Hazard-aware navigation
* 3D safety demonstrations

The web platform acts as the administrative and backend component supporting the broader ecosystem.

---

# 🏗️ System Architecture

A high-level architecture can be represented as:

```text
                         USER
                          │
                          ▼
                ┌───────────────────┐
                │ KAVACHAR Mobile   │
                │    Application    │
                └─────────┬─────────┘
                          │
                          │ API Requests
                          ▼
                ┌───────────────────┐
                │ Django Backend    │
                │ KAVACHAR-WEB      │
                └─────────┬─────────┘
                          │
             ┌────────────┴────────────┐
             │                         │
             ▼                         ▼
      ┌──────────────┐         ┌────────────────┐
      │ Django Admin │         │ REST/API Layer │
      └──────────────┘         └───────┬────────┘
                                       │
                                       ▼
                              ┌─────────────────┐
                              │   PostgreSQL    │
                              │    Database     │
                              └─────────────────┘
```

---

# 🛠️ Technology Stack

## Backend

* 🐍 Python
* 🌐 Django
* 🔐 Django Authentication
* 🔧 Django Admin

## Database

### Development

* SQLite

### Production

* PostgreSQL

## Frontend

* HTML5
* CSS3
* JavaScript
* Django Templates

## Mobile Application

The broader KAVACHAR ecosystem can integrate with:

* Android
* ARCore
* ML Kit / TensorFlow Lite
* On-device ML models

## Development Tools

* Git
* GitHub
* Visual Studio Code

---

# 📁 Project Structure

The current Django project follows a modular structure:

```text
KavachAR-Admin/
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── dashboard/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   └── ...
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

> The exact structure may evolve as the project grows.

---

# 🚀 Getting Started

## Prerequisites

Before running the project, install:

* Python 3.x
* Git
* Visual Studio Code (recommended)
* pip

Verify Python:

```bash
python --version
```

Verify Git:

```bash
git --version
```

---

# 📥 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/sritamasarkar494-code/KAVACHAR-WEB.git
```

Move into the project:

```bash
cd KAVACHAR-WEB
```

---

# 🐍 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

# 📦 3. Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

# 🗄️ Database Setup

For local development, the project can use SQLite.

The database file is:

```text
db.sqlite3
```

The database file is intentionally excluded from Git:

```gitignore
db.sqlite3
```

Instead, Django migrations are tracked in Git.

---

# 🔄 Apply Migrations

After cloning the project, run:

```bash
python manage.py migrate
```

This creates the database structure based on the migration files.

> **Note:** `migrate` does not copy another developer's existing database or users. It creates the required database schema locally.

---

# 👤 Create an Admin User

To create a local Django administrator:

```bash
python manage.py createsuperuser
```

Follow the prompts:

```text
Username:
Email address:
Password:
Password (again):
```

Then run the server.

---

# ▶️ Running the Project

Start the development server:

```bash
python manage.py runserver
```

The website will normally be available at:

```text
http://127.0.0.1:8000/
```

The Django admin panel is available at:

```text
http://127.0.0.1:8000/admin/
```

---

# 👨‍💼 Django Admin Panel

The Django admin interface provides authorized administrators with access to backend management functionality.

Typical workflow:

```text
Admin Login
     ↓
Dashboard
     ↓
Manage Users / Workers
     ↓
Manage Training
     ↓
Manage Assessments
     ↓
Monitor Progress
     ↓
Certificates
```

Administrators should only receive the permissions required for their role.

---

# 👥 Team Collaboration

This project uses GitHub for source-code collaboration.

Repository:

```text
https://github.com/sritamasarkar494-code/KAVACHAR-WEB
```

Team members should have their **own GitHub accounts** and be added as collaborators.

Never share your personal GitHub password with teammates.

---

# 🌿 Git Branching Strategy

The `main` branch should contain stable code.

Develop new features using separate branches.

Example:

```text
main
│
├── feature/admin-panel
├── feature/authentication
├── feature/worker-management
├── feature/certificates
└── feature/api-integration
```

Create a branch:

```bash
git checkout -b feature/your-feature
```

---

# 🔄 Recommended Git Workflow

Before starting work:

```bash
git checkout main
git pull
```

Create or switch to your feature branch:

```bash
git checkout -b feature/your-feature
```

After making changes:

```bash
git status
```

Add changes:

```bash
git add -A
```

Commit:

```bash
git commit -m "Describe your changes"
```

Push:

```bash
git push -u origin feature/your-feature
```

Then create a **Pull Request** on GitHub.

After review and testing, merge the feature into `main`.

---

# 📌 Updating Your Local Project

If another team member has pushed changes:

```bash
git checkout main
git pull
```

Then continue your work on your feature branch.

---

# ⚠️ Database & Git

Migration files **should be committed**:

```text
dashboard/
└── migrations/
    ├── __init__.py
    ├── 0001_initial.py
    └── 0002_....py
```

Do **not** ignore migrations.

However, the local SQLite database should not be committed:

```text
db.sqlite3 ❌
```

The recommended development setup is:

```text
GitHub
  │
  ├── Source code
  ├── Migrations
  ├── Templates
  └── Static files
       │
       ▼
Each developer's own local database
```

For production/shared data:

```text
Django
   │
   ▼
PostgreSQL
```

---

# 🔐 Security

Never commit sensitive information to GitHub.

The following should remain excluded:

```text
.env
.env.*
db.sqlite3
venv/
.venv/
__pycache__/
```

Do not commit:

* API keys
* Database passwords
* Secret keys
* Authentication tokens
* Private credentials

For production, sensitive configuration should be provided through environment variables.

---

# 🌍 Production Deployment

For production deployment, the recommended architecture is:

```text
                 Internet
                    │
                    ▼
             Django Application
                    │
                    ▼
               PostgreSQL
```

A suitable deployment setup can use:

* Django
* Gunicorn
* PostgreSQL
* WhiteNoise
* Environment variables
* Render / Railway / similar cloud platforms

For example:

```text
GitHub
   │
   ▼
Render
   │
   ├── Django Web Service
   │
   └── PostgreSQL
```

The production environment should **not** use the development SQLite database.

---

# 🧪 Testing

Before pushing changes, verify that the application runs:

```bash
python manage.py check
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Test:

* Authentication
* Admin panel
* Worker management
* Training modules
* Forms
* Navigation
* API endpoints
* Database operations

---

# 📈 Future Scope

KAVACHAR-WEB can be expanded with:

### 🔹 REST API

Integrate the Django backend with the Android application.

### 🔹 PostgreSQL

Use a production-grade shared database.

### 🔹 Advanced Analytics

Provide administrators with:

* Training completion rates
* Assessment scores
* Worker performance
* Module-wise performance
* Certification statistics

### 🔹 Certificate Verification

Introduce:

* QR-based certificates
* Certificate IDs
* Online verification

### 🔹 AI/ML Analytics

Use collected safety-training data to identify:

* Common training weaknesses
* Frequently failed assessments
* High-risk safety topics
* Worker learning patterns

### 🔹 Role-Based Access Control

Introduce roles such as:

```text
Super Administrator
       │
       ├── Training Manager
       ├── Safety Manager
       ├── Instructor
       └── Worker
```

---

# 🤝 Contributing

Contributions are welcome.

### Recommended process

1. Fork or clone the repository.
2. Create a feature branch.
3. Implement your changes.
4. Test the changes locally.
5. Commit your changes.
6. Push your branch.
7. Open a Pull Request.
8. Wait for review.
9. Merge after approval.

Example:

```bash
git checkout -b feature/new-feature
git add -A
git commit -m "Add new feature"
git push -u origin feature/new-feature
```

---

# 📝 License

This project is currently developed as a hackathon/project submission.

Add the appropriate open-source license here if the project is later released publicly.

---

# 👨‍💻 Project Team

### KAVACHAR

**AI-Powered Industrial Safety Training Platform**

Built with ❤️ using:

```text
Python
Django
PostgreSQL
Android
AR
AI / ML
GitHub
```

---

# ⭐ Vision

> **Making industrial safety training interactive, intelligent, accessible, and measurable.**

KAVACHAR aims to bridge the gap between **traditional safety education and modern immersive technology**, helping workers learn safety not just by reading about hazards, but by **experiencing, understanding, and responding to them.**

---

## 🛡️ KAVACHAR

### Learn Safety. Experience Safety. Practice Safety. Work Safely.
