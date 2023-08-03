from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud_flask'
app.secret_key = 'flsh msg'

mysql=MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student;")
    no=0
    data=cur.fetchall()
    cur.close()
    
    return render_template('index.html',student=data,no=no)

@app.route('/create',methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        flash('data added succesfully!')
        nim = request.form['tnim']
        nama = request.form['tnama']
        email = request.form['temail']

    cur = mysql.connection.cursor()
    cur.execute("INSERT into student (nim,nama,email) values(%s,%s,%s)",(nim,nama,email))
    mysql.connection.commit()
    
    return redirect(url_for('index'))

@app.route('/update',methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        flash('data changed succesfully!')
        nim = request.form['tnim1']
        nama = request.form['tnama1']
        email = request.form['temail1']
        cur = mysql.connection.cursor()
        cur.execute(" UPDATE student SET nama=%s,email=%s WHERE nim=%s",(nama,email,nim))
        mysql.connection.commit()
        
        return redirect(url_for('index'))
    
@app.route('/delete/<string:nim>',methods=['POST','GET'])
def delete(nim):
    if request.method == 'POST':
        flash('data deleted succesfully!')
        cur = mysql.connection.cursor()
        cur.execute(""" DELETE from student where nim=%s""",(nim,))
        mysql.connection.commit()
    
    return redirect(url_for('index'))
    
        


if __name__=="__main__":
    app.run(debug=True)