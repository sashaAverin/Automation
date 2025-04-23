from selenium import webdriver # инициализация драйвера
from webdriver_manager.chrome import ChromeDriverManager # инициализация драйвера Chrome из webdriver.manager
from selenium.webdriver.chrome.service import Service # импорт класса Service (открытие/закрытие браузера)
from selenium.webdriver.support.ui import WebDriverWait # импорт класса ожиданий
from selenium.webdriver.support import expected_conditions as EC # импорт класса явных ожиданий

# опции браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

# объекты
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

# открытие страницы
driver.get("https://demo.automationtesting.in/WebTable.html")

# локаторы
SWITCH_TO = ("xpath", "//a[text()='SwitchTo']")
ALERT_LINK = ("xpath", "//a[text()='Alerts']")
ALERT_CANCEL_LINK = ("xpath", "//a[text()='Alert with OK & Cancel ']")
ALERT_CALL_BUTTON = ("xpath", "//button[contains(@class, 'btn-danger')]")
ALERT_CANCEL_CALL_BUTTON = ("xpath", "//button[contains(@class, 'btn-primary')]")
ALERT_TEXT_LINK = ("xpath", "//a[text()='Alert with Textbox ']")
ALERT_TEXT_CALL_BUTTON = ("xpath", "//button[contains(@class, 'btn-info')]")

wait.until(EC.element_to_be_clickable(SWITCH_TO)).click()
wait.until(EC.element_to_be_clickable(ALERT_LINK)).click()
wait.until(EC.element_to_be_clickable(ALERT_CALL_BUTTON)).click()

alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
alert.text
if alert.text == "I am an alert box!":
    print("С текстом окна всё в порядке")
else:
    print("С текстом в окне что-то не так")
alert.accept()

url = driver.current_url
driver.switch_to.new_window("tab")
driver.get(url)

wait.until(EC.element_to_be_clickable(ALERT_CANCEL_LINK)).click()
wait.until(EC.element_to_be_clickable(ALERT_CANCEL_CALL_BUTTON)).click()
alert.dismiss()

driver.switch_to.new_window("tab")
driver.get(url)

wait.until(EC.element_to_be_clickable(ALERT_TEXT_LINK)).click()
wait.until(EC.element_to_be_clickable(ALERT_TEXT_CALL_BUTTON)).click()
alert.send_keys("Ура! Задание выполнено!")
alert.accept()
