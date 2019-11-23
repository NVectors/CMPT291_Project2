from bsddb3 import db

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
emailDB = emailDB.cursor()
dateDB = dateDB.cursor()
recDB = recDB.cursor()

iter = termCursor.first()
while (iter):
    print(termCursor.count()) #prints no. of rows that have the same key for the current key-value pair referred by the cursor
    print(iter)

    #iterating through duplicates
    dup = termCursor.next_dup()
    while(dup!=None):
        print(dup)
        dup = termCursor.next_dup()

    iter = termCursor.next()

# Close Databases when done
termDB.close()
emailDB.close()
dateDB.close()
recDB.close()


