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
    operations = parser.rec_parse(q)
    result = []
    for op in operations:
        if op[0] == "email":
            # do call email query stuff here
            # Maybe result.append("My result string")
            pass

        if op[0] == "date":
            # do date stuff
            pass

        if op[0] == "mode":
            # do mode stuff
            pass

        if op[0] == "term":
            # Do term stuff 

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


def emailQuery(queryTerm, cursor):
    query_output = set()

    result = cursor.set(queryTerm.encode("UTF-8"))
    row_ids = result[1].decode('UTF-8').split(',')
    email_id = row_ids[0]

    query_output.add(email_id)

    dup = cursor.next_dup()
    while dup is not None:
        dup_row_ids = dup[1].decode('UTF-8').split(',')
        dup_email_id = dup_row_ids[0]
        query_output.add(dup_email_id)
        dup = cursor.next_dup()

    return query_output

def dateQuery(queryTerm, cursor):
    query_output = set()

def recSearch(index, cursor):
    result = cursor.set(index.encode("UTF-8"))
    records = result[1].decode('UTF-8').split(',')
    record = records[0]
    print(record)


# test = termSearch('s-confidential', termCursor)
# for t in test:
#    recSearch(t,recCursor)

test = emailQuery('to-phillip.allen@enron.com', emailCursor)
print(len(test))

# Close Databases when done
termDB.close()
emailDB.close()
dateDB.close()
recDB.close()
