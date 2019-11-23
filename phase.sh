# Run...
# > chmod u+x phase02.sh
# > ./phase02.sh

# make sure to install: "sudo apt-get install db-util"

# Remove db files if they are there
rm data/indexes/re.idx
rm data/indexes/te.idx
rm data/indexes/em.idx
rm data/indexes/da.idx
rm data/indexes/test/*

# Create db files
# db_create -T -t hash data.indexes/re.idx
# db_load -c dupsort=1 -T -t btree data/indexes/te.idx
# db_load -c dupsort=1 -T -t btree data/indexes/em.idx
# db_load -c dupsort=1 -T -t btree data/indexes/da.idx

# touch data/indexes/re.idx
# touch data/indexes/te.idx
# touch data/indexes/em.idx
# touch data/indexes/da.idx


sort -u -o data/output/$ recs.txt > data/output/$ recs.txt
sort -u -o data/output/$ terms.txt > data/output/$ terms.txt
sort -u -o data/output/$ emails.txt > data/output/$ emails.txt
sort -u -o data/output/$ dates.txt > data/output/$ dates.txt


# Load each result from stdout into it's apporpriate index
perl break.pl < data/output/recs.txt | db_load -T -t hash data/indexes/re.idx
perl break.pl < data/output/terms.txt | db_load -T -c dupsort=1 -t btree data/indexes/te.idx
perl break.pl < data/output/emails.txt | db_load -T -c dupsort=1 -t btree data/indexes/em.idx
perl break.pl < data/output/dates.txt | db_load -T -c dupsort=1 -t btree data/indexes/da.idx

# Test results of each index, outputted into the tests folder (remove when submitting)
db_dump -p -f data/indexes/test/ad_res.txt data/indexes/re.idx
db_dump -p -f data/indexes/test/tm_res.txt data/indexes/te.idx
db_dump -p -f data/indexes/test/da_res.txt data/indexes/em.idx
db_dump -p -f data/indexes/test/pr_res.txt data/indexes/da.idx