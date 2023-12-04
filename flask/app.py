from flask import render_template
from PBLapp import app

if __name__ == '__main__':
    app.run(debug=True)




#@app.route('/main')
def calendar():
    return render_template('main.html')
