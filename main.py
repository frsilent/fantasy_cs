"""A module for getting the 'best' fantasy team using analytics
    1. Need to scrape html to create a player and add them to a Pool
    2. Create all potential Rosters consisting of players * ROSTER_SIZE & capped at SALARY_CAP
    3. Find the valid Roster with the highest total of points this season
    4. Maybe give the top 4 recommendations or something
    5. Incorporate last game's stats as well to see hot-streaks
"""

import bs4
import itertools

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


class Roster():
    size = ROSTER_SIZE
    salary = SALARY_CAP

    def __init__(self, players=[]):
        self.players = players

    def add_player(self, player):
        # if player.__class__.__name__ not 'Player':
        if not isinstance(player, Player):
            raise TypeError("Must be of type 'Player', instead received " + str(player.__class__.__name__))
        if len(self.players) >= ROSTER_SIZE:
            pass
            # raise RosterException("Amount of players exceeds roster size limitation.")
        else:
            self.players.append(player)

    def __str__(self):
        return ", ".join([player.name for player in self.players])


class Pool():
    def __init__(self, players=[]):
        self.players = players

    def add_player(self, player):
        self.players.append(player)

    def build_rosters(self):
        """
        Create all valid permutations of the pool.
        This brute force solution is n! / r! / (n-r)! so for now just need to get the first few rosters.
        """
        # TODO:  Replace this with a sane method, ala buckets or something to optimize roster building.
        # TODO: Should look into maybe sorting the players, maybe make a roster of the best possible past average. Then continuously remove & add until the salary/team requirements are met.

        rosters = itertools.combinations_with_replacement(self.players, ROSTER_SIZE)

        for i in range(0,50):  # Only using the first 50 roster possibilities for testing
            r = (next(rosters))


    def __str__(self):
        return ", ".join([player.name for player in self.players])


if __name__ == '__main__':
    vulcun_site = bs4.BeautifulSoup(open('example.html'), 'html.parser')

    # players = [player.attrs.get('id') for player in vulcun_site.select('.addplayer')]

    pool = Pool()

    for player in vulcun_site.select('.addplayer'):
        name = player.select('.player-name')[0].string
        points = float(player.select('.player-season_avg')[0].string)
        salary = int(player.select('.player-price')[0].string[1:])
        team = player.select('.player-team-name')[0].string

        # pool.add_player(Player(name, points, salary, team))
        p = Player(name, points, salary, team)
        # print(p)
        # print(p.__class__.__name__)
        # print(isinstance(p, Player))
        pool.add_player(p)

    # print(pool)
    pool.build_rosters()
    print('ended')
