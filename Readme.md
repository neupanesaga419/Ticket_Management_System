# Ticket Management System

#### This System is made using python, django, django-rest and postgresql database


##### Two user exists here
    1. Customer - The user which is not a admin
    2. Manager - The user which is admin.

###### This application contains given apps.
    1. accounts - This app contains the details about user accounts, its serializer, permissions.

    2. movie  - This app contains the details about movie, models, serializer views and url.
    3. showtime - This app contains details about showtime and shows.
    4. Studio - This app contains details about Studio
    5. tickets - This app contains details about tickets.
    6. core  - This contains all the settings and environments for running the apps.
    

## To use this project in your computer
### RUN

    
    git clone https://github.com/sagarneupane/Ticket_Management_System.git
    cd Ticket_management_system
    pip3 install -r requirements.txt
    

### Docker

    docker-compose build
    docker-compose up

