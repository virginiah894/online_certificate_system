## Author
[Virginiah Periah](https://github.com/virginiah894)
##  Features


As a user of the web application you will be able to:

1. Access a landing page with a list of students and courses.
2. Request a certificate on the courses done.
3. View a real time visualization of courses, grades  and certificates.

## Specifications
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| User visits the  webpage and views all students registered and courses available | There are buttons redirecting the user to either view the statistics of request for their own certificate |

## Getting started
### Prerequisites
* python3.6 >
* virtual environment
* pip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/virginiah894/online_certificate_system

        $ cd studentpage

## Running the Application
* Install virtual environment using `$ python3.6 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3.6 pip install -r requirements.txt`
* Create a database and edit the database configurations in `settings.py` to your own credentials.
* Make migrations

        $ python manage.py makemigrations 
        $ python3.6 manage.py migrate 

* To run the application, in your terminal:

        $ python3 manage.py runserver

        
## Technologies Used
* Python3.6
* Django
* HTML
* Bootstrap

This application is developed using [Python3.6](https://www.python.org/doc/), [Django](https://www.djangoproject.com/), [HTML](https://getbootstrap.com/) and [Bootstrap](https://getbootstrap.com/)[chart.js](https://www.chartjs.org/docs/latest/)

## Future Implementation
1. Django Authentication System
