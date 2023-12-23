import pdfplumber
import json

#scrapes case data


def scrape(path:str): #extract text from pdf file
    with pdfplumber.open(path) as pdf:
        pages = [i.extract_text() for i in pdf.pages]
    final = "\n".join(pages)
    return final

def isNum(inp:str): #checks whether or not value is numerical
    return inp in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")

def sep(datum:str): #seperates a line of text between the school name and cases reported
    i = 0
    while True:
        if isNum(datum[i]):
            final = i
            break
        i += 1
    return i

#date
date = "02-18-22"

export = {}
raw = scrape(f"C:\\Users\\erict\\Desktop\\MCPS COVID\\PDF\\{date}.pdf") #replaces this with whatever path for the INPUT pdf file
data = raw.split("\n")

#this sorts all the data
for i in data:
    if not("Population" in i or "Cases" in i or "CASES" in i or "Daily" in i or "2022" in i or "as of" in i or "Grand Total" in i or "4:00" in i or "Thomas Edison" in i or "School or Office Location Name" in i or "Staff" in i or "Total" in i): #this gets rid of page headers
        center = sep(i)
        school = i[:center-1]
        cases = i[center:].split(" ")
        total = int((cases[-1].replace(",","")).replace("NA","0"))
        if "Technology" in school:
            school = "Thomas Edison High School of Technology"
        export[school] = total
    else:
        pass


with open(f"C:\\Users\\erict\\Desktop\\MCPS COVID\\JSON\\{date}.json", 'w') as fp: #replace this with whatever path for the OUTPUT json file
    json.dump(export, fp)