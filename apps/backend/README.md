<!-- #! python version: Python 3.11.4 -->
<!-- Use python version above to make sure the project run effectively -->

### step 1: create virtual environment

```bash
python -m venv venv
```

### step 2: activate virtual environment

```bash
# linux/unix
source venv/bin/activate
# window
.\venv\Scripts\activate
```

### step 3: install requirements if exist file requirements.txt

```bash

pip install -r requirements.txt
```

### step 4: make migrations

```bash

python src/manage.py makemigrations
```

### step 5: migrate the project

```bash
python src/manage.py migrate
```

### optional: in first time you need to run this command

```bash
python src/manage.py makemigrations
python src/manage.py migrate

# python src/manage.py initial_data <username_admin> <email_admin> <password_admin>
# example
python src/manage.py initial_data admin admin@example.com !@#ABC123
```

### step 6 (optional): create superuser if needed

```bash
python src/manage.py createsuperuser

# example
# username: admin
# email: admin@admin
# password: !@#ABC123

```

### step 7: run the project

```bash
python src/manage.py runserver
```

### option: if you want to install any new packages, you need save them in requirements.txt

```bash
pip freeze > requirements.txt
```

### option: if you want to create a new app in main app

```bash
cd src && python manage.py startapp <name_app>
```

### option: if you want to clear pycache

```bash
pyclean .\src
```
