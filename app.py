from flask import Flask
import sqlite3
from flask import redirect, render_template,url_for, request


app = Flask(__name__)


@app.route('/para')
def read_para():
    #return 'Hello'
    try:
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute('select * from paragraph')
        paragraph = c.fetchall()
        conn.commit()
    except sqlite3.IntegrityError:
        return {"error"}
    except Exception as exception:
        print(exception)
    finally:
        if conn:
            conn.close()
    return render_template('view_para.html', para = paragraph[0][0])

@app.route('/update/',methods=['POST'])
def update():
    if request.form['str']:
        new_paragraph = request.form['str']
        print(new_paragraph)
    try:
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute('UPDATE paragraph SET para="' + new_paragraph + '";')
        print(new_paragraph)
        conn.commit()
    except Exception as exception:
        print(exception)

    finally:
        if conn:
            conn.close()

    return new_paragraph



if __name__ == '__main__':
    app.run(debug=True)
