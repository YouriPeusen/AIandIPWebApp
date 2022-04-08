from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/keuzeAI")
def keuzeAI():
    return render_template("keuzeAI.html")


@app.route("/training")
def training():
    return render_template("training.html")


@app.route("/dataset")
def dataset():
    return render_template("dataset.html")


@app.route("/afbeelding")
def afbeelding():
    ImgList = ["img1.jpg", "img2.jpg", "img3.jpg", "img4.jpg"]

    return render_template("afbeelding.html", imglist=ImgList)


@app.route("/resultaat")
def resultaat():
    ImgResultsList = ["img1.jpg", "img2.jpg", "img3.jpg", "img4.jpg"]

    return render_template("resultaat.html", imgresultlist=ImgResultsList)


@app.route("/eind")
def eind():
    return render_template("eind.html")


if __name__ == "__main__":
    app.run(debug=True)
