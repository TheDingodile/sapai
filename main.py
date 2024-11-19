from sapai.teams import Team
from sapai.battle import Battle

def timing_test():
    team0 = Team(["ant", "ox", "tiger"])
    team1 = Team(["sheep", "tiger"])
    b = Battle(team0, team1)
    winner = b.battle()

def main():
    timing_test()

if __name__ == "__main__":
    main()