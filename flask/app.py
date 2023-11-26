from flask import render_template
from PBLapp import app

if __name__ == '__main__':
    app.run(debug=True)

events =[
    {
        'title':'event1',
        'date':'2023-12-11'
    },
    {
        'title':'event2',
        'date':'2023-12-01'
    }
]


#@app.route('/main')
def calendar():
    return render_template('main.html',events=events)
