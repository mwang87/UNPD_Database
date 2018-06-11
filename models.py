# models.py
import datetime
from peewee import *
from app import db

class UNPDEntry(Model):
    accession = TextField(primary_key=True)
    inchi = TextField()
    exactmass = FloatField()

    class Meta:
        database = db

    def getDict(self):
        return {"accession": self.accession, "inchi" : self.inchi, "exactmass": self.exactmass}
