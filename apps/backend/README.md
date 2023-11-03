### step 1: create virtual environment

```bash
python -m venv venv
```

### step 2: activate virtual environment

```bash
.\venv\Scripts\activate
```

### step 3: install requirements if exist file requirements.txt

```bash

pip install -r requirements.txt
```

### step 4: run the project

```bash
python src/manage.py runserver
```

### option: if you to install new package and save in requirements.txt

```bash
pip freeze > requirements.txt
```
