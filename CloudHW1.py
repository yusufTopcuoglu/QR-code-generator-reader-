from flask import Flask, redirect, url_for, request, render_template
import requests
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('CloudQr.html')



@app.route('/qr', methods = ['POST'])
def qr():
    background_color = request.form['background_color']
    color = request.form['color']
    name = request.form['name']
    url = 'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=' \
            + name + '&color=' + color + '&bgcolor=' + background_color
    print(url)
    return render_template('CloudQr.html', url = url)



if __name__ == '__main__':
   app.run(debug = True)
