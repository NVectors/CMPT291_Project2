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



def print_results(results):
    if len(results) < 2:
        print(("-" * 35) + "No Records" + ("-" * 35))
        return
    # TODO De-escape data
    if results[0] == 'full':
        full = True
    else:
        full = False


    for result in results[1:]:
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
