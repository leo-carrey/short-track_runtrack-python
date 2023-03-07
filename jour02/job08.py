def fruit(type,saison):
    if type == 'fruits':
        if saison == 'hiver':
            return 'orange, mandarine et kiwi'
        elif saison == 'ete':
            return 'Poire, fraise et cassis'
    elif type == 'legume':
        if saison == 'hiver':
            return 'carotte, topinambour et endive'
        elif saison == 'ete':
            return 'artichaut, aubergine et navet'
        
print(fruit('fruits','ete'))
print(fruit('legume','hiver'))