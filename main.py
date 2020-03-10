from flask import Flask, render_template, request, redirect, url_for
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d  

app = Flask('app')

# con = sqlite3.connect('historybook.db')
# cur = con.cursor()
# cur.execute("DELETE FROM feedbacks")
# con.commit()
# cur.close()

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/update')
def update():  
  return render_template('update.html')

@app.route('/download')
def download():
  return render_template('download.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  if request.method == 'POST':
    fname = request.form['fname']
    lname = request.form['lname']
    comment = request.form['comment']

    con = sqlite3.connect('historybook.db')
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute("INSERT INTO feedbacks(fname, lname, comment) VALUES (?, ?, ?)", (fname, lname, comment))
    con.commit()
    cur.close()
    return redirect(url_for('feedbacks'))
  return render_template('contact.html')

@app.route('/feedbacks')
def feedbacks():
  con = sqlite3.connect('historybook.db')
  con.row_factory = dict_factory
  cur = con.cursor()
  feedbacksql = """
  SELECT * FROM feedbacks
  """
  cur.execute(feedbacksql)
  feedbacks = cur.fetchall()

  return render_template('feedbacks.html', feedbacks=feedbacks)  
  cur.close()

if __name__ == "__main__":
  app.run(host='0.0.0.0', port='7000')