"""A module for getting the 'best' fantasy team using analytics
    1. Need to scrape html to create a player and add them to a Pool
    2. Create all potential Rosters consisting of players * ROSTER_SIZE & capped at SALARY_CAP
    3. Find the valid Roster with the highest total of points this season
    4. Maybe give the top 4 recommendations or something
    5. Incorporate last game's stats as well to see hot-streaks
"""

import bs4
import itertools

from exceptions import RosterFullException, InvalidRosterException

SALARY_CAP = 10000
ROSTER_SIZE = 8
SAME_TEAM_LIMIT = 2  # Limit to how many players from the same team can be on a roster


class Player:
    def __init__(self, name, points, salary, team):
        self.name = name
        self.points = points
        self.salary = salary
        self.team = team

    def value_ratio(self):
        return self.points / self.salary

    def __str__(self):
        return self.name


class Roster:
    size = ROSTER_SIZE
    salary = SALARY_CAP
    teams_limit = SAME_TEAM_LIMIT

    def __init__(self, players={}):
        self.players = players

    def add_player(self, player):
        print(player)
        if not isinstance(player, Player):
            raise TypeError("Must be of type 'Player', instead received " + str(player.__class__.__name__))
        if len(self.players) >= ROSTER_SIZE:
            raise RosterFullException("Roster cannot exceed {} players".format(self.size))
        elif self.players.values('team') > self.teams_limit:
            raise InvalidRosterException("Cannot have more than {} players from the same team on a roster".format(self.teams_limit))

        else:
            self.players[player.name] = player

    def __str__(self):
        return ", ".join([player.name for player in self.players])


class Pool:
    def __init__(self, players=[]):
        self.players = players

    def add_player(self, player):
        self.players.append(player)

    def build_rosters(self):
        """
        Create all valid permutations of the pool.
        This brute force solution is n! / r! / (n-r)! so for now just need to get the first few rosters.
        """
        # TODO: Build new way of making rosters, sort all players in pool by a value_to_cost metric, take first 8, replace until roster is valid.

        rosters = itertools.combinations_with_replacement(self.players, ROSTER_SIZE)
        r = []

        for i in range(0,50):  # Only using the first 50 roster possibilities for testing
            # r = (next(rosters))
            r.append((next(rosters)))


    def __str__(self):
        return ", ".join([player.name for player in self.players])


if __name__ == '__main__':
    vulcun_site = bs4.BeautifulSoup(open('example.html'), 'html.parser')

    # players = [player.attrs.get('id') for player in vulcun_site.select('.addplayer')]

    pool = Pool()

    for player in vulcun_site.select('.addplayer'):
        t_name = player.select('.player-name')[0].string
        t_points = float(player.select('.player-season_avg')[0].string)
        t_salary = int(player.select('.player-price')[0].string[1:])
        t_team = player.select('.player-team-name')[0].string

        # pool.add_player(Player(name, points, salary, team))
        p = Player(t_name, t_points, t_salary, t_team)
        pool.add_player(p)

    # print(pool)
    pool.build_rosters()
    print('ended')
