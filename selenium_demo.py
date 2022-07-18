import csv
from selenium.common.exceptions import NoSuchElementException
from re import findall
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement

driver = Chrome("/Users/sandeep/Desktop/Training/_selenium/chromedriver")
driver.get("file:///Users/sandeep/Desktop/demo-html/demo.html")
driver.maximize_window()
sleep(3)


elements = driver.find_elements_by_xpath("//table[@name='customers']//td[2]")

actual_fnames = [element.text for element in elements]

# Get the sorted version of the actula_fnames
sorted_fnames = sorted(actual_fnames)

if actual_fnames == sorted_fnames:
    print("PASS")
else:
    print("FAIL")


# # Printing the headers
# print(f"{'AAPL':>10} {'MSFT':>10} {'AA':>10} {'FB':>10}")

# # Infinitely monitering the prices 
# while True:
#     aapl_price = driver.find_element_by_xpath("//td[text()='AAPL']/..//td[3]").text
#     msft_price = driver.find_element_by_xpath("//td[text()='MSFT']/..//td[3]").text
#     aa_price = driver.find_element_by_xpath("//td[text()='AA']/..//td[3]").text
#     fb_price = driver.find_element_by_xpath("//td[text()='FB']/..//td[3]").text

#     print(f"{aapl_price:>10} {msft_price:>10} {aa_price:>10} {fb_price:>10}", end="")
#     print("")
#     sleep(2)







# driver.find_element_by_xpath("//span[text()='Upload Resume']").click()
# sleep(2)

# driver.find_element_by_id("file-upload").send_keys("/Users/sandeep/Desktop/Training/_selenium/data_files/sample.txt")








# driver.find_element_by_xpath("//a[text()='Twitter']").click()
# sleep(5)

# handles = driver.window_handles
# driver.switch_to.window(handles[1])
# sleep(3)

# driver.close()

# sleep(5)


# sleep(2)

# driver.switch_to.window(handles[1])
# sleep(2)

# driver.find_element_by_xpath("//input[@placeholder='Search Twitter']").send_keys("hello")
# sleep(2)

# driver.switch_to.window(handles[0])
# sleep(2)

# driver.find_element_by_link_text("Register").click()
# sleep(2)


# for handle in handles:
#     print(handle)












# driver.find_element_by_id("delete").click()
# sleep(1)

# driver.switch_to.alert.accept()
# sleep(1)

# driver.find_element_by_id("delete").click()
# sleep(1)

# print(driver.switch_to.alert.text)

# driver.switch_to.alert.dismiss()














# driver.find_element_by_xpath("//span[text()='Departure']").click()

# def select_date(month, year, day):
#     _xpath = f"//div[text()='{month} {year}']/../..//p[text()='{day}']"
#     for _ in range(0, 12):
#         try:
#             driver.find_element_by_xpath(_xpath).click()
#             return True
#         except NoSuchElementException:
#             driver.find_element_by_xpath("//span[@aria-label='Next Month']").click()
#             sleep(1)
#     return False
















# driver.implicitly_wait(10)

# element = driver.find_element_by_name("hello world")












# 1. Check if the element is loaded in the DOM
# 2. Check if the element is visible on the webpage.
# 3. Check if the element is enabled or not?

# class _visibility_of_element_located(visibility_of_element_located):
#     def __init__(self, locator):
#         super().__init__(locator)   # initlising parent class constructor

#     # over-riding __call__ method of parent class
#     def __call__(self, driver):
#         print("Calling __call__ method of Child Class")
#         result = super().__call__(driver)
#         if isinstance(result, WebElement):
#             # Extra functionality that you are adding in child class
#             # checking for enablement of the element
#             return result.is_enabled()
#         else:
#             return False

# driver.find_element_by_xpath("//button[text()='Click Me']").click()

# w = WebDriverWait(driver, 20)
# v = _visibility_of_element_located(("xpath", "//div[text()='100%']"))
# w.until(v, message="Progress bar was not loaded even after 20 seconds")
# print("DONE!")
















# Finding all the links that are present on the left navigation pane
# links = driver.find_elements_by_xpath("//div[@class='block block-category-navigation']//a")
# links = driver.find_elements_by_xpath("//div[@class='footer-menu-wrapper']//a")
# headers = driver.find_elements_by_xpath("//div[@class='footer-menu-wrapper']//h3")
# links = driver.find_elements_by_xpath("//div[@class='footer-main-wrapper']//a")

# driver.find_element_by_id("SE_home_autocomplete").send_keys("HTML")
# sleep(2)
# driver.find_element_by_xpath("//input[@value='Search']").submit()
# sleep(5)

# titles = driver.find_elements_by_xpath("//div[@class='job-tittle']/h3/a")

# for title in titles:
#     print(title.text)
#     sleep(1)

# for header in headers:
#     print(header.text)
#     sleep(1)

# for link in links:
#     print(link.text)
#     sleep(1)

# glasses = { 'Sunglasses Aero': 139.00,
#             'ORIGINAL COLLECTION': 149.00,
#             'Custom Sunglasses': 179.00
#         }

# def read_csv():
#     expected_prices = { }
#     with open("./data_files/smart_prices.csv") as f:
#         rows = csv.reader(f)
#         headers = next(rows)     # skip headers
#         for row in rows:
#             expected_prices[row[0]] = float(row[1])
#     return expected_prices

# d = read_csv()

# for product, expected_price in d.items():
#     _xpath = f"//span[text()='{product}']/../../..//span[@class='art-price' or @class='art-price art-price--offer']"
#     temp = driver.find_element_by_xpath(_xpath).text
#     actual_price = findall(r"[\d\.]", temp)
#     actual_price = float("".join(actual_price))
#     if actual_price == expected_price:
#         print("PASS")
#     else:
#         print(f"FAIL: {product}: Expceted {expected_price}: actual: {actual_price}")

















# General Syntax
# //HTMLTAG[@attribute = "attribute_value"]
# //HTMLTAG[text()='text_of_element']


# elements = driver.find_elements_by_xpath("//span[@class='price actual-price']")
# print(driver.find_element_by_xpath("(//span[@class='price actual-price'])[6]").text)

# products = {
#     'Build your own expensive computer': 1800.00,
#     'Simple Computer': 700.00,
#     '$25 Virtual Gift Card': 25.00, 
#     '14.1-inch Laptop': 1590.00, 
#     'Build your own cheap computer': 800.00, 
#     'Build your own computer': 1200.00
# }

# for item, expected_price in products.items():
#     _xpath = f"//a[text()='{item}']/../..//span[@class='price actual-price']"
#     actual_price = driver.find_element_by_xpath(_xpath).text
#     if float(actual_price) == expected_price:
#         print("PASS")
#     else:
#         print(f"FAIL: The actual price of {item} is {actual_price}- But expected is {expected_price}")

#     sleep(1)

# if float(actual_price_simple_computer) == expected_price_simple_computer:
#     print('PASS')
# else:
#     print('FAIL')

# for element in elements:
#     print(element.text)
#     sleep(1)










# driver.find_element_by_xpath("(//input[@name='download'])[3]").click()
# driver.find_element_by_xpath("//td[text()='Python']/..//input[@name='download']").click()
# driver.find_element_by_xpath("//a[text()='Python 3.9.12']/../..//a[text()='Release Notes']").click()
# driver.find_element_by_xpath("//a[text()='14.1-inch Laptop']/../..//input[@value='Add to cart']").click()

# box = driver.find_element_by_id("standard_cars")
# s = Select(box)

# all_options = s.options

# items = [ ]
# for item in all_options:
#     items.append(item.text)

# Using comprehension
# items = [  item.text for item in all_options ]

# s.select_by_visible_text("Mercedes")
# sleep(2)

# current_selected_option = s.first_selected_option
# print(current_selected_option.text)

# s.select_by_visible_text()

# car = "Mercedes"
# for index, item in enumerate(items):
#     if item == car:
#         s.select_by_visible_text(car)
#         print(f"Index of {car} is {index}")



# s.select_by_visible_text(items[-1])
# sleep(2)
# s.select_by_visible_text(items[0])


# for item in items:
#     s.select_by_visible_text(item)
#     sleep(1)

# for item in items[::-1]:
#     s.select_by_visible_text(item)
#     sleep(1)

# for item in reversed(items):
#     s.select_by_visible_text(item)
#     sleep(1)

# for i in range(len(items)-1, -1, -1):
#     s.select_by_visible_text(items[i])
#     sleep(1)


# s.select_by_visible_text("Mercedes")
# sleep(1)

# s.select_by_visible_text("Toyota")
# sleep(1)

# s.select_by_index(5)
# sleep(1)

# s.select_by_index(3)
# sleep(1)

# s.select_by_value("vol")
# sleep(1)

# s.select_by_value("hda")
# sleep(1)


# links = driver.find_elements_by_xpath("//a")

# for link in links:
#     print(link.get_attribute("href"))
# urls = [ ]
# for link in links:
#     link_text = link.text
#     if "Python" in link_text:
#         urls.append((link_text, link.get_attribute("href")))
#         sleep(1)

# boxes = driver.find_elements_by_xpath("//input[@name='fname']")
# words = ["hello", "world", "apple", "google", "micorosft", "walmart", "bestbuy", "watsapp", "facebook"]

# for box, word in zip(boxes, words):
#     box.send_keys(word)    
#     sleep(1)


# boxes[0].send_keys("hello")
# boxes[1].send_keys("world")
# boxes[2].send_keys("apple")
# boxes[3].send_keys("google")
# boxes[4].send_keys("micorosft")
# boxes[5].send_keys("walmart")
# boxes[6].send_keys("bestbuy")
# boxes[7].send_keys("watsapp")
# boxes[8].send_keys("facebook")

# for box in boxes:
#     box.send_keys("hello")
#     sleep(1)



# links = driver.find_elements_by_xpath("//a")

# text used to get the text of a webelement
# for link in links:
#     print(link.text)

# links = driver.find_elements_by_xpath("//a")
# images = driver.find_elements_by_xpath("//img")
# inputs = driver.find_elements_by_xpath("//input[@type='text']")
# radios = driver.find_elements_by_xpath("//input[@type='radio']")
# checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
# tables = driver.find_elements_by_xpath("//table")

# print(f"No of links {len(links)}")
# print(f"No of images {len(images)}")
# print(f"No of textboxes {len(inputs)}")
# print(f"No of radio buttons {len(radios)}")
# print(f"No of radio checkboxes {len(checkboxes)}")
# print(f"No of tables {len(tables)}")


# for element in elements:
#     element.click()
#     sleep(1)

# for element in elements[::-1]:
#     element.click()
#     sleep(1)

# for element in reversed(elements):
#     element.click()
#     sleep(1)

# for i in range(len(elements)-1, -1, -1):
#     elements[i].click()
#     sleep(1)


# class AddTeacherCS:
#     def __init__(self, _class, _section):
#         self._class = _class
#         self._section = _section
    
#     def click_add_teacher(self):
#         print("Clicking on add teacher using CS")

# class AddTeacherDir:
#     def click_add_teacher(self):
#         print("Clicking on add teacher using Dir")


# class AddInfoCSV:
#     def __init__(self, filepath):
#         self.filepath = filepath
    
#     def add_info(self):
#         print("Adding info using CSV")

# class AddInfoManually:
#     def __init__(self, name):
#         self.name = name
    
#     def add_info(self):
#         print("Adding info using manually")

# class CreateTeacher:
#     def __init__(self, click_mode, info_mode):
#         self.click_mode = click_mode
#         self.info_mode = info_mode

#     def click_add_teacher(self):
#         self.click_mode.click_add_teacher()
    
#     def add_info(self):
#         self.info_mode.add_info()
    
# # addcs = AddTeacherCS("myclass", "A")  
# adddir = AddTeacherDir()  
# info = AddInfoManually("hello") 
# t = CreateTeacher(adddir, info)
# t.click_add_teacher()
# t.add_info()