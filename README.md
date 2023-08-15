# AirBnB Console

This project is a command-line interface (CLI) for managing objects using a JSON file as storage. It allows you to create, show, update, and delete instances of various models in an AirBnB-like application.

## Description

The AirBnB console provides a way to interact with your application's data models through the command line. It enables you to perform operations such as creating, updating, and deleting instances, as well as querying and displaying information about them.

## Getting Started

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the `console.py` script to start the command interpreter.

## Usage

Once inside the command interpreter, you can use the following commands:
    create <class_name>: Create a new instance of the specified class and save it to the JSON file.
    show <class_name> <id>: Show the string representation of an instance based on the class name and ID.
    destroy <class_name> <id>: Delete an instance based on the class name and ID.
    all [class_name]: Show all string representations of instances, or those of a specific class.
    update <class_name> <id> <attribute_name> "<attribute_value>": Update an instance's attribute based on class name and ID.

## Examples

Creating a new User instance:
    (hbnb) create User
    b658391b-13af-497f-87b1-01717485526f

Showing a User instance:
    (hbnb) show User b658391b-13af-497f-87b1-01717485526f
    [User] (b658391b-13af-497f-87b1-01717485526f) {'id': 'b658391b-13af-497f-87b1-01717485526f', 'created_at': '2023-08-13T12:34:56.789012', 'updated_at': '2023-08-13T12:34:56.789012'}

Updating a User instance:
    (hbnb) update User b658391b-13af-497f-87b1-01717485526f first_name "John"
    (hbnb) show User b658391b-13af-497f-87b1-01717485526f
    [User] (b658391b-13af-497f-87b1-01717485526f) {'id': 'b658391b-13af-497f-87b1-01717485526f', 'created_at': '2023-08-13T12:34:56.789012', 'updated_at': '2023-08-13T12:34:56.789012', 'first_name': 'John'}
