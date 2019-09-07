import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    if not (request.form.get("Name") or not request.form.get("Sirname") or not request.form.get("Email")
            or not request.form.get("PreferredSport") or not request.form.get("Continent")):
        return render_template("error.html")
    with open("survey.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Sirname", "Email", "PreferredSport", "Continent"])
        writer.writerow({"Name": request.form.get("Name"), "Sirname": request.form.get("Sirname"), "Email": request.form.get(
            "Email"), "PreferredSport": request.form.get("PreferredSport"), "Continent": request.form.get("Continent")})
    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    with open("survey.csv", "r") as file:
        reader = csv.DictReader(file)
        students = list(reader)
    return render_template("registered.html", students=students)
