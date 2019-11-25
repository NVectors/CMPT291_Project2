#!/bin/bash
rm -f data/indexes/re.idx
rm -f data/indexes/te.idx
rm -f data/indexes/em.idx
rm -f data/indexes/da.idx
rm -f data/indexes/test/*


for f in "recs.txt" "terms.txt" "emails.txt" "dates.txt"
do
    if [ ! -e "data/output/$f" ]; then
        printf "Output files not found!\nRun python3 read.py <XML file> first\n"
        exit 1
    fi
done

#Use Linux sort command to sort output files
sort -u -o data/output/recs.txt data/output/recs.txt
sort -u -o data/output/terms.txt data/output/terms.txt
sort -u -o data/output/emails.txt data/output/emails.txt
sort -u -o data/output/dates.txt data/output/dates.txt

# Load each output file into it's apporpriate index file after we run break.pl on the output file
perl break.pl < data/output/recs.txt | db_load -c dupsort=1 -T -t hash data/indexes/re.idx
perl break.pl < data/output/terms.txt | db_load -c dupsort=1 -T -t btree data/indexes/te.idx
perl break.pl < data/output/emails.txt | db_load -c dupsort=1 -T -t btree data/indexes/em.idx
perl break.pl < data/output/dates.txt | db_load -c dupsort=1 -T -t btree data/indexes/da.idx

# Test results of each index, outputted into the tests folder (remove when submitting)
#db_dump -p -f data/indexes/test/re_results.txt data/indexes/re.idx
#db_dump -p -f data/indexes/test/te_results.txt data/indexes/te.idx
#db_dump -p -f data/indexes/test/em_results.txt data/indexes/em.idx
#db_dump -p -f data/indexes/test/da_results.txt data/indexes/da.idx
