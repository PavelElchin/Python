from flask import Flask, render_template, redirect, request
import pandas as pd
import matplotlib.pyplot as plt
import io, base64
import db

app = Flask(__name__)

def plot():
    df = db.get_data()
    fig, ax = plt.subplots()
    df.hist(ax=ax)
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

@app.route('/')
def home():
    return render_template('index.html', img=plot())

@app.route('/data')
def data():
    return render_template('data.html', table=db.get_data().to_html(classes='table table-striped'))

@app.route('/update', methods=['POST'])
def update():
    db.update_data()
    return redirect('/data')

@app.route('/delete_last', methods=['POST'])
def delete_last():
    db.delete_last_row()
    return redirect('/data')

if __name__ == '__main__':
    db.init()
    app.run(debug=True)

