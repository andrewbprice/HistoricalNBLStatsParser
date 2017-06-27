############################
##### IMPORT LIBRARIES #####
############################

import urllib.request as urllib
from bs4 import BeautifulSoup
import csv
import pandas as pd
import os


############################################
##### INSERT URL FROM SPORTSTG WEBSITE #####
############################################

page = urllib.urlopen("http://websites.sportstg.com/rpt_fixture.cgi?fixture_type=2&client=0-189-0-125723-0&pool=-1")


###############################################
##### GET URLS OF ALL BOXSCORES IN SEASON #####
###############################################

urlList = []

soup = BeautifulSoup(page, "html.parser")

for link in soup.find_all('a', href=True, text='View'):
    urlList.append("http://websites.sportstg.com/" +str(link['href']))

print(str(len(urlList)) +" boxscores found")
print("Beginning Processessing")
print("")
print("###############################################")
print("")


###################################
##### PULL BOXSCORE FUNCTION ######
###################################

def createData():
    page = urllib.urlopen(url)  
    soup = BeautifulSoup(page, "html.parser")
    table = soup.find_all('table', {'class' : 'tableClass stats table player-stats-table'})
    rows = table[0].find_all('tr')
    team1 = str(soup.find_all('h4')[2].get_text())
    team2 = str(soup.find_all('h4')[3].get_text())
    date = soup.find_all('span', {'class' : 'matchdate'})
    date = str(date[0].get_text())

    print("Reading Boxscore...")


    outputWriter.writerow(["Team", "Opponent", "Player", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%", "FTM", "FTA", "FT%",\
                       "PFS", "AST", "BLK", "TOV", "oREB", "dREB", "STL", "tREB", "PTS"," MIN", "Date"])
    
    for row in rows:
        data = row.find_all('td')
        for row in data:
            Team1 = team1
            Opponent = team2
            PLAYER = str.strip(data[0].get_text())
            MIN = str(data[20].get_text())
            FGM = str(data[2].get_text())
            FGA = str(data[3].get_text())
            FGP = str(data[4].get_text())
            TPM = str(data[5].get_text())
            TPA = str(data[6].get_text())
            TPP = str(data[7].get_text())
            FTM = str(data[8].get_text())
            FTA = str(data[9].get_text())
            FTP = str(data[10].get_text())
            TOV = str(data[14].get_text())
            PFS = str(data[11].get_text())
            oREB = str(data[15].get_text())
            dREB = str(data[16].get_text())
            tREB = str(data[18].get_text())
            AST = str(data[12].get_text())
            STL = str(data[17].get_text())
            BLK = str(data[13].get_text())
            PTS = str(data[19].get_text())
            DATE = date[11:]

            outputWriter.writerow([Team1, Opponent, PLAYER, FGM, FGA, FGP, TPM, TPA, TPP, FTM, FTA, FTP, PFS, AST, BLK, TOV,\
                           oREB, dREB, STL, tREB, PTS, MIN, DATE])


    rows = table[1].find_all('tr')
     
    for row in rows:
        data = row.find_all('td')
        for row in data:
            Team2= team2
            Opponent = team1
            PLAYER = str.strip(data[0].get_text())
            MIN = str(data[20].get_text())
            FGM = str(data[2].get_text())
            FGA = str(data[3].get_text())
            FGP = str(data[4].get_text())
            TPM = str(data[5].get_text())
            TPA = str(data[6].get_text())
            TPP = str(data[7].get_text())
            FTM = str(data[8].get_text())
            FTA = str(data[9].get_text())
            FTP = str(data[10].get_text())
            TOV = str(data[14].get_text())
            PFS = str(data[11].get_text())
            oREB = str(data[15].get_text())
            dREB = str(data[16].get_text())
            tREB = str(data[18].get_text())
            AST = str(data[12].get_text())
            STL = str(data[17].get_text())
            BLK = str(data[13].get_text())
            PTS = str(data[19].get_text())
            DATE = date[11:]

            outputWriter.writerow([Team2, Opponent, PLAYER, FGM, FGA, FGP, TPM, TPA, TPP, FTM, FTA, FTP, PFS, AST, BLK, TOV,\
                           oREB, dREB, STL, tREB, PTS, MIN, DATE])

    outputFile.close()


#############################################################################################################################

###################################
####### CLEAN DATA FUNCTION #######
###################################


def pandaClean():
    print("Cleaning Boxscore...")
    inputFile = pd.read_csv(tempFile, encoding = "ISO-8859-1", low_memory=False)
    df = pd.DataFrame(inputFile, columns = ["Team", "Opponent", "Player", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%", "FTM", "FTA", "FT%",\
                       "PFS", "AST", "BLK", "TOV", "oREB", "dREB", "STL", "tREB", "PTS"," MIN", "Date"])

    export = df.drop_duplicates()
    export.to_csv(exportFile)
    os.remove(tempFile)


#############################################################################################################################    



#########################
##### EXPORT TO CSV #####
#########################

i = 0

for url in urlList:
    outputFile = open('rawdata' +'.csv', 'w', newline='')
    outputWriter = csv.writer(outputFile)
    i += 1
    tempFile = 'rawdata.csv'
    exportFile = 'Boxscore' +str(i) +'.csv'
    createData()
    pandaClean()
    print("Boxscore " +str(i)  +" Successfully Exported")
    print("")