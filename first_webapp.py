from flask import Flask

app = Flask(__name__)

@app.route("/homepage")
def index():
    return "hello"

if __name__ == "__main__":
    app.run(debug=False, port=82)
