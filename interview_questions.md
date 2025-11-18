Task 4: Interview Questions
1. What is Flask?
Flask is a "micro" web framework for Python. It's called "micro" because it's lightweight and doesn't force any particular tools or project structure. It provides the basics for web development, like request handling, routing, and sending responses, allowing the developer to add other tools as needed.
2. What is REST?
REST (REpresentational State Transfer) is an architectural style for designing networked applications. It's not a protocol, but a set of rules for how APIs should work. Key principles include:
Client-Server: A clear separation between the user interface (client) and the data storage (server).
Stateless: The server does not store any information about the client's "state" between requests. Every request must contain all the information needed to process it.
Resource-Based: Applications are built around "resources" (e.g., a "user"). You use standard HTTP methods to interact with these resources.
3. Difference between GET and POST?
GET: Used to retrieve data. A GET request should only read data and not change it. It's considered "idempotent" (running it multiple times has the same effect as running it once). Data is often sent in the URL (e.g., ?id=123).
POST: Used to submit new data to the server. A POST request is used to create a new resource (e.g., create a new user). It is not idempotent (running it multiple times will create multiple new users). Data is sent in the body of the request.
4. How does a Flask route work?
A Flask route uses a decorator (like @app.route('/users')) to map a URL path and an HTTP method to a specific Python function. When Flask receives a request that matches the URL and method, it executes the decorated function and sends its return value back as the response.
5. What is request.json?
In Flask, request.json is an object that automatically parses the incoming request body if it is formatted as JSON. This gives you a Python dictionary (or list) to easily work with the data sent by a client (e.g., from a POST or PUT request).
6. What are status codes like 200, 404?
HTTP status codes are 3-digit numbers that the server sends back with every response to indicate the result of the request.
200 OK: The request was successful.
404 Not Found: The server could not find the resource (e.g., the URL or the user) you asked for.
Other common codes include 201 Created (a new resource was made), 400 Bad Request (the client sent invalid data), and 500 Internal Server Error (the server had a problem).
7. How do you run a Flask app?
There are two common ways:
Using the flask command: Set an environment variable FLASK_APP=app.py and then run flask run. (This is common for production).
Using python: Add if __name__ == '__main__': app.run(debug=True) to your file and then run it simply with python app.py. (This is great for development).
8. What is JSON?
JSON (JavaScript Object Notation) is a lightweight, text-based data format that is easy for humans to read and for machines to parse. It is the most common format for sending data in REST APIs. It uses key-value pairs, just like a Python dictionary.
9. How to test an API?
You cannot easily test an API with just a browser (except for GET requests). You must use a specialized tool that can send different types of HTTP requests (POST, PUT, DELETE) and include data in the request body.
Postman: A popular graphical application for testing APIs.
curl: A command-line tool for making HTTP requests.
10. Can we use a database instead of memory?
Yes, and you absolutely should for any real application! The in-memory list we used is only for development because all data is lost when the server restarts. In a real app, you would use a database (like PostgreSQL, MySQL, or SQLite) and a library like SQLAlchemy to store your data permanently.
