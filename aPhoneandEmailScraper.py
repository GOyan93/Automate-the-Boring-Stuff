#! python3

import re, pyperclip


# Create a regex for phone numbers
phone_regex = re.compile(r'''
# 415-555-0000, 555-000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

((\d\d\d)|(\(d\d\d\)))?     # area code (optional)
(\s|-)                      # first separator
\d\d\d                      # first three digits
-                           # separator
\d\d\d\d                    # last for digits
(((ext(\.)?/s)|x)           # extension word-part (optiona;)
(/d{2,5})))?                # extension number part (optional)
''', re.VERBOSE)



# TODO: Create a regex for emails
email_regex = re.compile(r"""


""", re.VERBOSE
# TODO: Get the text off the clipboard
# TODO: Extract the email/phone form this text
# TODO: Copy the extracted email/phone to the clipboard
