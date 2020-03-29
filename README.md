# Training_schedule

Object of this task is to create a REST API to manage the training schedule.
User can:
  - Register
  - Login
  - Get list of trainings and detils about single training

Admin can:
  - Add training to schedule
  - Delete or update it using API or Django Admin panel
  - Get list of users
  - Get detail information about user
  - Update user info, delete user.
 
# New Features!

  - Token authorization
  
## Project deployed on Heroku
https://training-shedule-app.herokuapp.com/
 - Admin panel: 
 `/admin/`
`Admin username: admin`
`Admin password: admin`
 - POST method for registration of user. Admin can use GET, POST, PUT, DELETE
 `/users/api/`
`example: curl --header "Content-Type:application/json" --request POST --data '{"username":"<name_user>", "email":"<your_email>" "password":"<your_pass>"}' https://training-shedule-app.herokuapp.com/users/api/ `
 - Detail information about user
`/users/api/<id>/`
 - Schedule of training
`/training/api/`
 - Detail information about training
`/training/api/<id>/`
 - Get your token (POST)
`/api-token-auth/`
`example: curl --header "Content-Type:application/json" --request POST --data '{"username":"test_user", "password":"test_pass"}' https://training-shedule-app.herokuapp.com/api-token-auth/ `

## Deploy on your local machine
1. Install requirements
`pip install -r requirements.txt`
2. Database settings
Rename example.env to .env and edit it
`SECRET_KEY=Your_secret_key`
3. Postgres settings
Set your db settings in .env
`DB_NAME=database_name`
`DB_USER=user`
`DB_PASS=password`
4. Make migrations
`python manage.py makemigrations`
`python manage.py migrate`
5. Create superuser
`python manage.py createsuperuser`
6. Start project
`python manage.py runserver`


