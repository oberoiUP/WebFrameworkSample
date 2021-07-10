from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Welcome!', text='This is Daman\'s home page')
    
@app.route("/about")
def second_page():
    return render_template('about.html', subtitle='About Daman', text='Daman loves basketball!')
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")