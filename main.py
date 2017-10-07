import sys
import json
from flask import Flask, render_template, request
from watson-developer-cloud import ToneAnalyzerV3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>hello world</h1>"


@app.route('/version',methods=['GET'])
def version():
    return sys.version

@app.route("/tone",methods=["GET"])
def tone():
    return render_template("tone.html")

@app.route("/tone",methods=["POST"])
def analyzeTone():
    u = "0f02dd95-69ff-42f9-82f5-5a87c7d8707b"
    p = "HC2AZdsjGOFC"
    v = "2016-05-19"
    text = request.values['tone']
    t = ToneAnalyzerV3(username=u, password=p, version=v)
    d = t.tone(text)

    from IPython import embed; embed()    
    return render_template("tone.html")


app.run(host="0.0.0.0", port=4000, debug=True)
