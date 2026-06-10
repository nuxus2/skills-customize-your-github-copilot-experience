from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html', title='Home')

# About route
@app.route('/about')
def about():
    return render_template('about.html', title='About')

# Contact route - GET to display form, POST to handle submission
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Basic validation
        if not name or not email or not message:
            return render_template('contact.html', title='Contact', error='All fields are required')
        
        # Display confirmation with submitted data
        return render_template('confirmation.html', title='Confirmation', 
                             name=name, email=email, message=message)
    
    return render_template('contact.html', title='Contact')

if __name__ == '__main__':
    app.run(debug=True)
