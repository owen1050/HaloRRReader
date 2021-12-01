from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://halotracker.com/halo-infinite/leaderboards/csr/all/default?page=5&playlist=3")
driver.execute_script("window.scrollTo(0, 6000)") 
time.sleep(1)

profiles = []

for i in range(1,100):                                                                                                                                       
    name = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/main/div[3]/div[2]/div/div/div[1]/div/table/tbody/tr["+str(i)+"]/td[2]/div/a[1]")
    profiles.append(str(name.get_attribute('href')))

accuracy = []

for link in profiles:

    try:
        driver.get(link)
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(1)
        val = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]")
        n = str(val.text)[:-1]
        accuracy.append(float(n))
        print(n, link)
        ran = True
    except:
        pass
print(accuracy)