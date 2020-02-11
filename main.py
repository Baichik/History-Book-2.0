from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/update')
def update():  
  return render_template('update.html')

@app.route('/download')
def download():
  return render_template('download.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port='7000')


