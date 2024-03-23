from seleniumbase import SB
from bs4 import BeautifulSoup
import csv

def verify_success(sb):
    sb.assert_element('img[alt="PCPartPicker"]', timeout=8)
    sb.sleep(4)

    # Read the links from build_links.csv and store them in a list named 'build_links'
build_links = []
with open('build_links.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        build_links.append(row[0])

print("links imported")

for link in build_links[1:6]:
    with SB(uc_cdp=True, guest_mode=True) as sb:
            sb.open(link)
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