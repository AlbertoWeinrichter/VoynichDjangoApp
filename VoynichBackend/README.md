# VoynichBackend


1- Set up enviroment variables
    
    decide how to do it, if .envrc or others

2-Create IAM account in AWS for deployment credentials

    research the best way
    https://medium.com/engineering-on-the-incline/continuous-integration-with-circleci-2-0-github-and-elastic-beanstalk-cf1a0b7f05c6
    and store credentials in .envrc file
    
3-create s3 bucket and add key details

    complete with bucket policies
    add keys to envrc
    collectstatic with django

4-Create confoiguration in Auth0 app

    and store credentials in .envrc file


5-Add support for githooks

    Add	"hooksPath = .githooks" into .git/config
    maybe in the setup script ass well

6-Make migrations and create super user... 
    worth creating a setup script for this maybe
    
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
