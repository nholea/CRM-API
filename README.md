# CRM-API
Create a customer relationship management API as part of the CodeSherpas selection process.

## :desktop_computer: Project Instructions
* **Create a new customer**. A customer must have the following attributes: name, surname, email and birthdate.
* **Get a single customer** with all the attributes mentioned above.
* **Get all customers**. For each customer, the same information must be obtained as in the previous point. 
* **Update all the attributes (at once) of an existing customer** mentioned above.
* **Delete an existing customer**.

## :clipboard: Requirements before start
* **Docker** :       
  * Build a Docker image : `docker build -t crm-api .`

* **Pyhton*** :
  * Create a virtual environment: `pip install virtualenv`
  * Name your virtualenv : `virtualenv [name of your new virtual environment]`
  * Activate virtualenv : `.\[name of your new virtual environment]\Scripts\activate`
  * Install Flask : `pip install Flask`

## :rocket: How to run the application

* **Docker**: `docker run -p 3000:3000 crm-api`
* **Python**: `python app.py`

## :mailbox: Endpoints
* `/customers`
* `/customers/customer_id`

## Built with :hammer_and_wrench:
<img src=https://1000marcas.net/wp-content/uploads/2020/02/Docker-Logo-1.png width="100" height="50"><img src=https://www.pue.es/Areas/Education/Resources/Images/Sections/Programs/Python/logo-python.png  width="40" height="40"> <img src= https://cdn.worldvectorlogo.com/logos/flask.svg  width="50" height="50"> <img src= https://testerhouse.com/wp-content/uploads/2019/09/postman-logo.png  width="100" height="50">

:woman_technologist: with :heart: by Natalia Hernández :blush:
