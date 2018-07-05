GitHubAPI
=================


Our stack
---------

Back-end:
    - Python 2.7
    - Django 1.11
    - MySQL 5.7
    - Linux

Fron-end:
    - Jquery
    - Bootstrap 3
    - Jquery DataTable

Third-party services:
    None


Installation
------------

Follow the instructions for setup the project:

1. Clone the project repository from Git::

    $ git clone https://github.com/venkatpython/GithubAPI.git
    ##### Make Sure you have the access to the repo

2. Create and active local virtual env with below command.
    - virtualenv '<env_name>'
    - <env_name>/bin/activate

3. Install all required python packages with the below command.
     - pip install -r requirements.txt

3. Create DB in mysql with the name "github",
    - log into mysql client and create database with the below command
    - mysql> create database github;

4. Run Django Migrations
    - python manage.py migrate.

5. If any changes made on models in future run makemigrations and then migrate to aplly new schema to the DB
    - python manage.py makemigrations <app_label>
    - python manage.py migrate

6. Start Server and access the application at localhost:8000
    - python manage.py runserver

Available Feature:
------------------
1. Github oAuth Integration.
2. Searching  the Github users
3. Admin End seach and filter provisions
4. Data table integration
5. Maintaining the API stats(API calls count)


Issues/Tasks/Limitations
-------------------
1. Use oAuth Integration for another GitHub API services like get report details etc.,
2. Django user registration
3. Incorporate design.(css and theme integration)
4. Maintain git branching model for code maintenance.
https://nvie.com/posts/a-successful-git-branching-model/?
