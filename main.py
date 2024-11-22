from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


def start_func():
    pass


@app.route("/")
async def index():
    try:
        return render_template("index.html")
    except Exception as e:
        print(f"Error in index route: {e}")
        return render_template("error.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True, port=5055)
