from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict/' , methods=["GET" ,"POST"])
def predict():
    if requests.method == "POST":
        Open = requests.form.get("Open");

if __name__ == "__main__":
    app.run(debug=True)