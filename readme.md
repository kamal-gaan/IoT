### Setting Up the Virtual Environment and Installing Dependencies

 - **Create a virtual environment:**
 - -   `python -m venv env`
 - **Activate the virtual environment:**
 - -  `.\env\Scripts\activate`
 -  **Install Requirements**
 - - `pip install -r requirements.txt`
- **Create a `requirements.txt` file to list your dependencies:**
- - `pip freeze > requirements.txt`

### Step-by-Step Guide to Set Up and Run Django Project:

#### Setting Up the Django Project & get it running:

 - **CD Django project**
 - - `cd IoTProject`
 -  **Start Django server**
 - - `python manage.py runserver`

#### Setting Up the Django Project & make some configuration:

 - **CD Django project**
 - - `cd IoTProject`

 - **Creating a Superuser**
 - - `python manage.py createsuperuser`
- **You will be prompted to enter a username, email address, and password. Fill in the required information:** <br/>
 `Username: admin`<br/>
`Email address: admin@example.com`<br/>
`Password: ********`<br/>
`Password (again): ********`<br/>

#### Migrating the Database
- **Make migrations for your models:** 
- - `python manage.py makemigrations`

- **Apply the migrations to your database:**
- - `python manage.py migrate`
-  **Start Django server**
- - `python manage.py runserver`

## Optional steps:

#### **Configure the database** in `IoTProject/settings.py`:
 
 -- `DATABASES = { 'default': { 'ENGINE': 'django.db.backends.postgresql_psycopg2', 'NAME': 'your_db_name', 'USER': 'your_db_user', 'PASSWORD': 'your_db_password', 'HOST': 'localhost', 'PORT': '', } }` <-- Postgres

-- `DATABASES  = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': BASE_DIR  /  'db.sqlite3',}}` <-- SQLlite


### Final Project Structure

IoTProject/<br/>
&ensp;&ensp;    ├── IoTProject/<br/>
&ensp;&ensp;    │&ensp;&ensp;   ├── __init__.py<br/>
&ensp;&ensp;    │&ensp;&ensp;   ├── asgi.py<br/>
&ensp;&ensp;    │&ensp;&ensp;   ├── settings.py<br/>
&ensp;&ensp;    │&ensp;&ensp;   ├── urls.py<br/>
&ensp;&ensp;    │&ensp;&ensp;   └── wsgi.py<br/>
&ensp;&ensp;    ├── devices/<br/>
&ensp;&ensp;    │&ensp;&ensp;   ├── __init__.py<br/>
&ensp;&ensp;    │&ensp;&ensp;   ├── admin.py<br/>
&ensp;&ensp;    │&ensp;&ensp;   ├── apps.py<br/>
&ensp;&ensp;    │&ensp;&ensp;   ├── models.py<br/>
&ensp;&ensp;    │&ensp;&ensp;   ├── serializers.py<br/>
&ensp;&ensp;    │&ensp;&ensp;   ├── tests.py<br/>
&ensp;&ensp;    │&ensp;&ensp;   ├── urls.py<br/>
&ensp;&ensp;    │&ensp;&ensp;   └── views.py<br/>
&ensp;&ensp;    ├── env/<br/>
&ensp;&ensp;    ├── db.sqlite3<br/>
&ensp;&ensp;    ├── manage.py<br/>
&ensp;&ensp;    └── requirements.txt<br/>
