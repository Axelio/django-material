from selenium.webdriver.common.keys import Keys

from tests.integration.tests.test_fileinput import Test as TestFileInput
from . import VisualTest


class Test(VisualTest):
    urls = TestFileInput.urls

    def test_test_default_usecase(self):
        self.driver.get('%s%s' % (self.live_server_url, TestFileInput.test_default_usecase.url))
        self.assertScreenshot('form', 'fileinput_default_usecase', threshold=1)

    def test_invalid_value(self):
        self.driver.get('%s%s' % (self.live_server_url, TestFileInput.test_invalid_value.url))
        self.driver.find_element_by_css_selector("button").send_keys(Keys.RETURN)
        self.assertScreenshot('form', 'fileinput_missing_value_error', threshold=1)

    def test_part_group_class(self):
        self.driver.get('%s%s' % (self.live_server_url, TestFileInput.test_part_group_class.url))
        self.assertScreenshot('form', 'fileinput_part_group_class', threshold=1)

    def test_part_add_group_class(self):
        self.driver.get('%s%s' % (self.live_server_url, TestFileInput.test_part_add_group_class.url))
        self.assertScreenshot('form', 'fileinput_part_add_group_class', threshold=1)

    def test_part_prefix(self):
        self.driver.get('%s%s' % (self.live_server_url, TestFileInput.test_part_prefix.url))
        self.assertScreenshot('form', 'fileinput_part_prefix', threshold=1)

    def test_part_add_control_class(self):
        self.driver.get('%s%s' % (self.live_server_url, TestFileInput.test_part_add_control_class.url))
        self.driver.find_element_by_css_selector("#id_test_field_container label").click()
        self.assertScreenshot('form', 'fileinput_part_add_control_class', threshold=1)

    def test_part_label(self):
        self.driver.get('%s%s' % (self.live_server_url, TestFileInput.test_part_label.url))
        self.assertScreenshot('form', 'fileinput_part_label', threshold=1)

    def test_part_add_label_class(self):
        self.driver.get('%s%s' % (self.live_server_url, TestFileInput.test_part_add_label_class.url))
        self.assertScreenshot('form', 'fileinput_part_add_label_class', threshold=1)

    def test_part_help_text(self):
        self.driver.get('%s%s' % (self.live_server_url, TestFileInput.test_part_help_text.url))
        self.assertScreenshot('form', 'fileinput_part_help_text', threshold=1)

    def test_part_errors(self):
        self.driver.get('%s%s' % (self.live_server_url, TestFileInput.test_part_errors.url))
        self.assertScreenshot('form', 'fileinput_part_errors', threshold=1)
