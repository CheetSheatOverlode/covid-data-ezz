# MCPS COVID DATA
This project is no longer active!
This is the backend half of a small project I worked on with a friend back in January 2022.
Back then, Montgomery County Public Schools (MCPS) was having a major wave of the COVID-19 virus. 
Officially, they claimed to consider closing down schools when more than 5% of a school's student body was infected.
However, students claimed that they did not honor this announcement.
This repo had python code that scraped the PDF files of daily cases data released by MCPS, converting them to JSON.
My friend HereticSibyl then compiled these JSON files onto a website, showing the number of infections in the last 10 days.
As a result, it was determined that many schools did indeed have large portions of infections, and parents were able to use the website to make an educated decision regarding whether or not to send their children to school.

# Breakdown
The `/PDF` folder contains released data downloaded from the MCPS website in early 2022.
The `/JSON` folder contains that data converted to JSON.
`population.py` compiles the total population of each school into a single JSON file.
`scrape.py` compiles the PDF from the given day, then outputs a corresponding JSON file.
