# Developer Dashboard

A full-stack developer productivity dashboard built with Flask, SQLite, GitHub API integration, and AWS S3 cloud storage.

This project started as a simple Flask learning project and gradually evolved into a complete developer dashboard with authentication, task management, GitHub profile integration, and cloud-based profile image uploads.

---

## Features

* User authentication system
* Login and registration flow
* Session-based authentication
* GitHub profile integration using GitHub API
* Personal task management system
* Task completion and deletion
* AWS S3 profile image upload
* SQLite database integration
* Flask backend architecture
* Dynamic dashboard rendering

---

## Tech Stack

### Backend

* Python
* Flask
* SQLAlchemy
* SQLite

### Cloud & APIs

* AWS S3
* GitHub REST API
* boto3

### Frontend

* HTML
* CSS
* Jinja2 Templates

### Other Tools

* Git
* GitHub
* python-dotenv

---

## Project Structure

```bash
developer-dashboard-api/
│
├── instance/
├── static/
│   └── style.css
│
├── templates/
│   ├── dashboard.html
│   ├── index.html
│   ├── login.html
│   └── register.html
│
├── venv/
├── .env
├── .gitignore
├── app.py
├── models.py
├── requirements.txt
└── s3_utils.py
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/Krishhna1/developer-dashboard-api.git
cd developer-dashboard-api
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

#### Windows

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the root directory.

```env
AWS_ACCESS_KEY=your_access_key
AWS_SECRET_KEY=your_secret_key
AWS_BUCKET_NAME=your_bucket_name
AWS_REGION=your_bucket_region
```

---

### 5. Run Application

```bash
python app.py
```

Open:

```bash
http://127.0.0.1:5000
```

---

## AWS Integration

This project uses AWS S3 for cloud-based profile image uploads.

The upload system is implemented using:

* boto3
* IAM access keys
* S3 bucket storage
* Flask file handling

Uploaded images are stored in S3 while image URLs are saved in the SQLite database.

---

## Learning Outcomes

This project helped me learn:

* Flask backend development
* Authentication systems
* Session handling
* Database operations with SQLAlchemy
* REST API integration
* AWS S3 cloud storage
* Git and GitHub workflow
* Environment variable management
* Debugging backend applications

---

## Future Improvements

Planned upgrades:

* Password hashing
* Better UI design
* Resume upload system
* Project gallery uploads
* Database migrations
* Deployment on cloud platform
* User profile customization

---

## Screenshots

```md
<img width="1832" height="835" alt="register" src="https://github.com/user-attachments/assets/f0a2cd2e-64e3-41c0-bad2-03c22aabf506" />
<img width="1806" height="993" alt="1" src="https://github.com/user-attachments/assets/a8148564-7b10-4d66-9f7b-9079c490f561" />
<img width="1637" height="1000" alt="2" src="https://github.com/user-attachments/assets/f7b501bf-05fc-4a1b-bd1b-0412a0e2747b" />


```

---

## Author

Krishna Sharma

BTech CSE student exploring backend development, cloud technologies, and real-world software projects.
![Uploading register.png…]()
