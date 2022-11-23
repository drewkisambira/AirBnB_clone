<h1>AirBnB clone - The console</h1>

![airbnb](https://user-images.githubusercontent.com/107510227/203648414-29c7b375-ebcf-445a-94d7-8da12804d18a.png)

<h2>Description of the project</h2>
<p>This is the first phase of the Airbnb Clone: the console. This repository holds a command interpreter and classes (i.e. BaseModel class and several other classes that inherit from it: Amenity, City, State, Place, Review), and a command interpreter. The command interpreter, like a shell, can be activated, take in user input, and perform certain tasks to manipulate the object instances.</P>

<p> The goal of the project is to deploy on your server a simple copy of the AirBnB website. At the end, we will have a complete web application composed of:
A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)</oi>
A website (the front-end) that shows the final product to everybody: static and dynamic
A database or files that store data (data = objects)
An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)</p>

<h1>description of the command interpreter</h1>
<p> Through the command interpreter we will create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object

<h1>Files</h1>
models/base_model.py
Defines all common attributes/methods for other classes:
Public instance attributes:

id - string - assigned with an uuid when an instance is created
created_at - datetime - assigned with the current datetime when an instance is created
updated_at - datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
Public instance methods:

save(self) - updates the public instance attribute updated_at with the current datetime

to_dict(self) - returns a dictionary containing all keys/values of dict of the instance.

__str__ - prints [<class name>] (<self.id>) <self.__dict__>

models/init.py
Creates a unique FileStorage instance called storage for the application that is used to reload previous objects created.

models/engine/file_storage.py
This class has methods that serializes a python dictionary to JSON string and reverses the process from JSON string to a python dictionary

Private class attributes:

__file_path - string - path to the JSON file
__objects - dictionary - empty but will store all objects by .id
Public instance methods:
all(self) - returns the dictionary __objects
new(self, obj) - sets in __objects the obj with key .id
save(self) - serializes __objects to the JSON file (path: __file_path)
reload(self) - deserializes the JSON file to __objects (only if the JSON file (__file_path) exists

<h1>Installation<h1>
git clone git@github.com:Janengethe/AirBnB_clone.git
cd AirBnB_clone

<h1>Usage</h1)
Interactive Mode

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
Non-Interactive Mode

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$

<h1>AUTHORS</h1>
<li>
<oi><a href="https://github.com/dtumuhaise">Davis Tumuhaise</a></oi>
</li>
<li>
<oi><a href="https://github.com/drewkisambira">Kisambira Andrew</a></oi>
</li>



