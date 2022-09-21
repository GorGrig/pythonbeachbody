
import time
from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys


class SeleniumBase:
    '''Base functionality'''
    
    
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(50, 0.2)
     
    '''use to find clicable element'''   
    def is_visible_element(self, locator_type : str, locator : str) -> WebElement:
        try:
            return self.wait.until(expected_conditions.visibility_of_element_located(locator_type, locator))
        except Exception as ex:
            print("Element not found. Wrong locator or locator_type" + str(ex))

             
    '''use to find non clickable element'''   
    def is_present_element(self, locator_type : str, locator : str) -> WebElement:
        try:
            return self.wait.until(expected_conditions.presence_of_element_located(locator_type, locator))
        except Exception as ex:
            print("Element not found. Wrong locator or locator_type" + str(ex))

   
    '''return list of elements'''
    def is_visible_element_or_elements(self, locator_type : str, locator : str) -> List:
        try:
            return self.wait.until(expected_conditions.visibility_of_all_elements_located(locator_type, locator))
        except Exception as ex:
            print("Element not found. Wrong locator or locator_type" + str(ex))


    '''return element from list'''
    def element_get_from_list(self, number_of_element : int, list : list) -> WebElement:
        try:
            return list[number_of_element]
        except Exception as ex:
            print("The list is empty" + str(ex))


    '''return list of elements'''
    def is_present_element_or_elements(self, locator_type : str, locator : str) -> List:
        try:
            return self.wait.until(expected_conditions.presence_of_all_elements_located(locator_type, locator))
        except Exception as ex:
            print("Element not found. Wrong locator or locator_type" + str(ex))
    

    def send_text(self, text : str, locator_type : str, locator : str) -> None:
        try:
            element = self.is_visible_element(locator_type, locator)
            element.clear()
            element.send_keys(text)
        except Exception as ex:
            print("Selected wrong webelement")
            
    def get_text():
        pass



    '''stop programm specified time'''
    def wait_time(self, wait_second) -> None:
        time.sleep(wait_second)