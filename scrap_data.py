print("Importing Necessary bibs")
import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#RUN pip install -r requirements
print("Define Necessary paths")  # Chrome Path is Local Defined
chrome_path = r"C:\Program Files\Google\Chrome\Application"
url = 'https://www.premierleague.com/'
df_final = pd.DataFrame()
chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")
print("Creating Functions")


def get_table(driver):
    table_element = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[1]/div[2]/table/tbody')
    rows = table_element.find_elements_by_tag_name('tr')

    table_data = []
    for row in rows:
        columns = row.find_elements_by_tag_name('td')
        row_data = []
        for column in columns:
            row_data.append(column.text)
        table_data.append(row_data)

    df = pd.DataFrame(table_data)

    return df





def lauch_and_go_players_goals(years_back):
    years_back_ = years_back + 2
    print('Creating Dataframe to append all results')
    df_final = pd.DataFrame()
    print("Launching Webdriver and going to Premier League Website")
    driver = webdriver.Chrome(executable_path=os.path.join(chrome_path, "chromedriver.exe"), options=chrome_options)
    driver.get(url)

    print('Acepting Cookies')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()

    print('Check ADS')
    time.sleep(3)
    try:
        driver.find_element_by_xpath('//*[@id="advertClose"]').click()
    except:
        print("No ADS")
    print("Going to goals Stats")

    time.sleep(5)
    driver.find_element_by_xpath('/html/body/header/div/nav/ul/li[5]/a').click()

    print('Check ADS')
    time.sleep(3)
    try:
        driver.find_element_by_xpath('//*[@id="advertClose"]').click()
    except:
        print("No ADS")
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/section[1]/ul/li[1]/div/header/h4/a').click()
    print('On the page')

    print('first page is the current season, 23/22')

    time.sleep(5)
    df = get_table(driver)
    df['season'] = '22/23'
    df_final = df_final.append(df)

    time.sleep(5)
    print("For past seasons, use a for loop")  # The get list is same xpath
    # Only thing changing is the selected season, starting at i=3 on xpath
    for i in range(3, years_back_):
        season_1 = 24 - i
        season_2 = 25 - i
        season = str(season_1) + '/' + str(season_2)
        print(season)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[1]/section/div[1]/div[2]').click()
        time.sleep(5)
        driver.find_element_by_xpath(
            f'//*[@id="mainContent"]/div[2]/div/div[2]/div[1]/section/div[1]/ul/li[{i}]').click()
        time.sleep(5)
        df_ = get_table(driver)
        df_['season'] = season
        df_final = df_final.append(df_)

    driver.quit()
    df_final.columns = ['Ranking Season', 'Player', 'Team', 'Player Nationality', 'Goals', 'drop', 'Season']
    df_final.drop('drop', axis=1, inplace=True)
    return df_final


def lauch_and_go_club_goals(years_back):
    years_back_ = years_back+2
    print('Creating Dataframe to append all results')
    df_final = pd.DataFrame()
    print("Launching Webdriver and going to Premier League Website")
    driver = webdriver.Chrome(executable_path=os.path.join(chrome_path, "chromedriver.exe"), options=chrome_options)
    driver.get(url)

    print('Acepting Cookies')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()

    print('Check ADS')
    time.sleep(3)
    try:
        driver.find_element_by_xpath('//*[@id="advertClose"]').click()
    except:
        print("No ADS")
    print("Going to goals Stats")

    time.sleep(5)
    driver.find_element_by_xpath('/html/body/header/div/nav/ul/li[5]/a').click()

    print('Check ADS')
    time.sleep(3)
    try:
        driver.find_element_by_xpath('//*[@id="advertClose"]').click()
    except:
        print("No ADS")
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/section[2]/ul/li[1]/div/header/h4/a').click()
    print('On the page')

    print('first page is the current season, 23/22')

    time.sleep(5)
    df = get_table(driver)
    df['season'] = '22/23'
    df_final = df_final.append(df)

    time.sleep(5)
    print("For past seasons, use a for loop")  # The get list is same xpath
    # Only thing changing is the selected season, starting at i=3 on xpath
    for i in range(3, years_back_):
        season_1 = 24 - i
        season_2 = 25 - i
        season = str(season_1) + '/' + str(season_2)
        print(season)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[1]/section/div[1]/div[2]').click()
        time.sleep(5)
        driver.find_element_by_xpath(
            f'//*[@id="mainContent"]/div[2]/div/div[2]/div[1]/section/div[1]/ul/li[{i}]').click()
        time.sleep(5)
        df_ = get_table(driver)
        df_['season'] = season
        df_final = df_final.append(df_)

    driver.quit()
    df_final.columns = ['Ranking Season', 'Team', 'Goals', 'drop', 'Season']
    df_final.drop('drop', axis=1, inplace=True)
    return df_final


