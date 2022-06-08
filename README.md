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

## Technologies used
- ✨ [Python](https://www.python.org/) - Programming Language
- ✨ [Django](https://docs.djangoproject.com/en/3.2/releases/3.2/) - Web Framework
- ✨ [Django Rest Framework](https://www.django-rest-framework.org/) - For Building RESTful APIs
- ✨ [Docker](https://www.docker.com/) - Container Platform
- ✨ [PostgreSQL](https://www.postgresql.org/) - Database
- ✨ [Git](https://git-scm.com/doc) - Version Control System
- ✨ [Gunicorn](https://gunicorn.org/) - WSGI HTTP Server
- ✨ [Celery](https://github.com/celery/celery) - Task Queue
- ✨ [Celery Beat](https://github.com/celery/django-celery-beat) - Task Scheduler (for scheduling fines)

## Installation
Clone the project
``` 
git clone https://github.com/meghiaws/library-management.git
```

📄 Note that there are three environment files:
- `.env`: for developing locally
- `.env.dev`: for developing locally but inside docker container
- `.env.prod`: for production 

⚠️ Remove `.sample` postfix after all of them and considering your development environment (local or inside docker) change `env_file` field ind `docker-compose.yml`

Now you can run the project
```
docker-compose up -d --build
```
You currently have 7 containers running
- web
- db
- pgadmin
- redis
- celery
- celery-beat

You access to app from `http://0.0.0.0:8000` and access to pdadmin from `http://0.0.0.0:5050`

## API Documantaion
You can also access to all of the endpoints with OpenAPI schemas

Using Swagger UI
```
http://0.0.0.0:8000/api/docs
``` 
Using Redoc
```
http://0.0.0.0:8000/api/redoc
```
