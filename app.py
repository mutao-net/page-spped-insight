from flask import Flask,render_template
import requests
import json

app = Flask(__name__)
@app.route("/")
def index():
    url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="
    target = "https://mutaonet.hatenablog.com/"
    params = "&category=performance&strategy=mobile"
    headers = {"content-type": "application/json"}
    response = requests.get(url+ target + params, headers).json()
    return render_template("index.html", response=response["lighthouseResult"]["audits"])

if __name__ == "__main__":
    app.run(debug=True)