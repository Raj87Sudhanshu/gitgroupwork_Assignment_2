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

#This part is done by Bhavya Negi
def notify(score):
    # Function for Windows toast desktop notification
    toaster = ToastNotifier()
    toaster.show_toast(score,
                       "Go India, Jai Ho!",
                       duration=10)
