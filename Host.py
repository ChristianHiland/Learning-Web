# Importings Flask, and render_template.
from flask import Flask, render_template
app = Flask(__name__)

files = ['Index.html', 'Create.html', 'script.js']
# This tells that the Index file needs to be shown. Flask will look in a folder called temeplates.
@app.route('/')
def Index():
    return render_template("Index.html")
@app.route('/Create.html')
def Create():
    return render_template("Create.html")
    
# Runs it in debug mode.
if __name__ == '__main__':
    app.run(debug=True)
