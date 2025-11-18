from flask import Flask, request, jsonify

# 🚀 Initialize the Flask app
app = Flask(__name__)

# --- In-Memory Database ---
# We use a list of dictionaries to store users.
# We add one starting user for testing.
users = [
    {"id": 1, "name": "Test User"}
]
# A counter to ensure new user IDs are unique
user_id_counter = 2

# --- API Endpoints (Routes) ---

# 1. GET ALL USERS (Read)
@app.route('/users', methods=['GET'])
def get_users():
    """Returns a list of all users."""
    print("Serving all users...")
    return jsonify(users), 200  # 200 OK

# 2. GET A SINGLE USER (Read)
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Returns a single user by their ID."""
    print(f"Finding user with id {user_id}...")
    
    # Find the user in our list
    user = next((u for u in users if u['id'] == user_id), None)
    
    if user:
        return jsonify(user), 200  # 200 OK
    else:
        # 404 Not Found is a standard response
        return jsonify({"error": "User not found"}), 404

# 3. CREATE A NEW USER (Create)
@app.route('/users', methods=['POST'])
def create_user():
    """Creates a new user."""
    global user_id_counter # We need to modify the global counter
    
    # Get the data from the request body
    # request.json parses the incoming JSON data
    data = request.json
    
    if not data or 'name' not in data:
        return jsonify({"error": "Missing 'name' in request body"}), 400 # 400 Bad Request

    # Create the new user object
    new_user = {
        "id": user_id_counter,
        "name": data['name']
    }
    
    # Add to our list and increment the counter
    users.append(new_user)
    user_id_counter += 1
    
    print(f"Created new user: {new_user['name']}")
    # 201 Created is the standard response for a successful POST
    return jsonify(new_user), 201

# 4. UPDATE A USER (Update)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Updates an existing user's name."""
    data = request.json
    
    if not data or 'name' not in data:
        return jsonify({"error": "Missing 'name' in request body"}), 400 # 400 Bad Request

    # Find the user
    user = next((u for u in users if u['id'] == user_id), None)
    
    if user:
        user['name'] = data['name'] # Update the name
        print(f"Updated user {user_id} to name: {user['name']}")
        return jsonify(user), 200  # 200 OK
    else:
        return jsonify({"error": "User not found"}), 404

# 5. DELETE A USER (Delete)
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Deletes an existing user."""
    global users # We need to modify the global 'users' list
    
    user = next((u for u in users if u['id'] == user_id), None)
    
    if user:
        users.remove(user)
        print(f"Deleted user with id {user_id}")
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

# --- Run the App ---
if __name__ == '__main__':
    # debug=True will auto-reload the server when you save the file
    app.run(debug=True)
