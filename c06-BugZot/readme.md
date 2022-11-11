Bugzot can be used to track bugs reported by various stakeholders
of products that are marketed by the Omega Corporation.

Bugzot will use various concepts to build the system in a manner that allows it to
be scaled easily as the number of users interacting with the system grows.

Bugzot utilizes various techniques of optimized data access and storage,
highly scalable deployments, and caching, to build an application that performs well,
even in high load scenarios.


## Ability for users to report bugs in products: 
    The users, be they internal or
    external, should be able to file bugs against a particular product of the
    organization, and while filing these bugs, the users should be able to select the
    release version of the product they are filing bugs against so as to provide
    increased granularity.

## Ability to control who can see the bug details
Since the application allows both   
internal and external users to file bugs, it is possible that internal users, such as
quality engineers or internal IT teams, may file bugs against a product that has
not yet been made available to the customers. This will mean that BugZot should 
be able to hide the details about the bugs that have a confidential status.

## Support for file uploads: 
When a bug is filed, usually an error report or a log file
from the product greatly helps to drill down to the root cause. This will mean
that BugZot should be able to deal with file uploads and link the uploaded files
to their respective bugs.

## Search functionality: 
A person using BugZot should be able to search for the
bugs that are filed into the system based upon certain filter criteria, such as the
identity of the user who filed the bugs, the current status of the bug, filing bugs
against, and so on.

## Integration with email: 
When a bug changes state—for example, if a bug is
moved from NEW to ASSIGNED—there should be an email notifying the people
associated with the bug. This will require BugZot to provide integration with the
email service provider of Omega Corporation.

## Ease of integration: 
Omega Corporation plans to extend the usage of BugZot at a
later time by integrating BugZot with the various other internal applications they
have. For this, BugZot should provide an easy way to achieve this integration.
# Deploying for concurrent access

Until now, we were in the development stage and we could easily use the development
server that comes packaged with Flask to quickly test our changes. 

But this development server is not a good choice if you are planning to run the application in production, 
and we need something more dedicated for that. 

This is because, in a production environment, 
we will be more concerned about the concurrency of the application, 
as well as its security aspects, 
like enabling SSL and providing more restricted access to some of the endpoints.

So, 
we need to figure out some choices here based on the fact that we need our application 
to handle a lot of concurrent accesses, while constantly maintaining a good response time for the users.

With this in mind, we end up with the following set of choices, which, 
by their nature are also fairly common in many production environments:

Application server: Gunicorn
Reverse Proxy: Nginx

Here, 
Gunicorn will be the application 
that will be responsible for handling the requests that are to be served by our Flask application, 
while Nginx takes care of request queuing and handling the distribution of the static assets.

So, first, let's set up Gunicorn and how we are going to serve the application through it.

## Setting up Gunicorn
The first step that is involved in the setup of Gunicorn is its installation, which is quite an
easy task. All we need to do is run the following command:
pip install gunicorn
Once this is done, we have Gunicorn available to be run. Gunicorn runs the application
through WSGI, which stands for Web Server Gateway Interface. For Gunicorn to run our
application, we need to create an additional file in our project workspace, known as
wsgi.py, with the following contents:
'''
File: wsgi.py
Description: WSGI interface file to run the application through WSGI
interface
'''
from bugzot import app
if __name__ == '__main__':
app.run()

Once we have defined the interface file, all we need to do is to run the following command
to make Gunicorn serve our application:
gunicorn –bind 0.0.0.0:8000 wsgi:app
Wasn't this simple?
Now, the next thing is to set up Nginx as our reverse proxy to proxy the requests to the
application server.

Setting up Nginx as reverse proxy
To use Nginx as our reverse proxy solution, we first need to get it installed on our system.
For Fedora-based distributions, this can be easily installed by using the dnf or yum based
package manager by running the following command:
$ sudo dnf install nginx
For other distributions, their package managers can be used to install the Nginx package.
Once the Nginx package is installed, we now need to do its configuration to allow it to
communicate with our application server.
To configure Nginx to proxy the communication to our application server, create a file
named bugzot.conf under the /etc/nginx/conf.d directory, with the following
contents:
server {
listen 80;
server_name <your_domain> www.<your_domain>;
location / {
include proxy_params;
proxy_pass http://unix:<path_to_project_folder>/bugzot.sock;
}
}
Now with the Nginx configured, we need to establish a relationship between our Gunicorn
application server and Ngnix. So, let's do it.

Establishing communication between Nginx and
Gunicorn
One thing to note inside the Nginx configuration that we just completed was the
proxy_pass line:
proxy_pass http://unix:<path_to_project_folder>/bugzot.sock
The line tells Nginx to look for a socket file through which Nginx can communicate to the
application server. We can tell Gunicorn to create this proxy file for us. This can be done by
executing the following command:
gunicorn –bind unix:bugzot.sock -m 007 wsgi:app
After executing this command, our Gunicorn web server will create a Unix socket and bind
to it. Now, all that is remaining is to start our Nginx web server, which can be easily
achieved by executing the following command:
systemctl start nginx.service
Once this is done, we can visit http://localhost:80 to access our web application.
With this, our web application is now ready to be served in production and is able to take
up a large number of concurrent requests.