# Pedro's Catalog of Bands

This application contains a list of bands organized in categories. It is editable by authenticated users.


## Contents

#### Vagrant
A Vagrant folder and Vagrant file for initializing the virtual machine in which the app must be run.

#### Static and Template Folders
Folders containing the HTML and CSS files pertaining to the application.

#### Database
Python files to initialize a database (fakeitems.py and database_setup), and the generated database (itemcatalog.db)

#### Application
A Python file named application.py, which contains and initializes the app.


## Setting Up

To start using the app, first clone the [Catalog Repository](https://github.com/pperone/pedroscatalog).

#### Requirements
Python must be installed in you machine, as well as the Flask and SQLAlchemy libraries.


## Using the App

1. From the terminal, 'cd' to the cloned folder and run 'vagrant up'
2. Run 'vagrant ssh'
3. Once inside the vagrant machine, type 'cd /vagrant'
4. Run the application by typing 'python application.py'
5. On your browser, access 'http://localhost:8000'
