from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators import UIElementsLocators as L
from selenium.webdriver.support.ui import Select

class UIElementsPage:
    def __init__(self, driver):
        self.driver = driver

    #Text Field
    def set_text_field(self,text):
        WebDriverWait (self.driver, 10).until(EC.visibility_of_element_located(L.TEXT_FIELD_INPUT)).send_keys(text)
    def get_output_text_field(self):
        return self.driver.find_element(*L.OUTPUT_TEXT_FIELD).text

    #Text Area
    def set_text_area(self,text_area):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(L.TEXT_AREA_INPUT)).send_keys(text_area)
    def get_output_text_area_field(self):
        return self.driver.find_element(*L.OUTPUT_TEXT_AREA_FIELD).text

    #Button Click Me
    def click_button_click_me(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(L.BUTTON_CLICK_ME))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)

        try:
            button.click()
        except Exception:
            # Fallback: clic vía JS si algo (como un anuncio) sigue tapándolo
            self.driver.execute_script("arguments[0].click();", button)

    def get_counter_clic_me(self):
        text = self.driver.find_element(*L.OUTPUT_COUNT_CLIK_ME).text
        return int(text.split()[1])

    # Checkbox
    def click_checkbox_single(self):
        button_checkbox_single=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(L.CHECKBOX_SINGLE))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button_checkbox_single)
        try:
            button_checkbox_single.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", button_checkbox_single)

    def get_output_checkbox_single(self):
        return self.driver.find_element(*L.OUTPUT_CHECKBOX_SINGLE).text

    #Multi Checkbox
    def check_checkbox_option1(self):
        box_checkbox_option1=WebDriverWait (self.driver, 10).until(EC.element_to_be_clickable(L.CHECKBOX_OPTION1))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", box_checkbox_option1)
        try:
            box_checkbox_option1.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", box_checkbox_option1)
    def check_checkbox_option2(self):
        box_checkbox_option2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(L.CHECKBOX_OPTION2))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", box_checkbox_option2)
        try:
            box_checkbox_option2.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", box_checkbox_option2)
    def check_checkbox_option3(self):
        box_checkbox_option3 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(L.CHECKBOX_OPTION3))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", box_checkbox_option3)
        try:
            box_checkbox_option3.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", box_checkbox_option3)
    def get_output_multi_checkbox(self):
        return self.driver.find_element(*L.OUTPUT_MULTICHECK_BOX).text

    #Radio Buttons
    def check_radio_button_R1(self):
        radio_button_R1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(L.RADIO_BUTTON_R1))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio_button_R1)
        try:
            radio_button_R1.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", radio_button_R1)
    def check_radio_button_R2(self):
        radio_button_R2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(L.RADIO_BUTTON_R2))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio_button_R2)
        try:
            radio_button_R2.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", radio_button_R2)
    def check_radio_button_R3(self):
        radio_button_R3 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(L.RADIO_BUTTON_R3))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio_button_R3)
        try:
            radio_button_R3.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", radio_button_R3)
    def get_output_radio_button(self):
        return self.driver.find_element(*L.OUTPUT_RADIO_BUTTONS).text
    def is_radio1_selected(self):
        return self.driver.find_element(*L.RADIO_BUTTON_R1).is_selected()
    def is_radio2_selected(self):
        return self.driver.find_element(*L.RADIO_BUTTON_R2).is_selected()
    def is_radio3_selected(self):
        return self.driver.find_element(*L.RADIO_BUTTON_R3).is_selected()

    #Dropdown
    def select_dropdown_country(self,country):
        dropdown= WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(L.DROPDOWN))
        select = Select (dropdown)
        select.select_by_visible_text(country)
    def get_output_dropdown_country(self):
        return self.driver.find_element(*L.OUTPUT_DROPDOWN).text
