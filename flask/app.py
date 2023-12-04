from flask import Flask, render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from PBLapp import app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///events.db'
db=SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

@app.route('/')
def main():
    events =Event.query.all()
    return render_template('main.html',events=events)

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        date = request.form['date']
        address = request.form['address']
        name = request.form['name']
        description = request.form['description']

        new_event = Event(date=date, address=address, name=name, description=description)
        db.session.add(new_event)
        db.session.commit()

        return redirect(url_for('main'))

    return render_template('post.html')


if __name__ == '__main__':
    app.run(debug=True)