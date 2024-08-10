[MAINTENANCE_BADGE]: https://img.shields.io/badge/Maintained%3F-yes-green.svg
[PYTHON_BADGE]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[LICENSE_BADGE]: https://img.shields.io/pypi/l/ansicolortags.svg
[DJANGO_BADGE]:https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white

<h1 align="center" style="font-weight: bold;"> drf-todo-list-api 💻</h1>

![Python][PYTHON_BADGE]
![Django][DJANGO_BADGE]
![License][LICENSE_BADGE]
![Maintenance][MAINTENANCE_BADGE]

`Content:`

<ul>
    <li><a href="#about">About</a></li>
    <li><a href="#features">Features</a></li>
    <li>
      <a href="#gettingStarted">Getting Started</a>
    </li>
    <li><a href="#howToRun">How To Run</a></li>
    <li><a href="#routes">API Endpoints</a></li>
    <li><a href="#collaborators">Collaborators</a></li>
    <li><a href="#contribute">Contribute</a></li>
    <li><a href="#license">License</a></li>
</ul>

<!-- <p align="center">
    <img src="./Docs/" alt="Image Example">
</p> -->

<h2 id="about">📌 About</h2>

<p>
This is a Todo List API built with Django Rest Framework (DRF). The purpose of this project is to practice building a RESTful API and to add a robust project to my portfolio. The API allows users to manage their daily tasks with features such as CRUD operations, user authentication, categorization, priority setting, and much more.
</p>

<h2 id="features">📄Features</h2>

- <strong>User Authentication and Authorization:</strong> Users can register, log in, and manage their own tasks. Authentication is handled via JWT, ensuring secure access to user-specific data.

- <strong>Task CRUD Operations:</strong> Create, read, update, and delete tasks with customizable fields such as title, description, due date, priority, and status.

- <strong>Task Prioritization:</strong> Assign priority levels (High, Medium, Low) to tasks, and easily sort or filter them.

- <strong>Advanced Search & Filtering:</strong> Search tasks by keywords in title or description, and filter by status, priority, category, and more

- <strong>Task Archiving:</strong> Archive completed tasks to keep the active task list organized.


<h2 id="gettingStarted">🚀 Getting started</h2>

This section describes how you can run this project locally.


<h2 id="howToRun">🔗 How to Run</h2>

- Clone the project repository from GitHub:

```bash
git clone https://github.com/EriveltoSilva/drf-todo-list-api.git
```

- Navigate to the project directory and install the virtual environment:

```bash
cd drf-todo-list-api
virtualenv .venv
```

- Install the required dependencies:
```bash
pip install -r requirements.txt
```

- Copy the .env.example to .env:
```bash
cp .env.example .env
```

- Open .env file;
- Fill project SECRET_KEY;
- Fill EMAIL configs;
- Choose the right database config uncommenting that and leave others commented;

- Start project
```bash
python manage.py runserver
```

<h2 id="routes">📍 API Endpoints </h2>

Here is a comprehensive list of the primary API endpoints, along with the expected request bodies and responses for each route.

<h3> Authentication </h3>

| Route                                  | Description                                         |
|----------------------------------------|-----------------------------------------------------|
| <kbd> POST /accounts/token</kbd>       | Get user authentication token                                      |
| <kbd> POST /accounts/token/refresh/</kbd>       | Refresh user token endpoint                |
| <kbd> POST /accounts/password/change/</kbd>     | Update Password endpoint                   |
| <kbd> GET /accounts/password/reset/{str:email}/</kbd>     | Get e-mail reset password        |


<h3> Users </h3>

| Route                                  | Description                                         |
|----------------------------------------|-----------------------------------------------------|
| <kbd> GET  /accounts/users/</kbd>       | List all users                                     |
| <kbd> POST /accounts/users/create/</kbd>| Create a new user                                  |
| <kbd> GET  /accounts/users/{uuid:id}/</kbd>| Retrieve a specific user by id                  |
| <kbd> PUT  /accounts/users/{uuid:id}/</kbd>| Update a specific user by id                    |
| <kbd> DELETE  /accounts/users/{uuid:id}/</kbd>| Delete a specific user by id                 |
| <kbd> GET /accounts/users?is_staff=True </kbd>| Filter - List all users admin                |
| <kbd> GET /accounts/users?is_staff=False </kbd>| Filter - List all users normal(not admin)   |


<h3> Profiles </h3>

| Route                                  | Description                                          |
|----------------------------------------|------------------------------------------------------|
| <kbd> GET  /accounts/profiles/ </kbd>       | List all users profiles                         |
| <kbd> GET  /accounts/profiles/{uuid:id}/</kbd>       | Retrieve a user profile by id          |
| <kbd> PUT  /accounts/profiles/{uuid:id}/</kbd>       | Update a user profile                  |
| <kbd> GET  /accounts/profiles?birthday=2001-03-18 </kbd> | Filter - List all users by birthday|
| <kbd> GET  /accounts/profiles?gender=MASCULINO </kbd> | Filter - List all users by gender     |

<h3> ToDo </h3>

| Route                                         | Description                                         |
|-----------------------------------------------|-----------------------------------------------------|
| <kbd> GET    /todo/ </kbd>                    | List all user task                                  |
| <kbd> POST   /todo/ </kbd>                    | Create a new task                                   |
| <kbd> GET    /todo/admin/ </kbd>              | List all users task in admin mode                   |
| <kbd> GET    /todo/{uuid:id}/ </kbd>          | Retrieve a specific task                            |
| <kbd> PUT    /todo/{uuid:id}/ </kbd>          | Update a specific task                              |
| <kbd> Delete /todo/{uuid:id}/ </kbd>          | Destroy a specific task                             |
| <kbd> GET    /todo/?status=pending </kbd>     | Filter - List all "pending" task                    |
| <kbd> GET    /todo/?status=defer </kbd>       | Filter - List all "deferred" task                   |
| <kbd> GET    /todo/?status=overdue </kbd>     | Filter - List all task with "overdue"               |
| <kbd> GET    /todo/?status=completed </kbd>   | Filter - List all "completed" task                  |
| <kbd> GET    /todo/?priority=low </kbd>       | Filter - List all task with "low" priority          |
| <kbd> GET    /todo/?priority=middle </kbd>    | Filter - List all task with "middle" priority       |
| <kbd> GET    /todo/?priority=high </kbd>      | Filter - List all task with "high" priority         |
| <kbd> GET    /todo/?due_date=2024-08-15 </kbd>| Filter - List all task with a specific due date     |
| <kbd> GET    /todo/?search=hell </kbd>        | Search all task with a string                       |
| <kbd> GET    /todo/archived/ </kbd>           | List all task archived                              |
| <kbd> PATCH  /todo/archived/{uuid:id}/ </kbd> | Archive a specific task completed                   |


<h3> GET /accounts/token/ </h3>

**REQUEST BODY**
```json
{
    "email":"eriveltoclenio@gmail.com",
    "password":"admin@1234"
}
```

**RESPONSE**
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzMyMzU5MiwiaWF0IjoxNzIzMjM3MTkyLCJqdGkiOiI5MDY0ODRiNmQ2M2Q0NWI3YTBkZjAyNzI1ODQ0OGE4NiIsInVzZXJfaWQiOiIxNWI2MzEwNC0wY2M1LTRmYzUtOWQyZS1mYTFhZmE5YjBjYWYiLCJmaXJzdF9uYW1lIjoiRVJJVkVMVE8iLCJsYXN0X25hbWUiOiJTSUxWQSIsImVtYWlsIjoiZXJpdmVsdG9jbGVuaW9AZ21haWwuY29tIiwidXNlcm5hbWUiOiJhZG1pbiJ9.1uyTj12E_QqC-jkrtPo3DZUfL0LACrxXxOLsygovce4",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMzIzNTkyLCJpYXQiOjE3MjMyMzcxOTIsImp0aSI6ImNkMmQyMjY5N2QwZTQ5ZTc5ZGMxZGEwNjZjNTc0Mjc0IiwidXNlcl9pZCI6IjE1YjYzMTA0LTBjYzUtNGZjNS05ZDJlLWZhMWFmYTliMGNhZiIsImZpcnN0X25hbWUiOiJFUklWRUxUTyIsImxhc3RfbmFtZSI6IlNJTFZBIiwiZW1haWwiOiJlcml2ZWx0b2NsZW5pb0BnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImFkbWluIn0.OojVxfitloQC6Tvrycl3utDAhYbUe42YZmWLDQ3Nc70"
}
```

<h3> GET /accounts/token/refresh/ </h3>

**REQUEST BODY**
```json
{
    "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzMxOTA2MSwiaWF0IjoxNzIzMjMyNjYxLCJqdGkiOiIzNDA3YmY5NjA1N2M0OTdhYjMzMzlkMWYzNTVmYWZmYSIsInVzZXJfaWQiOiIxNWI2MzEwNC0wY2M1LTRmYzUtOWQyZS1mYTFhZmE5YjBjYWYiLCJmaXJzdF9uYW1lIjoiRVJJVkVMVE8iLCJsYXN0X25hbWUiOiJTSUxWQSIsImVtYWlsIjoiZXJpdmVsdG9jbGVuaW9AZ21haWwuY29tIiwidXNlcm5hbWUiOiJhZG1pbiJ9.xBAGZwW3vIb4OI5QOE4n4PWhyK-JGlAGihfkPt3Unm8"
}
```

**RESPONSE**
```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMzIzNzA2LCJpYXQiOjE3MjMyMzI2NjEsImp0aSI6ImM4Y2VlNzc5MzY0YzRkNjdiYTNmNThlODQyY2UzOWNhIiwidXNlcl9pZCI6IjE1YjYzMTA0LTBjYzUtNGZjNS05ZDJlLWZhMWFmYTliMGNhZiIsImZpcnN0X25hbWUiOiJFUklWRUxUTyIsImxhc3RfbmFtZSI6IlNJTFZBIiwiZW1haWwiOiJlcml2ZWx0b2NsZW5pb0BnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImFkbWluIn0.6h2H8-gqNkdNlcL8SqRDp7gYida64H1dVsX6byZUMBs"
}
```


<h3> GET /accounts/users/ </h3>

**RESPONSE**
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "15b63104-0cc5-4fc5-9d2e-fa1afa9b0caf",
            "first_name": "ERIVELTO",
            "last_name": "SILVA",
            "email": "eriveltoclenio@gmail.com",
            "username": "admin",
            "profile": "253408a5-a4b9-4168-8f21-78cdc384fffe"
        },
        {
            "id": "cb71dcfe-523b-45e3-b824-774c0cbcc7f4",
            "first_name": "Clénio",
            "last_name": "Costa",
            "email": "cleniocosta18@gmail.com",
            "username": "clenio",
            "profile": "71db16a4-c66e-4caa-ac30-92eac0615ca9"
        },
        ...
    ]
}
```

<h3> GET /accounts/profiles/ </h3>

**RESPONSE**
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "253408a5-a4b9-4168-8f21-78cdc384fffe",
            "bio": "",
            "birthday": "2001-03-18",
            "gender": "MASCULINO",
            "phone": "940811141",
            "address": "Rangel",
            "image": null,
            "user": "15b63104-0cc5-4fc5-9d2e-fa1afa9b0caf"
        },
        {
            "id": "71db16a4-c66e-4caa-ac30-92eac0615ca9",
            "bio": "Hello World",
            "birthday": "2000-01-01",
            "gender": "MASCULINO",
            "phone": "+244951749112",
            "address": "Viana",
            "image": null,
            "user": "cb71dcfe-523b-45e3-b824-774c0cbcc7f4"
        },
        ...
    ]
}
```

<h3> POST /todo/ </h3>

**REQUEST BODY**
```json
{
    "title": "Teste4",
    "description": "Teste description3",
    "due_date": "2024-08-15 10:00:00",
    "status": "pending",
    "priority":"middle"
}
```

**RESPONSE**
```json
{
    "id": "4b11b514-b3d5-4354-9995-4c2c33afca46",
    "title": "Teste4",
    "description": "Teste description3",
    "due_date": "2024-08-15T10:00:00+01:00",
    "status": "pending",
    "priority": "middle",
    "owner": {
        "id": "15b63104-0cc5-4fc5-9d2e-fa1afa9b0caf",
        "first_name": "ERIVELTO",
        "last_name": "SILVA",
        "email": "eriveltoclenio@gmail.com",
        "username": "admin",
        "profile": "253408a5-a4b9-4168-8f21-78cdc384fffe"
    },
    "created_at": "2024-08-09T23:50:47.164481+01:00",
    "updated_at": "2024-08-09T23:50:47.164492+01:00"
}
```


<h2 id="collaborators">🤝 Collaborators</h2>

Special thank you for all people that contributed for this project.

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/EriveltoSilva">
        <img src="https://github.com/eriveltosilva.png" width="100px;" alt="Erivelto Silva Profile Picture"/><br>
        <sub>
          <b>Erivelto Silva</b>
        </sub>
      </a>
    </td>
  </tr>
</table>



<h2 id="contribute">📫 Contribute</h2>

1. `git clone https://github.com/EriveltoSilva/drf-todo-list-api.git`
2. `git checkout -b feature/NAME`
3. Follow commit patterns
4. Open a Pull Request explaining the problem solved or feature made, if exists, append screenshot of visual modifications and wait for the review!


<h2 id="license"></h2>License</h2>

This project is licensed under the MIT License - see the <a href="./LICENSE.txt">LICENSE</a> file for details.