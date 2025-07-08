from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import json
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Load data from JSON files
def load_posts():
    try:
        with open('posts.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def load_users():
    try:
        with open('users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_posts(posts):
    with open('posts.json', 'w') as f:
        json.dump(posts, f, indent=2)

def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=2)

# Routes
@app.route('/')
def home():
    posts = load_posts()
    # Get featured posts (first 3)
    featured_posts = posts[:3] if posts else []
    return render_template('home.html', featured_posts=featured_posts)

@app.route('/posts')
def all_posts():
    posts = load_posts()
    category = request.args.get('category')
    search = request.args.get('search')
    
    if category:
        posts = [post for post in posts if post['category'].lower() == category.lower()]
    
    if search:
        posts = [post for post in posts if search.lower() in post['title'].lower() or 
                search.lower() in post['summary'].lower()]
    
    # Get unique categories for filter
    all_posts = load_posts()
    categories = list(set(post['category'] for post in all_posts))
    
    return render_template('posts.html', posts=posts, categories=categories, 
                         current_category=category, search_query=search)

@app.route('/post/<post_id>')
def view_post(post_id):
    posts = load_posts()
    post = next((p for p in posts if p['id'] == post_id), None)
    
    if not post:
        flash('Post not found', 'error')
        return redirect(url_for('all_posts'))
    
    return render_template('post.html', post=post)

@app.route('/write', methods=['GET', 'POST'])
def write_post():
    if 'user_id' not in session:
        flash('Please log in to write a post', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        posts = load_posts()
        
        new_post = {
            'id': str(uuid.uuid4()),
            'user_id': session['user_id'],
            'title': request.form['title'],
            'subtitle': request.form['subtitle'],
            'summary': request.form['summary'],
            'category': request.form['category'],
            'featured_image': request.form.get('featured_image', ''),
            'main_content': request.form['content'],
            'created_at': datetime.now().strftime('%a, %m/%d/%Y'),
            'updated_at': datetime.now().strftime('%a, %m/%d/%Y'),
            'user': get_user_info(session['user_id']),
            'comments': [],
            'tags': []
        }
        
        posts.append(new_post)
        save_posts(posts)
        
        flash('Post published successfully!', 'success')
        return redirect(url_for('view_post', post_id=new_post['id']))
    
    return render_template('write.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        users = load_users()
        user = next((u for u in users if u['username'] == username), None)
        
        if user and user['password'] == password:  # In production, use proper password hashing
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        
        users = load_users()
        
        # Check if username already exists
        if any(u['username'] == username for u in users):
            flash('Username already exists', 'error')
            return render_template('register.html')
        
        new_user = {
            'id': str(uuid.uuid4()),
            'username': username,
            'password': password,  # In production, hash this
            'user_id': str(uuid.uuid4()),
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'role': 'User',
            'created_at': datetime.now().strftime('%a, %m/%d/%Y'),
            'updated_at': datetime.now().strftime('%a, %m/%d/%Y')
        }
        
        users.append(new_user)
        save_users(users)
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        flash('Please log in to view your profile', 'error')
        return redirect(url_for('login'))
    
    posts = load_posts()
    user_posts = [post for post in posts if post['user_id'] == session['user_id']]
    
    return render_template('profile.html', user_posts=user_posts)

def get_user_info(user_id):
    users = load_users()
    user = next((u for u in users if u['user_id'] == user_id), None)
    if user:
        return {
            'id': user['user_id'],
            'first_name': user.get('first_name', ''),
            'last_name': user.get('last_name', ''),
            'username': user['username'],
            'email': user.get('email', ''),
            'role': user.get('role', 'User')
        }
    return None

if __name__ == '__main__':
    app.run(debug=True)
