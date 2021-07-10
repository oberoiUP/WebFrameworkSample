from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '6c3da44efe0b9fcd6bb377c7b9851041'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Welcome!', text='This is Daman\'s home page')
    
@app.route("/about")
def second_page():
    return render_template('about.html', subtitle='About Daman', text='Daman loves basketball!')
  
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Register', form=form)
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")