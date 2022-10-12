# Weather Forecast
A web application that allows to upload forecase data and query with details of Date and Time...
The application is implemented with **Python** and 
**Django** on the backend side and **ReactJS** on the front end
side. **SQLite** is used as a database.

# Setup and Configuration
```
git clone https://github.com/ramganez/weather_app.git
cd weather_app

# Backend setup (Python 3.8.10)
cd backend
virtualenv w_env
source w_env/bin/activate
pip install -r requirements.txt
python manage.py migrate

# Frontend setup (Node v16.17.0 and npm v8.15.0)
cd frontend
npm install
```

![](./weather_system.png)
