from selenium import webdriver
from Pages_Objects import UIElementsPage as PO

URL="https://www.qapractice.com/practice-different-ui-elements"
INPUT="Test 1"
INPUT2= "Second Test, testing Text Area"

class TestUIElementsPage:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_set_text_field_input(self):
        self.driver.get(URL)
        text_field = INPUT
        page = PO(self.driver)
        page.set_text_field(text_field)
        assert page.get_output_text_field() == text_field

    def test_set_text_area_field_input(self):
        self.driver.get(URL)
        text_area = INPUT2
        page = PO(self.driver)
        page.set_text_area(text_area)
        assert page.get_output_text_area_field() == text_area

    def test_click_button_click_me(self):
        self.driver.get(URL)
        page = PO(self.driver)
        counter = page.get_counter_clic_me()
        page.click_button_click_me()
        page.click_button_click_me()
        page.click_button_click_me()
        counter = 3
        assert page.get_counter_clic_me() == counter

    def test_click_checkbox_single(self):
        self.driver.get(URL)
        page = PO(self.driver)
        page.click_checkbox_single()
        assert page.get_output_checkbox_single() == "Checked"

    def test_click_checkbox_multiple(self):
        self.driver.get(URL)
        page = PO(self.driver)
        page.check_checkbox_option1()
        page.check_checkbox_option3()
        assert page.get_output_checkbox_single() == "option1,option3"

    def test_click_radio_button(self):
        self.driver.get(URL)
        page = PO(self.driver)
        page.check_radio_button_R1()
        assert page.get_output_radio_button() == "Radio 1"
        page.check_radio_button_R2()
        assert page.get_output_radio_button() == "Radio 2"
        assert page.is_radio1_selected() is False
        assert page.is_radio2_selected() is True
        page.check_radio_button_R3()
        assert page.get_output_radio_button() == "Radio 3"
        assert page.is_radio1_selected() is False
        assert page.is_radio2_selected() is False
        assert page.is_radio3_selected() is True

    def test_select_dropdown(self):
         self.driver.get(URL)
         page = PO(self.driver)
         page.select_dropdown_country("Canada")
         assert page.get_output_dropdown_country() == "Canada"
         page.select_dropdown_country("UK")
         assert page.get_output_dropdown_country() == "UK"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()