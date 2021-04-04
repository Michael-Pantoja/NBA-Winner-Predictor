from teams import *
from variances import *


HOME_TEAM = 'Los Angeles Lakers'
AWAY_TEAM = 'Sacramento Kings'

if __name__ == '__main__':
    outcome = Parse(HOME_TEAM, AWAY_TEAM)
    outcome.main()
    PlayerStats = PlayerStats(outcome.homeTeamPlayerIds, outcome.awayTeamPlayerIds)
    PlayerStats.main()
