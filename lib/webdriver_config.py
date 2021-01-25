from selenium import webdriver

def initialize():
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--ignore-certificate-errors")
    capabilities = options.to_capabilities()
    return webdriver.Chrome(desired_capabilities=capabilities)
