import re

def pig_it(text):
    return re.sub(r'\b(\w)(\w*)\b',r'\2\1ay',text)
