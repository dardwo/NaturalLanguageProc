import re

def find_emails(text):
    # regex ze strony podanej na wykladzie, link:
    # https://blog.polengmt.com/blog/wyrazenia-regularne-czyli-jak-znalezc-wiele-igiel-w-stogu-siana?fbclid=IwAR3blT5xVrjFmkxtbJtk0pCVL28ArzfmCIfsc9BImsaLTjWe6xFgy6ZGUd0
    email_pattern = "\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\\b"
    matches = re.findall(email_pattern, text)
    return matches


with open("data_B04.txt", "r") as data:
    content = data.read()
    matches = find_emails(content)
    print(matches)
