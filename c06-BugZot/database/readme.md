Setting up the database
=====
Our web application relies heavily on the database for managing the individual records
related to the users and the bugs that have been filed. 

For the demo application, we will set back with the PostgreSQL as the choice for our database. 

To install it on an RPM-based distribution, such as Fedora, the following command needs to be executed:
```
dnf install postgresql postgresql-server postgresql-devel
```

To install postgresql on any other distribution of Linux or any other operating system like Windows or Mac OS, 
the required commands for the distribution/OS will need to be executed.

Once we have the database installed, 
the next step is to initialize the database so that it can be used to store our application data. 

For setting up PostgreSQL, the following steps need to be executed:
```
    sudo postgresql-setup –initdb –unit postgresql
```

This command helps to initialize the postgresql database server and start the server process. 

If no configuration has been changed, the server will default to listen to traffic on port 5432.

Once our server has been initialized, the next thing we need to do is to set up our database
and the user that will be used by our BugZot application.

Now, let's switch our user to postgres and create the user and database. Once we have
switched the user, the following commands need to be executed to create the required user and database:
```commandline
psql
CREATE ROLE bugzot_admin WITH LOGIN PASSWORD 'bugzotuser';
CREATE DATABASE bugzot;
GRANT ALL PRIVILEGES ON DATABASE bugzot TO bugzot_admin;
```

With this, we have our database up and running along with the required user 
and database that our application needs to connect to. 

From here on, 
we can work on our application directly without much of a manual interaction with the database.

Note: Although in the demo application we have granted all the privileges to a single user for the database, 
this is not a recommended practice for a production use case if security is of top-most concern. 

For a production use case, 
we will recommend that different users be created with varying permissions to the database, 
based on the extent of access required by a particular user.