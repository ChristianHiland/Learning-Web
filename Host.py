# Importings Flask, and render_template.
from flask import Flask, render_template
app = Flask(__name__)

# This tells that the Index file needs to be shown. Flask will look in a folder called temeplates.
@app.route('/')
def index():
    return render_template('Index.html')

# Runs it in debug mode.
if __name__ == '__main__':
    app.run(debug=True)
