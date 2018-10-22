from flask import Flask, request, render_template, flash, redirect, url_for
from forms import EquationForm
import sys
from khwarizmi import exc, equations, linear
from solver import solve

print(linear.Linear("y = 2x + 5").solve_for("x", 3))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is my secret :)'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


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
