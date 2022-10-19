#LIVE CRICKET NOTIFICATION DISPLAY
#This part is done by Sudhanshu Raj
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import re
from time import sleep


def ascii_art():
    # An artistic banner for the script
    print("""
██╗     ██╗██╗   ██╗███████╗     ██████╗██████╗ ██╗ ██████╗██╗  ██╗███████╗████████╗    ███████╗ ██████╗ ██████╗ ██████╗ ███████╗
██║     ██║██║   ██║██╔════╝    ██╔════╝██╔══██╗██║██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝    ██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
██║     ██║██║   ██║█████╗      ██║     ██████╔╝██║██║     █████╔╝ █████╗     ██║       ███████╗██║     ██║   ██║██████╔╝█████╗  
██║     ██║╚██╗ ██╔╝██╔══╝      ██║     ██╔══██╗██║██║     ██╔═██╗ ██╔══╝     ██║       ╚════██║██║     ██║   ██║██╔══██╗██╔══╝  
███████╗██║ ╚████╔╝ ███████╗    ╚██████╗██║  ██║██║╚██████╗██║  ██╗███████╗   ██║       ███████║╚██████╗╚██████╔╝██║  ██║███████╗
╚══════╝╚═╝  ╚═══╝  ╚══════╝     ╚═════╝╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝       ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝""")

def get_current_matches():
    # Function to fetch the live matches currently in play
    page = requests.get('http://static.cricinfo.com/rss/livescores.xml') # HTTP Get request to cricinfo rss feed
    soup = BeautifulSoup(page.text,'lxml') # parsing and building xml tree out of the returned xml file
    matches = soup.find_all('description') # description tags contain the score
    live_matches = [s.get_text() for s in matches if '*' in s.get_text()] # returns only the live matches and ignores the completed ones
    return live_matches

#This part is done by Priyanshu Rai
def fetch_score(matchNum):
    # Function to return the live score of the match specified
    page = requests.get('http://static.cricinfo.com/rss/livescores.xml')
    soup = BeautifulSoup(page.text,'lxml')
    matches = soup.find_all('description')
    live_matches = [s.get_text() for s in matches if '*' in s.get_text()]
    return live_matches[matchNum]


#This part is done by Swati Pal

### The Main Function ###
if _name_ == "_main_":
    ascii_art() 
    matches = get_current_matches()
    print('Current matches in play')
    print('='*23)
    # printing a list of all the current live matches 
    for i,match in enumerate(matches):
                print('[{}] '.format(i) + 
                        re.search('\D+',match.split('v')[0]).group() + 'vs.' +
                        re.search('\D+',match.split('v')[1]).group()
                      )

    print()
    matchNum = int(input('Pick the match number [0,1,2...] => '))
#This part is done by Bhavya Negi
def notify(score):
    # Function for Windows toast desktop notification
    toaster = ToastNotifier()
    toaster.show_toast(score,
                       "Go India, Jai Ho!",
                       duration=10)


