# 📘 Assignment: Building Your First Website with Flask

## 🎯 Objective

Learn web development fundamentals by building a multi-page website using Flask, Python's lightweight web framework. You'll create routes, use HTML templates, and handle user input through forms.

## 📝 Tasks

### 🛠️ Set Up Flask and Create Routes

#### Description
Create a Flask application and define multiple routes to handle different pages.

#### Requirements
Completed program should:

- Install Flask and create a Flask application instance
- Define at least three routes (e.g., `/` for home, `/about` for an about page, `/contact` for contact)
- Each route should return a simple HTML response with page-specific content
- Run the Flask development server so pages are accessible in a browser

### 🛠️ Use Templates and Static Files

#### Description
Organize your website using HTML templates and add styling with CSS.

#### Requirements
Completed program should:

- Create a `templates/` directory with HTML template files for each page
- Use Jinja2 templating to pass dynamic data from Flask routes to templates
- Create a `static/` directory with a `style.css` file to style your pages
- Include a navigation menu that links between pages on all templates

### 🛠️ Handle Form Data and User Input

#### Description
Create a form page that accepts user input and displays the submitted data.

#### Requirements
Completed program should:

- Create a form in an HTML template with fields like name, email, and a message
- Define a POST route to handle form submissions
- Display a confirmation page with the submitted data
- Include basic validation to ensure required fields are not empty
