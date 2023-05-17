
                                    EMPLOYEE HANDLING SYSTEM


An Employee Handling System(EHS), that lets you manage your organization/company/business employees. 

                 #############################################################
                                 
                                            DETAILS


-> Complete CRUD App.
-> With this easy to use system, we can ADD as much emplyees as much we want for our use.
->Adeded employees can be EDITTED.
->Also, added employees can be DELETE.
->Furthermore, we can view the full detail of a specific employee by VIEW module.
->Application has a home page, that lists all added employees and indicates no employees if added none.
->Against each employee in the list we can choose the action if to perform on an employee, either by editting,viewing or deleting button.
->App consist of 3 pages, one for edit employee,one for adding employee and one as homepage.






                 ##############################################################

                                          ADMIN PANNEL

-> App has an admin pannel that can be accesses at      ""  https://ehs.herokuapp.com/admin   ""

-> Admin can act as a superuser/superadmin and can also edit/delete add and view the employees. Admin can re-overview any of the acts performed by the one who is using/handing the site(employees handling system).

->Login credentials for accessing admin are :: 
                                              username: admin
                                              password: project-4



                 ###########################################################


                               APP LOGIN SYSTEM

 The app contains a login module. By default there are 2 users in the app. For user creation, there are 2 categories either user as a manager role or a user as a simple user.

 -> The user with manager role can perofrom all CRUD, for the employees.
 -> Whereas, the user with simple_user role can only add and view the employee.
 -> Authentication applied so that no one can access app other pages without logging in through any way.
 -> User with simple_user role can not access edit or delete functionality even by writing url for that in browser. He will be redirected to login page.

 Depending on the user role after logging in , he will be able to perform operations as per his role.


       ------ Following are the 2 default users in the app depending upon their role :

       1 ) USER WITH " MANAGER " ROLE (LOGIN CREDENTIALS BELOW):
              username: zubair-ahmed
              password: 1234567.


       2 ) USER WITH " SIMPLE_USER " ROLE (LOGIN CREDENTIALS BELOW):
              username: user
              password: 12345678.




               ######################################################
                            DEPLOYMENT ROCESS DETAILS

-> At first, created an app on my heroku account named as ehs.
->Created Postgresql database for the app via heroku resources section.
->Added Database credentials to settings.py file in Database section.
->Created requirements.txt file.
->Installed necessary dependencies like guicorn,whitenoise etc, for the deployment
->Created Procfile and added one line instruction :web: gunicorn ehs.wsgi --log-file -
->Set Allowed Host to my app url in settings.py file .
->Set debug-false in settings.py file.
->Created static files directory through collectstatic  after adding required static root and url in settings.py file.
->Created github repository.
->Committed complete code to github repository named Project-4.
-> Linked my heroku account with github.
->Connected to github project-4 repository through heroku deploy section.
->Selected main branch for deployment.
->Successful deployment.






                 ###########################################################
                                       TOTAL WEB PAGES
                    
1: Login Page(can login either as manager or as a simple_user)
2: Index (main page) that displays the complete list of employees, if employees registered
3: Edit Employee page , through which the record of an existing employee can be changed.
4: Add Employee Page, through which an employee can be registered.
5: Info Page: It displays the basic information related to Admin pannel and its access method.
6: By entering credentials you can login to admi pannel through this page.
7: Admin Home Page, as a dashboard for all app related to info and from here we can also further go to sub pages in admin pannel for CRUD employee. 


                 #############################################################
                                          TECHNOLOGIES

                               HTML,CSS,DJANGO,POSTGRESQL,BOOTSTRAP
                  
                 #############################################################
                                             
                                             NOTE

->To the successful completion of this project, learnt alot through erorors that took time and focus to get resolved. Several time un-successful deployment occured but at last learnt the right way. After that deployed app several times successfully. In all ups and downs, obviously got help from blogs or any other helping material , like for deployment, etc, and learnt from themand did by own them. Overall, with several failiures and bugs that occured time to time helped me to learn a lot and creaed good understandingip of the used tools/languages/processes.


                                                
                                              

           
