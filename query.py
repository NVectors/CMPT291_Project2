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


# Close Databases when done
termDB.close()
emailDB.close()
dateDB.close()
recDB.close()


