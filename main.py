"""A module for getting the 'best' fantasy team using analytics
    1. Need to scrape html to create a player and add them to a Pool
    2. Create all potential Rosters consisting of players * ROSTER_SIZE & capped at SALARY_CAP
    3. Find the valid Roster with the highest total of points this season
    4. Maybe give the top 4 recommendations or something
    5. Incorporate last game's stats as well to see hot-streaks
"""

import bs4

SALARY_CAP = 10000
ROSTER_SIZE = 8


class Player():
    def __init__(self, name, points, salary, team):
        self.name = name
        self.points = points
        self.salary = salary
        self.team = team

    def __str__(self):
        return self.name


class Pool():
    def __init__(self, players=None):
        self.players = players
        if players is None:
            self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def __str__(self):
        return ", ".join([player.name for player in self.players])


class Roster():
    def __init__(self, players):
        self.players = players


if __name__ == '__main__':
    vulcun_site = bs4.BeautifulSoup(open('example.html'), 'html.parser')

    # players = [player.attrs.get('id') for player in vulcun_site.select('.addplayer')]

    pool = Pool()
    # players = []
    for player in vulcun_site.select('.addplayer'):
        name = player.select('.player-name')[0].string
        points = float(player.select('.player-season_avg')[0].string)
        salary = int(player.select('.player-price')[0].string[1:])
        team = player.select('.player-team-name')[0].string

        # players.append(Player(name, points, salary, team))
        pool.addPlayer(Player(name, points, salary, team))

    print pool
