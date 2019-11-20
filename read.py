#!/usr/bin/env python3

import sys
import re
import xml.etree.ElementTree as ET


def output_terms(file):
    output_file = open("terms.txt", 'w+')

    for mail in file.findall('mail'):  # For every line (child of root element) that starts with the tag <mail>
        # Created boolean var. to check if the elements of the child have non-empty data
        subject_check = False
        body_check = False

        row = mail.find('row').text  # Find the element via the tag 'row'

        subject = mail.find('subj')  # Find the element via the tag 'subj'
        new_subj_list = []
        if subject.text is not None:  # If the element is not empty
            subject_check = True  # Boolean var. is now True
            alist = re.sub(r'[^a-zA-Z0-9-\w]', ' ', subject.text)
            convert = alist.replace('\n', ' ')  # Replace converted special char converted to \n with a space ' '
            subject_list = convert.split(' ')  # Make a list by splitting the text of emails by ' '
            for word in subject_list:
                # \w -> Replace any word character except alphanumeric, underscore and dashed with ''
                stripped_word = re.sub(r'[^a-zA-Z0-9-\w]', '', word)
                if len(stripped_word) > 2:  # Ignored words with length 2 or less
                    new_subj_list.append(stripped_word.lower())  # Add to new list with only what we want

        body = mail.find('body')  # Find the element via the tag 'body'
        new_body_list = []
        if body.text is not None:  # If the element is not empty
            body_check = True  # Boolean var. is now True
            alist2 = re.sub(r'[^a-zA-Z0-9-\w]', ' ', body.text)
            convert2 = alist2.replace('\n', ' ')  # Replace converted special char converted to \n with a space ' '
            body_list = convert2.split(' ')  # Make a list by splitting the text of emails by ' '
            for word in body_list:
                # \w -> Replace any word character except alphanumeric, underscore and dashed with ''
                reduced_word = re.sub(r'[^a-zA-Z0-9-\w]', '', word)
                if len(reduced_word) > 2:  # Ignored words with length 2 or less
                    new_body_list.append(reduced_word.lower())  # Add to new list with only what we want

        # Write out the subject info first word by word each on a new line, example: s-special:13 as form (s-word:row#)
        if subject_check is True:  # Element is not empty
            if len(new_subj_list) > 0:  # If the list of words is greater than 0
                for word in new_subj_list:  # Go through the list and print each word out in the form above
                    output_file.write("{}".format(subject.tag[0] + "-" + word + ":" + row + "\n"))
    
        # Write out the body info next word by word each on a new line, example: b-good:11 as form (b-word:row#)
        if body_check is True:  # Element is not empty
            if len(new_body_list) > 0:  # If the list of words is greater than 0
                for word in new_body_list:  # Go through the list and print each email out in the form above
                    output_file.write("{}".format(body.tag[0] + "-" + word + ":" + row + "\n"))

    output_file.close()


def output_emails(input_file):
    output_file = open("emails.txt", 'w+')  # Open a new file which we will write to

    for mail in input_file.findall('mail'):  # For every line (child of root element) that starts with the tag <mail>
        # Created boolean var. to check if the elements of the child have non-empty data
        receiver_check = False
        cc_check = False
        bcc_check = False

        row = mail.find('row').text  # Find the element via the tag 'row'
        sender = mail.find('from')  # Find the element via the tag 'from'

        receiver = mail.find('to')  # Find the element via the tag 'to'
        if receiver.text is not None:  # If the element is not empty
            receiver_check = True  # Boolean var. is now True
            receiver_list = receiver.text.split(',')  # Make a list by splitting the text of emails by ','

        cc = mail.find('cc')  # Find the element via the tag 'cc'
        if cc.text is not None:  # If the element is not empty
            cc_check = True  # Boolean var. is now True
            cc_list = cc.text.split(',')  # Make a list by splitting the text of emails by ','

        bcc = mail.find('bcc')  # Find the element via the tag 'bcc'
        if bcc.text is not None:  # If the element is not empty
            bcc_check = True  # Boolean var. is now True
            bcc_list = bcc.text.split(',')  # Make a list by splitting the text of emails by ','

        # Write out the sender info first, example: from-critical.notice@enron.com:44 as form (tag-email:row#)
        output_file.write("{}".format("" if sender.text is None else (sender.tag + "-" + sender.text + ":" + row + "\n")))

        # Write out the receiver info next, example: to-ywang@enron.com:44 as form (tag-email:row#)
        if receiver_check is True:  # Element is not empty
            if len(receiver_list) > 0:  # If the list of emails is greater than 0
                for email in receiver_list:  # Go through the list and print each email out in the form above
                    output_file.write("{}".format(receiver.tag + "-" + email + ":" + row + "\n"))

        # Write out the cc info next, example: cc-alb@cpuc.ca.gov:13 as form (tag-email:row#)
        if cc_check is True:  # Element is not empty
            if len(cc_list) > 0:  # If the list of emails is greater than 1
                for email in cc_list:  # Go through the list and print each email out in the form above
                    output_file.write("{}".format(cc.tag + "-" + email + ":" + row + "\n"))

        # Write out the bcc info next, example: bcc-alb@cpuc.ca.gov:13 as form (tag-email:row#)
        if bcc_check is True:  # Element is not empty
            if len(bcc_list) > 0:  # If the list of emails is greater than 1
                for email in bcc_list:  # Go through the list and print each email out in the form above
                    output_file.write("{}".format(bcc.tag + "-" + email + ":" + row + "\n"))

    output_file.close()  # Close the output file once we're done writing and reading to it


def output_dates(file):
    output_file = open("dates.txt", 'w+')  # Open a new file which we will write to

    for mail in file.findall('mail'):  # For every line (child of root element) that starts with the tag <mail>
        row = mail.find('row').text  # Find the element via the tag 'row' and convert it to text
        date = mail.find('date').text  # Find the element via the tag 'date' and convert it to test
        output_file.write("{}:{}\n".format(date, row))

    output_file.close()  # Close the output file once we're done writing and reading to it


def output_recs(file, doc):
    output_file = open("recs.txt", 'w+')  # Open a new file which we will write to

    for mail in file.findall('mail'):  # For every line (child of root element) that starts with the tag <mail>
        row = mail.find('row').text  # Find the element via the tag 'row' and convert it to text

        line = ET.tostring(mail, encoding='UTF-8', method="xml")

        output_file.write("{}:{}\n".format(row, line))

    output_file.close()


def main():
    file_name = ''  # File Name is blank for now
    if len(sys.argv) == 2:
        try:
            file_name = sys.argv[1]  # File name is set to command line argument given by user
            file = open(file_name, 'r')  # Open file with file name given by user as a command line argument

            doc = ET.parse(file.name)
            root = doc.getroot()

            output_terms(root)
            output_emails(root)
            output_dates(root)
            output_recs(root, doc)

            file.close()
        except(FileNotFoundError, IOError):
            print("Wrong file or file path")
    else:
        print("Invalid format, type: 'python read.py xml_file_name'")  # No data file is given by user via command line argument


if __name__ == "__main__":
    main()
