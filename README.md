# AY-cycling
## Visit at [https://ayy-cycling.herokuapp.com/](https://ayy-cycling.herokuapp.com/)


# Description :

### ayy-cycling, It is a webapp that allows you to buy all your bike accessories.
### Create your account and join us !
### this webapp is an academic project still under development.


# routes documentation:

| Route  |Method|Params| Description|
|----------|-------|------|------------|
|```/```| POST | (firstname, lastname, email, password) (Required) |render an HTML file containes a registration form where will create a new user if the all fields are valid , If the email adress is already existed an erreur page will be rendred |
|```user_login/```|POST| (email, password) (Required) |render an HTML file containes a login form where  this will search for the user's email & password in the DB  and render an HTML page containes the main page of the website |
|```api/auth-login/```|POST|(email, password) Required |Returns a valid JsonResponse if the user is valid |
|```add_users/```|GET|| this allow admins to check the list of pre-auth users |
|```api-auth/```|POST| (id, password) (Required)  |this allow admins to login in order to check the list of pre-auth users |
|```main/```|GET| |this will render an HTML page that present the main gage of this web project|
|```/admin```|POST|(id, password) (Required) | in order to login to the django administration env where you can add new products and save them to the query. |
|```/main/gloves```|GET||this will render a page containes all glove-type products |
|```/main/bikelube```|GET||this will render a page containes all bikelube-type products |
|```/main/jackets```|GET||this will render a page containes all jackets-type products |
|```/main/suit```|GET||this will render a page containes all suit-type products |
|```/main/boots```|GET||this will render a page containes all boots-type products |
|```/main/helmets```|GET||this will render a page containes all helmets-type products |
|```/err_ne```|GET||this will render an HTML page that present an error (401 bad request) in case the user try to login with an invalid email adresse or password  |
|```/err```|GET||this will render an HTML page that present an error (401 bad request) in case the user try to regest with an existing email adresse |
|```/API_gl```|GET||this api suitable to differentiate between types of products |