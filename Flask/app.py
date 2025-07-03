from flask import Flask, render_template
app = Flask(__name__)

# a decorator for registering with the given/default URL
@app.route('/')
def welcome():
    #return 'Hello, Im learning flask';
    return render_template("welcome.html")

@app.route('/about')
def about():
    #return 'This is the about section';
    return render_template('about.html')

@app.route('/contact')
def contact():
    #return 'You can contact from this domain';
    return render_template('contact.html')

@app.route("/user/<name>")
def user(name):
    return render_template("index.html", name = name)

@app.route("/post/<int:id>", methods = ['GET'])
def post(id):
    # return f'Post ID: {id}'
    return render_template("post.html", id = id)

if __name__ == '__main__':
    app.run(debug=True)