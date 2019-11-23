"""
Parses Queries.  

"""

NUMBERS = "1234567890"
DATE_CMP = [':', '<', '>', '<=', '>=']]
WHITESPACE = " \t\n"

#ret = [(type, val)]

def is_date_pre(Str):
    if Str[0:4] == 'date':
        cmp_start = None
        for c in range(5, len(Str)):
            if Str[c] not in WHITESPACE:
                cmp_start = c
                break
        if not cmp_start or Str[cmp_start] not in DATE_CMP:
            return None

        cmp_end = cmp_start

        if Str[cmp_start + 1] == '=':
            cmp_end = cmp_start + 1

        return (cmp_start, cmp_end)

    return None


def is_date(Str):
    for c in  Str[0:4]:
        if c not in NUMBERS:
            return None
    
    if Str[4] != '/' or Str[7] != '/':
        return None

    for c in Str[5:7]:
        if c not in NUMBERS:
            return None

    for c in Str[8:10]:
        if c not in NUMBERS:
            return None

    return 10

    return None

def is_date_query(Str):
    dp = is_date_pre(Str)
    if not dp:
         return None

    date_start = None
    for c in range(len(Str)):
        if Str[c] not in WHITESPACE:
            date_start = c
            break
    
    if not date_start or not is_date(date_start):
        return None

    
    val = (Str[dp[0] : dp[1] + 1], Str[date_start : date_start + 11]) # (op, date)

    return (date_start + 10, val)
    

def is_email_term(Str):
    #TODO Figure out WTF alphanumeric+ is
    size = 0
    for c in range(len(Str)):
        if Str[c] != '.' or not Str[c].isalnum():
            break

        if Str[c] == '.' and Str[c + 1] == '.':
            return None

        size += 1

    return size

def is_email(Str):
    p1 = is_email_term(Str)
    if not p1 or Str[p1 + 1] != '@':
        return None

    return p1 + 1 + is_email_term(Str[p1 + 2:])
        



def rec_parse(Str):
    if len(Str) == 0:
        return []

    date = is_date_query(Str)
    if date:
        return ["date", date[1]] + re_parse(Str[date[1] + 1])


    # TODO Add rest of endpoints




    if Str[0].isalnum():
       last = ret[-1]

       if last[0] == "alpha":
           last[1] = last[1] + Str[0]
       else:
           ret.append(("alpha", Str[0]))

        return parse(Str[1:])






