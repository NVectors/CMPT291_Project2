#!/usr/bin/env python3


from bsddb3 import db
from datetime import datetime
import query_parser as parser

# Instances of BerkeleyDB
termDB = db.DB()
emailDB = db.DB()
dateDB = db.DB()
recDB = db.DB()

termDB.set_flags(db.DB_DUP)

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
    if not operations:
        return set()
    ids = set()
    mode = 'brief'
    for op in operations:
        if op[0] == "email":
            new_ids = query_email(op[1])
            if len(ids) < 1:
                ids = new_ids
            else:
                ids = ids.intersection(new_ids)
            continue

        if op[0] == "date":
            query_date(op[1])
            #if len(ids) < 1:
            #    ids = new_ids

        if op[0] == "mode":
            print("mode =", op[1])
            mode = op[1]
            continue

        if op[0] == "term":
            new_ids = query_term(op[1])
            if len(ids) < 1:
                ids = new_ids
            else:
                ids = ids.intersection(new_ids)
            continue

    # Got set of row id's now. Translate them to email records.
    result = set()
    for id in ids:
        result.add(recCursor.set(id)[1].decode('utf-8'))

    result.add(mode)

    return result


"""
term in the form (pre, term, post)
"""


def query_term(term):
    if term[0] == "body":
        search = [b"b-"]
    elif term[0] == 'subj':
        search = [b"s-"]
    else:
        search = [b"s-", b"b-"]

    result = set()
    last = None
    for s in search:
        q = termCursor.set(s + term[1].encode())

        if not q:
            continue

        while q:
            result.add(q[1])
            q = termCursor.next_dup()

        # cursor should be pointing at last exaxt match
        nxt = termCursor.next()
        t = term[1].encode()
        while nxt:
            if s + t == nxt[0][0: len(s + t)]:
                result.add(nxt[1])
            nxt = termCursor.next()

    return result


"""
email in form (operator, email)
"""


def query_email(eml):
    print("email =", eml)
    if eml[0] == "from":
        search = [b"from-"]
    elif eml[0] == 'to':
        search = [b"to-"]
    elif eml[0] == 'cc':
        search = [b"cc-"]
    elif eml[0] == 'bcc':
        search = [b"bcc-"]

    query_output = set()
    result = emailCursor.set(search[0] + eml[1].encode('UTF-8'))
    row_ids = result[1].decode('UTF-8').split(',')
    email_id = row_ids[0]

    query_output.add(email_id.encode())

    dup = emailCursor.next_dup()
    while dup is not None:
        dup_row_ids = dup[1].decode("UTF-8").split(',')
        dup_email_id = dup_row_ids[0]
        query_output.add(dup_email_id.encode())
        dup = emailCursor.next_dup()

    return query_output


def query_date(dte):
    # TODO Make this query fn
    operator = dte[0]
    date = dte[1]

    query_output = set()

    if operator in (":", ">", ">=", "<="):
        result = dateCursor.set(date.encode('UTF-8'))

        while result is not None:
            row_value = result[0].decode('UTF-8').split(',')
            date_value = row_value[0]
            value = result[1].decode('UTF-8').split(',')
            date_id = value[0]

            sd1 = date.split('/')
            sd2 = date_value.split('/')

            #TODO what the fuck
            date1 = datetime.date(sd1[0], sd1[1], sd1[2])
            date2 = datetime.date(sd2[0], sd2[1], sd2[2])

            print(date1, date2)

            if operator == ':':
                if date2 == date1:
                    query_output.add(date_id.encode())

            elif operator is '>':
                if date2 > date1:
                    query_output.add(date_id.encode())

            elif operator is '<':
                if date2 < date1:
                    query_output.add(date_id.encode())

            elif operator == '>=':
                if date2 >= date1:
                    query_output.add(date_id.encode())

            elif operator == '<=':
                if date2 <= date1:
                    query_output.add(date_id.encode())
            else:
                break

            result = dateCursor.next()

    return query_output


def exit():
    termDB.close()
    emailDB.close()
    dateDB.close()
    recDB.close()
