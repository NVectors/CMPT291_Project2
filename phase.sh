# Run...
# > chmod u+x phase02.sh
# > ./phase02.sh
# Make sure to install: "sudo apt-get install db-util"

# Remove Index database files if they are there
rm data/indexes/te.idx
rm data/indexes/em.idx
rm data/indexes/da.idx
rm data/indexes/re.idx
rm data/indexes/tests/*

# # Create db files
# db_create -T -t hash data.indexes/re.idx
# db_load -c dupsort=1 -T -t btree data/indexes/te.idx
# db_load -c dupsort=1 -T -t btree data/indexes/em.idx
# db_load -c dupsort=1 -T -t btree data/indexes/da.idx

# touch data/indexes/re.idx
# touch data/indexes/te.idx
# touch data/indexes/em.idx
# touch data/indexes/da.idx

for file_name in $(ls data/output/);
  sort -u -o data/output/$ {file_name} data/output/$ {file_name}

# Load each result from stdout into it's apporpriate index
perl break.pl < data/output/recs.txt | db_load -T -t hash data/indexes/re.idx
perl break.pl < data/output/terms.txt | db_load -T -c dupsort=1 -t btree data/indexes/te.idx
perl break.pl < data/output/emails.txt | db_load -T -c dupsort=1 -t btree data/indexes/em.idx
perl break.pl < data/output/dates.txt | db_load -T -c dupsort=1 -t btree data/indexes/da.idx

# Test results of each index, outputted into the tests folder (remove when submitting)
db_dump -p -f data/indexes/tests/re_results.txt data/indexes/re.idx
db_dump -p -f data/indexes/tests/te_results.txt data/indexes/te.idx
db_dump -p -f data/indexes/tests/em_results.txt data/indexes/em.idx
db_dump -p -f data/indexes/tests/da_results.txt data/indexes/da.idx