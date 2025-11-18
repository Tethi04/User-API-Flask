<div align="center">
🧑‍💻 USER-API-FLASK 🚀
A simple REST API for managing users, built with Python and Flask.
</div>
Overview
This project is a simple in-memory REST API for Task 4 of the Python Developer Internship. It demonstrates the fundamentals of API development by providing all four CRUD (Create, Read, Update, Delete) operations for a list of users.
All data is stored in a list in the app's memory, so it will reset every time the server is restarted.

Features
 * GET /users: Get a list of all users.
 * GET /users/<id>: Get a single user by their ID.
 * POST /users: Create a new user.
 * PUT /users/<id>: Update an existing user.
 * DELETE /users/<id>: Delete a user.
   
🛑 How to Run & Test This Project 🛑
This is a server, not a normal script. You must run it first, then test it with a separate tool.
Part 1: Run the Server
 * Clone the Repository:
   git clone []
cd User-API-Flask

   (Remember to replace YOUR-USERNAME with your actual GitHub username!)
 * Install Dependencies:
   It's highly recommended to use a virtual environment, but for a simple test, you can install Flask directly:
   pip install -r requirements.txt

 * Run the Server:
   Run the app.py script.
   python app.py

   You will see output like this, which means the server is running and waiting for requests:
    * Running on [http://127.0.0.1:5000/](http://127.0.0.1:5000/) (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: ...

Part 2: Test the API (In a NEW Terminal)
Leave the server running! Open a new terminal or open Postman. Here are the commands to test each endpoint using curl (a command-line tool).
1. GET /users (Read All)
Gets the full list of users.
curl [http://127.0.0.1:5000/users](http://127.0.0.1:5000/users)

Expected Response:
[
  {
    "id": 1, 
    "name": "Test User"
  }
]

2. POST /users (Create)
Creates a new user named "New Coder".
curl -X POST [http://127.0.0.1:5000/users](http://127.0.0.1:5000/users) -H "Content-Type: application/json" -d "{\"name\": \"New Coder\"}"

Expected Response:
{
  "id": 2, 
  "name": "New Coder"
}

(Now try running GET /users again to see the new list!)
3. GET /users/2 (Read One)
Gets the user you just created.
curl [http://127.0.0.1:5000/users/2](http://127.0.0.1:5000/users/2)

Expected Response:
{
  "id": 2, 
  "name": "New Coder"
}

4. PUT /users/2 (Update)
Updates user 2's name to "Updated Coder".
curl -X PUT [http://127.0.0.1:5000/users/2](http://127.0.0.1:5000/users/2) -H "Content-Type: application/json" -d "{\"name\": \"Updated Coder\"}"

Expected Response:
{
  "id": 2, 
  "name": "Updated Coder"
}

5. DELETE /users/2 (Delete)
Deletes user 2.
curl -X DELETE [http://127.0.0.1:5000/users/2](http://127.0.0.1:5000/users/2)

Expected Response:
{
  "message": "User deleted successfully"
}

<div align="center">
Created for the Python Developer Internship
</div>
