from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=').text
soup=BeautifulSoup(html_text,'lxml')
jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')
comp_names=[]
def strip_spaces_and_empty_lines(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)
for job in jobs:
    company_name = job.find('h3', class_='joblist-comp-name').text
    company_name = strip_spaces_and_empty_lines(company_name)
    comp_names.append(company_name)
print(comp_name)