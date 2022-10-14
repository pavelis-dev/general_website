from flask import Flask, render_template, request, flash
import requests
import json
import random
from password_generator import password
from send_mail import send_email
from setting import secret_key, my_mail, password_mail
import smtplib
from email.mime.text import MIMEText


app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key


# главная страница
@app.route("/")
def main_page():
    return render_template('index.html')


# просмотр фото с марса
rovers_src = {
    'Perseverance': 'https://www.ridus.ru/images/2021/4/22/1259190/in_article_391a9d0039.jpeg',
    'Curiosity': 'https://argumenti.ru/images/arhnews/453984.jpg',
    }

@app.route("/marsphoto", methods=['POST','GET'])
def mars_photos():
    marsohod = 'Perseverance'
    if request.args.get('rover') == 'Perseverance' or request.args.get('') == '':
        marsohod = 'Perseverance'
    elif request.args.get('rover') == 'Curiosity':
        marsohod = 'Curiosity'

    # r = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/' + marsohod + '/latest_photos?api_key=DEMO_KEY')
    # jsondata = json.loads(r.text)
    with open('latest_photos.json') as f:   # скачиваем экземпляр json данных в файл для тестирования
        jsondata = json.load(f)
    photos = jsondata['latest_photos']
    date_list = photos[0]['earth_date'].split('-')
    date_list.reverse()
    date = '.'.join(date_list)
    return render_template('marsphoto.html', photos=photos, date=date, marsohod=marsohod, rovers_src=rovers_src)


# моё резюме
@app.route("/cv", methods=['POST','GET'])
def cv_func():
    if request.method == 'POST':
        flag_mail = send_email(request.form.get('name'), request.form.get('email'), request.form.get('message'))
        if flag_mail == 'ok':
            flash('Сообщение отправлено', category='success')
            return render_template('cv.html')
        else:
            flash('Сообщение не отправлено, проверьте корректность вводимых данных', category='error')
            return render_template('cv.html')

    return render_template('cv.html')


# генератор паролей
@app.route("/passwgenerator", methods=['GET'])
def password_generator():
    password_total = ['Укажите параметры пароля и нажмите "сгенерировать"']
    if request.args.get('btn-gen') == "сгенерировать":
        password_total = password(request.args.get('a'), request.args.get('b'), request.args.get('c'), request.args.get('d'), 
               request.args.get('e'), request.args.get('length'), request.args.get('count_password'))
        return render_template('passwgenerator.html', password_total=password_total)
    else:
        return render_template('passwgenerator.html', password_total=password_total)


app.run()