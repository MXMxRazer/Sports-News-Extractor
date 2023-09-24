# Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os

# GLOBAL VARIABLES
website = "https://www.thesun.co.uk/sport/football/"
driverPath = "C:/chromedriver-win64/chromedriver.exe"


# Data Frame Storage Service
def data_frame_service(titles, links):
    # Dataframe storage scheme
    df_dict = {
        "Titles": titles,
        "Links": links
    }

    # Dataframe storage
    df = pd.DataFrame(df_dict)

    df.to_csv(path_management())


# Data Frame Storage Service * END *

# Directory File Management Method
def path_management():

    application_path = "C:\\Users\\varkr\\PycharmProjects\\pythonProject1\\data"

    print(f"Executing the default application path.")

    file_name = f'headline-{get_date_time()}.csv'
    final_path = os.path.join(application_path, file_name)

    return final_path

# DateTime Management Method
def get_date_time():
    now = datetime.now()
    month_day_year_format = now.strftime("%m-%d-%Y")

    return month_day_year_format


# Main Method
def main():
    # Initializing Service
    service = Service(executable_path=driverPath)
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Chrome(service=service, options=options)

    # Specifying website
    driver.get(website)

    # Searching for element
    containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

    # Variables to store data values
    titles = []
    links = []

    for container in containers:
        title = container.find_element(by="xpath", value="./a/h3").text
        link = container.find_element(by="xpath", value='./a').get_attribute("href")

        titles.append(title)
        links.append(link)

    driver.quit()

    data_frame_service(titles, links)


# Main Method * END *


# Method Executor
def method_executor():
    main()


# Method Executor * END *


method_executor()
