from flask import Flask, render_template
import requests
import json
import random
import datetime
import web3_data

app = Flask(__name__)


@app.route("/")
def home():
    answers = web3_data.ethereum()
    blocks = answers[0]
    pending = answers[1]
    year = datetime.datetime.now().year
    random_num = random.randint(1, 10)
    return render_template("index.html", num=random_num, year=year, blocks=[blocks.to_html(classes='data', header='true')],
                           pending=[pending.to_html(classes='data', header='true')])


if __name__ == "__main__":
    app.run(debug=True, port=5500)
