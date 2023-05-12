from flask import Flask
from markupsafe import escape
from flask import request

app = Flask(__name__)


# главная страница сервера
@app.route('/')
def index():
    msg = """
    [
  {
    "type": "BUTTON",
    "name" : "name_of_button1",
    "coord_x": 2.2,
    "coord_y": 4.5,
    "width": 12,
    "height": 10
  },
  {
    "type": "SLIDER",
    "name" : "name_of_slider1",
    "coord_x": 32.2,
    "coord_y": 44.5,
    "width": 212,
    "height": 15
  },
  {
    "type": "TEXT",
    "name" : "name_of_text1",
    "coord_x": 2.2,
    "coord_y": 4.5,
    "width": 12,
    "height": 10
  }
]
    """
    return msg


# присылаем чиселки
@app.route('/numbers/<float:digit>')
def floatNumber(digit):
    print(f"I got number {escape(digit)}")
    return f"I got number {escape(digit)}"


# присылаем чиселки
@app.route('/numbers/<int:digit>')
def intNumber(digit):
    print(f"I got number {escape(digit)}")
    return f"I got number {escape(digit)}"


# присылаем чиселки
@app.route('/arguments')
def newNumber():
    num = request.args.get("n")
    tag = request.args.get("tag")
    print(f"I got number {num} and tag {tag}")
    # print(f"I got number {num}")
    return f"I got number {num}"


# разрешаем общий доступ
if __name__ == "__main__":
    app.run(host='0.0.0.0')
