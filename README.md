# TodoApp

A simple todo list webapp I made to get familiar with the Django framework.

This project uses Django and SQLite3 for the backend and HTML, CSS, and Javascript for the frontend along with Bootstrap for some of the CSS elements.

![Screenshot 2023-06-28 032512](https://github.com/Vidyut01/TodoApp/assets/73650180/4de17f23-5395-4c4b-b432-2257a15867c5)

# Getting the code

To get the code from the repo, clone it by running 

```
git clone https://github.com/Vidyut01/TodoApp.git
```

# Running the app using Django development server
Before running the project, we need to install the required python packages. Run

```
pip -r requirments.txt
```

This will install Django and whitenoise. Whitenoise is used to serve static files when `DEBUG = False` in `TodoApp/settings.py`

From the project directory run

```
python manage.py migrate
```

This will create the database for this project. Then run

```
python manage.py collectstatic
```

This will collect all static files to a `staticfiles` directory to be served to the server.

To start the development server, run

```
python manage.py runserver
```

This will start the server at `127.0.0.1`(`localhost`) in port 8000. To visit it open a browser and go to http://127.0.0.1:8000/todo.
