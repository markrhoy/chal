from flask import Flask, jsonify, render_template, request
from utils.x7xxvv import x7xvv

app = Flask(__name__)


@app.route('/')
def challenge():
    return render_template("challenge.html")


@app.route("/verify", methods=['POST'])
def verify():
    vault_pins = x7xvv()

    data = [
        request.form.get('first'),
        request.form.get('second'),
        request.form.get('third'),
        request.form.get('fourth'),
        request.form.get('fifth'),
        request.form.get('sixth'),
        request.form.get('seventh'),
        request.form.get('eighth'),
        request.form.get('ninth'),
        request.form.get('tenth'),
    ]

    for i, j in zip(vault_pins, data):
        if float(i) != float(j):
            return render_template("generic.html", type="is-danger", message="Wrong pin. Try again")

    return render_template("generic.html", type="is-primary",
                           message=f"Congrats! Here is your flag: {open('flag.txt', 'r').read()}")


if __name__ == "__main__":
    app.run(port=1337)
