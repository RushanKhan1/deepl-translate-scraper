#! /usr/bin/python3
import sys
import bs4, requests, time, pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options

# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.chrome import ChromeDriverManager
# browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
options = Options()
options.headless = True
fromLang = "en"
lis = sys.argv;
string = ""
# parsing the input arguments
for i in range(len(sys.argv)):
    if(i != 0 and i != 1):
        string = string + sys.argv[i] + " "
string = string.split(" ")
string = "%20".join(string)
toLang = sys.argv[1]
url = "https://deepl.com/en/translator#" + fromLang + "/" + toLang + "/" + string
browser = webdriver.Firefox(options=options)
browser.get(url);
# trick to bypass their protective measures.
elem = browser.find_element_by_css_selector('#dl_translator > div.lmt__text > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--source > div.lmt__textarea_container > div.lmt__inner_textarea_container > textarea')
time.sleep(4) # if you have a slow internet connection then please increase the sleep time here, time is in seconds
browser.execute_script("document.getElementById('target-dummydiv').style.visibility = 'visible';")
elem = browser.find_element_by_css_selector('#target-dummydiv')
text = elem.text;
lines = text.split('\n')
print('Translation: ' + lines[len(lines)-1]);
browser.close();
