from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# from app import Todo
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mypassword@192.168.52.125:4532/todo_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db. Column(db.String(200), nullable=False)
    desc = db. Column(db. String(500), nullable=False)
    date_created = db. Column(db. DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/', methods=['GET', 'POST'])
def hello():
   # todo = todo.show_all()
    return 'Welcome to Home Buddy!!!'


@app.route('/delete/<int:sno>')
def delete(sno):

    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    print("Deleting form second service")
    url = "http: //192.168.52.125:8000"
   # url = "http://127.0.0.1/8000"
    return redirect(url)


@app.route('/update')
def update():
    todo = todo.show_all()
    return 'Welcome to Update Buddy in diffrent service now arrived from the first!!!'


if __name__ == '__main__':

    app.run(debug=True)
