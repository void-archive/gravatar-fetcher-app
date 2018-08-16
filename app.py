# Authored by void (@missingbinaries)
# Licensed under MIT

from libgravatar import Gravatar
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

"""
@app.route('/end_result.html')
def end_result():
    g = Gravatar(html_element.textbox.value) # This kind of thing
"""

if __name__ == '__main__':
    app.run(port=8080)
