# Stock Portfolio Tracker

A Django-based web application designed to help users manage, monitor, and track their stock investment portfolios.

## Features

- Manage stock portfolio information.
- Add and organize stock holdings.
- View portfolio details through a web dashboard.
- Track investment-related information.
- Responsive user interface.
- SQLite database integration.
- Django-powered backend.

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Tools:** Git, GitHub

## Project Structure

```text
Stock_Portfolio_Tracker/
│
├── manage.py
├── requirements.txt
├── portfolio/
│   ├── migrations/
│   ├── static/
│   │   └── portfolio/
│   │       ├── css/
│   │       └── js/
│   ├── templates/
│   │   └── portfolio/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
└── portfolio_project/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/adarshguptas/Stock_Portfolio_Tracker.git
cd Stock_Portfolio_Tracker
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open your browser:

http://127.0.0.1:8000/

## Future Improvements

- Live stock market price integration.
- Investment performance analytics.
- Interactive portfolio charts.
- User authentication and personalized dashboards.

## Author

**Adarsh Gupta**

B.Tech CSE (AI/ML) Student

GitHub: [@adarshguptas](https://github.com/adarshguptas)

---

*Developed as a Django-based stock portfolio management project.*
