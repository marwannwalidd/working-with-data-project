# 📚 Library Management System — Django App

## ✅ SETUP INSTRUCTIONS (follow in order)

---

### STEP 1 — Open Anaconda Prompt and run:
```
conda create -n library_env python=3.11
conda activate library_env
pip install django psycopg2-binary
```

---

### STEP 2 — Open this folder in VS Code
Drag the `library_project` folder into VS Code, OR run:
```
cd path\to\library_project
code .
```

---

### STEP 3 — Select Python Interpreter in VS Code
1. Press Ctrl + Shift + P
2. Type: Python: Select Interpreter
3. Choose the one that says: library_env

---

### STEP 4 — Update your database credentials
Open `library_project/settings.py` and find the DATABASES section.
Replace these 3 values with your own pgAdmin info:

```python
'NAME': 'your_db_name',      # your actual database name in pgAdmin
'USER': 'postgres',           # your pgAdmin username
'PASSWORD': 'your_password',  # your pgAdmin password
```

---

### STEP 5 — Open VS Code Terminal (Ctrl + `) and run:
```
conda activate library_env
python manage.py migrate --fake-initial
python manage.py createsuperuser
python manage.py runserver
```

---

### STEP 6 — Open your browser at:
- http://127.0.0.1:8000/           → Dashboard
- http://127.0.0.1:8000/members/   → Members
- http://127.0.0.1:8000/books/     → Books
- http://127.0.0.1:8000/devices/   → Devices
- http://127.0.0.1:8000/loans/     → Loans
- http://127.0.0.1:8000/fines/     → Fines
- http://127.0.0.1:8000/events/    → Events
- http://127.0.0.1:8000/staff/     → Staff
- http://127.0.0.1:8000/admin/     → Admin Panel

---

## ⚠️ IMPORTANT NOTE about models.py

The `library/models.py` file was written to match your exact database schema.
If your PostgreSQL table names use different capitalization, run this command
to auto-regenerate models directly from your database:

```
python manage.py inspectdb > library/models.py
```

Then make sure every model class has `managed = False` in its Meta class.
