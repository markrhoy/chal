from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def challenge():
    return render_template("challenge.html")


@app.route("/embed")
def b64data():
    filename = request.args.get("milknmocha")
    if filename == "":
        return "???? what are u doing"
    try:
        with open(f'static/{filename}', 'rb') as data:
            return data.read()
    except Exception as e:
        return """
            random error ???? <!-- flag.txt is located in flag/ -->
        """


if __name__ == "__main__":
    app.run(port=1338)
