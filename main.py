from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from splinter import Browser
import time

Person = {
    'First Name' : 'Test',
    'Last Name' : 'testson',
    'Epost' : 'em',
    'Phonenr' : '0123456789',
    'Month' : 4,
    'Day' : 31
}

PATH = "C:\Program Files (x86)/chromedriver.exe"


def website():
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.get("https://bokapass.nemoq.se/Booking/Booking/Index/stockholm")

    #First page
    driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[2]/div[1]/div/form/div[2]/input').click()

    #Second PageNumber of persons
    time.sleep(1)
    driver.find_element('xpath', '/html/body/div[2]/div/div/div/form/div[1]/div[2]/div/input[1]').click()
    #select = Select(driver.find_element('xpath', '/html/body/div[2]/div/div/div/form[1]/div/div[2]/div/select'))
    #select.select_by_value('1')#Number of persons
    driver.find_element('xpath', '/html/body/div[2]/div/div/div/form/div[2]/input').click()

    #Third page Living in sweden
    time.sleep(1)
    driver.find_element('xpath', '/html/body/div[2]/div/div/div/form/div[1]/div/div/label[1]').click()
    driver.find_element('xpath', '/html/body/div[2]/div/div/div/form/div[2]/input').click()

    #Drop down menu and boking time
    time.sleep(1)
    select = Select(driver.find_element('xpath', '/html/body/div[2]/div/div/div/form[1]/div/div[2]/div/select'))
    select.select_by_value('48')#Sodra roslagen Taby
    driver.find_element('xpath', '/html/body/div[2]/div/div/div/form[1]/div/div[6]/div/input[2]').click()

    containers = driver.find_elements(By.XPATH, '//div[@data-function="timeTableCell"]')
    for items in containers:
        if items.text != 'Bokad':
            date = (items.get_attribute('aria-label'))
            print(date)
            month = int(date[5:7])
            day = int(date[8:10])
            if month <= Person['Month'] and day <= Person['Day']:
                items.click()
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form[2]/div[3]/input').click()

                #Personal information
                search = driver.find_element(By.ID, 'Customers_0__BookingFieldValues_0__Value')
                search.send_keys(Person['First Name'])
                search = driver.find_element(By.ID, 'Customers_0__BookingFieldValues_1__Value')
                search.send_keys(Person['Last Name'])
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/div[1]/div[4]/div/label[1]').click()#Pass
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/div[2]/input').click()

                #Inforpage
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/div/input').click()

                #Email and Phone nr
                search = driver.find_element(By.ID, 'EmailAddress')
                search.send_keys(Person['Epost'])
                search = driver.find_element(By.ID, 'ConfirmEmailAddress')
                search.send_keys(Person['Epost'])
                search = driver.find_element(By.ID, 'PhoneNumber')
                search.send_keys(Person['Phonenr'])
                search = driver.find_element(By.ID, 'ConfirmPhoneNumber')
                search.send_keys(Person['Phonenr'])

                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/div[1]/div[5]/div/label[2]').click() # sms confermation
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/div[1]/div[5]/div/label[1]').click()  # Email confermation
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/div[1]/div[6]/div/label[2]').click()  # sms reminder
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/div[1]/div[5]/div/label[1]').click()  # Email reminder
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/div[2]/input').click()

                #Confirm apointment
                #driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/div[3]/input')#Uncomment to finish the appointment


                return 'Time', date


            else:
                #time.sleep(5)
                print('No time')
                driver.quit()
                return 'No Time', date


def main():
    boked = 'No Time'
    date = ''
    while boked == 'No Time':
        boked, date = website()
        time.sleep(60)
    print(date)

if __name__ == '__main__':
    main()