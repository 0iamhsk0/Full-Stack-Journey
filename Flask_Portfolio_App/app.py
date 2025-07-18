from flask import Flask
from blueprints.main import main_bp
from blueprints.blog import blog_bp
from blueprints.contact import contact_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Register Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(contact_bp)

if __name__ == "__main__":
    app.run(debug=True)
