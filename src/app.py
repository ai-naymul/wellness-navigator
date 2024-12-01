from flask import Flask, request, redirect, url_for, render_template, flash
import subprocess
import json

app = Flask(__name__)
import secrets

app.config['SECRET_KEY'] = secrets.token_hex(16)
@app.route('/')
def index():
    return render_template('fitness_routine.html')

@app.route('/fitness-routine', methods=['POST'])
def submit_form():
    # Retrieve form data
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender'].lower()
    if gender == 'male':
        gender = 'M'
    elif gender == 'female':
        gender = 'F'
    else:
        gender = 'O'
    body_weight = request.form['body_weight']
    parts = json.dumps([request.form['parts'].lower()])
    location = request.form['location'].lower()
    discord_webhook = str(request.form['discord_webhook'])
    fitness_level = request.form['fitness_level']

    # Construct curl command
    curl_command = [
        'curl', '-v', '-X', 'POST',
        '-H', 'Content-Type: multipart/form-data',
        '-F', f'name={name}',
        '-F', f'age={age}',
        '-F', f'gender={gender}',
        '-F', f'body_weight={body_weight}',
        '-F', f'parts={parts}',
        '-F', f'location={location}',
        '-F', f'discord_webhook={discord_webhook}',
        '-F', f'fitness_level={fitness_level}',
        '-u', 'naymul504@gmail.com:kestra',
        'http://54.159.172.223:8080/api/v1/executions/fitness-flow-upd/fitness-notification-flow-upd'
    ]

    try:
        # Execute curl command
        result = subprocess.run(curl_command, capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            flash("Congrats! We have sent you a fitness routine recommendation on your Discord. We also created a flow where we wll sent you a unique fitness routine for that week on every week Sunday 7:14PM", "success")
        else:
            flash("There was an error sending your fitness routine recommendation. Please try again later.", "error")
            print("Error:", result.stderr)
    except Exception as e:
        flash("There was an error processing your request. Please try again later.", "error")
        print("Exception:", str(e))

    return redirect(url_for('index'))

@app.route('/customer_support', methods=['GET'])
def customer_support():
    return render_template('customer_support.html')

@app.route('/customer_support', methods=['POST'])
def handle_customer_support():
    # Retrieve form data
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    curl_command = [
        'curl', '-v', '-X', 'POST',
        '-H', 'Content-Type: multipart/form-data',
        '-F', f'name={name}',
        '-F', f'ticket_content={message}',
        '-F', f'email={email}',
        '-u', 'naymul504@gmail.com:kestra',
        'http://54.159.172.223:8080/api/v1/executions/customer_support_upd/customer_support_flow-upd'
    ]
    # Here you can handle the message (e.g., send an email or store it)
    
    # For demonstration purposes, we'll just flash a success message
    try:
        # Execute curl command
        result = subprocess.run(curl_command, capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            flash("We have received your message. We will get back to you soon.", "success")
        else:
            flash("There was an error sending your message. Please try again later.", "error")
            print("Error:", result.stderr)
    except Exception as e:
        flash("There was an error processing your request. Please try again later.", "error")
        print("Exception:", str(e))

    return redirect(url_for('customer_support'))

if __name__ == '__main__':
    app.run(debug=True)