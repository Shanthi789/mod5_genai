#gemini
from flask import Flask,request,render_template
import google.generativeai as genai
import os
import sqlite3
import datetime
#gemini_api_key = os.getenv["gemini_api_key_1"]
#genai.configure(api_key=gemini_api_key)
genai.configure(api_key="AIzaSyBRGx27_7YzosWJloObAdCB7PeX4yKrjmw")
model = genai.GenerativeModel("gemini-1.5-flash")
app = Flask(__name__)

first_time=0

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))


@app.route("/main",methods=["GET","POST"])
def main():
    q = request.form.get("q")
    print(q)
    t = datetime.datetime.now()
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("insert into users(name,timestamp) values(?,?)",(q,t))
    conn.commit()
    c.close()
    conn.close()
    return(render_template("main.html"))

@app.route("/user_log",methods=["GET","POST"])
def user_log():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("select * from users")
    #user_logs = c.fetchall()
    r=""
    for row in c:
        print(row)
        r = r+str(row)+"\n"
    c.close()
    conn.close()
    return render_template("user_log.html", r=r)

@app.route("/delete_log",methods=["GET","POST"])
def delete_log():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("delete from users")
    conn.commit()
    c.close()
    conn.close()
    return render_template("delete_log.html")

@app.route("/gemini",methods=["GET","POST"])
def gemini():
    return(render_template("gemini.html"))

@app.route("/paynow",methods=["GET","POST"])
def paynow():
    return(render_template("paynow.html"))

@app.route("/gemini_reply",methods=["GET","POST"])
def gemini_reply():
    q = request.form.get("q")
    print(q)
    r = model.generate_content(q)
    r = r.text
    return(render_template("gemini_reply.html",r=r))

@app.route("/logout",methods=["GET","POST"])
def logout():
    global first_time
    first_time = 1
    return(render_template("index.html"))
    

if __name__ == "__main__":
    app.run()

