from flask import render_template,session,redirect,flash,url_for
from flask.forms import LoginForm, SignupForm
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from flask.bd import get_user, user_put
from flask.models  import UserData, UserModel


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    context = {
        'user' : login_form.username.data, 
        'passw' : login_form.password.data
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        
        user_doc = get_user(username)
        print(user_doc is not None)
        if not user_doc.empty:
            password_from_db = user_doc['password'][0]
            name = user_doc['name'][0]
            email = user_doc['email'][0]
            if password == check_password_hash(user_doc['password'][0], password):
                user_data = UserData(username,password,name,email)
                user = UserModel(user_data)
                login_user(user)
                flash('Bienvenido de nuevo')
                redirect(url_for('main'))
            else:
                flash('La informacion no coincide')
            
        else:
            flash('Usuario no existe')

        
        return redirect(url_for('index'))
    return render_template('login.html',**context)

@auth.route('signup',methods=['GET','POST'])
def signup():
    signup_form = SignupForm()
    context = {
        'name': signup_form.name.data,
        'email': signup_form.email.data,
        'userdb': signup_form.username.data,
        'passw': signup_form.password.data
    }
    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data
        name = signup_form.name.data
        email = signup_form.email.data

        user_doc = get_user(username)
        if user_doc.empty:
            password_hash = generate_password_hash(password)
            user_data = UserData(username,password_hash,name,email)
            user_put(user_data)
            user = UserModel(user_data)
            login_user(user)
            flash('Bienvenidos') 
            return redirect(url_for('login'))
        else:
            flash('el usuario ya existe')
        
    return render_template('add_client.html',**context)

