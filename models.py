# models.py
import datetime
from peewee import *
from app import db

class UNPDEntry(Model):
    accession = TextField(unique=True)
    unpd_accession = TextField()
    common_name = TextField()
    inchi = TextField()
    exactmass = FloatField()
    molecular_formula = TextField()
    inchik = TextField()

    class Meta:
        database = db

    def getDict(self):
        return {"accession": self.accession, "inchi" : self.inchi, "exactmass": self.exactmass, "common_name": self.common_name, "unpd_accession" : self.unpd_accession, "molecular_formula" : self.molecular_formula, "inchik": self.inchik}
