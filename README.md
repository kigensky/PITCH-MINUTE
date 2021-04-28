##  PITCH-MINUTE
# Author

[victor-kigen](https://github.com/kigensky)

## Description
This is a flask application that allows users to post one minute pitches and also allows other users who have signed up to comment and upvote or downvote a pitch. It also allows a person to signup to be able to access the functionalities of the application

You can view the site at:[HEROKU]()

# User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* Comment on the different pitches posted py other uses.
* See the pitches posted by other uses.
* Vote on s pitch they have viwed by giving it a upvote or a downvote.
* Register to be allowed to log in to the application
* View pitches from the different categories.
* Submit a pitch to a specific category of their choice.

# Specifications

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all posts, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with app pitches based on categories and commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|

# Prerequisites
* python3.8
* pip3
* virtualenv
* Cloning
### In your terminal:

  * $ git clone https://github.com/kigensky/news-app.git

  * $ cd pitch-minute

### Running the Application
To get the code..

1. Cloning the repository:
  ```git
  https://github.com/kigensky/PITCH-MINUTE.git
  ```
2. Move to the folder and install requirements
  ```git
  cd pitch-minute
  pip3 install -r requirements.txt
  ```
3. Exporting Configurations
  ```git
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```git
  python3.8 manage.py runserver
  ```
5. Testing the application
  ```git
  python3.8 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technologies Used
* Python3.8

* Flask

* Heroku

* Javascript

## known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## License
[MIT](https://choosealicense.com/licenses/mit/)

Copyright (c) 2021 victor kigen

