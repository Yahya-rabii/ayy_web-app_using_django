# AY-cycling
## Visit at [https://ayy-cycling.herokuapp.com/](https://ayy-cycling.herokuapp.com/)


# Description :

### ayy-cycling, a Webapp which allows you to buy all your bike accessories you need.
### Create your account and join us for a fun journey!
### this Webapp is an academic project still under development.


# routes documentation:

| Route  |Method|Params| Description|
|----------|-------|------|------------|
|```/```| POST | (firstname, lastname, email, password) (Required) |Render an HTML file which contains a registration form where anyone can create a new user if all the fields are valid , If the email adress is already existing, an error page will be rendered. |
|```user_login/```|POST| (Email, Password) (Required) |Render an HTML file which contains a login form where this will search for the user's email & password in the DB and render an HTML page that contains the main page of the website. |
|```api/auth-login/```|POST|(Email, Password) Required |Returns a valid JsonResponse if the user is valid. |
|```add_users/```|GET|| This allows admins to check the list of pre-auth users. |
|```api-auth/```|POST| (Id, Password) (Required)  |This allows admins to login in order to check the list of pre-auth users. |
|```main/```|GET| |This will render an HTML page that presents the main gage of this web project.|
|```/admin```|POST|(Id, Password) (Required) | In order to login to the django administration env where you can add new products and save them to the query. |
|```/main/gloves```|GET||This will render a page containing all glove-type products. |
|```/main/bikelube```|GET||This will render a page containing all bikelube-type products. |
|```/main/jackets```|GET||This will render a page containing all jackets-type products. |
|```/main/suit```|GET||This will render a page containing all suit-type products. |
|```/main/boots```|GET||This will render a page containing all boot-types products. |
|```/main/helmets```|GET||This will render a page containes all helmets-type products. |
|```/err_ne```|GET||This will render an HTML page that presents an error (401 bad request) in case the user tries to login with an invalid email address or password.  |
|```/err```|GET||This will render an HTML page that presents an error (401 bad request) in case the user tries to register with an existing email address. |
|```/API_gl```|GET||This API is suitable to differentiate between types of products and add each product into the right page. |
