from flask import Flask, request, render_template
import sqlite3
import os

current =os.path.dirname(os.path.abspath(__file__))


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

app.route("/", methods = [" POST", "GET"])
def home1():
    FNAME = request.form ["FNAME"]
    FNUM = (int) (request.form ["FNAME"])
    FPASS = request.form ["FNAME"]
    connection -=sqlite3.connect(current + "SQLSERVER.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM user WHERE Username =?", FNAME,FPASS )
    user = cur.fetchone()
    if user is not None:
        return render_template("")
    else:
        error = "USERNAME NOT FOUND"
    #cur.execute("INSERT INTO user (NAME , NUMBER , PASS) values (?,?,?)", FNAME,FNUM,FPASS )
    #connection.commit()
    #return render_template()



if __name__=="__main__":
    app.run(debug=True)