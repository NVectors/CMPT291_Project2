# Load each result from stdout into it's apporpriate index
perl break.pl < data/output/1recs.txt | db_load -T -t hash data/output/re.idx
perl break.pl < data/output/1terms.txt | db_load -T -c dupsort=1 -t btree data/output/te.idx
perl break.pl < data/output/1emails.txt | db_load -T -c dupsort=1 -t btree data/output/em.idx
perl break.pl < data/output/1dates.txt | db_load -T -c dupsort=1 -t btree data/output/da.idx
