from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Dog')
def dog():
    return render_template('borzoi.html')

@app.route('/Borzoi', methods=['GET', 'POST'])
def borzoi():
    if request.method == 'POST':
        creatureName = request.form['creatureName']
        return render_template('creatureName.html', creatureName=creatureName)
    return render_template('borzoi.html')

@app.route('/Contact')
def contact():
    return render_template('contact.html')

#A dynamic route for if the user wants to be directly addressed by their name on the front page.
@app.route('/Doggonit/<name>')
def user(name):
    return render_template('index.html', name=name, adminRights=False)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
