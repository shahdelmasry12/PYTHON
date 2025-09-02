# n1=float(input("enter your first num: "))
# n2=float(input("enter your second num: "))
# n3=float(input("enter your third num: "))
# average = (n1 + n2 + n3) / 3
# print(f" the avge is {average:.2f}")                 
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# ????? ????? ????????
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'university'

mysql = MySQL(app)

# ?????? ???????? ???? ????? ???? ???????
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM faculty")
    faculty_data = cur.fetchall()
    cur.close()
    return render_template('index.html', faculty=faculty_data)

# ????? ?? ????? ???? ???????
@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM faculty WHERE name LIKE %s OR department LIKE %s", (f"%{query}%", f"%{query}%"))
    faculty_data = cur.fetchall()
    cur.close()
    return render_template('index.html', faculty=faculty_data)

# ????? ??? ???? ?????
@app.route('/add', methods=['POST'])
def add_faculty():
    name = request.form['name']
    department = request.form['department']
    courses = request.form['courses']
    email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO faculty (name, department, courses, email) VALUES (%s, %s, %s, %s)", (name, department, courses, email))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
