from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post_request():
    data = request.get_json()
    
    # Extract data
    input_data = data.get('data', [])
    file_b64 = data.get('file_b64', '')

    # Processing logic
    numbers = [item for item in input_data if item.isdigit()]
    alphabets = [item for item in input_data if item.isalpha()]
    highest_lowercase_alphabet = [max([char for char in alphabets if char.islower()])] if any(char.islower() for char in alphabets) else []
    
    # File handling logic
    file_valid = bool(file_b64)  # Example: just checking if a file was provided
    file_mime_type = "image/png"  # Placeholder
    file_size_kb = len(file_b64) / 1024 if file_b64 else 0  # Example size calculation

    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",  # Replace with actual logic for user ID
        "email": "john@xyz.com",          # Placeholder
        "roll_number": "ABCD123",         # Placeholder
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet,
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": file_size_kb
    }

    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get_request():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post_request():
    data = request.get_json()
    user_id = "john_doe_17091999"
    email = "john@xyz.com"
    roll_number = "ABCD123"
    
    if 'data' in data:
        input_data = data['data']
        numbers = [item for item in input_data if item.isdigit()]
        alphabets = [item for item in input_data if item.isalpha()]
        
        lowest_alpha = [ch for ch in alphabets if ch.islower()]
        highest_lowercase_alphabet = [max(lowest_alpha)] if lowest_alpha else []
        
        file_valid = True  # Assume the file is valid for this example
        file_mime_type = "image/png"  # Example MIME type
        file_size_kb = "400"  # Format as a string
        
        return jsonify({
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet,
            "file_valid": file_valid,
            "file_mime_type": file_mime_type,
            "file_size_kb": file_size_kb
        })
    else:
        return jsonify({"is_success": False}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

