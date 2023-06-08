import scrap_data
import data_prep
import plot_data
from selenium.webdriver.chrome.options import Options

print("Define Necessary paths")  # Chrome Path is Local Defined
chrome_path = r"C:\Program Files\Google\Chrome\Application"
url = 'https://www.premierleague.com/'

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")


if __name__== "__main__":
    #Insert Seasons to colect data for arg inside function
    df_goal_players = scrap_data.lauch_and_go_players_goals(5)
    df_goal_clubs = scrap_data.lauch_and_go_club_goals(5)

    #Ajust data
    df_goal_players = data_prep.transform_col(df_goal_players)
    df_goal_clubs = data_prep.transform_col(df_goal_clubs)

    #Plot information related to players and clubs
    plot_data.plot_simu(df_goal_players, 'Season', 'Player Nationality', 'Player')
    plot_data.pieplot_2(df_goal_clubs, 'Season', 'Goals', 'Team')




