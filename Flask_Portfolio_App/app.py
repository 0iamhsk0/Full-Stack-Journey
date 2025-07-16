from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/skills')
def skills():
    return render_template('skills.html')

@main.route('/projects')
def projects():
    # Load projects from a Python list or JSON
    return render_template('projects.html', projects=projects_list)

# @main.route('/experience')
# def experience():
#     # Load experiences from a Python list or JSON
#     return render_template('experience.html', experiences=experiences_list)

projects_list = [
    {"name": "Project 1", "description": "Description...", "tech_stack": "Python, Flask", "github_link": "...", "demo_link": "..."},
    # more projects...
]
