# main.py
from app import app
from models import *
import views



if __name__ == '__main__':
    UNPDEntry.create_table(True)
    app.run(host='0.0.0.0')
