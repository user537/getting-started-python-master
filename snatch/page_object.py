# page_object.py

from selene import browser, by, be, have

class SeleniumPracticePage:
    def __init__(self):
        # Initialize input elements
        self.name_input = browser.element(by.id('name'))
        self.email_input = browser.element(by.id('email'))
        self.mobile_input = browser.element(by.id('mobile'))
        self.subjects_input = browser.element(by.id('subjects'))
        # todo Initialize the address input element using a CSS selector for the placeholder
        # self.address_input = browser.element(by.css_selector('[placeholder="Currend Address"]'))

    def open(self):
        # Open the specified URL
        browser.open('https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php')
        return self

    def set_text_field(self, element, text):
        # Helper method to set text for any input element
        element.should(be.visible).send_keys(text)
        return self

    def verify_text_field_value(self, element, expected_value):
        # Helper method to verify the value of any input element
        element.should(have.value(expected_value))
        return self

    def set_name(self, name):
        # Set the name in the name input field
        self.set_text_field(self.name_input, name)
        # Assert that the name input value is correctly set
        self.verify_text_field_value(self.name_input, name)
        return self

    def set_email(self, email):
        # Set the email in the email input field
        self.set_text_field(self.email_input, email)
        # Assert that the email input value is correctly set
        self.verify_text_field_value(self.email_input, email)
        return self

    def set_mobile(self, mobile):
        # Set the mobile number in the mobile input field
        self.set_text_field(self.mobile_input, mobile)
        # Assert that the mobile input value is correctly set
        self.verify_text_field_value(self.mobile_input, mobile)
        return self

    def set_subjects(self, subjects):
        # Set the subjects in the subjects input field
        self.set_text_field(self.subjects_input, subjects)
        # Assert that the subjects input value is correctly set
        self.verify_text_field_value(self.subjects_input, subjects)
        return self
