# views.py
from flask import abort, jsonify, render_template, request, redirect, url_for

from app import app
from models import *
import json
import urllib

@app.route('/', methods=['GET'])
def querypage():
    return render_template("query.html")


MAX_DB_QUERY_RESULT = 1000
@app.route('/results', methods=['GET'])
def resultspage():
    print(request.args)
    db_query = UNPDEntry.select()
    try:
        exactmass = float(request.args["exactmass"])
        ppm_tolerance = float(request.args["toleranceppm"])
        mass_tolerance = exactmass * ppm_tolerance / 1000000
        db_query = db_query.where( UNPDEntry.exactmass.between(exactmass - mass_tolerance, exactmass + mass_tolerance) )
    except:
        print("No ppm query")

    

    common_name = request.args["common_name"]
    if len(common_name) > 0:
        db_query = db_query.where(UNPDEntry.common_name.contains(common_name) )



    molecular_formula = request.args["molecular_formula"]
    if len(molecular_formula) > 0:
        db_query = db_query.where(UNPDEntry.molecular_formula == molecular_formula )



    db_query = db_query.limit(MAX_DB_QUERY_RESULT)




    all_entries_list = [entry.getDict() for entry in db_query]



    for entry in all_entries_list:
        entry["structurelink"] = "http://ccms-support.ucsd.edu:5000/smilesstructure?inchi=%s" % (urllib.quote_plus(entry["inchi"]))



    return json.dumps(all_entries_list)
