from plistlib import UID
import xmlrpc.client

#agregar aqui url del servicio, nombre de la DB, usuario y clave

url = 'http://localhost:8071'
db = 'odooIBP'
username = 'yeye'
password = '12345'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

if uid:
    print("succesfully")
else: 
    print("failed")

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

#write -------------------------

gen = models.execute_kw(db, uid, password, 'genres', 'create', [{'name': "Acustic"}])
gen = models.execute_kw(db, uid, password, 'genres', 'create', [{'name': "afrobeat"}])
gen = models.execute_kw(db, uid, password, 'genres', 'create', [{'name': "alt-rock"}])
gen = models.execute_kw(db, uid, password, 'genres', 'create', [{'name': "alternative"}])
gen = models.execute_kw(db, uid, password, 'genres', 'create', [{'name': "ambient"}])
gen = models.execute_kw(db, uid, password, 'genres', 'create', [{'name': "anime"}])
gen = models.execute_kw(db, uid, password, 'genres', 'create', [{'name': "black-meta"}])
gen = models.execute_kw(db, uid, password, 'genres', 'create', [{'name': "bluegrass"}])
gen = models.execute_kw(db, uid, password, 'genres', 'create', [{'name': "bossanova"}])
gen = models.execute_kw(db, uid, password, 'genres', 'create', [{'name': "brazil"}])
gen = models.execute_kw(db, uid, password, 'genres', 'create', [{'name': "breakbeat"}])
gen = models.execute_kw(db, uid, password, 'genres', 'create', [{'name': "british"}])
gen = models.execute_kw(db, uid, password, 'genres', 'create', [{'name': "cantopop"}])
gen = models.execute_kw(db, uid, password, 'genres', 'create', [{'name': "chicago-house"}])
gen = models.execute_kw(db, uid, password, 'genres', 'create', [{'name': "children"}])








