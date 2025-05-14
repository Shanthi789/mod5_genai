#gemini
from flask import Flask,request,render_template
import google.generativeai as genai
import os
gemini_api_key = os.getenv("gemini_api_key")
genai.configure(api_key=gemini_api_key)
#genai.configure(api_key="AIzaSyBRGx27_7YzosWJloObAdCB7PeX4yKrjmw")
model = genai.GenerativeModel("gemini-1.5-flash")
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))
@app.route("/gemini",methods=["GET","POST"])
def gemini():
    return(render_template("gemini.html"))
@app.route("/gemini_reply",methods=["GET","POST"])
def gemini_reply():
    q = request.form.get("q")
    print(q)
    r = model.generate_content(q)
    r = r.text
    return(render_template("gemini_reply.html",r=r))
if __name__ == "__main__":
    app.run()

