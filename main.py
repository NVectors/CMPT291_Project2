#!/usr/bin/python3

import query


def main():
    while True:
        user_input = input("Query: ").lower()
        if user_input == 'q':
            print("Exiting")
            raise SystemExit

        result = query.query(user_input)
        print(result)





if __name__ == '__main__':
    main()
