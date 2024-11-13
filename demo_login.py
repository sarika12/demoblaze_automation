import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import StaleElementReferenceException

class Browser:
    def call_browser(self):
        global driver
        options=Options()
        options.add_experimental_option("detach",True)
        driver= webdriver.Chrome(options=options)
        driver.get("https://www.demoblaze.com/index.html")
        driver.maximize_window()
        return driver


class Demoblaze:
    def login_page(self):
        user_name="sarikavds"
        pasword_name ="Sarika@123"
        login_bnt=driver.find_element(By.XPATH,"//a[@id='login2']").click()
        driver.implicitly_wait(4)
        user =driver.find_element(By.ID,"loginusername").send_keys(user_name)
        password=driver.find_element(By.ID,"loginpassword").send_keys(pasword_name)
        click_login_bnt=driver.find_element(By.XPATH,"//button[contains(text(),'Log in')]")
        click_login_bnt.click()
        print(driver.title)
        print(driver.save_screenshot("login_page.png"))
        user_name=driver.find_element(By.LINK_TEXT,"Welcome sarikavds")
        print(user_name.text)

    def add_card(self):
        # try:
        # time.sleep(3)
        element=WebDriverWait(driver,10).\
            until(EC.visibility_of_element_located((By.XPATH,"//a[contains(text(), 'Samsung galaxy s6')]")))
        print("text for first element added in card ",element.text)
        click_on_item1=driver.find_element(By.XPATH,"//a[contains(text(), 'Samsung galaxy s6')]")
        # click_on_item1=driver.find_element(By.XPATH,"(//div[@id='tbodyid']//div//div[@class='card h-100'])[1]")
        #//div[@id='tbodyid']//div//div[@class='card h-100']//a[@href="prod.html?idp_=1"][1]
        time.sleep(3)
        click_on_item1.click()
        time.sleep(3)
        add_to_card = driver.find_element(By.XPATH, "//a[contains(@class,'btn btn-success btn-lg')]")
        add_to_card.click()

        time.sleep(2)
        Alert(driver).accept()
        # Ok for accpet the alart

        click_home_btn = driver.find_element(By.XPATH, "//a[text()='Home ']")
        click_home_btn.click()

        # except:
        element=WebDriverWait(driver,10).\
            until(EC.visibility_of_element_located((By.XPATH,"//a[text()='Nokia lumia 1520']")))
        print("text for second element added in card ",element.text)

        try:
            click_on_item2 = driver.find_element(By.XPATH, "//a[text()='Nokia lumia 1520']")

            click_on_item2.click()

        except StaleElementReferenceException:
            click_on_item2 = driver.find_element(By.XPATH, "//a[text()='Nokia lumia 1520']")

            click_on_item2.click()



        add_to_card2 = driver.find_element(By.XPATH, "//a[contains(@class,'btn btn-success btn-lg')]")
        add_to_card2.click()

        time.sleep(2)
        Alert(driver).accept()

        click_home_btn = driver.find_element(By.XPATH, "//a[text()='Home ']")
        click_home_btn.click()
        # print(click_home_btn.get_attribute('Home'))

    def campare_text(self):

        time.sleep(3)
        click_card=driver.find_element(By.XPATH,'//a[@id="cartur"]')
        click_card.click()
        compare_items1=driver.find_elements(By.XPATH,"//tr[@class='success']//td[2]")
        compare_items2=driver.find_elements(By.XPATH,"//tr[@class='success']//td[3]")
        # item_in_home_page=driver.find_elements(By.XPATH,"//div[@id='tbodyid']//div//div[@class='card h-100']//div//h4")
        dict={}
        list1=[]
        for compare_item1,compare_item2 in zip(compare_items1,compare_items2):
            dict["title"]=compare_item1.text
            dict["price"]=compare_item2.text
            list1.append(dict)
        print(len(list1))
        print(dict)
        if len(list1)>=2:
            item1=list1[0]
            item2=list1[1]
            if item1["title"]==item2["title"]:
                print("both title are same")
            else:
                print("both title is not same")
        else:
            print("Not enough items in the cart to compare.")

    def place_order_from_card(self):

        time.sleep(3)
        place_order = driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]")
        place_order.click()
        name = driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Sarika")
        countery = driver.find_element(By.XPATH, "//input[@id='country']").send_keys("india")
        city = driver.find_element(By.XPATH, "//input[@id='city']").send_keys("Banaglore")
        driver.find_element(By.XPATH, "//input[@id='card']").send_keys("1234567890")
        driver.find_element(By.XPATH, "//input[@id='month']").send_keys("11")
        driver.find_element(By.XPATH, "//input[@id='year']").send_keys("2024")
        click_Purchase = driver.find_element(By.XPATH, "//button[contains(text(),'Purchase')]")
        click_Purchase.click()
        ok_bnt = driver.find_element(By.XPATH, "//button[contains(text(),'OK')]")
        print(ok_bnt.text)
        print(driver.save_screenshot("place_order.png"))
        ok_bnt.click()
        time.sleep(2)

        click_on_close = driver.find_element(By.XPATH, "(//div[@class='modal-content']//div//span)[3]")
        click_on_close.click()

        click_home_btn = driver.find_element(By.XPATH, "//a[text()='Home ']")
        click_home_btn.click()


    def delete_element_from_card(self):

        self.add_card()
        go_to_card_again = driver.find_element(By.XPATH, '//a[@id="cartur"]')
        go_to_card_again.click()

        delete_button = driver.find_elements(By.XPATH, "//a[contains(text(), 'Delete')]")
        for delete in delete_button:
            delete.click()
        print("Items are:",delete.text)
        time.sleep(2)
        delete_items = driver.find_elements(By.XPATH, "//tr[@class='success']//td[4]")
        # print("delete_items", delete_items)
        if not delete_items:
            print("card is empty")
        else:
            print("card having item ", len(delete_items))

    def log_out_store(self):

        log_out=driver.find_element(By.XPATH,"//a[@id='logout2']")
        log_out.click()
        element=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//a[@id='login2']")))
        print("ready to :",element.text,"again")
        time.sleep(3)
        driver.quit()
        #


browser_instance = Browser()
driver = browser_instance.call_browser()

dblz=Demoblaze()
dblz.login_page()
dblz.add_card()
dblz.campare_text()
dblz.place_order_from_card()
dblz.delete_element_from_card()
dblz.log_out_store()