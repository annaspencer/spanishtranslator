from flask import Flask
from flask import Flask, render_template, redirect, session, flash, request
from forms import UserForm, RegisterForm, NewVocabForm, AddWords
from models import connect_db, db, User, Vocab, Word
import requests

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///spanishverbs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "272-379-544"
connect_db(app)
##app routes

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    """creates a user"""
    if "username" in session:
        return redirect(f"/users/{session['username']}")
    try:
        form = RegisterForm()

        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data

            user = User.register(username, password)

            db.session.commit()
            session['username'] = user.username

            return redirect(f"/users/{user.username}")

        else:
            return render_template("register.html", form=form)
    except:
        flash('Sorry, username already exists. Try again.')
        return render_template("register.html", form=form)

@app.route('/users/<username>', methods=["GET", "POST"])
def show_secret(username):
    """secret page for users only"""
    if "username" not in session or username != session['username']:
        return redirect('/')
    else:
        user = User.query.get(username)
       
        return render_template("userpage.html", user =user, )


@app.route('/login', methods=['GET', 'POST'])
def login_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            flash(f"Welcome Back, {user.username}!")
            session['username'] = user.username
            return redirect(f"/users/{user.username}")
        else:
            form.username.errors =["Invalid username or password."]
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')

@app.route("/translate", methods=['GET'])
def translate():
    """gets input, pushes to api, returns translation"""
    try:
        word = request.args["translator"]
        resp = requests.get(f"https://www.dictionaryapi.com/api/v3/references/spanish/json/{word}?key=98667e43-1171-42d9-b280-c8670f31ec09")
        translation = resp.json()[0]["shortdef"][0]
    # audio= resp.json()[0]["hwi"]["prs"][0]["sound"]["audio"]
        return render_template('websters.html', word=word, translation=translation)
    except:
        flash("Try a different word")
    return redirect("/")

   

# @app.route('/websters', methods=['GET'])
# def websters():
#     resp = requests.get("https://www.dictionaryapi.com/api/v3/references/spanish/json/ser?key=98667e43-1171-42d9-b280-c8670f31ec09")
#     data = resp.json()[0]["suppl"]["cjts"][1]["cjfs"]

    
#     return render_template('websters.html', data=data)

@app.route('/users/<username>/addvocab')
def new_list():
    form = NewVocabForm()
    return render_template('/new-info.html', form=form)














@app.route('/users/<username>/addvocab', methods=["POST"])
def create_list(username):
    if username not in session or username != session[username]:
        return redirect('/')
    else:
        user = User.query.get(username)
    print(session)
    try:
        form = NewVocabForm()
        
        if form.validate_on_submit():
            title = form.title.data
            

            addvocab = Vocab(title =title, username=username)

            db.session.add(new_list)
            db.session.commit()
            flash("New Vocabulary List Created!")
            return render_template("/new-list")
        else:
            return render_template("/addvocab.html", form=form)
    except:
        flash("That title is taken, try again.")
        return render_template("/addvocab.html", form=form)

        

@app.route('/users/<username>/new-list/', methods=["GET", "POST"])
def add_word(username):
    if "username" not in session or username != session['username']:
        return redirect('/')
    try:
        form = AddWords()
        
        if form.validate_on_submit():
            word= form.word.data
            translation= form.translation.data
            
            new_word= Word(word=word, translation=translation, list_title=title)

            db.session.add(new_word)
            db.session.commit()
            flash("Word added. Add another or hit done.")
            return redirect(f"/new-list.html", user=user, new_word=new_word)
        else:
            return render_template(f"/new-list.html", form=form)
    except:
        flash("Opps, there's an error. Try again.")
        return render_template(f"/addvocab.html", form=form)



    