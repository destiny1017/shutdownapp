from flask import Flask, render_template
import os
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/batch")
def execute():
    os.system(r'E:/shutdownapp/test.bat')
    return "OK"

@app.route("/startapp")
def startapp():
    os.system(r'E:/shutdownapp/startapp.bat')
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
