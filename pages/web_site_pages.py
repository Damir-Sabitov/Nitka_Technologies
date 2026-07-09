from dataclasses import dataclass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver


@dataclass
class WebsitePage:
    driver: object

    def click_contact_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH,"//*[contains(@class, 'rounded-full') and text()='Contact']"))).click()

    def set_up_managed_services(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//button[text()='Set up managed services (NOC, QA, support)']"))).click()


    def click_continue_button(self):
        element=WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,"//button[text()='Continue']")))

        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def choose_application_engeenering(self):
        element=WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,"//button[text()='Application engineering']")))

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        element.click()


    def choose_team_members(self):
        element=WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,"//button[text()='1–3 engineers']")))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        element.click()

    def start_event(self):
        element=WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,"//button[text()='Within a month']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        element.click()


    def find_elements(self):
        fields=self.driver.find_elements(By.XPATH,"//*[@class='grid gap-5']//label")
        texts=[fields.text for fields in fields]
        texts=[texts.replace("*"," ").replace("?"," ").strip() for texts in texts]
        return texts



