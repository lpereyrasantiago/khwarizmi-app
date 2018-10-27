from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flaskr.forms import EquationForm
import sys
from khwarizmi import exc, equations, linear
from flaskr.solver import solve
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is my secret :)'
# Sets location of the SQLAlchemy file. Three slashes indicate relative path.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return "User: {}, Picture: {}".format(self.username, self.image_file)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    post_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "Post: {}, Date: {}".format(self.title, self.post_date)

@app.route('/', methods=['GET', 'POST'])
def main():

    form = EquationForm()

    if request.method == 'POST':
        result = str(solve(form.equation.data, form.operation.data))
    else:
        result = ''

    return render_template('main', title='Equation', form=form, solution=result)


if __name__ == "__main__":
    app.run(debug=True)

