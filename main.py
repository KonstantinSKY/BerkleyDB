#!/bin/python

import berkeleydb

from berkeleydb import db


fDB = db.DB()
fDB.open("fdb.fb", None, db.DB_HASH, db.DB_CREATE)

print(db.DB_VERSION_STRING)

fDB.close()
fDB = db.DB()
fDB.open("fdb.fb", None, db.DB_HASH)

fDB.put(b"main3", b'sada34{}')
cursor = fDB.cursor()
rec = cursor.first()
while rec:
        print (rec)
        print(type(rec[0]))
        key = rec[0].decode()
        print(type(key))
        print(key)
        rec = cursor.next()
fDB.close()