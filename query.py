#!/usr/bin/env python3


from bsddb3 import db
import sys
import query_parser as parser

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


def query(q):
    pass



def termSearch(queryTerm, cursor):
    # TODO Range search if we have wild card % example confidential% as in confidential, confidentially, confidentiality
    # TODO termSearch
    wildcard = queryTerm[-1]

    if wildcard == '%':
        pass
    else:
        query_output = set()

        result = cursor.set(queryTerm.encode("UTF-8"))
        row_ids = result[1].decode('UTF-8').split(',')
        term_id = row_ids[0]

        query_output.add(term_id)

        dup = cursor.next_dup()
        while dup is not None:
                dup_row_ids = dup[1].decode('UTF-8').split(',')
                dup_term_id = dup_row_ids[0]
                query_output.add(dup_term_id)
                dup = cursor.next_dup()

        return query_output


def output(id_set, cursor, outputType):
    if not id_set:
        print("No results")
        return

    for id in id_set:
        result = cursor.set(id.encode('UTF-8'))
        rec = result[1].decode('UTF-8')
        if outputType.lower() == "brief":
            parser.rec_parse(rec)


test = termSearch('s-confidential', termCursor)
output(test, recCursor, "Brief")

# Close Databases when done
termDB.close()
emailDB.close()
dateDB.close()
recDB.close()
