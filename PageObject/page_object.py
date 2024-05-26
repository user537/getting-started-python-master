from selene import browser, by, be, have


class SeleniumPracticePage:
    def __init__(self):
        self.name_input = browser.element(by.id('name'))
        self.email_input = browser.element(by.id('email'))
        self.mobile_input = browser.element(by.id('mobile'))
        self.subjects_input = browser.element(by.id('subjects'))
        self.address_input = browser.element(by.css('[placeholder="Current Address"]'))

    def open(self):
        browser.open('https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php')
        return self

    def set_text_field(self, element, text):
        # Helper method to set text for any input element
        element.should(be.visible).set_value(text)
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

    def set_address(self, address):
        # Set the address in the address input field
        self.set_text_field(self.address_input, address)
        # Assert that the address input value is correctly set
        self.verify_text_field_value(self.address_input, address)
        return self
