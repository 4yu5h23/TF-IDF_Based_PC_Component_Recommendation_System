from seleniumbase import SB
from bs4 import BeautifulSoup
import csv


def verify_success(sb):
    sb.assert_element('img[alt="PCPartPicker"]', timeout=8)
    sb.sleep(4)


build_links=[]       
for i in range(1, 21):
    with SB(uc_cdp=True, guest_mode=True) as sb:
        sb.open("https://pcpartpicker.com/builds/#c=1495,1401,1505,1504,1503,1525,1508,1527,1510,1465&g=552,553,550,549,542,539&page="+str(i))
        try:
            verify_success(sb)
        except Exception:
            if sb.is_element_visible('input[value*="Verify"]'):
                sb.click('input[value*="Verify"]')
            elif sb.is_element_visible('iframe[title*="challenge"]'):
                sb.switch_to_frame('iframe[title*="challenge"]')
                sb.click("span.mark")
            else:
                raise Exception("Detected!")
            
        html= sb.get_page_source()
        soup=BeautifulSoup(html, 'lxml')
        
        builds=soup.find_all('a', class_='logGroup__target')
        for build in builds:
            build_links.append("www.pcpartpicker.com"+build['href'])


with open('build_links.csv', 'a', newline='') as file: # a=append and w=write
    writer = csv.writer(file)
    writer.writerow(["Build Links"])  # Write header
    for link in build_links:
        writer.writerow([link])


