import os
from selenium import webdriver # инициализация драйвера
from webdriver_manager.chrome import ChromeDriverManager # инициализация драйвера Chrome из webdriver.manager
from selenium.webdriver.chrome.service import Service # импорт класса Service (открытие/закрытие браузера)
from selenium.webdriver.support.ui import WebDriverWait # импорт класса ожиданий
from selenium.webdriver.support import expected_conditions as EC # импорт класса явных ожиданий
from selenium.webdriver.support.select import Select # импорт класса Select для работы с селекторами (старая реализация)
from selenium.webdriver.common.action_chains import ActionChains # импорт класса ActionsChains цепочки действий
from scrolls import Scrolls # импорт класса Scrolls из файла scroll.py для управления прокрутки страницы

# опции браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

# объекты
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)
action = ActionChains(driver)
scrolls = Scrolls(driver, action)

# локаторы
FIRST_NAME_FIELD = ("xpath", "//input[@placeholder='First Name']")
LAST_NAME_FIELD = ("xpath", "//input[@placeholder='Last Name']")
EMAIL_FIELD = ("xpath", "//input[@type='email']")
PHONE_FIELD = ("xpath", "//input[@type='tel']")
PASSWORD_FIELD = ("xpath", "//input[@id='firstpassword']")
PASSWORD_CONFIRM_FIELD = ("xpath", "//input[@id='secondpassword']")
COUNTRY_FIELD = ("xpath", "//select[@id='country']")
YEAR_FIELD = ("xpath", "//select[@id='yearbox']")
MONTH_FIELD = ("xpath", "//select[@placeholder='Month']")
DAY_FIELD = ("xpath", "//select[@id='daybox']")
UPLOAD_FIELD = ("xpath", "//input[@id='imagesrc']")
SUBMIT_BUTTON = ("xpath", "//button[@id='submitbtn']")

BASE_URL = "https://demo.automationtesting.in/Register.html"

# открытие страницы
driver.get(BASE_URL)

url = driver.current_url
assert url == "https://demo.automationtesting.in/Register.html", "URL страницы, на которой вы находитесь не верный"

wait.until(EC.element_to_be_clickable(FIRST_NAME_FIELD)).send_keys("Sasha")
driver.find_element(*LAST_NAME_FIELD).send_keys("Averin")
driver.find_element(*EMAIL_FIELD).send_keys("test.mail@gmail.com")
driver.find_element(*PHONE_FIELD).send_keys("9960753970")
driver.find_element(*PASSWORD_FIELD).send_keys("Nimbus2000")
driver.find_element(*PASSWORD_CONFIRM_FIELD).send_keys("Nimbus2000")
country = Select(driver.find_element(*COUNTRY_FIELD))
country.select_by_visible_text("Japan")
year_of_birth = Select(driver.find_element(*YEAR_FIELD))
year_of_birth.select_by_visible_text("1996")
month_of_birth = Select(driver.find_element(*MONTH_FIELD))
month_of_birth.select_by_value("January")
day_of_birth = Select(driver.find_element(*DAY_FIELD))
day_of_birth.select_by_index(15)
driver.find_element(*UPLOAD_FIELD).send_keys(f"{os.getcwd()}/avatar.png")
driver.execute_script("window.scrollTo(0, 300);")
driver.find_element(*SUBMIT_BUTTON).click()

