#!/usr/bin/python3

import query


def main():
    while True:
        nput = input("Query: ").lower()
        if nput == 'q':
            print("Exiting")
            raise SystemExit

        result = query.query(nput)
        print(result)





if __name__ == '__main__':
    main()
