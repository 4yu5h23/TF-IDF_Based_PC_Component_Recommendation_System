from seleniumbase import SB
from bs4 import BeautifulSoup
import csv
import tkinter as tk
import threading


stop_flag = False

def stop():
    global stop_flag
    stop_flag = True

def create_window():
    window = tk.Tk()
    button = tk.Button(window, text="Stop", command=stop)
    button.pack()
    window.mainloop()

threading.Thread(target=create_window).start()

def verify_success(sb):
    sb.assert_element('img[alt="PCPartPicker"]', timeout=8)
    sb.sleep(4)

    # Read the links from build_links.csv and store them in a list named 'build_links'
build_links = []
with open('missedlinksrun.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        build_links.append(row[0])

def removeprice(text):    
    text=text.replace("\n","").replace("$"," ")
    text=text.split(" ")
    text.pop(-1)
    text = " ".join(text)
    return text

print("links imported")
print(len(build_links))
for link in build_links:
    if stop_flag:
        print("Stopping...")
        break
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
        try:
            html = sb.get_page_source()
            soup = BeautifulSoup(html, 'lxml')

            partslist = soup.find('tbody')
            build1 = []
            parts = partslist.find_all('tr')
            pl=len(parts)
            for i in range(0,pl,2):
                    if parts[i].find('td', class_='td__component').find('h4').text == "CPU":
                        cpu=removeprice(parts[i+1].find('td', class_='td__name').text)

                    elif parts[i].find('td', class_='td__component').find('h4').text == "Motherboard":
                        motherboard=removeprice(parts[i+1].find('td', class_='td__name').text)
                    
                    elif parts[i].find('td', class_='td__component').find('h4').text == "Memory":
                        ram=removeprice(parts[i+1].find('td', class_='td__name').text)
                    
                    elif parts[i].find('td', class_='td__component').find('h4').text == "Video Card":
                        gpu=removeprice(parts[i+1].find('td', class_='td__name').text)
                    
                    elif parts[i].find('td', class_='td__component').find('h4').text == "Power Supply":
                        psu=removeprice(parts[i+1].find('td', class_='td__name').text)
                    
            build=[build_links.index(link)+1,link,cpu,motherboard,ram,gpu,psu]
            with open('builds.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(build)
            print(build_links.index(link)+1," Done")
        except Exception:
            with open('missedlinks.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([build_links.index(link)+1,link])
            print("Error Occured on link number ",build_links.index(link)+1)
            continue

print("Ended")
        
    