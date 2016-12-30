from datetime import datetime
from pony.orm import *

db = Database()

class Akt(db.Entity):
    id = PrimaryKey(int, auto=True)
    XMLBarcodeCompressed = Optional(str, 30)
    Barcode2 = Optional(str, 30)
    XMLmark2 = Optional(str, 40)
    DateModified = Required(datetime)
    XMLBrojPredmeta = Optional(str, 30)
    XMLDatumAktaCeo = Optional(datetime)
    BrojPredmeta = Optional(str, 30)
    BrojaktaVanUC = Optional(str, 50)
    DatumAktaVanUC = Optional(datetime)
    XMLtitle = Optional(str, 300)
    XMLComments = Optional(str, 300)
    XMLPrimalac = Optional(str, 100)
    XMLAdresaPrimaoca = Optional(str, 300)
    XMLVeza = Optional(str, 200)
    XMLInicijali = Optional(str, 20)
    primalac_tip = Optional('PrimalacTip')
    potpisnik_tip = Optional('PotpisnikTip')
    opis_tip = Optional('OpisTip')
    #XMLPotpisnik = Optional(str)

class PrimalacTip(db.Entity):
    id = PrimaryKey(int, auto=True)
    akts = Set(Akt)
    PrimalacTip = Optional(str)

class PotpisnikTip(db.Entity):
    id = PrimaryKey(int, auto=True)
    akts = Set(Akt)
    PotpisnikTip = Optional(str)


class OpisTip(db.Entity):
    id = PrimaryKey(int, auto=True)
    akts = Set(Akt)
    OpisTip = Optional(str)

sql_debug(True)

db.bind("sqlite", "PEvidencija2.sqlite", create_db = True)
db.generate_mapping(create_tables=True)

print("kraj definicija")

with db_session:
    p1 = OpisTip(OpisTip="Prosledjivanje")
    p2 = OpisTip(OpisTip="Prosledjivanje2")
    p3 = OpisTip(OpisTip="Prosledjivanje3")
    p4 = OpisTip(OpisTip="Prosledjivanje4")
    p5 = OpisTip(OpisTip="Prosledjivanje5")

    p1 = PotpisnikTip(PotpisnikTip="potpisnik")
    p2 = PotpisnikTip(PotpisnikTip="potpisnik2")
    p3 = PotpisnikTip(PotpisnikTip="potpisnik3")
    p4 = PotpisnikTip(PotpisnikTip="potpisnik4")
    p5 = PotpisnikTip(PotpisnikTip="potpisnik5")

    p1=PrimalacTip(PrimalacTip="potpisnik")
    p2=PrimalacTip(PrimalacTip="potpisnik2")
    p3=PrimalacTip(PrimalacTip="potpisnik3")
    p4=PrimalacTip(PrimalacTip="potpisnik4")
    p5=PrimalacTip(PrimalacTip="potpisnik5")

print("kraj2")
