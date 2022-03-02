import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.expected_conditions import presence_of_element_located

options = Options()
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")
options.add_argument("--log-level=1")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

path = "D:\Drive\Famille\Schell\Gaby\For fun\Code\Projects\Python\PayementAway\chromedriver\chromedriver.exe"
data = json.load(open('./token.json'))
"""for i in data:
    print(i, data[i])"""

URL = 'https://www.abritel.fr/p/home'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 60)

# Connection to Abritel
driver.get(URL)
wait.until(presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[3]/div/div[1]/div/div/div[2]/div/form/div[1]/div/input')))
driver.find_element(By.XPATH, '/html/body/div/div/div/div[3]/div/div[1]/div/div/div[2]/div/form/div[1]/div/input').send_keys(data["user"])
driver.find_element(By.XPATH, '/html/body/div/div/div/div[3]/div/div[1]/div/div/div[2]/div/form/div[2]/div[1]/input').send_keys(data["password"])
driver.find_element(By.XPATH, '/html/body/div/div/div/div[3]/div/div[1]/div/div/div[2]/div/form/div[2]/button').click()

# Going to reservation list
wait.until(presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/nav/div[2]/div/div[2]/div[5]/div[3]/div/div[1]/a')))
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/nav/div[2]/div/div[2]/div[5]/div[3]/div/div[1]/a').click()
wait.until(presence_of_element_located((By.XPATH, '/html/body/div[2]/section/div/div/div[2]/div[3]/table/tbody/tr[1]/td[4]/a/ul/li[1]')))
