"""A module for getting the 'best' fantasy team using analytics
    1. Need to scrape html to create a player and add them to a Pool
    2. Create all potential Rosters consisting of players * ROSTER_SIZE & capped at SALARY_CAP
    3. Find the valid Roster with the highest total of points this season
    4. Maybe give the top 4 recommendations or something
    5. Incorporate last game's stats as well to see hot-streaks
"""

SALARY_CAP = 10000
ROSTER_SIZE = 8


class Player(name, points, salary):
    pass


class Pool(players=None):
    pass


class Roster(players=None):
    pass


if __name__ == '__main__':
    print 'called'
