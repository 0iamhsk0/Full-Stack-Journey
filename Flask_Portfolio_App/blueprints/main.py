from flask import Blueprint, render_template, jsonify
import json

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/skills')
def skills():
    return render_template('skills.html')

@main_bp.route('/projects')
def projects():
    with open('static/data/projects.json') as f:
        projects = json.load(f)
    return render_template('projects.html', projects=projects)

@main_bp.route('/experience')
def experience():
    return render_template('experience.html')
