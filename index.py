from flask import Flask, render_template, url_for, request, redirect, flash, session
import os


app = Flask(__name__)
app.secret_key = "9lSvS9c%dza!v@sX!vhaY1T5evsNEw*eqIl5jRxGm*vp!^f0LbyLWLYFj97*XRswcI&GiuEFCFyUg^am27OHYA"


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


@app.route("/afbeelding", methods=["GET", "POST"])
def afbeelding():
    ProgressPosition = 5
    ImgList = ["PreDefDatasets/Dataset1/Positive/Toyota 3.jpg", "PreDefDatasets/Dataset1/Positive/Toyota 5.jpg", "PreDefDatasets/Dataset1/Positive/Skoda 4.jpg", "images/UM-logo.jpg"]
    apiUrl= ""

    if request.method == "POST":

        UploadImg = request.form["UploadFile"]
        session["UploadImg"] = UploadImg

        return redirect(url_for('afbeeldingVerwerking'))
    else:
        return render_template("afbeelding.html", step=ProgressPosition, imglist=ImgList)


@app.route("/afbeeldingVerwerking")
def afbeeldingVerwerking():
    ProgressPosition = 6

    return render_template("afbeeldingVerwerking.html", step=ProgressPosition)


@app.route("/resultaat", methods=["GET", "POST"])
def resultaat():
    ProgressPosition = 7

    if "UploadImg" in session:
        UploadImg = session["UploadImg"]
        #getresults
        JsonResult = {"Toyota 1.jpg": 0.944, "Volkswagen 1.jpg": 0.666, "Opel 1.jpg": 0.777}
        sorted_values = sorted(JsonResult.values(), reverse=True)
        sorted_results = {}
        for i in sorted_values:
            for k in JsonResult.keys():
                if JsonResult[k] == i:
                    sorted_results[k] = JsonResult[k]
                    break
        firstImage = next(iter(sorted_results))
        firstImagePath = "PreDefDatasets/Dataset1/Anchor/"+firstImage
        sortedresultslist = []
        for i in sorted_results:
            sortedresultslist.append("PreDefDatasets/Dataset1/Anchor/"+i)
        return render_template("resultaat.html", step=ProgressPosition, imgresultlist=sortedresultslist, firstImage=firstImagePath)
    else:
        return redirect(url_for("afbeelding"))

@app.route("/eind")
def eind():
    ProgressPosition = 8
    return render_template("eind.html", step=ProgressPosition)


if __name__ == "__main__":
    app.run(debug=True)
