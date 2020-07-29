import re
email_regex = r"[\w.]+@\w+\.\w+"

def is_correct_email(email):
    match = re.fullmatch(email_regex, email)
    if match != None:
        return True
    else:
        return False