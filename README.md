# Employee Handling System

An Employee Handling System (EHS) that allows you to manage employees in your organization or business.

## FEATURES

- Login/Logout.
- Complete CRUD App.
- Easily add as many employees as needed.
- Edit and delete existing employees.
- View detailed information about specific employees.
- Home page lists all added employees and indicates if none have been added.

## Total Web Pages

1. Login Page (can login either as a manager or as a simple user).

![Login](/media/login.PNG)


2. Index (main page) displays the complete list of employees if any employees are registered.
- User with manager role:

![ManagerDashboard](/media/manager_dashboard.PNG)

- User with simple_user role:

![SimpleUserDashboard](/media/simpleUser_dashboard.PNG)

3. Edit Employee page allows changing the record of an existing employee.

![EditEmployee](/media/edit_employee.PNG)

4. Add Employee Page allows registering a new employee.

![Add Employee](/media/add_employee.PNG)

5. Info Page displays basic information related to the admin panel and its access method.

![Info](/media/info.PNG)

6. Login to the admin panel by entering credentials through this page.

![Admin](/media/django_admin.PNG)

7. Admin Home Page serves as a dashboard for all app-related information and provides access to sub-pages in the admin panel for CRUD operations on employees.



## App Login System

The app contains a login module with two user roles: manager and simple user.
- Managers can perform all CRUD operations on employees.
- Simple users can only add and view employees.
- Authentication is applied to prevent unauthorized access to other app pages.
- Simple users cannot access edit or delete functionality by directly entering the URL in the browser; they will be redirected to the login page.

Default users in the app based on their roles:
1. User with "Manager" role:
   - Username: zubair-ahmed
   - Password: 1234567.

2. User with "Simple User" role:
   - Username: user
   - Password: 12345678.


## Admin Panel

The app includes an admin panel that can be accessed at [https://ehs.herokuapp.com/admin](https://ehs.herokuapp.com/admin). The admin can act as a superuser/superadmin and has the ability to edit, delete, add, and view employees. The admin can review all actions performed by other users of the employee handling system.

Login credentials for accessing the admin panel:
- Username: admin
- Password: project-4


## Deployment Process Details

- Created an app named "ehs" on Heroku.
- Created a PostgreSQL database for the app via Heroku resources section.
- Added database credentials to the `settings.py` file in the Database section.
- Created a `requirements.txt` file.
- Installed necessary dependencies (e.g., Gunicorn, Whitenoise) for deployment.
- Created a `Procfile` and added the following line: `web: gunicorn ehs.wsgi --log-file -`
- Set the allowed host to the app's URL in the `settings.py` file.
- Set `debug=False` in the `settings.py` file.
- Created a static files directory using `collectstatic` command after adding the required static root and URL in the `settings.py` file.
- Created a GitHub repository.
- Committed the complete code to the GitHub repository named "Project-4."
- Linked Heroku account with the GitHub repository.
- Connected the GitHub repository to the Heroku deploy section.
- Selected the main branch for deployment.
- Successfully deployed the app.



## Technologies

HTML, CSS, Django, PostgreSQL, Bootstrap


## Note

To the successful completion of this project, learnt alot through erorors that took time and focus to get resolved. Several time un-successful deployment occured but at last learnt the right way. After that deployed app several times successfully. In all ups and downs, obviously got help from blogs or any other helping material , like for deployment, etc, and learnt from themand did by own them. Overall, with several failiures and bugs that occured time to time helped me to learn a lot and creaed good understandingip of the used tools/languages/processes.







