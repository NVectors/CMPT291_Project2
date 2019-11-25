#!/usr/bin/python3

import query
import re
import time

OUTPUT = 'brief'


def main():
    while True:
        user_input = input("Query: ").lower()
        if user_input == 'q' or user_input == 'exit':
            print("Exiting")
            # time.sleep(3) # if you want the user to see the words exit before the terminal closes
            query.exit()
            raise SystemExit

        user_input = user_input.replace(" ", '') # leave this in, just in case the equivalent stops working in the parser
        results = query.query(user_input)
        print_results(results)


def print_results(results):
    global OUTPUT

    if 'full' in results:
        OUTPUT = 'full'
    if 'brief' in results:
        OUTPUT = 'brief'

    full = OUTPUT == 'full'
    if len(results) < 2:
        print(("-" * 35) + "No Records" + ("-" * 35))
        return



    for result in results:
        if result == 'full' or result == 'brief':
            continue

        print("-" * 80)

        try:
            print("Row ID =", re.findall('<row>(.*)</row>', result)[0])
        except:
            pass
        try:
            print("Subject =", re.findall('<subj>(.*)</subj>', result)[0])
        except:
            pass
        if full:
            try:
                print("Date =", re.findall('<date>(.*)</date>', result)[0])
            except:
                pass
            try:
                print("From =", re.findall('<from>(.*)</from>', result)[0])
            except:
                pass
            try:
                print("To =", re.findall('<to>(.*)</to>', result)[0])
            except:
                pass
            try:
                print("cc =", re.findall('<cc>(.*)</c>', result)[0])
            except:
                pass
            try:
                print("bcc =", re.findall('<bcc>(.*)</bcc>', result)[0])
            except:
                pass
            try:
                print("Body =", re.findall('<body>(.*)</body>', result)[0])
            except:
                pass

    print("-" * 80)


if __name__ == '__main__':
    main()
