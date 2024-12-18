from flask import Flask, request, redirect, jsonify

app = Flask(__name__)

@app.route('/api/', methods=['POST'])
def handle_form():
    # Collect form data
    name = request.form.get('name')
    surname = request.form.get('surname')
    phone = request.form.get('phone')
    
    # Log the received data (optional)
    print(f"Received: Name={name}, Surname={surname}, Phone={phone}")
    
    # Redirect to the welcome page
    return redirect('/welcome', code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
