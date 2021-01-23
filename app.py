from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
from mysql import connector

app = Flask(__name__)
db = MySQL(app)

app.config['SECRET_KEY'] = "e61cf1ff76b8853376878db31a3c782d"
app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'myblog'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

@app.route('/')
def index():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM blog")
    blog = cursor.fetchall()
    
    return render_template("index.html", blogs=blog)


@app.route("/blog/<int:id>")
def blog(id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM blog WHERE id='%s'" , (id,))
    blog = cursor.fetchall()
    return render_template("blog.html", blogs=blog)

@app.route("/gallery")
def gallery():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM gallery")
    img = cursor.fetchall()
    return render_template("gallery.html", imgs=img)

@app.route('/tambah/')
def tambah_data():
    return render_template('tambah.html')

@app.route('/proses_tambah/', methods=['POST'])
def proses_tambah():
    img = request.form['image']
    cur = db.connection.cursor()
    cur.execute('INSERT INTO `gallery` (`image`) VALUES (%s)', (img,))
    db.connection.commit()
    return redirect(url_for('gallery'))


if __name__ == '__main__':
    app.run(debug=True)