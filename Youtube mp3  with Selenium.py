from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

document = []
mylist = []
options = webdriver.ChromeOptions()
options.add_argument("headless")
serv = Service(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver = webdriver.Chrome(service= serv, options=options)
driver.get('https://www.youtube.com/results?search_query=' + input('Cantor(a): ') + input('Música: ').title().strip())
search_youtube = driver.find_element(By.ID, "search-icon-legacy").click()
links = driver.find_elements(By.XPATH, "//a[@href]")


for l in links:
    mylist.append(l.get_attribute('href'))
    for m in mylist:
        replace_link = m.replace("https://www.youtube", "https://www.yout")
        if len(replace_link) == 40:
            document.append(replace_link)
            print(replace_link)
        else:
            pass

sleep(4)
driver2 = webdriver.Chrome(service= serv)
driver2.get(document[0])
sleep(5)
download = driver2.find_element(By.CLASS_NAME, "recorder-type").click()
sleep(50)

