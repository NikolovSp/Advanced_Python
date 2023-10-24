def team_lineup(*args):
    teams = {}
    for name, country in args:
        if country not in teams:
            teams[country] = []
        teams[country].append(name)

    sorted_teams = dict(sorted(teams.items(), key=lambda kvp: (-len(kvp[1]), kvp)))
    result = []
    for country, players in sorted_teams.items():
        result.append(f'{country}:')
        for player in players:
            result.append(f'  -{player}')
    return '\n'.join(result)


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

