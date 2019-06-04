def getLegalRoad(data):
    coords = []
    if data.turn == 1:
        for key in data.p1Ex:
            if key == "city" or key == "settle":
                for i in data.p1Ex[key]:
                    if i == (1, 1):
                        if (267.5, 93.75) not in data.occupiedRoads:
                            coords += [(267.5, 93.75)]
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                    if i == (2, 1):
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                    if i == (3, 1):
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (592.5, 93.75) not in data.occupiedRoads:
                            coords += [(592.5, 93.75)]
                    if i == (1, 2):
                        if (267.5, 93.75) not in data.occupiedRoads:
                            coords += [(267.5, 93.75)]
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                    if i == (2, 2):
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)] 
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)] 
                    if i == (3, 2):
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)] 
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]  
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)] 
                    if i == (4, 2):
                        if (592.5, 93.75) not in data.occupiedRoads:
                            coords += [(592.5, 93.75)] 
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)] 
                    if i == (1, 3):
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)] 
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)] 
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)] 
                    if i == (2, 3):
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)] 
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)] 
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)] 
                    if i == (3, 3):
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)] 
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)] 
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)] 
                    if i == (4, 3):
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)] 
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)] 
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                    if i == (1, 4):
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                    if i == (2, 4):
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                    if i == (3, 4):
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                    if i == (4, 4):
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                    if i == (5, 4):
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                    if i == (1, 5):
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                    if i == (2, 5):
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                    if i == (3, 5):
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                    if i == (4, 5):
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                    if i == (5, 5):
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                    if i == (1, 6):
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (105, 375) not in data.occupiedRoads:
                            coords += [(105, 375)]
                    if i == (2, 6):
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                    if i == (3, 6):
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                    if i == (4, 6):
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                    if i == (5, 6):
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                    if i == (6, 6):
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                        if (755, 375) not in data.occupiedRoads:
                            coords += [(755, 375)]
                    if i == (1, 7):
                        if (105, 375) not in data.occupiedRoads:
                            coords += [(105, 375)]
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                    if i == (2, 7):
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                    if i == (3, 7):
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                    if i == (4, 7):
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                    if i == (5, 7):
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                    if i == (6, 7):
                        if (755, 375) not in data.occupiedRoads:
                            coords += [(755, 375)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                    if i == (1, 8):
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                    if i == (2, 8):
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                    if i == (3, 8):
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                    if i == (4, 8):
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                    if i == (5, 8):
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                    if i == (1, 9):
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                    if i == (2, 9):
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                    if i == (3, 9):
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                    if i == (4, 9):
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                    if i == (5, 9):
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                    if i == (1, 10):
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                    if i == (2, 10):
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (3, 10):
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (4, 10):
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
                    if i == (1, 11):
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                        if (267.5, 656.25) not in data.occupiedRoads:
                            coords += [(267.5, 656.25)]
                    if i == (2, 11):
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                    if i == (3, 11):
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)]
                    if i == (4, 11):
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
                        if (592.5, 656.25) not in data.occupiedRoads:
                            coords += [(592.5, 656.25)]
                    if i == (1, 12):
                        if (267.5, 656.25) not in data.occupiedRoads:
                            coords += [(267.5, 656.25)]
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                    if i == (2, 12):
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                    if i == (3, 12):
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)] 
                        if (592.5, 656.25) not in data.occupiedRoads:
                            coords += [(592.5, 656.25)]
            if key == 'road':
                for i in data.p1Ex[key]:
                    if i == (267.5, 93.75):
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                    if i == (332.5, 93.75):
                        if (267.5, 93.75) not in data.occupiedRoads:
                            coords += [(267.5, 93.75)]
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                    if i == (397.5, 93.75):
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                    if i == (462.5, 93.75):
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                    if i == (527.5, 93.75):
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                        if (592.5, 93.75) not in data.occupiedRoads:
                            coords += [(592.5, 93.75)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                    if i == (592.5, 93.75):
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                    if i == (235, 150):
                        if (267.5, 93.75) not in data.occupiedRoads:
                            coords += [(267.5, 93.75)]
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                    if i == (365, 150):
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                    if i == (495, 150):
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                    if i == (625, 150):
                        if (592.5, 93.75) not in data.occupiedRoads:
                            coords += [(592.5, 93.75)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                    if i == (202.5, 206.25):
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                    if i == (267.5, 206.25):
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                    if i == (332.5, 206.25):
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                    if i == (397.5, 206.25):
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                    if i == (462.5, 206.25):
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                    if i == (527.5, 206.25):
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                    if i == (592.5, 206.25) not in data.occupiedRoads:
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                    if i == (657.5, 206.25):
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                    if i == (170, 262.5):
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                    if i == (300, 262.5):
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                    if i == (430, 262.5):
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                    if i == (560, 262.5):
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                    if i == (690, 262.5):
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                    if i == (137.5, 318.75):
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                        if (105, 375) not in data.occupiedRoads:
                            coords += [(105, 375)]
                    if i == (202.5, 318.75):
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                    if i == (267.5, 318.75):
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                    if i == (332.5, 318.75):
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                    if i == (397.5, 318.75):
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                    if i == (462.5, 318.75):
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                    if i == (527.5, 318.75):
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                    if i == (592.5, 318.75):
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                    if i == (657.5, 318.75):
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                    if i == (722.5, 318.75):
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                        if (755, 375) not in data.occupiedRoads:
                            coords += [(755, 375)]
                    if i == (105, 375):
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                    if i == (235, 375):
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                    if i == (365, 375):
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                    if i == (495, 375):
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                    if i == (625, 375):
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                    if i == (755, 375):
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                    if i == (137.5, 431.25):
                        if (105, 375) not in data.occupiedRoads:
                            coords += [(105, 375)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                    if i == (202.5, 431.25):
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                    if i == (267.5, 431.25):
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                    if i == (332.5, 431.25):
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                    if i == (397.5, 431.25):
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                    if i == (462.5, 431.25):
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                    if i == (527.5, 431.25):
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                    if i == (592.5, 431.25):
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                    if i == (657.5, 431.25):
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                    if i == (722.5, 431.25):
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                        if (755, 375) not in data.occupiedRoads:
                            coords += [(755, 375)]
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                    if i == (170, 487.5):
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                    if i == (300, 487.5):
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                    if i == (430, 487.5):
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                    if i == (560, 487.5):
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                    if i == (690, 487.5):
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                    if i == (202.5, 543.75):
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                    if i == (267.5, 543.75):
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                    if i == (332.5, 543.75):
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (397.5, 543.75):
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (462.5, 543.75):
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (527.5, 543.75):
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (592.5, 543.75):
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
                    if i == (657.5, 543.75):
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
                    if i == (235, 600):
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (267.5, 656.25) not in data.occupiedRoads:
                            coords += [(267.5, 656.25)]
                    if i == (365, 600):
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                    if i == (495, 600):
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)]
                    if i == (625, 600):
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                        if (592.5, 656.25) not in data.occupiedRoads:
                            coords += [(592.5, 656.25)]
                    if i == (267.5, 656.25):
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                    if i == (332.5, 656.25):
                        if (267.5, 656.25) not in data.occupiedRoads:
                            coords += [(267.5, 656.25)]
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (397.5, 656.25):
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (462.5, 656.25):
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (527.5, 656.25):
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                        if (592.5, 656.25) not in data.occupiedRoads:
                            coords += [(592.5, 656.25)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (592.5, 656.25):
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)]
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
    if data.turn == 2:
        for key in data.p2Ex:
            if key == "city" or key == "settle":
                for i in data.p2Ex[key]:
                    if i == (1, 1):
                        if (267.5, 93.75) not in data.occupiedRoads:
                            coords += [(267.5, 93.75)]
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                    if i == (2, 1):
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                    if i == (3, 1):
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (592.5, 93.75) not in data.occupiedRoads:
                            coords += [(592.5, 93.75)]
                    if i == (1, 2):
                        if (267.5, 93.75) not in data.occupiedRoads:
                            coords += [(267.5, 93.75)]
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                    if i == (2, 2):
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                    if i == (3, 2):
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                    if i == (4, 2):
                        if (592.5, 93.75) not in data.occupiedRoads:
                            coords += [(592.5, 93.75)]
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                    if i == (1, 3):
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                    if i == (2, 3):
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                    if i == (3, 3):
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                    if i == (4, 3):
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                    if i == (1, 4):
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                    if i == (2, 4):
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                    if i == (3, 4):
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                    if i == (4, 4):
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                    if i == (5, 4):
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                    if i == (1, 5):
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                    if i == (2, 5):
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                    if i == (3, 5):
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                    if i == (4, 5):
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                    if i == (5, 5):
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                    if i == (1, 6):
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (105, 375) not in data.occupiedRoads:
                            coords += [(105, 375)]
                    if i == (2, 6):
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                    if i == (3, 6):
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                    if i == (4, 6):
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                    if i == (5, 6):
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                    if i == (6, 6):
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                        if (755, 375) not in data.occupiedRoads:
                            coords += [(755, 375)]
                    if i == (1, 7):
                        if (105, 375) not in data.occupiedRoads:
                            coords += [(105, 375)]
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                    if i == (2, 7):
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                    if i == (3, 7):
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                    if i == (4, 7):
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                    if i == (5, 7):
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                    if i == (6, 7):
                        if (755, 375) not in data.occupiedRoads:
                            coords += [(755, 375)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                    if i == (1, 8):
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                    if i == (2, 8):
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                    if i == (3, 8):
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                    if i == (4, 8):
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                    if i == (5, 8):
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                    if i == (1, 9):
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                    if i == (2, 9):
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                    if i == (3, 9):
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                    if i == (4, 9):
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                    if i == (5, 9):
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                    if i == (1, 10):
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                    if i == (2, 10):
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (3, 10):
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (4, 10):
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
                    if i == (1, 11):
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                        if (267.5, 656.25) not in data.occupiedRoads:
                            coords += [(267.5, 656.25)]
                    if i == (2, 11):
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                    if i == (3, 11):
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)]
                    if i == (4, 11):
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
                        if (592.5, 656.25) not in data.occupiedRoads:
                            coords += [(592.5, 656.25)]
                    if i == (1, 12):
                        if (267.5, 656.25) not in data.occupiedRoads:
                            coords += [(267.5, 656.25)]
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                    if i == (2, 12):
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                    if i == (3, 12):
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)] 
                        if (592.5, 656.25) not in data.occupiedRoads:
                            coords += [(592.5, 656.25)]
            if key == 'road':
                for i in data.p2Ex[key]:
                    if i == (267.5, 93.75):
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                    if i == (332.5, 93.75):
                        if (267.5, 93.75) not in data.occupiedRoads:
                            coords += [(267.5, 93.75)]
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                    if i == (397.5, 93.75):
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                    if i == (462.5, 93.75):
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                    if i == (527.5, 93.75):
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                        if (592.5, 93.75) not in data.occupiedRoads:
                            coords += [(592.5, 93.75)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                    if i == (592.5, 93.75):
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                    if i == (235, 150):
                        if (267.5, 93.75) not in data.occupiedRoads:
                            coords += [(267.5, 93.75)]
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                    if i == (365, 150):
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                    if i == (495, 150):
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                    if i == (625, 150):
                        if (592.5, 93.75) not in data.occupiedRoads:
                            coords += [(592.5, 93.75)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                    if i == (202.5, 206.25):
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                    if i == (267.5, 206.25):
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                    if i == (332.5, 206.25):
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                    if i == (397.5, 206.25):
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                    if i == (462.5, 206.25):
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                    if i == (527.5, 206.25):
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                    if i == (592.5, 206.25) not in data.occupiedRoads:
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                    if i == (657.5, 206.25):
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                    if i == (170, 262.5):
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                    if i == (300, 262.5):
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                    if i == (430, 262.5):
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                    if i == (560, 262.5):
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                    if i == (690, 262.5):
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                    if i == (137.5, 318.75):
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                        if (105, 375) not in data.occupiedRoads:
                            coords += [(105, 375)]
                    if i == (202.5, 318.75):
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                    if i == (267.5, 318.75):
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                    if i == (332.5, 318.75):
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                    if i == (397.5, 318.75):
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                    if i == (462.5, 318.75):
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                    if i == (527.5, 318.75):
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                    if i == (592.5, 318.75):
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                    if i == (657.5, 318.75):
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                    if i == (722.5, 318.75):
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                        if (755, 375) not in data.occupiedRoads:
                            coords += [(755, 375)]
                    if i == (105, 375):
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                    if i == (235, 375):
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                    if i == (365, 375):
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                    if i == (495, 375):
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                    if i == (625, 375):
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                    if i == (755, 375):
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                    if i == (137.5, 431.25):
                        if (105, 375) not in data.occupiedRoads:
                            coords += [(105, 375)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                    if i == (202.5, 431.25):
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                    if i == (267.5, 431.25):
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                    if i == (332.5, 431.25):
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                    if i == (397.5, 431.25):
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                    if i == (462.5, 431.25):
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                    if i == (527.5, 431.25):
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                    if i == (592.5, 431.25):
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                    if i == (657.5, 431.25):
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                    if i == (722.5, 431.25):
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                        if (755, 375) not in data.occupiedRoads:
                            coords += [(755, 375)]
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                    if i == (170, 487.5):
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                    if i == (300, 487.5):
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                    if i == (430, 487.5):
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                    if i == (560, 487.5):
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                    if i == (690, 487.5):
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                    if i == (202.5, 543.75):
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                    if i == (267.5, 543.75):
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                    if i == (332.5, 543.75):
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (397.5, 543.75):
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (462.5, 543.75):
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (527.5, 543.75):
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (592.5, 543.75):
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
                    if i == (657.5, 543.75):
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
                    if i == (235, 600):
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (267.5, 656.25) not in data.occupiedRoads:
                            coords += [(267.5, 656.25)]
                    if i == (365, 600):
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                    if i == (495, 600):
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)]
                    if i == (625, 600):
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                        if (592.5, 656.25) not in data.occupiedRoads:
                            coords += [(592.5, 656.25)]
                    if i == (267.5, 656.25):
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                    if i == (332.5, 656.25):
                        if (267.5, 656.25) not in data.occupiedRoads:
                            coords += [(267.5, 656.25)]
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (397.5, 656.25):
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (462.5, 656.25):
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (527.5, 656.25):
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                        if (592.5, 656.25) not in data.occupiedRoads:
                            coords += [(592.5, 656.25)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (592.5, 656.25):
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)]
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
    if data.turn == 3:
        for key in data.p3Ex:
            if key == "city" or key == "settle":
                for i in data.p3Ex[key]:
                    if i == (1, 1):
                        if (267.5, 93.75) not in data.occupiedRoads:
                            coords += [(267.5, 93.75)]
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                    if i == (2, 1):
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                    if i == (3, 1):
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (592.5, 93.75) not in data.occupiedRoads:
                            coords += [(592.5, 93.75)]
                    if i == (1, 2):
                        if (267.5, 93.75) not in data.occupiedRoads:
                            coords += [(267.5, 93.75)]
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                    if i == (2, 2):
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                    if i == (3, 2):
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                    if i == (4, 2):
                        if (592.5, 93.75) not in data.occupiedRoads:
                            coords += [(592.5, 93.75)]
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                    if i == (1, 3):
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                    if i == (2, 3):
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                    if i == (3, 3):
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                    if i == (4, 3):
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                    if i == (1, 4):
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                    if i == (2, 4):
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                    if i == (3, 4):
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                    if i == (4, 4):
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                    if i == (5, 4):
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                    if i == (1, 5):
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                    if i == (2, 5):
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                    if i == (3, 5):
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                    if i == (4, 5):
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                    if i == (5, 5):
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                    if i == (1, 6):
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (105, 375) not in data.occupiedRoads:
                            coords += [(105, 375)]
                    if i == (2, 6):
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                    if i == (3, 6):
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                    if i == (4, 6):
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                    if i == (5, 6):
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                    if i == (6, 6):
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                        if (755, 375) not in data.occupiedRoads:
                            coords += [(755, 375)]
                    if i == (1, 7):
                        if (105, 375) not in data.occupiedRoads:
                            coords += [(105, 375)]
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                    if i == (2, 7):
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                    if i == (3, 7):
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                    if i == (4, 7):
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                    if i == (5, 7):
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                    if i == (6, 7):
                        if (755, 375) not in data.occupiedRoads:
                            coords += [(755, 375)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                    if i == (1, 8):
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                    if i == (2, 8):
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                    if i == (3, 8):
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                    if i == (4, 8):
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                    if i == (5, 8):
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                    if i == (1, 9):
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                    if i == (2, 9):
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                    if i == (3, 9):
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                    if i == (4, 9):
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                    if i == (5, 9):
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                    if i == (1, 10):
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                    if i == (2, 10):
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (3, 10):
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (4, 10):
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
                    if i == (1, 11):
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                        if (267.5, 656.25) not in data.occupiedRoads:
                            coords += [(267.5, 656.25)]
                    if i == (2, 11):
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                    if i == (3, 11):
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)]
                    if i == (4, 11):
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
                        if (592.5, 656.25) not in data.occupiedRoads:
                            coords += [(592.5, 656.25)]
                    if i == (1, 12):
                        if (267.5, 656.25) not in data.occupiedRoads:
                            coords += [(267.5, 656.25)]
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                    if i == (2, 12):
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                    if i == (3, 12):
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)] 
                        if (592.5, 656.25) not in data.occupiedRoads:
                            coords += [(592.5, 656.25)]
            if key == 'road':
                for i in data.p3Ex[key]:
                    if i == (267.5, 93.75):
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                    if i == (332.5, 93.75):
                        if (267.5, 93.75) not in data.occupiedRoads:
                            coords += [(267.5, 93.75)]
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                    if i == (397.5, 93.75):
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                    if i == (462.5, 93.75):
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                    if i == (527.5, 93.75):
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                        if (592.5, 93.75) not in data.occupiedRoads:
                            coords += [(592.5, 93.75)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                    if i == (592.5, 93.75):
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                    if i == (235, 150):
                        if (267.5, 93.75) not in data.occupiedRoads:
                            coords += [(267.5, 93.75)]
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                    if i == (365, 150):
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                    if i == (495, 150):
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                    if i == (625, 150):
                        if (592.5, 93.75) not in data.occupiedRoads:
                            coords += [(592.5, 93.75)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                    if i == (202.5, 206.25):
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                    if i == (267.5, 206.25):
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                    if i == (332.5, 206.25):
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                    if i == (397.5, 206.25):
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                    if i == (462.5, 206.25):
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                    if i == (527.5, 206.25):
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                    if i == (592.5, 206.25) not in data.occupiedRoads:
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                    if i == (657.5, 206.25):
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                    if i == (170, 262.5):
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                    if i == (300, 262.5):
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                    if i == (430, 262.5):
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                    if i == (560, 262.5):
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                    if i == (690, 262.5):
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                    if i == (137.5, 318.75):
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                        if (105, 375) not in data.occupiedRoads:
                            coords += [(105, 375)]
                    if i == (202.5, 318.75):
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                    if i == (267.5, 318.75):
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                    if i == (332.5, 318.75):
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                    if i == (397.5, 318.75):
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                    if i == (462.5, 318.75):
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                    if i == (527.5, 318.75):
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                    if i == (592.5, 318.75):
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                    if i == (657.5, 318.75):
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                    if i == (722.5, 318.75):
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                        if (755, 375) not in data.occupiedRoads:
                            coords += [(755, 375)]
                    if i == (105, 375):
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                    if i == (235, 375):
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                    if i == (365, 375):
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                    if i == (495, 375):
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                    if i == (625, 375):
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                    if i == (755, 375):
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                    if i == (137.5, 431.25):
                        if (105, 375) not in data.occupiedRoads:
                            coords += [(105, 375)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                    if i == (202.5, 431.25):
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                    if i == (267.5, 431.25):
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                    if i == (332.5, 431.25):
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                    if i == (397.5, 431.25):
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                    if i == (462.5, 431.25):
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                    if i == (527.5, 431.25):
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                    if i == (592.5, 431.25):
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                    if i == (657.5, 431.25):
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                    if i == (722.5, 431.25):
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                        if (755, 375) not in data.occupiedRoads:
                            coords += [(755, 375)]
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                    if i == (170, 487.5):
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                    if i == (300, 487.5):
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                    if i == (430, 487.5):
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                    if i == (560, 487.5):
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                    if i == (690, 487.5):
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                    if i == (202.5, 543.75):
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                    if i == (267.5, 543.75):
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                    if i == (332.5, 543.75):
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (397.5, 543.75):
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (462.5, 543.75):
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (527.5, 543.75):
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (592.5, 543.75):
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
                    if i == (657.5, 543.75):
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
                    if i == (235, 600):
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (267.5, 656.25) not in data.occupiedRoads:
                            coords += [(267.5, 656.25)]
                    if i == (365, 600):
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                    if i == (495, 600):
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)]
                    if i == (625, 600):
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                        if (592.5, 656.25) not in data.occupiedRoads:
                            coords += [(592.5, 656.25)]
                    if i == (267.5, 656.25):
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                    if i == (332.5, 656.25):
                        if (267.5, 656.25) not in data.occupiedRoads:
                            coords += [(267.5, 656.25)]
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (397.5, 656.25):
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (462.5, 656.25):
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (527.5, 656.25):
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                        if (592.5, 656.25) not in data.occupiedRoads:
                            coords += [(592.5, 656.25)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (592.5, 656.25):
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)]
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
    if data.turn == 4:
        for key in data.p4Ex:
            if key == "city" or key == "settle":
                for i in data.p4Ex[key]:
                    if i == (1, 1):
                        if (267.5, 93.75) not in data.occupiedRoads:
                            coords += [(267.5, 93.75)]
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                    if i == (2, 1):
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                    if i == (3, 1):
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (592.5, 93.75) not in data.occupiedRoads:
                            coords += [(592.5, 93.75)]
                    if i == (1, 2):
                        if (267.5, 93.75) not in data.occupiedRoads:
                            coords += [(267.5, 93.75)]
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                    if i == (2, 2):
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                    if i == (3, 2):
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                    if i == (4, 2):
                        if (592.5, 93.75) not in data.occupiedRoads:
                            coords += [(592.5, 93.75)]
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                    if i == (1, 3):
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                    if i == (2, 3):
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                    if i == (3, 3):
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                    if i == (4, 3):
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                    if i == (1, 4):
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                    if i == (2, 4):
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                    if i == (3, 4):
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                    if i == (4, 4):
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                    if i == (5, 4):
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                    if i == (1, 5):
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                    if i == (2, 5):
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                    if i == (3, 5):
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                    if i == (4, 5):
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                    if i == (5, 5):
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                    if i == (1, 6):
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (105, 375) not in data.occupiedRoads:
                            coords += [(105, 375)]
                    if i == (2, 6):
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                    if i == (3, 6):
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                    if i == (4, 6):
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                    if i == (5, 6):
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                    if i == (6, 6):
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                        if (755, 375) not in data.occupiedRoads:
                            coords += [(755, 375)]
                    if i == (1, 7):
                        if (105, 375) not in data.occupiedRoads:
                            coords += [(105, 375)]
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                    if i == (2, 7):
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                    if i == (3, 7):
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                    if i == (4, 7):
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                    if i == (5, 7):
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                    if i == (6, 7):
                        if (755, 375) not in data.occupiedRoads:
                            coords += [(755, 375)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                    if i == (1, 8):
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                    if i == (2, 8):
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                    if i == (3, 8):
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                    if i == (4, 8):
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                    if i == (5, 8):
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                    if i == (1, 9):
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                    if i == (2, 9):
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                    if i == (3, 9):
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                    if i == (4, 9):
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                    if i == (5, 9):
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                    if i == (1, 10):
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                    if i == (2, 10):
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (3, 10):
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (4, 10):
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
                    if i == (1, 11):
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                        if (267.5, 656.25) not in data.occupiedRoads:
                            coords += [(267.5, 656.25)]
                    if i == (2, 11):
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                    if i == (3, 11):
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)]
                    if i == (4, 11):
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
                        if (592.5, 656.25) not in data.occupiedRoads:
                            coords += [(592.5, 656.25)]
                    if i == (1, 12):
                        if (267.5, 656.25) not in data.occupiedRoads:
                            coords += [(267.5, 656.25)]
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                    if i == (2, 12):
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                    if i == (3, 12):
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)] 
                        if (592.5, 656.25) not in data.occupiedRoads:
                            coords += [(592.5, 656.25)]
            if key == 'road':
                for i in data.p4Ex[key]:
                    if i == (267.5, 93.75):
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                    if i == (332.5, 93.75):
                        if (267.5, 93.75) not in data.occupiedRoads:
                            coords += [(267.5, 93.75)]
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                    if i == (397.5, 93.75):
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                    if i == (462.5, 93.75):
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                    if i == (527.5, 93.75):
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                        if (592.5, 93.75) not in data.occupiedRoads:
                            coords += [(592.5, 93.75)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                    if i == (592.5, 93.75):
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                    if i == (235, 150):
                        if (267.5, 93.75) not in data.occupiedRoads:
                            coords += [(267.5, 93.75)]
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                    if i == (365, 150):
                        if (332.5, 93.75) not in data.occupiedRoads:
                            coords += [(332.5, 93.75)]
                        if (397.5, 93.75) not in data.occupiedRoads:
                            coords += [(397.5, 93.75)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                    if i == (495, 150):
                        if (462.5, 93.75) not in data.occupiedRoads:
                            coords += [(462.5, 93.75)]
                        if (527.5, 93.75) not in data.occupiedRoads:
                            coords += [(527.5, 93.75)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                    if i == (625, 150):
                        if (592.5, 93.75) not in data.occupiedRoads:
                            coords += [(592.5, 93.75)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                    if i == (202.5, 206.25):
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                    if i == (267.5, 206.25):
                        if (235, 150) not in data.occupiedRoads:
                            coords += [(235, 150)]
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                    if i == (332.5, 206.25):
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                    if i == (397.5, 206.25):
                        if (365, 150) not in data.occupiedRoads:
                            coords += [(365, 150)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                    if i == (462.5, 206.25):
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                    if i == (527.5, 206.25):
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (495, 150) not in data.occupiedRoads:
                            coords += [(495, 150)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                    if i == (592.5, 206.25) not in data.occupiedRoads:
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                    if i == (657.5, 206.25):
                        if (625, 150) not in data.occupiedRoads:
                            coords += [(625, 150)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                    if i == (170, 262.5):
                        if (202.5, 206.25) not in data.occupiedRoads:
                            coords += [(202.5, 206.25)]
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                    if i == (300, 262.5):
                        if (267.5, 206.25) not in data.occupiedRoads:
                            coords += [(267.5, 206.25)]
                        if (332.5, 206.25) not in data.occupiedRoads:
                            coords += [(332.5, 206.25)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                    if i == (430, 262.5):
                        if (397.5, 206.25) not in data.occupiedRoads:
                            coords += [(397.5, 206.25)]
                        if (462.5, 206.25) not in data.occupiedRoads:
                            coords += [(462.5, 206.25)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                    if i == (560, 262.5):
                        if (527.5, 206.25) not in data.occupiedRoads:
                            coords += [(527.5, 206.25)]
                        if (592.5, 206.25) not in data.occupiedRoads:
                            coords += [(592.5, 206.25)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                    if i == (690, 262.5):
                        if (657.5, 206.25) not in data.occupiedRoads:
                            coords += [(657.5, 206.25)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                    if i == (137.5, 318.75):
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                        if (105, 375) not in data.occupiedRoads:
                            coords += [(105, 375)]
                    if i == (202.5, 318.75):
                        if (170, 262.5) not in data.occupiedRoads:
                            coords += [(170, 262.5)]
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                    if i == (267.5, 318.75):
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                    if i == (332.5, 318.75):
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (300, 262.5) not in data.occupiedRoads:
                            coords += [(300, 262.5)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                    if i == (397.5, 318.75):
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                    if i == (462.5, 318.75):
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (430, 262.5) not in data.occupiedRoads:
                            coords += [(430, 262.5)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                    if i == (527.5, 318.75):
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                    if i == (592.5, 318.75):
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (560, 262.5) not in data.occupiedRoads:
                            coords += [(560, 262.5)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                    if i == (657.5, 318.75):
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                    if i == (722.5, 318.75):
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (690, 262.5) not in data.occupiedRoads:
                            coords += [(690, 262.5)]
                        if (755, 375) not in data.occupiedRoads:
                            coords += [(755, 375)]
                    if i == (105, 375):
                        if (137.5, 318.75) not in data.occupiedRoads:
                            coords += [(137.5, 318.75)]
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                    if i == (235, 375):
                        if (202.5, 318.75) not in data.occupiedRoads:
                            coords += [(202.5, 318.75)]
                        if (267.5, 318.75) not in data.occupiedRoads:
                            coords += [(267.5, 318.75)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                    if i == (365, 375):
                        if (332.5, 318.75) not in data.occupiedRoads:
                            coords += [(332.5, 318.75)]
                        if (397.5, 318.75) not in data.occupiedRoads:
                            coords += [(397.5, 318.75)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                    if i == (495, 375):
                        if (462.5, 318.75) not in data.occupiedRoads:
                            coords += [(462.5, 318.75)]
                        if (527.5, 318.75) not in data.occupiedRoads:
                            coords += [(527.5, 318.75)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                    if i == (625, 375):
                        if (592.5, 318.75) not in data.occupiedRoads:
                            coords += [(592.5, 318.75)]
                        if (657.5, 318.75) not in data.occupiedRoads:
                            coords += [(657.5, 318.75)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                    if i == (755, 375):
                        if (722.5, 318.75) not in data.occupiedRoads:
                            coords += [(722.5, 318.75)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                    if i == (137.5, 431.25):
                        if (105, 375) not in data.occupiedRoads:
                            coords += [(105, 375)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                    if i == (202.5, 431.25):
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                    if i == (267.5, 431.25):
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (235, 375) not in data.occupiedRoads:
                            coords += [(235, 375)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                    if i == (332.5, 431.25):
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                    if i == (397.5, 431.25):
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (365, 375) not in data.occupiedRoads:
                            coords += [(365, 375)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                    if i == (462.5, 431.25):
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                    if i == (527.5, 431.25):
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (495, 375) not in data.occupiedRoads:
                            coords += [(495, 375)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                    if i == (592.5, 431.25):
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                    if i == (657.5, 431.25):
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                        if (625, 375) not in data.occupiedRoads:
                            coords += [(625, 375)]
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                    if i == (722.5, 431.25):
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                        if (755, 375) not in data.occupiedRoads:
                            coords += [(755, 375)]
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                    if i == (170, 487.5):
                        if (137.5, 431.25) not in data.occupiedRoads:
                            coords += [(137.5, 431.25)]
                        if (202.5, 431.25) not in data.occupiedRoads:
                            coords += [(202.5, 431.25)]
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                    if i == (300, 487.5):
                        if (267.5, 431.25) not in data.occupiedRoads:
                            coords += [(267.5, 431.25)]
                        if (332.5, 431.25) not in data.occupiedRoads:
                            coords += [(332.5, 431.25)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                    if i == (430, 487.5):
                        if (397.5, 431.25) not in data.occupiedRoads:
                            coords += [(397.5, 431.25)]
                        if (462.5, 431.25) not in data.occupiedRoads:
                            coords += [(462.5, 431.25)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                    if i == (560, 487.5):
                        if (527.5, 431.25) not in data.occupiedRoads:
                            coords += [(527.5, 431.25)]
                        if (592.5, 431.25) not in data.occupiedRoads:
                            coords += [(592.5, 431.25)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                    if i == (690, 487.5):
                        if (657.5, 431.25) not in data.occupiedRoads:
                            coords += [(657.5, 431.25)]
                        if (722.5, 431.25) not in data.occupiedRoads:
                            coords += [(722.5, 431.25)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                    if i == (202.5, 543.75):
                        if (170, 487.5) not in data.occupiedRoads:
                            coords += [(170, 487.5)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                    if i == (267.5, 543.75):
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                    if i == (332.5, 543.75):
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (300, 487.5) not in data.occupiedRoads:
                            coords += [(300, 487.5)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (397.5, 543.75):
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (462.5, 543.75):
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (430, 487.5) not in data.occupiedRoads:
                            coords += [(430, 487.5)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (527.5, 543.75):
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (592.5, 543.75):
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                        if (560, 487.5) not in data.occupiedRoads:
                            coords += [(560, 487.5)]
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
                    if i == (657.5, 543.75):
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                        if (690, 487.5) not in data.occupiedRoads:
                            coords += [(690, 487.5)]
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
                    if i == (235, 600):
                        if (202.5, 543.75) not in data.occupiedRoads:
                            coords += [(202.5, 543.75)]
                        if (267.5, 543.75) not in data.occupiedRoads:
                            coords += [(267.5, 543.75)]
                        if (267.5, 656.25) not in data.occupiedRoads:
                            coords += [(267.5, 656.25)]
                    if i == (365, 600):
                        if (332.5, 543.75) not in data.occupiedRoads:
                            coords += [(332.5, 543.75)]
                        if (397.5, 543.75) not in data.occupiedRoads:
                            coords += [(397.5, 543.75)]
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                    if i == (495, 600):
                        if (462.5, 543.75) not in data.occupiedRoads:
                            coords += [(462.5, 543.75)]
                        if (527.5, 543.75) not in data.occupiedRoads:
                            coords += [(527.5, 543.75)]
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)]
                    if i == (625, 600):
                        if (592.5, 543.75) not in data.occupiedRoads:
                            coords += [(592.5, 543.75)]
                        if (657.5, 543.75) not in data.occupiedRoads:
                            coords += [(657.5, 543.75)]
                        if (592.5, 656.25) not in data.occupiedRoads:
                            coords += [(592.5, 656.25)]
                    if i == (267.5, 656.25):
                        if (235, 600) not in data.occupiedRoads:
                            coords += [(235, 600)]
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                    if i == (332.5, 656.25):
                        if (267.5, 656.25) not in data.occupiedRoads:
                            coords += [(267.5, 656.25)]
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (397.5, 656.25):
                        if (332.5, 656.25) not in data.occupiedRoads:
                            coords += [(332.5, 656.25)]
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                        if (365, 600) not in data.occupiedRoads:
                            coords += [(365, 600)]
                    if i == (462.5, 656.25):
                        if (397.5, 656.25) not in data.occupiedRoads:
                            coords += [(397.5, 656.25)]
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (527.5, 656.25):
                        if (462.5, 656.25) not in data.occupiedRoads:
                            coords += [(462.5, 656.25)]
                        if (592.5, 656.25) not in data.occupiedRoads:
                            coords += [(592.5, 656.25)]
                        if (495, 600) not in data.occupiedRoads:
                            coords += [(495, 600)]
                    if i == (592.5, 656.25):
                        if (527.5, 656.25) not in data.occupiedRoads:
                            coords += [(527.5, 656.25)]
                        if (625, 600) not in data.occupiedRoads:
                            coords += [(625, 600)]
    finalCoords = []
    for coord in coords:
        if coord not in finalCoords:
            finalCoords += [coord]
    return finalCoords