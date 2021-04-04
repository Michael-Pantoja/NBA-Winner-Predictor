from teams import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

class PlayerStats:
    def __init__(self, homeIds, awayIds):
        self.df = pd.read_csv('PlayerData.csv')
        self.df = self.df[['Player_ID', 'PTS']]
        self.homeTeamIds = homeIds
        self.awayTeamIds = awayIds
        self.activeHome = []
        self.activeAway = []
        self.homeStats = []
        self.awayStats = []
        self.homeAvg = []
        self.awayAvg = []
        self.homeSd = []
        self.awaySd = []
        self.ITERATIONS = 101

    def main(self):
        self.array('HOME')
        self.array('AWAY')
        self.iteration()

    def array(self, team):
        if team == 'HOME':
            for i in self.homeTeamIds:
                temp_df = self.df.loc[self.df['Player_ID'] == i]
                array = temp_df[['PTS']].to_numpy()
                if len(array) > 0:
                    avg = np.average(array)
                    sd = np.std(array)
                    dic = {f'{i}': [avg, sd]}
                    self.homeStats.append(dic)
                    self.homeAvg.append(avg)
                    self.homeSd.append(sd)
                    self.activeHome.append(i)

        elif team == 'AWAY':
            for i in self.awayTeamIds:
                temp_df = self.df.loc[self.df['Player_ID'] == i]
                array = temp_df[['PTS']].to_numpy()
                if len(array) > 0:
                    avg = np.average(array)
                    sd = np.std(array)
                    dic = {f'{i}': [avg, sd]}
                    self.awayStats.append(dic)
                    self.awayAvg.append(avg)
                    self.awaySd.append(sd)
                    self.activeAway.append(i)

    def visualization(self):
        fig, ax = plt.subplots(2, 1, figsize = (12, 8), sharex= True)
        y1 = [1] * len(self.homeStats)
        y2 = [1] * len(self.awayStats)
        ax[0].scatter(self.homeAvg, y1)
        ax[1].scatter(self.awayAvg, y2)
        plt.show()

    def iteration(self):
        homeWin = 0
        homeLoss = 0
        n = 0
        while n <= self.ITERATIONS:
            randomHomePlayers = random.sample(set(self.activeHome), k = 5)
            randomAwayPlayers = random.sample(set(self.activeAway), k = 5)
            homeAvgNorm = []
            awayAvgNorm = []
            homeSdNorm = []
            awaySdNorm = []
            homeValue = []
            awayValue = []

            for i in randomHomePlayers:
                for j in self.homeStats:
                    try:
                        temp = j[str(i)]
                        homeAvgNorm.append(temp[0])
                        homeSdNorm.append(temp[1])
                    except:
                        pass
            for i in randomAwayPlayers:
                for j in self.awayStats:
                    try:
                        temp = j[str(i)]
                        awayAvgNorm.append(temp[0])
                        awaySdNorm.append(temp[1])
                    except:
                        pass

            homeSdNorm = (np.sum(np.square(homeSdNorm))) ** .5
            homeZ = np.random.normal(np.sum(homeAvgNorm), homeSdNorm, 1)
            homeZ = (homeZ - (np.sum(homeAvgNorm))) / homeSdNorm
            homeAvgNorm = np.sum(homeAvgNorm / np.linalg.norm(homeAvgNorm))
            tempHomeAvg = np.average(homeAvgNorm)
            homeSdNorm = np.std(tempHomeAvg)
            homeValue.append((homeZ * homeSdNorm) + homeAvgNorm)

            awaySdNorm = (np.sum(np.square(awaySdNorm))) ** .5
            awayZ = np.random.normal(np.sum(awayAvgNorm), awaySdNorm, 1)
            awayZ = (awayZ - (np.sum(awayAvgNorm))) / awaySdNorm
            awayAvgNorm = np.sum(awayAvgNorm / np.linalg.norm(awayAvgNorm))
            tempAwayAvg = np.average(awayAvgNorm)
            awaySdNorm = np.std(tempAwayAvg)
            awayValue.append((awayZ * awaySdNorm) + awayAvgNorm)

            if homeValue[0][0] > awayValue[0][0]:
                homeWin += 1
                n += 1
            elif homeValue[0][0] < awayValue[0][0]:
                homeLoss += 1
                n += 1
            else:
                print('Something Went Wrong . . .')

        if homeWin > homeLoss:
            print('HOME:', homeWin, 'AWAY:', homeLoss)
            print('Home Team Wins!')
        else:
            print('HOME:', homeWin, 'AWAY:', homeLoss)
            print('Home Team Lost.')

if __name__ == '__main__':

    TeamsTest = Parse('Golden State Warriors', 'Miami Heat')
    TeamsTest.main()
