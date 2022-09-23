# Library Managment System

This is a RESTful library managment system build with Django and Django REST Framework.

## Features

- ✅ Authentication with email using JWT
- ✅ Adding new Authors and Books to library by librarians and admins
- ✅ Viewing books by members and add their availability
- ✅ Filter books by their title, ISBN and author name
- ✅ Borrowing books for some days by members with confirmation of a librarian
- ✅ Reserving books for using inside library for some hours by members with confirmation of a librarian
- ✅ Automatically fine members who have not returned their borrowed books in time
- ✅ Ability to view and update user profiles for customers and admins
- ✅ Production-ready configuration for Static Files, Database Settings, Gunicorn, Docker
- ✅ Modular Design
- ✅ Cloud-native design using 12-factor methodology

## Apps

There are 6 django apps in this project

- 🔋 `core`: Abstract features that have been used in whole project
- 🔋 `accounts`: Responsible for authentication and registering members and librarians
- 🔋 `library`: Saving, retrieving and filtering books and authors
- 🔋 `borrowing`: Responsible to borrow books to members and save their records
- 🔋 `reservation`: Used for reserve books by members and save their records
- 🔋 `fines`: Responsible for automatically checking borrowed book records and fine members who haven't return their books at time

## Technologies used

- ✨ [Python](https://www.python.org/) - Programming Language
- ✨ [Django](https://docs.djangoproject.com/en/3.2/releases/3.2/) - Web Framework
- ✨ [Django REST Framework](https://www.django-rest-framework.org/) - For Building RESTful APIs
- ✨ [Docker](https://www.docker.com/) - Container Platform
- ✨ [PostgreSQL](https://www.postgresql.org/) - Database
- ✨ [Git](https://git-scm.com/doc) - Version Control System
- ✨ [Gunicorn](https://gunicorn.org/) - WSGI HTTP Server
- ✨ [Celery](https://github.com/celery/celery) - Task Queue
- ✨ [Celery Beat](https://github.com/celery/django-celery-beat) - Task Scheduler (for scheduling fines)

## Installation

Clone the project

``` git
git clone https://github.com/meghiaws/library-management.git
```

📄 Note that there are three environment files:

- `.env`: for developing locally
- `.env.dev`: for developing locally but inside docker container
- `.env.prod`: for production purposes

⚠️ Remove `.sample` postfix after all of them and considering your development environment (local or inside docker) change `env_file` field in `docker-compose.yml`

Now you can run the project

```docker
docker-compose up -d --build
```

You currently have 7 containers running (production docker-compose is not including pgadmin)

- web
- db
- pgadmin
- redis
- celery
- celery-beat

You can access to app from `http://0.0.0.0:8000` and access to pdadmin from `http://0.0.0.0:5050`

## API Documentations

You can also access to all of the endpoints with OpenAPI schemas

Using Swagger UI

```text
http://0.0.0.0:8000/api/docs
```

Using Redoc

```text
http://0.0.0.0:8000/api/redoc
```
