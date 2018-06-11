# views.py
from flask import abort, jsonify, render_template, request, redirect, url_for

from app import app
from models import *

import json

@app.route('/', methods=['GET'])
def homepage():
    all_entries = UNPDEntry.select()
    print(len(all_entries))
    all_entries_list = [entry.getDict() for entry in all_entries]

    return json.dumps(all_entries_list)

@app.route('/querypage', methods=['GET'])
def querypage():
    return render_template("query.html")

@app.route('/results', methods=['GET'])
def resultspage():
    exactmass = float(request.args["exactmass"])
    ppm_tolerance = float(request.args["toleranceppm"])

    mass_tolerance = exactmass * ppm_tolerance / 1000000
    results = UNPDEntry.select().where(UNPDEntry.exactmass.between(exactmass - mass_tolerance, exactmass + mass_tolerance))
    all_entries_list = [entry.getDict() for entry in results]

    return json.dumps(all_entries_list)
