import os, json
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


def start_func():
    """Функция для создания необходимых директорий и файлов настроек при запуске"""

    dirs = os.listdir()

    if "data" not in dirs:
        print("Creating data folder")
        os.mkdir("data")

    data_dirs = os.listdir("data")

    if "settings.json" not in data_dirs:
        print("Creating settings.json")
        with open("data/settings.json", "w") as f:
            data = {"API_ID": "", "API_HASH": ""}

            json.dump(data, f)


@app.route("/")
async def index():
    try:
        return render_template("index.html")
    except Exception as e:
        print(f"Error in index route: {e}")
        return render_template("error.html", error=str(e))


if __name__ == "__main__":
    start_func()
    app.run(debug=True, port=5055)
