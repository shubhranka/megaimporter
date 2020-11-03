from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
f = open("link.txt","r")
lines = f.readlines()
u = []
a = []
for i in range(len(lines)):
    for word in lines[i].split():
        if word == "Link":
            a.append(lines[i].split()[2])
        if word == "Key":
            a.append(lines[i].split()[2])
            u.append(a)
            a = []

for i in u:
    print(i)
driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://mega.nz/")
try:

    login = WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located((By.CLASS_NAME, "top-login-button")) 
        ) 
except():
    pass
login.click()

email = driver.find_element_by_id("login-name")
email.send_keys("email")
passw = driver.find_element_by_id("login-password")
passw.send_keys("pass")
but = driver.find_element_by_class_name("top-dialog-login-button")
but.click()
count = 0
for parts in u:
    link = parts[0]
    passw = parts[1]
    try:
        WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located((By.CLASS_NAME, "megaListItem")) 
        ) 
    except():
        pass
    while(len(driver.find_elements_by_class_name("megaListItem")) <= count):
        continue
    count +=1
    driver.get(link)
    try:
        dec = WebDriverWait(driver, 10).until( 
                EC.presence_of_element_located((By.CLASS_NAME, "fm-dialog-new-folder-input") )
            ) 
    except():
        pass
    # jscr = "document.getElementsByName('dialog-new-folder')[3].value = '{u[0][1]}'"
    jscr = "document.getElementsByName('dialog-new-folder')[3].value='" + passw + "'"
    jscr2 = "document.querySelectorAll('.fm-dialog-new-folder-button')[2].classList.remove('disabled')"
    jscr3 = "document.querySelectorAll('.fm-dialog-new-folder-button')[2].classList.add('active')"
    jscr4 = "document.querySelectorAll('.fm-dialog-new-folder-button')[2].click()"
    driver.execute_script(jscr)
    driver.execute_script(jscr2)
    driver.execute_script(jscr3)
    driver.execute_script(jscr4)
    icon = None
    try:
        icon = WebDriverWait(driver, 10).until( 
                EC.element_to_be_clickable((By.CLASS_NAME, "fm-import-to-cloudrive") )
            ) 
    except():
        pass


    icon.click()
    try:
        icon = WebDriverWait(driver, 10).until( 
                EC.element_to_be_clickable((By.CLASS_NAME, "default-light-green-button") )
            ) 
    except():
        pass
    icon.click()
    print(parts)