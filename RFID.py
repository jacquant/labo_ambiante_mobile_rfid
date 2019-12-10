from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.RFID import *
import traceback
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options)
driver.fullscreen_window()
deux_website = "http://vps747217.ovh.net/site2"
un_website = "http://user:pass@vps747217.ovh.net/site1"
# Declare any event handlers here. These will be called every time the associated event occurs.

def onRFID0_Tag(self, tag, protocol):
    if tag == "hello":
        driver.execute_script("alert('Connexion réussie');")
        time.sleep(2)
        try:
            driver.switch_to.alert.accept()
        except WebDriverException:
            pass
        driver.get(un_website)
    print("Tag: " + str(tag))
    print("Protocol: " + RFIDProtocol.getName(protocol))
    print("----------")


def onRFID0_TagLost(self, tag, protocol):
    if tag == "hello":
        driver.get(deux_website)
        driver.execute_script("alert('Déconnexion');")
        time.sleep(2)
        try:
            driver.switch_to.alert.accept()
        except WebDriverException:
            pass
    print("Tag: " + str(tag))
    print("Protocol: " + RFIDProtocol.getName(protocol))
    print("----------")


def onRFID0_Attach(self):
    print("Attach!")


def onRFID0_Detach(self):
    print("Detach!")


def onRFID0_Error(self, code, description):
    print("Code: " + ErrorEventCode.getName(code))
    print("Description: " + str(description))
    print("----------")


def main():
    try:
        # Create your Phidget channels
        rfid0 = RFID()

        # Set addressing parameters to specify which channel to open (if any)
        rfid0.setDeviceSerialNumber(384641)

        # Assign any event handlers you need before calling open so that no events are missed.
        rfid0.setOnTagHandler(onRFID0_Tag)
        rfid0.setOnTagLostHandler(onRFID0_TagLost)
        rfid0.setOnAttachHandler(onRFID0_Attach)
        rfid0.setOnDetachHandler(onRFID0_Detach)
        rfid0.setOnErrorHandler(onRFID0_Error)

        # Open your Phidgets and wait for attachment
        rfid0.openWaitForAttachment(5000)

        # Do stuff with your Phidgets here or in your event handlers.
        driver.get(deux_website)
        try:
            input("Press Enter to Stop\n")
        except (Exception, KeyboardInterrupt):
            pass

        # Close your Phidgets once the program is done.
        rfid0.close()

    except PhidgetException as ex:
        # We will catch Phidget Exceptions here, and print the error informaiton.
        traceback.print_exc()
        print("")
        print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)


main()
