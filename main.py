from flask import Flask
from markupsafe import escape

app = Flask(__name__)


#главная страница сервера
@app.route('/')
def index():
    return "I CAN SHOW YOU SOME IMAGES"

#присылаем чиселки
@app.route('/numbers/<float:digit>')
def floatNumber(digit):
    print(f"I got number {escape(digit)}")
    return f"I got number {escape(digit)}"

#присылаем чиселки
@app.route('/numbers/<int:digit>')
def intNumber(digit):
    print(f"I got number {escape(digit)}")
    return f"I got number {escape(digit)}"


#разрешаем общий доступ
if __name__ == "__main__":
    app.run(host='0.0.0.0')