# Disclaimer: This output contains AI-generated content; user is advised to review it before consumption.
#*Start of AI Generated Content*

python
# ***********************************************************
# * Imports
# ***********************************************************

import os
import re
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# ***********************************************************
# * Constants and Variables
# ***********************************************************

APP = Flask(__name__)

# Database Constants
DB_NAME = 'user_database'
DB_URL = 'mongodb://localhost:27017/'
APP.config['MONGO_URI'] = DB_URL + DB_NAME
MONGO = PyMongo(APP)

# Email Constants
EMAIL_ADDRESS = 'your-email@gmail.com'
EMAIL_PASSWORD = 'your-email-password'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Regex Patterns
EMAIL_PATTERN = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
PHONE_PATTERN = r'^\d{3}-\d{3}-\d{4}$'
PASSWORD_PATTERN = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
NAME_PATTERN = r'^[a-zA-Z]{2,}$'
AGE_PATTERN = r'^\d{1,2}$'
SEX_PATTERN = r'^(Male|Female)$'
ADDRESS_PATTERN = r'^[a-zA-Z0-9\s]{5,}$'

# Food Preferences
FOOD_PREFERENCES = ['Indian', 'Chinese', 'French', 'Italian', 'Mexican', 'Japanese', 'Thai', 'American', 'Greek', 'Mediterranean']

# ***********************************************************
# * Functions
# ***********************************************************

def validate_email(email):
    """
    Validate email address.
    
    Args:
        email (str): Email address.
    
    Returns:
        bool: True if email is valid, False otherwise.
    """
    try:
        if re.match(EMAIL_PATTERN, email):
            return True
        else:
            raise ValueError('Invalid email address')
    except Exception as e:
        return str(e)

def validate_phone(phone):
    """
    Validate phone number.
    
    Args:
        phone (str): Phone number.
    
    Returns:
        bool: True if phone number is valid, False otherwise.
    """
    try:
        if re.match(PHONE_PATTERN, phone):
            return True
        else:
            raise ValueError('Invalid phone number')
    except Exception as e:
        return str(e)

def validate_password(password):
    """
    Validate password.
    
    Args:
        password (str): Password.
    
    Returns:
        bool: True if password is valid, False otherwise.
    """
    try:
        if re.match(PASSWORD_PATTERN, password):
            return True
        else:
            raise ValueError('Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character')
    except Exception as e:
        return str(e)

def validate_name(name):
    """
    Validate name.
    
    Args:
        name (str): Name.
    
    Returns:
        bool: True if name is valid, False otherwise.
    """
    try:
        if re.match(NAME_PATTERN, name):
            return True
        else:
            raise ValueError('Invalid name')
    except Exception as e:
        return str(e)

def validate_age(age):
    """
    Validate age.
    
    Args:
        age (str): Age.
    
    Returns:
        bool: True if age is valid, False otherwise.
    """
    try:
        if re.match(AGE_PATTERN, age) and 18 <= int(age) <= 99:
            return True
        else:
            raise ValueError('Age must be between 18 and 99')
    except Exception as e:
        return str(e)

def validate_sex(sex):
    """
    Validate sex.
    
    Args:
        sex (str): Sex.
    
    Returns:
        bool: True if sex is valid, False otherwise.
    """
    try:
        if re.match(SEX_PATTERN, sex):
            return True
        else:
            raise ValueError('Invalid sex')
    except Exception as e:
        return str(e)

def validate_address(address):
    """
    Validate address.
    
    Args:
        address (str): Address.
    
    Returns:
        bool: True if address is valid, False otherwise.
    """
    try:
        if re.match(ADDRESS_PATTERN, address):
            return True
        else:
            raise ValueError('Invalid address')
    except Exception as e:
        return str(e)

def send_password_reset_link(email, password_reset_link):
    """
    Send password reset link to user's email.
    
    Args:
        email (str): User's email.
        password_reset_link (str): Password reset link.
    
    Returns:
        bool: True if email is sent successfully, False otherwise.
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = email
        msg['Subject'] = 'Password Reset Link'
        body = 'Please click on the following link to reset your password: ' + password_reset_link
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, email, text)
        server.quit()
        return True
    except Exception as e:
        return str(e)

# ***********************************************************
# * API Endpoints
# ***********************************************************

@APP.route('/register', methods=['POST'])
def register():
    """
    Register a new user.
    
    Args:
        email (str): Email address or phone number.
        password (str): Password.
        confirm_password (str): Confirm password.
        security_question (str): Security question.
    
    Returns:
        dict: Registration status.
    """
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']
        security_question = data['security_question']
        
        # Validate email or phone
        if '@' in email:
            email_validation = validate_email(email)
        else:
            email_validation = validate_phone(email)
        
        # Validate password
        password_validation = validate_password(password)
        
        # Check if password and confirm password match
        if password != confirm_password:
            return jsonify({'error': 'Password and confirm password do not match'}), 400
        
        # Check if any validation failed
        if email_validation != True or password_validation != True:
            return jsonify({'error': str(email_validation) if email_validation != True else str(password_validation)}), 400
        
        # Hash password
        hashed_password = generate_password_hash(password)
        
        # Insert user into database
        user = {
            'email': email,
            'password': hashed_password,
            'security_question': security_question
        }
        MONGO.db.users.insert_one(user)
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@APP.route('/forgot-password', methods=['POST'])
def forgot_password():
    """
    Send password reset link to user's email.
    
    Args:
        email (str): Email address.
        security_question_answer (str): Security question answer.
    
    Returns:
        dict: Password reset status.
    """
    try:
        data = request.get_json()
        email = data['email']
        security_question_answer = data['security_question_answer']
        
        # Find user in database
        user = MONGO.db.users.find_one({'email': email})
        
        # Check if user exists
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        
        # Check if security question answer is correct
        if user['security_question'] != security_question_answer:
            return jsonify({'error': 'Incorrect security question answer'}), 400
        
        # Generate password reset link
        password_reset_link = 'https://example.com/reset-password/' + email
        
        # Send password reset link to user's email
        send_password_reset_link(email, password_reset_link)
        return jsonify({'message': 'Password reset link sent successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@APP.route('/save-personal-info', methods=['POST'])
def save_personal_info():
    """
    Save user's personal information.
    
    Args:
        email (str): Email address.
        name (str): Name.
        age (str): Age.
        sex (str): Sex.
        address (str): Address.
        profile_picture (str): Profile picture.
    
    Returns:
        dict: Personal info save status.
    """
    try:
        data = request.get_json()
        email = data['email']
        name = data['name']
        age = data['age']
        sex = data['sex']
        address = data['address']
        profile_picture = data['profile_picture']
        
        # Validate personal info
        name_validation = validate_name(name)
        age_validation = validate_age(age)
        sex_validation = validate_sex(sex)
        address_validation = validate_address(address)
        
        # Check if any validation failed
        if name_validation != True or age_validation != True or sex_validation != True or address_validation != True:
            return jsonify({'error': str(name_validation) if name_validation != True else str(age_validation) if age_validation != True else str(sex_validation) if sex_validation != True else str(address_validation)}), 400
        
        # Find user in database
        user = MONGO.db.users.find_one({'email': email})
        
        # Check if user exists
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        
        # Update user's personal info in database
        MONGO.db.users.update_one({'email': email}, {'$set': {'name': name, 'age': age, 'sex': sex, 'address': address, 'profile_picture': profile_picture}})
        return jsonify({'message': 'Personal info saved successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@APP.route('/get-food-preferences', methods=['GET'])
def get_food_preferences():
    """
    Get list of food preferences.
    
    Returns:
        list: List of food preferences.
    """
    try:
        return jsonify({'food_preferences': FOOD_PREFERENCES}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@APP.route('/login', methods=['POST'])
def login():
    """
    Login a user.
    
    Args:
        email (str): Email address.
        password (str): Password.
    
    Returns:
        dict: Login status.
    """
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']
        
        # Find user in database
        user = MONGO.db.users.find_one({'email': email})
        
        # Check if user exists
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        
        # Check if password is correct
        if not check_password_hash(user['password'], password):
            return jsonify({'error': 'Incorrect email or password'}), 400
        
        return jsonify({'message': 'User logged in successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@APP.route('/logout', methods=['POST'])
def logout():
    """
    Logout a user.
    
    Returns:
        dict: Logout status.
    """
    try:
        return jsonify({'message': 'User logged out successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    APP.run(debug=True)


#*End of AI Generated Content*