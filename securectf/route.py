from flask import redirect, render_template, request, flash, url_for
from securectf import app
from securectf.form import Login, Register


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Register()
    if request.method == 'POST':
        if form.validate_on_submit():
            
            flash("User has been successfully registered!")
            return redirect(url_for('signup'))

    if request.method == 'GET':
        return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash("User has been successfully logged in!")
            return redirect(url_for('login'))
        
    if request.method == 'GET':
        return render_template('login.html', form=form)

@app.route('/ctf')
def ctf():
    return render_template('ctf.html')

@app.route('/forum')
def forum():
    return render_template('forum.html')

@app.route('/community')
def community():
    return render_template('community.html')