from flask import Flask
app = Flask(__name__)


#главная страница сервера
@app.route('/')
def index():
    return "I CAN SHOW YOU SOME IMAGES"


#разрешаем общий доступ
if __name__ == "__main__":
    app.run(host='0.0.0.0')