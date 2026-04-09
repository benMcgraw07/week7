from flask import Flask 

app = Flask(__name__)

@app.route('/')

def home():
    return 'Hello, World!'

"""
@app.route('/about')
def about():
    return 'About Us Page'
"""

@app.route('/htmlDemo')
def htmlDemo():
    return "<h1>Welcome to my site</h1><p>This is a paragraph.</p>"



if __name__ == '__main__':
    app.run()
