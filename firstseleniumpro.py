from selenium import webdriver
browser = webdriver.Chrome(executable_path = ''
                           'C:\\Users\\Marishwaran\\Downloads\\chromedriver_win32\\chromedriver.exe')
def search_result(query):
    url = 'https://www.startpage.com'
    browser.get(url)
    search_box = browser.find_element_by_id('query')
    search_box.send_keys(query)
    search_box.submit()
    links = search_box.find_element_by_xpath
    ("//ol[@class ='web_regular_results']")
    for link in links:
        href = link.get_attribute('href')
        print(href)

search_result('google')