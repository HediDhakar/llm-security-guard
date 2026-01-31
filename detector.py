import re

def find_email(text) -> list:
    """
    This function takes a string input and returns a list of all email addresses found in the text.
    An email address is defined as a string that matches the pattern: local-part@domain.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails


test_sentence_1 = "My email is hedi.dhakar@email.com, please contact me."
test_sentence_2 = "This is a clean sentence with no private data."  

print(f"Testing sentence 1: {find_email(test_sentence_1)}") 
print(f"Testing sentence 2: {find_email(test_sentence_2)}")

    