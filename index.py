from flask import Flask, render_template, url_for
import os


app = Flask(__name__)


@app.route("/")
def index():
    startpage = True
    ProgressPosition = 1
    return render_template("index.html", startpage=startpage, step=ProgressPosition)


@app.route("/keuzeAI")
def keuzeAI():
    ProgressPosition = 2
    return render_template("keuzeAI.html", step=ProgressPosition)


@app.route("/dataset")
def dataset():
    ProgressPosition = 3
    datasetImages = os.listdir("static/PreDefDatasets/Dataset1/Anchor")
    return render_template("dataset.html", step=ProgressPosition, datasetImages=datasetImages)


@app.route("/training")
def training():
    ProgressPosition = 4
    return render_template("training.html", step=ProgressPosition)


@app.route("/afbeelding")
def afbeelding():
    ProgressPosition = 5
    ImgList = ["img1.jpg", "img2.jpg", "img3.jpg", "img4.jpg"]

    return render_template("afbeelding.html", step=ProgressPosition, imglist=ImgList)


@app.route("/resultaat")
def resultaat():
    ProgressPosition = 6
    ImgResultsList = ["img1.jpg", "img2.jpg", "img3.jpg", "img4.jpg"]

    return render_template("resultaat.html", step=ProgressPosition, imgresultlist=ImgResultsList)


@app.route("/eind")
def eind():
    ProgressPosition = 7
    return render_template("eind.html", step=ProgressPosition)


if __name__ == "__main__":
    app.run(debug=True)
