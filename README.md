# ToonDo

A Todo app built with React Native, GraphQL, & Django. 

## Purpose

ToonDo was created to practice my skills creating mobile apps from the design mockups to the decoupled API.

### About Frontend

The frontend was designed with GRAVIT designer, and implemented with React Native.

### About Backend

The backend is GraphQL API built on the Django Web framework.

---

# Setting Up The Backend

Note this backend is currently not configured to be deployed to a server.

For all given instructions it's assumed that your some from of linux like terminal environment(as a windows user I use [gitbash](https://git-scm.com/downloads)).

1. Create a virtual environment.

2. Activate the virtual environment and install dependencies:

cd into your virtual environment and run:

`. Scripts/activate`

move the `requirements.txt` from the repo and in to your virtual environment and run:

`pip install -r requirements.txt`

put the cloned repo into the virtual environment's directory:

3. Move into the `app_backend` directory, and build the database:

```shell
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser:

`python manage.py createsuperuser`

5. Run the development server:

`python manage.py runserver`

## Adding data to the backend

### GraphiQL

Activate your virtual environment, and run your development server.

Append `"/graphql/"` to the end of the URL your development server is running the backend on to enter GraphiQL, and IDE for GraphQL.

Use the `createTodo` mutation to add Todos to the database.

### Admin Page

Activate your virtual environment, and run your development server.

Append `"/admin/"` to the end of the URL your development server is running the backend to enter the admin site, a graphical database editor for Django apps.

From the admin page you can create and delete todos Graphically.

### Shell Entry

Activate your virtual environment.

In the `app_backend` directory run `pyton manage.py shell`, to open the python shell in the project.

In the Shell:
Import the todo model:
`from todos.models import Todo`

Run the following command as many times as you need to create as many objects as you want:
`Todo.objects.create(title='your_title_here')`

## Guilds I used Building the Backend

I highly recommend this tutorial:
https://www.howtographql.com/graphql-python/0-introduction/

This one is out of date, it was still used:
https://www.techiediaries.com/django-graphql-tutorial/