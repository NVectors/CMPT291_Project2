#!/usr/bin/env python3


from bsddb3 import db
import sys
import query_parser

# Instances of BerkeleyDB
termDB = db.DB()
emailDB = db.DB()
dateDB = db.DB()
recDB = db.DB()

# Create path to index files
indexPath = "data/indexes/"

# Open Index Databases
termDB.open(indexPath + 'te.idx')
emailDB.open(indexPath + 'em.idx')
dateDB.open(indexPath + 'da.idx')
recDB.open(indexPath + 're.idx')

# Create cursor for each Database
termCursor = termDB.cursor()
emailCursor = emailDB.cursor()
dateCursor = dateDB.cursor()
recCursor = recDB.cursor()


class EmailQuery:
    def __int__(self, searchEmail, keyword):
        self.searchEmail = searchEmail
        self.keyword = keyword



# Close Databases when done
termDB.close()
emailDB.close()
dateDB.close()
recDB.close()
