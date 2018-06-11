
import sys
sys.path.insert(0, "..")

from models import *

import csv

def main():
    input_filename = sys.argv[1]

    with open(input_filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for result in reader:
            accession = result["PMA_ID"]
            inchi = result["InChI"]
            exactmass = float(result["EXACTMASS"])

            print(accession)
            UNPDEntry.get_or_create(accession=accession, inchi=inchi, exactmass=exactmass)


if __name__ == '__main__':
    main()
