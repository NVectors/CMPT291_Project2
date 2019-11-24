"""
Parses Queries.  

Query Grammer (taken from eclass):


    alphanumeric    ::= [0-9a-zA-Z_-]
    numeric		::= [0-9]
    date            ::= numeric numeric numeric numeric '/' numeric numeric '/' numeric numeric
    datePrefix      ::= 'date' whitespace* (':' | '>' | '<' | '>=' | '<=')
    dateQuery       ::= datePrefix whitespace* date
    emailterm	::= alphanumeric+ | alphanumeric+ '.' emailterm
    email		::= emailterm '@' emailterm
    emailPrefix	::= (from | to | cc | bcc) whitespace* ':'
    emailQuery	::= emailPrefix whitespace* email
    term            ::= alphanumeric+
    termPrefix	::= (subj | body) whitespace* ':'
    termSuffix      ::= '%' 
    termQuery       ::= termPrefix? whitespace* term termSuffix?
    
    expression      ::= dateQuery | emailQuery | termQuery 
    query           ::= expression (whitespace expression)*
    
    modeChange	::= 'output=full' | 'output=brief'
    
    command		::= query | modeChange

"""

NUMBERS = "1234567890"
DATE_CMP = [':', '<', '>', '<=', '>=']
WHITESPACE = " \t\n"
EMAIL_PRE = ["from", "to", "cc", "bcc"]


"""
Desc    : Checks if String is a date prefix.
returns : None | (index of operator start, index of operator end)
"""
def is_date_pre(Str):
    if Str[0:4] == 'date':
        cmp_start = None
        for c in range(4, len(Str)):
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


"""
Desc    : Checks if string is a date
returns : None | index of last char of date
"""
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

    return 9

    return None


"""
Desc    : Checks if string is a date query
returns : None | (index of last char in date, (operator, date))
"""
def is_date_query(Str):
    dp = is_date_pre(Str)
    if not dp:
         return None

    date_start = None
    for c in range(dp[1] + 1, len(Str)):
        if Str[c] not in WHITESPACE:
            date_start = c
            break
    
    if not date_start or not is_date(Str[date_start :]):
        return None

    
    val = (Str[dp[0] : dp[1] + 1], Str[date_start : date_start + 11]) # (op, date)

    return (date_start + 9, val)
    

"""
Desc    : Checks if Str is an email term
returns : None | index of last char in email term
"""
def is_email_term(Str):
    #TODO Figure out WTF alphanumeric+ is
    size = 0
    for c in range(len(Str)):
        if Str[c] != '.' and not Str[c].isalnum():
            break

        if Str[c] == '.' and Str[c + 1] == '.':
            return None

        size += 1

    if size == 0:
        return None

    return size -1 


"""
Desc    : Checks if Str is an email
returns : None | index of last char in email
"""
def is_email(Str):
    p1 = is_email_term(Str)
    if not p1 or Str[p1 + 1] != '@':
        return None
    p2 = is_email_term(Str[p1 + 2:])
    if not p2:
        return None

    return p1 + 1 + p2 + 1


"""
Desc    : Checks if Str is an email prefix
returns : None | (operator, index of last char in prefix)
"""
def is_email_pre(Str):
    start = None
    end = None
    for i in range(2, 5):
        if Str[0:i] in EMAIL_PRE:
            start = i

    if not start:
        return None

    for c in range(start, len(Str)):
        if Str[c] not in WHITESPACE and Str[c] != ':':
            break
        if Str[c] == ':':
            end = c
            break

    if not end:
        return None

    return(Str[0:start], end)


"""
Desc    : Checks if Str is an email query.
returns : None | (index of last char in email, (operator, email))
"""
def is_email_query(Str):
    pre = is_email_pre(Str)
    if not pre:
        return None
    eml_start = None
    for c in range(pre[1] + 1, len(Str)):
        if Str[c] not in WHITESPACE:
            eml_start = c
            break

    if not eml_start:
        return None

    eml_end = is_email(Str[eml_start :])
    if not eml_end:
        return None

    return (eml_start + eml_end, (pre[0], Str[eml_start : eml_end + 1]))


"""
Desc    : Recurrsively parse a string, getting nessesary info to perform a query
returns : [(query_type, val), ...]
"""
def rec_parse(Str):
    print("len =", len(Str))
    print("str =", Str)
    if len(Str) == 0:
        return []

    date = is_date_query(Str)
    if date:
        return [("date", date[1])] + rec_parse(Str[date[0] + 1 :])


    email = is_email_query(Str)
    if email:
        print(email[0])
        return [("email", email[1])] + rec_parse(Str[email[0] + 1 :])

    if Str[0] in WHITESPACE:
        return rec_parse(Str[1:])


print(is_date_query("date>2001/03/10"))


