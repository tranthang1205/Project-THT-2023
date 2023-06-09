from flask import Flask, render_template, request, session, redirect
from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'caigicungduoc'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        username = session['username']
        return render_template('user.html', Email = username)
    
    form = LoginForm()
    
    if request.method == 'POST':
        # username = session['username'] = request.form['Email']
        # return render_template('user.html', Email = username) # Truyền 1 biến Email có giá trị bằng username vào user.html
        return render_template('user.html', FORM = form)
    
    return render_template('login.html')

@app.route('/landing')
def landing():

    return render_template('landing.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/search-food')
def searchfood():
    return render_template('search-food.html')

@app.route('/search-ingredients')
def searchingredients():
    return render_template('search-ingredients.html')

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect('login')
