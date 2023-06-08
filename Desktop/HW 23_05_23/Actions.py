from time import sleep

from selenium.webdriver.common.by import By


class Actions:
    def __init__(self,driver. dict):
        self.driver = driver

    def send_keys(self,element, test_data):
        pass

    def click(self):
        pass

    def take_screenshot(self):
        pass

    def find_element(self, by, value):
        return self.driver.find_element(by, value)
    
    def find_elements():
        pass

    def type_date(self, date):
#        return self.find_element(By.XPATH, f"//span[@data-date='{date}']")

    def test_form(self,data: list, test_elements: list):
        print(data)

        elements_to_test = []

        self.driver.get("http://booking.com")

        sleep (2)

        self.find_element(
#            By.XPATH, "//button[@aria-label='Dismiss sing in information.]"
        )
        sleep(1)

        for test_element in test_elements:

            found_element = self.find_element(
                By.XPATH, list(test_element.values())[0]
            )
            key = list(test_element.keys())[0]

            elements_to_test.append({key: found_element})

        for element in elements_to_test:
            key = list(element.keys())[0]
            print("[KEY]", key)

            found_element = list(element.values())[0]
            print("[FOUND_ELEMENT]", found_element)

            for data_obj in data:
                data_obj_key = list(data_obj.keys())[0]
                data_obj_values = list(data_obj.values())[0]

                print(data_obj_key)
                print(data_obj_values)

                if data_obj_key ==key:
                    sleep(2)

                    found_element.click()

                if data_obj_key =='Data':
                    self.type_date(data_obj_values)
                else:
                    found_element.send_keys(data_obj_values)

                if data_obj_key == "Person":
                    plus_btn = self.find_element(
                        By.XPATH, 'button[@class="fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 e1b7cfea84 d64a4ea64d"]')
#                print()_______
        sleep(1)

        print(elements_to_test)                

