#!/usr/bin/python3

import query
import re

def main():

    while True:
        user_input = input("Query: ").lower()
        if user_input == 'q':
            print("Exiting")
            raise SystemExit

        results = query.query(user_input)
        #result = query.test(nput)
        print_results(results)
    query.exit()



def print_results(results):
    if len(results) < 2:
        print(("-" * 35) + "No Records" + ("-" * 35))
        return
    # TODO De-escape data
    full = 'full' in results


    for result in results:
        if result == 'full' or result == 'brief':
            continue

        print("-" * 80)

        try: print("Row ID =",  re.findall('<row>(.*)</row>', result)[0])
        except: pass
        try: print("Subject =", re.findall('<subj>(.*)</subj>', result)[0])
        except: pass
        if full:
            try: print("Date =", re.findall('<date>(.*)</date>', result)[0])
            except: pass
            try: print("From =", re.findall('<from>(.*)</from>', result)[0])
            except: pass
            try: print("To =", re.findall('<to>(.*)</to>', result)[0])
            except: pass
            try: print("cc =", re.findall('<cc>(.*)</c>', result)[0])
            except: pass
            try: print("bcc =", re.findall('<bcc>(.*)</bcc>', result)[0])
            except: pass
            try: print("Body =", re.findall('<body>(.*)</body>', result)[0])
            except: pass
    
    print("-" * 80)

if __name__ == '__main__':
    main()
