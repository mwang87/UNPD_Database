
import sys
sys.path.insert(0, "..")

from models import *

import csv

def main():
    input_filename = sys.argv[1]

    with db.atomic():
        with open(input_filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for result in reader:
                #for key in result.keys():
                #    print(key, result[key])

                accession = result["PMA_ID"]
                inchi = result["InChI"]
                exactmass = float(result["EXACTMASS"])
                unpd_accession = (result["UNPD_ID"])
                common_name = (result["cn"])
                molecular_formula = result["mf"]
                inchik = result["inchik"]

                print(accession)
                UNPDEntry.get_or_create(accession=accession, inchi=inchi, exactmass=exactmass, unpd_accession=unpd_accession, common_name=common_name, molecular_formula=molecular_formula, inchik=inchik)



if __name__ == '__main__':
    main()
