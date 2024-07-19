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

---


## API Documentation

### Base URL
The base URL for all API endpoints is `/`.

### Endpoints

#### Users

- **GET /users/**: Retrieve a list of all users.
- **POST /users/**: Create a new user.
- **GET /users/{id}/**: Retrieve a specific user by ID.
- **PUT /users/{id}/**: Update a specific user by ID.
- **DELETE /users/{id}/**: Delete a specific user by ID.

#### Devices Date Range

- **GET /date-range/**: Retrieve a list of all device readings.
- **POST /date-range/{id}/date_range/**: Retrieve readings for a specific device within a date range.
  - **Parameters**:
    - `device_name` (query parameter, required): The name of the device.
    - `start_date` (query parameter, required): The start date of the range (YYYY-MM-DD).
    - `end_date` (query parameter, required): The end date of the range (YYYY-MM-DD).
  - **Response**: List of readings within the specified date range.

#### Devices

- **GET /add_devices/**: Retrieve a list of all devices.
- **POST /add_devices/**: Create a new device.
- **GET /add_devices/{id}/**: Retrieve a specific device by ID.
- **PUT /add_devices/{id}/**: Update a specific device by ID.
- **DELETE /add_devices/{id}/**: Delete a specific device by ID.
- **GET /add_devices/{id}/reads/**: Retrieve all readings for a specific device.

#### Reads

- **GET /add_read/**: Retrieve a list of all readings.
- **POST /add_read/**: Create a new reading.
- **GET /add_read/{id}/**: Retrieve a specific reading by ID.
- **PUT /add_read/{id}/**: Update a specific reading by ID.
- **DELETE /add_read/{id}/**: Delete a specific reading by ID.

#### Custom Endpoints

- **GET /list-device-all/**: Retrieve a list of all devices.
  - **Response**: List of all devices.
- **GET /list-device/{device_name}/**: Retrieve a device by its name.
  - **Parameters**:
    - `device_name` (path parameter, required): The name of the device.
  - **Response**: The device with the specified name.
- **POST /create-user/**: Create a new user.
  - **Request Body**:
    - `username` (string, required): The username of the new user.
    - `password` (string, required): The password of the new user.
  - **Response**: The created user.
- **POST /summary/**: Retrieve a summary of readings (min, max, avg) for a device within a date range.
  - **Request Body**:
    - `device_name` (string, required): The name of the device.
    - `start_date` (string, required): The start date of the range (YYYY-MM-DD).
    - `end_date` (string, required): The end date of the range (YYYY-MM-DD).
  - **Response**: Summary of readings including max, min, and average temperatures.

### Example Requests

#### Retrieve All Users

```http
GET /users/
```

#### Create a New User
```
POST /users/
Content-Type: application/json

{
  "username": "newuser",
  "password": "newpassword"
}
```
#### Retrieve Device Readings within Date Range
```
POST /date-range/{id}/date_range/?device_name=Device1&start_date=2024-01-01&end_date=2024-01-31

```
#### Retrieve Summary of Readings
```
POST /summary/
Content-Type: application/json

{
  "device_name": "Device1",
  "start_date": "2024-01-01",
  "end_date": "2024-01-31"
}

```

#### Retrieve All Devices
```
GET /list-device-all/
```

#### Retrieve a Device by Name
```
GET /list-device/Device1/
```

```
Error Responses:
- 400 Bad Request: Returned when required parameters are missing or invalid.
- 404 Not Found: Returned when the requested resource does not exist.
- 500 Internal Server Error: Returned when an unexpected error occurs on the server.
```