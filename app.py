from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Route to serve the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')

    # Validate the email format (ensure it's an NYU email)
    if not email.endswith('@nyu.edu'):
        return "Invalid email address. Please enter a valid @nyu.edu email address.", 400

    # Read existing data from JSON file
    try:
        with open('emails.json', 'r') as f:
            email_data = json.load(f)
    except FileNotFoundError:
        email_data = []

    # Add the new email to the list
    email_data.append(email)

    # Write the updated list back to the JSON file
    with open('emails.json', 'w') as f:
        json.dump(email_data, f, indent=4)

    return "Thank you for signing up! You have been added to the waitlist."

if __name__ == '__main__':
    app.run(debug=True)
