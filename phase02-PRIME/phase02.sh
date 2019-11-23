# Run...
# > chmod u+x phase02.sh
# > ./phase02.sh

# make sure to install: "sudo apt-get install db-util"



# Remove db files if they are there
#rm data/output/re.idx
#rm data/output/te.idx
#rm data/output/em.idx
#rm data/output/da.idx

# Create db files
# db_create -T -t hash data.indexes/ad.idx
# db_load -c dupsort=1 -T -t btree data/indexes/tm.idx
# db_load -c dupsort=1 -T -t btree data/indexes/da.idx
# db_load -c dupsort=1 -T -t btree data/indexes/pr.idx

# touch data/indexes/ad.idx
# touch data/indexes/tm.idx
# touch data/indexes/da.idx
# touch data/indexes/pr.idx


sort -u data/input/10-recs.txt > data/output/recs.txt
sort -u data/input/10-terms.txt > data/output/terms.txt
sort -u data/input/10-emails.txt > data/output/emails.txt
sort -u data/input/10-dates.txt > data/output/dates.txt


# Load each result from stdout into it's apporpriate index
perl break.pl < data/output/1recs.txt | db_load -T -t hash data/output/re.idx
perl break.pl < data/output/1terms.txt | db_load -T -c dupsort=1 -t btree data/output/te.idx
perl break.pl < data/output/1emails.txt | db_load -T -c dupsort=1 -t btree data/output/em.idx
perl break.pl < data/output/1dates.txt | db_load -T -c dupsort=1 -t btree data/output/da.idx

