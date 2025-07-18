from flask import Blueprint, render_template
import json

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/blog')
def blog():
    with open('static/data/blog.json') as f:
        posts = json.load(f)
    return render_template('blog.html', posts=posts)
