from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'test'
app.config['MYSQL_UNIX_SOCKET'] = '/Applications/MAMP/tmp/mysql/mysql.sock'


mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        username = details['username']
        email = details['email']
        age = details['age']
        price = details['price']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO posts(username, email, age, price) VALUES (%s, %s, %s, %s)", (username, email, age, price))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

if __name__ == '__main__':
    app.run()