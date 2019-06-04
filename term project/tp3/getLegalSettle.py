from essentials import *

def getLegalSettle(data):
    coords = []
    if data.turn == 1:
        for key in data.p1Ex:
            if key == 'city' or key == 'settle':
                for i in data.p1Ex[key]:
                    if i == (1, 1):
                        if (267.5, 93.75) in data.p1Ex['road']:
                            if (1, 2) not in data.occupied:
                                if (235, 150) in data.p1Ex['road']:
                                    if (235, 187.5) not in coords and (1, 3) not in data.occupied:
                                        coords += [(235, 187.5)]
                        if (332.5, 93.75) in data.p1Ex['road']:
                            if (2, 2) not in data.occupied:
                                if (397.5, 93.75) in data.p1Ex['road']:
                                    if (430, 75) not in coords and (2, 1) not in data.occupied:
                                        coords += [(430, 75)]
                                if (365, 150) in data.p1Ex['road']:
                                    if (365, 187.5) not in coords and (2, 3) not in data.occupied:
                                        coords += [(365, 187.5)]
                    if i == (2, 1):
                        if (397.5, 93.75) in data.p1Ex['road']:
                            if (2, 2) not in data.occupied:
                                if (332.5, 93.75) in data.p1Ex['road']:
                                    if (300, 75) not in coords and (1, 1) not in data.occupied:
                                        coords += [(300, 75)]
                                if (365, 150) in data.p1Ex['road']:
                                    if (365, 187.5) not in coords and (2, 3) not in data.occupied:
                                        coords += [(365, 187.5)]
                        if (462.5, 93.75) in data.p1Ex['road']:
                            if (3, 2) not in data.occupied:
                                if (527.5, 93.75) in data.p1Ex['road']:
                                    if (560, 75) not in coords and (3, 1) not in data.occupied:
                                        coords += [(560, 75)]
                                if (495, 150) in data.p1Ex['road']:
                                    if (495, 187.5) not in coords and (3, 3) not in data.occupied:
                                        coords += [(495, 187.5)]
                    if i == (3, 1):
                        if (527.5, 93.75) in data.p1Ex['road']:
                            if (3, 2) not in data.occupied:
                                if (462.5, 93.75) in data.p1Ex['road']:
                                    if (430, 75) not in coords and (2, 1) not in data.occupied:
                                        coords += [(430, 75)]
                                if (495, 150) in data.p1Ex['road']:
                                    if (495, 187.5) not in coords and (3, 3) not in data.occupied:
                                        coords += [(495, 187.5)]
                        if (592.5, 93.75) in data.p1Ex['road']:
                            if (4, 2) not in data.occupied:
                                if (625, 150) in data.p1Ex['road']:
                                    if (625, 187.5) not in coords and (4, 3) not in data.occupied:
                                        coords += [(625, 187.5)]
                    if i == (1, 2):
                        if (267.5, 93.75) in data.p1Ex['road']:
                            if (1, 1) not in data.occupied:
                                if (332.5, 93.75) in data.p1Ex['road']:
                                    if (365, 112.5) not in coords and (2, 2) not in data.occupied:
                                        coords += [(365, 112.5)]
                        if (235, 150) in data.p1Ex['road']:
                            if (1, 3) not in data.occupied:
                                if (202.5, 206.25) in data.p1Ex['road']:
                                    if (170, 225) not in coords and (1, 4) not in data.occupied:
                                        coords += [(170, 225)]
                                if (267.5, 206.25) in data.p1Ex['road']:
                                    if (300, 225) not in coords and (2, 4) not in data.occupied:
                                        coords += [(300, 225)]
                    if i == (2, 2):
                        if (332.5, 93.75) in data.p1Ex['road']:
                            if (1, 1) not in data.occupied:
                                if (267.5, 93.75) in data.p1Ex['road']:
                                    if coordConverter((1, 2)) not in coords and (1, 2) not in data.occupied:
                                        coords += [coordConverter((1, 2))]
                        if (397.5, 93.75) in data.p1Ex['road']:
                            if (2, 1) not in data.occupied:
                                if (462.5, 93.75) in data.p1Ex['road']:
                                    if coordConverter((3, 2)) not in coords and (3, 2) not in data.occupied:
                                        coords += [coordConverter((3, 2))]
                        if (365, 150) in data.p1Ex['road']:
                            if (2, 3) not in data.occupied:
                                if (332.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                                if (397.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                    if i == (3, 2):
                        if (462.5, 93.75) in data.p1Ex['road']:
                            if (2, 1) not in data.occupied:
                                if (397.5, 93.75) in data.p1Ex['road']:
                                    if coordConverter((2, 2)) not in coords and (2, 2) not in data.occupied:
                                        coords += [coordConverter((2, 2))]
                        if (527.5, 93.75) in data.p1Ex['road']:
                            if (3, 1) not in data.occupied:
                                if (592.5, 93.75) in data.p1Ex['road']:
                                    if coordConverter((4, 2)) not in coords and (4, 2) not in data.occupied:
                                        coords += [coordConverter((4, 2))]
                        if (495, 150) in data.p1Ex['road']:
                            if (3, 3) not in data.occupied:
                                if (462.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                                if (527.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                    if i == (4, 2):
                        if (592.5, 93.75) in data.p1Ex['road']:
                            if (3, 1) not in data.occupied:
                                if (527.5, 93.75) in data.p1Ex['road']:
                                    if coordConverter((3, 2)) not in coords and (3, 2) not in data.occupied:
                                        coords += [coordConverter((3, 2))]
                        if (625, 150) in data.p1Ex['road']:
                            if (4, 3) not in data.occupied:
                                if (592.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                                if (657.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((5, 4)) not in coords and (5, 4) not in data.occupied:
                                        coords += [coordConverter((5, 4))]
                    if i == (1, 3):
                        if (235, 150) in data.p1Ex['road']:
                            if (1, 2) not in data.occupied:
                                if (267.5, 93.75) in data.p1Ex['road']:
                                    if coordConverter((1, 1)) not in coords and (1, 1) not in data.occupied:
                                        coords += [coordConverter((1, 1))]
                        if (202.5, 206.25) in data.p1Ex['road']:
                            if (1, 4) not in data.occupied:
                                if (170, 262.5) in data.p1Ex['road']:
                                    if coordConverter((1, 5)) not in coords and (1, 5) not in data.occupied:
                                        coords += [coordConverter((1, 5))]
                        if (267.5, 206.25) in data.p1Ex['road']:
                            if (2, 4) not in data.occupied:
                                if (332.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((2, 3)) not in coords and (2, 3) not in data.occupied:
                                        coords += [coordConverter((2, 3))]
                                if (300, 262.5) in data.p1Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                    if i == (2, 3):
                        if (365, 150) in data.p1Ex['road']:
                            if (2, 2) not in data.occupied:
                                if (332.5, 93.75) in data.p1Ex['road']:
                                    if coordConverter((1, 1)) not in coords and (1, 1) not in data.occupied:
                                        coords += [coordConverter((1, 1))]
                                if (397.5, 93.75) in data.p1Ex['road']:
                                    if coordConverter((2, 1)) not in coords and (2, 1) not in data.occupied:
                                        coords += [coordConverter((2, 1))]
                        if (332.5, 206.25) in data.p1Ex['road']:
                            if (2, 4) not in data.occupied:
                                if (267.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((1, 3)) not in coords and (1, 3) not in data.occupied:
                                        coords += [coordConverter((1, 3))]
                                if (300, 262.5) in data.p1Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                        if (397.5, 206.25) in data.p1Ex['road']:
                            if (3, 4) not in data.occupied:
                                if (462.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((3, 3)) not in coords and (3, 3) not in data.occupied:
                                        coords += [coordConverter((3, 3))]
                                if (430, 262.5) in data.p1Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                    if i == (3, 3):
                        if (495, 150) in data.p1Ex['road']:
                            if (3, 2) not in data.occupied:
                                if (462.5, 93.75) in data.p1Ex['road']:
                                    if coordConverter((2, 1)) not in coords and (2, 1) not in data.occupied:
                                        coords += [coordConverter((2, 1))]
                                if (527.5, 93.75) in data.p1Ex['road']:
                                    if coordConverter((3, 1)) not in coords and (3, 1) not in data.occupied:
                                        coords += [coordConverter((3, 1))]
                        if (462.5, 206.25) in data.p1Ex['road']:
                            if (3, 4) not in data.occupied:
                                if (397.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((2, 3)) not in coords and (2, 3) not in data.occupied:
                                        coords += [coordConverter((2, 3))]
                                if (430, 262.5) in data.p1Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                        if (527.5, 206.25) in data.p1Ex['road']:
                            if (4, 4) not in data.occupied:
                                if (592.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((4, 3)) not in coords and (4, 3) not in data.occupied:
                                        coords += [coordConverter((4, 3))]
                                if (560, 262.5) in data.p1Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                    if i == (4, 3):
                        if (625, 150) in data.p1Ex['road']:
                            if (4, 2) not in data.occupied:
                                if (592.5, 93.75) in data.p1Ex['road']:
                                    if coordConverter((3, 1)) not in coords and (3, 1) not in data.occupied:
                                        coords += [coordConverter((3, 1))]
                        if (592.5, 206.25) in data.p1Ex['road']:
                            if (4, 4) not in data.occupied:
                                if (527.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((5, 3)) not in coords and (5, 3) not in data.occupied:
                                        coords += [coordConverter((5, 3))]
                                if (560, 262.5) in data.p1Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                        if (657.5, 206.25) in data.p1Ex['road']:
                            if (5, 4) not in data.occupied:
                                if (690, 262.5) in data.p1Ex['road']:
                                    if coordConverter((5, 5)) not in coords and (5, 5) not in data.occupied:
                                        coords += [coordConverter((5, 5))]
                    if i == (1, 4):
                        if (202.5, 206.25) in data.p1Ex['road']:
                            if (1, 3) not in data.occupied:
                                if (235, 150) in data.p1Ex['road']:
                                    if coordConverter((1, 2)) not in coords and (1, 2) not in data.occupied:
                                        coords += [coordConverter((1, 2))]
                                if (267.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                        if (170, 262.5) in data.p1Ex['road']:
                            if (1, 5) not in data.occupied:
                                if (137.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((1, 6)) not in coords and (1, 6) not in data.occupied:
                                        coords += [coordConverter((1, 6))]
                                if (202.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                    if i == (2, 4):
                        if (267.5, 206.25) in data.p1Ex['road']:
                            if (1, 3) not in data.occupied:
                                if (235, 150) in data.p1Ex['road']:
                                    if coordConverter((1, 2)) not in coords and (1, 2) not in data.occupied:
                                        coords += [coordConverter((1, 2))]
                                if (202.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((1, 4)) not in coords and (1, 4) not in data.occupied:
                                        coords += [coordConverter((1, 4))]
                        if (332.5, 206.25) in data.p1Ex['road']:
                            if (2, 3) not in data.occupied:
                                if (365, 150) in data.p1Ex['road']:
                                    if coordConverter((2, 2)) not in coords and (2, 2) not in data.occupied:
                                        coords += [coordConverter((2, 2))]
                                if (397.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                        if (300, 262.5) in data.p1Ex['road']:
                            if (2, 5) not in data.occupied:
                                if (267.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                                if (332.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                    if i == (3, 4):
                        if (397.5, 206.25) in data.p1Ex['road']:
                            if (2, 3) not in data.occupied:
                                if (365, 150) in data.p1Ex['road']:
                                    if coordConverter((2, 2)) not in coords and (2, 2) not in data.occupied:
                                        coords += [coordConverter((2, 2))]
                                if (332.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                        if (462.5, 206.25) in data.p1Ex['road']:
                            if (3, 3) not in data.occupied:
                                if (495, 150) in data.p1Ex['road']:
                                    if coordConverter((3, 2)) not in coords and (3, 2) not in data.occupied:
                                        coords += [coordConverter((3, 2))]
                                if (527.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                        if (430, 262.5) in data.p1Ex['road']:
                            if (3, 5) not in data.occupied:
                                if (397.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                                if (462.5, 318.75) in data.p1Ex['road']:
                                    if  coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                    if i == (4, 4):
                        if (527.5, 206.25) in data.p1Ex['road']:
                            if (3, 3) not in data.occupied:
                                if (495, 150) in data.p1Ex['road']:
                                    if coordConverter((3, 2)) not in coords and (3, 2) not in data.occupied:
                                        coords += [coordConverter((3, 2))]
                                if (462.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                        if (592.5, 206.25) in data.p1Ex['road']:
                            if (4, 3) not in data.occupied:
                                if (625, 150) in data.p1Ex['road']:
                                    if coordConverter((4, 2)) not in coords and (4, 2) not in data.occupied:
                                        coords += [coordConverter((4, 2))]
                                if (657.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((5, 4)) not in coords and (5, 4) not in data.occupied:
                                        coords += [coordConverter((5, 4))]
                        if (560, 262.5) in data.p1Ex['road']:
                            if (4, 5) not in data.occupied:
                                if (527.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                                if (592.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                    if i == (5, 4):
                        if (657.5, 206.25) in data.p1Ex['road']:
                            if (4, 3) not in data.occupied:
                                if (625, 150) in data.p1Ex['road']:
                                    if coordConverter((4, 2)) not in coords and (4, 2) not in data.occupied:
                                        coords += [coordConverter((4, 2))]
                                if (592.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                        if (690, 262.5) in data.p1Ex['road']:
                            if (5, 5) not in data.occupied:
                                if (657.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                                if (722.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((6, 6)) not in coords and (6, 6) not in data.occupied:
                                        coords += [coordConverter((6, 6))]
                    if i == (1, 5):
                        if (170, 262.5) in data.p1Ex['road']:
                            if (1, 4) not in data.occupied:
                                if (202.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((1, 3)) not in coords and (1, 3) not in data.occupied:
                                        coords += [coordConverter((1, 3))]
                        if (137.5, 318.75) in data.p1Ex['road']:
                            if (1, 6) not in data.occupied:
                                if (105, 375) in data.p1Ex['road']:
                                    if coordConverter((1, 7)) not in coords and (1, 7) not in data.occupied:
                                        coords += [coordConverter((1, 7))]
                        if (202.5, 318.75) in data.p1Ex['road']:
                            if (2, 6) not in data.occupied:
                                if (267.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                                if (235, 375) in data.p1Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                    if i == (2, 5):
                        if (300, 262.5) in data.p1Ex['road']:
                            if (2, 4) not in data.occupied:
                                if (267.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((1, 3)) not in coords and (1, 3) not in data.occupied:
                                        coords += [coordConverter((1, 3))]
                                if (332.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((2, 3)) not in coords and (2, 3) not in data.occupied:
                                        coords += [coordConverter((2, 3))]
                        if (267.5, 318.75) in data.p1Ex['road']:
                            if (2, 6) not in data.occupied:
                                if (202.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((1, 5)) not in coords and (1, 5) not in data.occupied:
                                        coords += [coordConverter((1, 5))]
                                if (235, 375) in data.p1Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                        if (332.5, 318.75) in data.p1Ex['road']:
                            if (3, 6) not in data.occupied:
                                if (397.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                                if (365, 375) in data.p1Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                    if i == (3, 5):
                        if (430, 262.5) in data.p1Ex['road']:
                            if (3, 4) not in data.occupied:
                                if (397.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((2, 3)) not in coords and (2, 3) not in data.occupied:
                                        coords += [coordConverter((2, 3))]
                                if (462.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((3, 3)) not in coords and (3, 3) not in data.occupied:
                                        coords += [coordConverter((3, 3))]
                        if (397.5, 318.75) in data.p1Ex['road']:
                            if (3, 6) not in data.occupied:
                                if (332.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                                if (365, 375) in data.p1Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                        if (462.5, 318.75) in data.p1Ex['road']:
                            if (4, 6) not in data.occupied:
                                if (527.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                                if (495, 375) in data.p1Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                    if i == (4, 5):
                        if (527.5, 318.75) in data.p1Ex['road']:
                            if (4, 6) not in data.occupied:
                                if (462.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                                if (495, 375) in data.p1Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                        if (560, 262.5) in data.p1Ex['road']:
                            if (4, 4) not in data.occupied:
                                if (527.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((3, 3)) not in coords and (3, 3) not in data.occupied:
                                        coords += [coordConverter((3, 3))]
                                if (592.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((4, 3)) not in coords and (4, 3) not in data.occupied:
                                        coords += [coordConverter((4, 3))]
                        if (592.5, 318.75) in data.p1Ex['road']:
                            if (5, 6) not in data.occupied:
                                if (657.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((5, 5)) not in coords and (5, 5) not in data.occupied:
                                        coords += [coordConverter((5, 5))]
                                if (625, 375) in data.p1Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                    if i == (5, 5):
                        if (690, 262.5) in data.p1Ex['road']:
                            if (5, 4) not in data.occupied:
                                if (657.5, 206.25) in data.p1Ex['road']:
                                    if coordConverter((4, 3)) not in coords and (4, 3) not in data.occupied:
                                        coords += [coordConverter((4, 3))]
                        if (657.5, 318.75) in data.p1Ex['road']:
                            if (5, 6) not in data.occupied:
                                if (592.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                                if (625, 375) in data.p1Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                        if (722.5, 318.75) in data.p1Ex['road']:
                            if (6, 6) not in data.occupied:
                                if (755, 375) in data.p1Ex['road']:
                                    if coordConverter((6, 7)) not in coords and (6, 7) not in data.occupied:
                                        coords += [coordConverter((6, 7))]
                    if i == (1, 6):
                        if (137.5, 318.75) in data.p1Ex['road']:
                            if (1, 5) not in data.occupied:
                                if (170, 262.5) in data.p1Ex['road']:
                                    if coordConverter((1, 4)) not in coords and (1, 4) not in data.occupied:
                                        coords += [coordConverter((1, 4))]
                                if (202.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                        if (105, 375) in data.p1Ex['road']:
                            if (1, 7) not in data.occupied:
                                if (137.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((1, 8)) not in coords and (1, 8) not in data.occupied:
                                        coords += [coordConverter((1, 8))]
                    if i == (2, 6):
                        if (202.5, 318.75) in data.p1Ex['road']:
                            if (1, 5) not in data.occupied:
                                if (170, 262.5) in data.p1Ex['road']:
                                    if coordConverter((1, 4)) not in coords and (1, 4) not in data.occupied:
                                        coords += [coordConverter((1, 4))]
                                if (137.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((1, 6)) not in coords and (1, 6) not in data.occupied:
                                        coords += [coordConverter((1, 6))]
                        if (267.5, 318.75) in data.p1Ex['road']:
                            if (2, 5) not in data.occupied:
                                if (300, 262.5) in data.p1Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                                if (332.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                        if (235, 375) in data.p1Ex['road']:
                            if (2, 7) not in data.occupied:
                                if (202.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((1, 8)) not in coords and (1, 8) not in data.occupied:
                                        coords += [coordConverter((1, 8))]
                                if (267.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                    if i == (3, 6):
                        if (332.5, 318.75) in data.p1Ex['road']:
                            if (2, 5) not in data.occupied:
                                if (300, 262.5) in data.p1Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                                if (267.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                        if (397.5, 318.75) in data.p1Ex['road']:
                            if (3, 5) not in data.occupied:
                                if (430, 262.5) in data.p1Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                                if (462.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                        if (365, 375) in data.p1Ex['road']:
                            if (3, 7) not in data.occupied:
                                if (332.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                                if (397.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                    if i == (4, 6):
                        if (462.5, 318.75) in data.p1Ex['road']:
                            if (3, 5) not in data.occupied:
                                if (430, 262.5) in data.p1Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                                if (397.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                        if (527.5, 318.75) in data.p1Ex['road']:
                            if (4, 5) not in data.occupied:
                                if (560, 262.5) in data.p1Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                                if (592.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                        if (495, 375) in data.p1Ex['road']:
                            if (4, 7) not in data.occupied:
                                if (462.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                                if (527.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                    if i == (5, 6):
                        if (592.5, 318.75) in data.p1Ex['road']:
                            if (4, 5) not in data.occupied:
                                if (560, 262.5) in data.p1Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                                if (527.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                        if (657.5, 318.75) in data.p1Ex['road']:
                            if (5, 5) not in data.occupied:
                                if (690, 262.5) in data.p1Ex['road']:
                                    if coordConverter((5, 4)) not in coords and (5, 4) not in data.occupied:
                                        coords += [coordConverter((5, 4))]
                                if (722.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((6, 6)) not in coords and (6, 6) not in data.occupied:
                                        coords += [coordConverter((6, 6))]
                        if (625, 375) in data.p1Ex['road']:
                            if (5, 7) not in data.occupied:
                                if (592.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                                if (657.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((5, 8)) not in coords and (5, 8) not in data.occupied:
                                        coords += [coordConverter((5, 8))]
                    if i == (6, 6):
                        if (722.5, 318.75) in data.p1Ex['road']:
                            if (5, 5) not in data.occupied:
                                if (690, 262.5) in data.p1Ex['road']:
                                    if coordConverter((5, 4)) not in coords and (5, 4) not in data.occupied:
                                        coords += [coordConverter((5, 4))]
                                if (657.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                        if (755, 375) in data.p1Ex['road']:
                            if (6, 7) not in data.occupied:
                                if (722.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((5, 8)) not in coords and (5, 8) not in data.occupied:
                                        coords += [coordConverter((5, 8))]
                    if i == (1, 7):
                        if (105, 375) in data.p1Ex['road']:
                            if (1, 6) not in data.occupied:
                                if (137.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((1, 5)) not in coords and (1, 5) not in data.occupied:
                                        coords += [coordConverter((1, 5))]
                        if (137.5, 431.25) in data.p1Ex['road']:
                            if (1, 8) not in data.occupied:
                                if (202.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                                if (170, 487.5) in data.p1Ex['road']:
                                    if coordConverter((1, 9)) not in coords and (1, 9) not in data.occupied:
                                        coords += [coordConverter((1, 9))]
                    if i == (2, 7):
                        if (235, 375) in data.p1Ex['road']:
                            if (2, 6) not in data.occupied:
                                if (202.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((1, 5)) not in coords and (1, 5) not in data.occupied:
                                        coords += [coordConverter((1, 5))]
                                if (267.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                        if (202.5, 431.25) in data.p1Ex['road']:
                            if (1, 8) not in data.occupied:
                                if (137.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((1, 7)) not in coords and (1, 7) not in data.occupied:
                                        coords += [coordConverter((1, 7))]
                                if (170, 487.5) in data.p1Ex['road']:
                                    if coordConverter((1, 9)) not in coords and (1, 9) not in data.occupied:
                                        coords += [coordConverter((1, 9))]
                        if (267.5, 431.25) in data.p1Ex['road']:
                            if (2, 8) not in data.occupied:
                                if (332.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                                if (300, 487.5) in data.p1Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                    if i == (3, 7):
                        if (365, 375) in data.p1Ex['road']:
                            if (3, 6) not in data.occupied:
                                if (332.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                                if (397.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                        if (332.5, 431.25) in data.p1Ex['road']:
                            if (2, 8) not in data.occupied:
                                if (267.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                                if (300, 487.5) in data.p1Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                        if (397.5, 431.25) in data.p1Ex['road']:
                            if (3, 8) not in data.occupied:
                                if (462.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                                if (430, 487.5) in data.p1Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                    if i == (4, 7):
                        if (495, 375) in data.p1Ex['road']:
                            if (4, 6) not in data.occupied:
                                if (462.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                                if (527.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                        if (462.5, 431.25) in data.p1Ex['road']:
                            if (3, 8) not in data.occupied:
                                if (397.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                                if (430, 487.5) in data.p1Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                        if (527.5, 431.25) in data.p1Ex['road']:
                            if (4, 8) not in data.occupied:
                                if (592.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                                if (560, 487.5) in data.p1Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                    if i == (5, 7):
                        if (625, 375) in data.p1Ex['road']:
                            if (5, 6) not in data.occupied:
                                if (592.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                                if (657.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((5, 5)) not in coords and (5, 5) not in data.occupied:
                                        coords += [coordConverter((5, 5))]
                        if (592.5, 431.25) in data.p1Ex['road']:
                            if (4, 8) not in data.occupied:
                                if (527.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                                if (560, 487.5) in data.p1Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                        if (657.5, 431.25) in data.p1Ex['road']:
                            if (5, 8) not in data.occupied:
                                if (722.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((6, 7)) not in coords and (6, 7) not in data.occupied:
                                        coords += [coordConverter((6, 7))]
                                if (690, 487.5) in data.p1Ex['road']:
                                    if coordConverter((5, 9)) not in coords and (5, 9) not in data.occupied:
                                        coords += [coordConverter((5, 9))]
                    if i == (6, 7):
                        if (755, 375) in data.p1Ex['road']:
                            if (6, 6) not in data.occupied:
                                if (722.5, 318.75) in data.p1Ex['road']:
                                    if coordConverter((5, 5)) not in coords and (5, 5) not in data.occupied:
                                        coords += [coordConverter((5, 5))]
                        if (722.5, 431.25) in data.p1Ex['road']:
                            if (5, 8) not in data.occupied:
                                if (657.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                                if (690, 487.5) in data.p1Ex['road']:
                                    if coordConverter((5, 9)) not in coords and (5, 9) not in data.occupied:
                                        coords += [coordCOnverter((5, 9))]
                    if i == (1, 8):
                        if (137.5, 431.25) in data.p1Ex['road']:
                            if (1, 7) not in data.occupied:
                                if (105, 375) in data.p1Ex['road']:
                                    if coordConverter((1, 6)) not in coords and (1, 6) not in data.occupied:
                                        coords += [coordConverter((1, 6))]
                        if (202.5, 431.25) in data.p1Ex['road']:
                            if (2, 7) not in data.occupied:
                                if (235, 375) in data.p1Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                                if (267.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                        if (170, 487.5) in data.p1Ex['road']:
                            if (1, 9) not in data.occupied:
                                if (202.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((1, 10)) not in coords and (1, 10) not in data.occupied:
                                        coords += [coordConverter((1, 10))]
                    if i == (2, 8):
                        if (267.5, 431.25) in data.p1Ex['road']:
                            if (2, 7) not in data.occupied:
                                if (235, 375) in data.p1Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                                if (202.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((1, 8)) not in coords and (1, 8) not in data.occupied:
                                        coords += [coordConverter((1, 8))]
                        if (332.5, 431.25) in data.p1Ex['road']:
                            if (3, 7) not in data.occupied:
                                if (365, 375) in data.p1Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                                if (397.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                        if (300, 487.5) in data.p1Ex['road']:
                            if (2, 9) not in data.occupied:
                                if (267.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((1, 10)) not in coords and (1, 10) not in data.occupied:
                                        coords += [coordConverter((1, 10))]
                                if (332.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                    if i == (3, 8):
                        if (397.5, 431.25) in data.p1Ex['road']:
                            if (3, 7) not in data.occupied:
                                if (332.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                                if (365, 375) in data.p1Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                        if (462.5, 431.25) in data.p1Ex['road']:
                            if (4, 7) not in data.occupied:
                                if (495, 375) in data.p1Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                                if (527.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                        if (430, 487.5) in data.p1Ex['road']:
                            if (3, 9) not in data.occupied:
                                if (397.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                                if (462.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                    if i == (4, 8):
                        if (527.5, 431.25) in data.p1Ex['road']:
                            if (4, 7) not in data.occupied:
                                if (495, 375) in data.p1Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                                if (462.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                        if (592.5, 431.25) in data.p1Ex['road']:
                            if (5, 7) not in data.occupied:
                                if (625, 375) in data.p1Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                                if (657.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((5, 8)) not in coords and (5, 8) not in data.occupied:
                                        coords += [coordConverter((5, 8))]
                        if (560, 487.5) in data.p1Ex['road']:
                            if (4, 9) not in data.occupied:
                                if (527.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                                if (592.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((4, 10)) not in coords and (4, 10) not in data.occupied:
                                        coords += [coordConverter((4, 10))]
                    if i == (5, 8):
                        if (657.5, 431.25) in data.p1Ex['road']:
                            if (5, 7) not in data.occupied:
                                if (625, 375) in data.p1Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                                if (592.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                        if (722.5, 431.25) in data.p1Ex['road']:
                            if (6, 7) not in data.occupied:
                                if (755, 375) in data.p1Ex['road']:
                                    if coordConverter((6, 6)) not in coords and (6, 6) not in data.occupied:
                                        coords += [coordConverter((6, 6))]
                        if (690, 487.5) in data.p1Ex['road']:
                            if (5, 9) not in data.p1Ex['road']:
                                if (657.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((4, 10)) not in coords and (4, 10) not in data.occupied:
                                        coords += [coordConverter((4, 10))]
                    if i == (1, 9):
                        if (170, 487.5) in data.p1Ex['road']:
                            if (1, 8) not in data.occupied:
                                if (137.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((1, 7)) not in coords and (1, 7) not in data.occupied:
                                        coords += [coordConverter((1, 7))]
                                if (202.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                        if (202.5, 543.75) in data.p1Ex['road']:
                            if (1, 10) not in data.occupied:
                                if (267.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                                if (235, 600) in data.p1Ex['road']:
                                    if coordConverter((1, 11)) not in coords and (1, 11) not in data.occupied:
                                        coords += [coordConverter((1, 11))]
                    if i == (2, 9):
                        if (300, 487.5) in data.p1Ex['road']:
                            if (2, 8) not in data.occupied:
                                if (267.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                                if (332.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                        if (267.5, 543.75) in data.p1Ex['road']:
                            if (1, 10) not in data.occupied:
                                if (202.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((1, 9)) not in coords and (1, 9) not in data.occupied:
                                        coords += [coordConverter((1, 9))]
                                if (235, 600) in data.p1Ex['road']:
                                    if coordConverter((1, 11)) not in coords and (1, 11) not in data.occupied:
                                        coords += [coordConverter((1, 11))]
                        if (332.5, 543.75) in data.p1Ex['road']:
                            if (2, 10) not in data.occupied:
                                if (397.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                                if (365, 600) in data.p1Ex['road']:
                                    if coordConverter((2, 11)) not in coords and (2, 11) not in data.occupied:
                                        coords += [coordConverter((2, 11))]
                    if i == (3, 9):
                        if (430, 487.5) in data.p1Ex['road']:
                            if (3, 8) not in data.occupied:
                                if (397.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                                if (462.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                        if (397.5, 543.75) in data.p1Ex['road']:
                            if (2, 10) not in data.occupied:
                                if (332.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                                if (365, 600) in data.p1Ex['road']:
                                    if coordConverter((2, 11)) not in coords and (2, 11) not in data.occupied:
                                        coords += [coordConverter((2, 11))]
                        if (462.5, 543.75) in data.p1Ex['road']:
                            if (3, 10) not in data.occupied:
                                if (527.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                                if (495, 600) in data.p1Ex['road']:
                                    if coordConverter((3, 11)) not in coords and (3, 11) not in data.occupied:
                                        coords += [coordConverter((3, 11))]
                    if i == (4, 9):
                        if (560, 487.5) in data.p1Ex['road']:
                            if (4, 8) not in data.occupied:
                                if (527.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                                if (592.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                        if (527.5, 543.75) in data.p1Ex['road']:
                            if (3, 10) not in data.occupied:
                                if (462.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                                if (495, 600) in data.p1Ex['road']:
                                    if coordConverter((3, 11)) not in coords and (3, 11) not in data.occupied:
                                        coords += [coordConverter((3, 11))]
                        if (592.5, 543.75) in data.p1Ex['road']:
                            if (4, 10) not in data.occupied:
                                if (657.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((5, 9)) not in coords and (5, 9) not in data.occupied:
                                        coords += [coordConverter((5, 9))]
                                if (625, 600) in data.p1Ex['road']:
                                    if coordConverter((4, 11)) not in coords and (4, 11) not in data.occupied:
                                        coords += [coordConverter((4, 11))]
                    if i == (5, 9):
                        if (690, 487.5) in data.p1Ex['road']:
                            if (5, 8) not in data.occupied:
                                if (657.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                                if (722.5, 431.25) in data.p1Ex['road']:
                                    if coordConverter((6, 7)) not in coords and (6, 7) not in data.occupied:
                                        coords += [coordConverter((6, 7))]
                        if (657.5, 543.75) in data.p1Ex['road']:
                            if (4, 10) not in data.occupied:
                                if (592.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                                if (625, 600) in data.p1Ex['road']:
                                    if coordConverter((4, 11)) not in coords and (4, 11) not in data.occupied:
                                        coords += [coordConverter((4, 11))]
                    if i == (1, 10):
                        if (202.5, 543.75) in data.p1Ex['road']:
                            if (1, 9) not in data.occupied:
                                if (170, 487.5) in data.p1Ex['road']:
                                    if coordConverter((1, 8)) not in coords and (1, 8) not in data.occupied:
                                        coords += [coordConverter((1, 8))]
                        if (267.5, 543.75) in data.p1Ex['road']:
                            if (2, 9) not in data.occupied:
                                if (300, 487.5) in data.p1Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                                if (332.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                        if (235, 600) in data.p1Ex['road']:
                            if (1, 11) not in data.occupied:
                                if (267.5, 656.25) in data.p1Ex['road']:
                                    if coordConverter((1, 12)) not in coords and (1, 12) not in data.occupied:
                                        coords += [coordConverter((1, 12))]
                    if i == (2, 10):
                        if (332.5, 543.75) in data.p1Ex['road']:
                            if (2, 9) not in data.occupied:
                                if (300, 487.5) in data.p1Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                                if (267.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((1, 10)) not in coords and (1, 10) not in data.occupied:
                                        coords += [coordConverter((1, 10))]
                        if (397.5, 543.75) in data.p1Ex['road']:
                            if (3, 9) not in data.occupied:
                                if (430, 487.5) in data.p1Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                                if (462.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                        if (365, 600) in data.p1Ex['road']:
                            if (2, 11) not in data.occupied:
                                if (332.5, 656.25) in data.p1Ex['road']:
                                    if coordConverter((1, 12)) not in coords and (1, 12) not in data.occupied:
                                        coords += [coordConverter((1, 12))]
                                if (397.5, 656.25) in data.p1Ex['road']:
                                    if coordConverter((2, 12)) not in coords and (2, 12) not in data.occupied:
                                        coords += [coordConverter((2, 12))]
                    if i == (3, 10):
                        if (462.5, 543.75) in data.p1Ex['road']:
                            if (3, 9) not in data.occupied:
                                if (430, 487.5) in data.p1Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                                if (397.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                        if (527.5, 543.75) in data.p1Ex['road']:
                            if (4, 9) not in data.occupied:
                                if (560, 487.5) in data.p1Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                                if (592.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((4, 10)) not in coords and (4, 10) not in data.occupied:
                                        coords += [coordConverter((4, 10))]
                        if (495, 600) in data.p1Ex['road']:
                            if (3, 11) not in data.occupied:
                                if (462.5, 656.25) in data.p1Ex['road']:
                                    if coordConverter((2, 12)) not in coords and (2, 12) not in data.occupied:
                                        coords += [coordConverter((2, 12))]
                                if (527.5, 656.25) in data.p1Ex['road']:
                                    if coordConverter((3, 12)) not in coords and (3, 12) not in data.occupied:
                                        coords += [coordConverter((3, 12))]
                    if i == (4, 10):
                        if (657.5, 543.75) in data.p1Ex['road']:
                            if (5, 9) not in data.occupied:
                                if (690, 487.5) in data.p1Ex['road']:
                                    if coordConverter((5, 8)) not in coords and (5, 8) not in data.occupied:
                                        coords += [coordConverter(5, 8)]
                        if (592.5, 543.75) in data.p1Ex['road']:
                            if (4, 9) not in data.occupied:
                                if (560, 487.5) in data.p1Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                                if (527.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                        if (625, 600) in data.p1Ex['road']:
                            if (4, 11) not in data.occupied:
                                if (592.5, 656.25) in data.p1Ex['road']:
                                    if coordConverter((3, 12)) not in coords and (3, 12) not in data.occupied:
                                        coords += [coordConverter((3, 12))]
                    if i == (1, 11):
                        if (235, 600) in data.p1Ex['road']:
                            if (1, 10) not in data.occupied:
                                if (202.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((1, 9)) not in coords and (1, 9) not in data.occupied:
                                        coords += [coordConverter((1, 9))]
                                if (267.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                        if (267.5, 656.25) in data.p1Ex['road']:
                            if (1, 12) not in data.occupied:
                                if (332.5, 656.25) in data.p1Ex['road']:
                                    if coordConverter((2, 11)) not in coords and (2, 11) not in data.occupied:
                                        coords += [coordConverter((2, 11))]
                    if i == (2, 11):
                        if (365, 600) in data.p1Ex['road']:
                            if (2, 10) not in data.occupied:
                                if (332.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                                if (397.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                        if (332.5, 656.25) in data.p1Ex['road']:
                            if (1, 12) not in data.occupied:
                                if (267.5, 656.25) in data.p1Ex['road']:
                                    if coordConverter((1, 11)) not in coords and (1, 11) not in data.occupied:
                                        coords += [coordConverter((1, 11))]
                        if (397.5, 656.25) in data.p1Ex['road']:
                            if (2, 12) not in data.occupied:
                                if (462.5, 656.25) in data.p1Ex['road']:
                                    if coordConverter((3, 11)) not in coords and (3, 11) not in data.occupied:
                                        coords += [coordConverter((3, 11))]
                    if i == (3, 11):
                        if (495, 600) in data.p1Ex['road']:
                            if (3, 10) not in data.occupied:
                                if (462.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                                if (527.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                        if (462.5, 656.25) in data.p1Ex['road']:
                            if (2, 12) not in data.occupied:
                                if (397.5, 656.25) in data.p1Ex['road']:
                                    if coordConverter((2, 11)) not in coords and (2, 11) not in data.occupied:
                                        coords += [coordConverter((2, 11))]
                        if (527.5, 656.25) in data.p1Ex['road']:
                            if (3, 12) not in data.occupied:
                                if (592.5, 656.25) in data.p1Ex['road']:
                                    if coordConverter((4, 11)) not in coords and (4, 11) not in data.occupied:
                                        coords += [coordConverter((4, 11))]
                    if i == (4, 11):
                        if (625, 600) in data.p1Ex['road']:
                            if (4, 10) not in data.occupied:
                                if (592.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                                if (657.5, 543.75) in data.p1Ex['road']:
                                    if coordConverter((5, 9)) not in coords and (5, 9) not in data.occupied:
                                        coords += [coordConverter((5, 9))]
                        if (592.5, 656.25) in data.p1Ex['road']:
                            if (3, 12) not in data.occupied:
                                if (527.5, 656.25) in data.p1Ex['road']:
                                    if coordConveter((3, 11)) not in coords and (3, 11) not in data.occupied:
                                        coords += [coordConveter((3, 11))]
                    if i == (1, 12):
                        if (267.5, 656.25) in data.p1Ex['road']:
                            if (1, 11) not in data.occupied:
                                if (235, 600) in data.p1Ex['road']:
                                    if coordConverter((1, 10)) not in coords and (1, 10) not in data.occupied:
                                        coords += [coordConverter((1, 10))]
                        if (332.5, 656.25) in data.p1Ex['road']:
                            if (2, 11) not in data.occupied:
                                if (365, 600) in data.p1Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                                if (397.5, 656.25) in data.p1Ex['road']:
                                    if coordConverter((2, 12)) not in coords and (2, 12) not in data.occupied:
                                        coords += [coordConverter((2, 12))]
                    if i == (2, 12):
                        if (397.5, 656.25) in data.p1Ex['road']:
                            if (2, 11) not in data.occupied:
                                if (332.5, 656.25) in data.p1Ex['road']:
                                    if coordConverter((1, 12)) not in coords and (1, 12) not in data.occupied:
                                        coords += [coordConverter((1, 12))]
                                if (365, 600) in data.p1Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                        if (462.5, 656.25) in data.p1Ex['road']:
                            if (3, 11) not in data.occupied:
                                if (495, 600) in data.p1Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                                if (527.5, 656.25) in data.p1Ex['road']:
                                    if coordConverter((3, 12)) not in coords and (3, 12) not in data.occupied:
                                        coords += [coordConverter((3, 12))]
                    if i == (3, 12):
                        if (527.5, 656.25) in data.p1Ex['road']:
                            if (3, 11) not in data.occupied:
                                if (495, 600) in data.p1Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                                if (462.5, 656.25) in data.p1Ex['road']:
                                    if coordConverter((2, 12)) not in coords and (2, 12) not in data.occupied:
                                        coords += [coordConverter((2, 12))]
                        if (592.5, 656.25) in data.p1Ex['road']:
                            if (4, 11) not in data.occupied:
                                if (625, 600) in data.p1Ex['road']:
                                    if coordConverter((4, 10)) not in coords and (4, 10) not in data.occupied:
                                        coords += [coordConverter((4, 10))] 
    if data.turn == 2:
        for key in data.p2Ex:
            if key == 'city' or key == 'settle':
                for i in data.p2Ex[key]:
                    if i == (1, 1):
                        if (267.5, 93.75) in data.p2Ex['road']:
                            if (1, 2) not in data.occupied:
                                if (235, 150) in data.p2Ex['road']:
                                    if (235, 187.5) not in coords and (1, 3) not in data.occupied:
                                        coords += [(235, 187.5)]
                        if (332.5, 93.75) in data.p2Ex['road']:
                            if (2, 2) not in data.occupied:
                                if (397.5, 93.75) in data.p2Ex['road']:
                                    if (430, 75) not in coords and (2, 1) not in data.occupied:
                                        coords += [(430, 75)]
                                if (365, 150) in data.p2Ex['road']:
                                    if (365, 187.5) not in coords and (2, 3) not in data.occupied:
                                        coords += [(365, 187.5)]
                    if i == (2, 1):
                        if (397.5, 93.75) in data.p2Ex['road']:
                            if (2, 2) not in data.occupied:
                                if (332.5, 93.75) in data.p2Ex['road']:
                                    if (300, 75) not in coords and (1, 1) not in data.occupied:
                                        coords += [(300, 75)]
                                if (365, 150) in data.p2Ex['road']:
                                    if (365, 187.5) not in coords and (2, 3) not in data.occupied:
                                        coords += [(365, 187.5)]
                        if (462.5, 93.75) in data.p2Ex['road']:
                            if (3, 2) not in data.occupied:
                                if (527.5, 93.75) in data.p2Ex['road']:
                                    if (560, 75) not in coords and (3, 1) not in data.occupied:
                                        coords += [(560, 75)]
                                if (495, 150) in data.p2Ex['road']:
                                    if (495, 187.5) not in coords and (3, 3) not in data.occupied:
                                        coords += [(495, 187.5)]
                    if i == (3, 1):
                        if (527.5, 93.75) in data.p2Ex['road']:
                            if (3, 2) not in data.occupied:
                                if (462.5, 93.75) in data.p2Ex['road']:
                                    if (430, 75) not in coords and (2, 1) not in data.occupied:
                                        coords += [(430, 75)]
                                if (495, 150) in data.p2Ex['road']:
                                    if (495, 187.5) not in coords and (3, 3) not in data.occupied:
                                        coords += [(495, 187.5)]
                        if (592.5, 93.75) in data.p2Ex['road']:
                            if (4, 2) not in data.occupied:
                                if (625, 150) in data.p2Ex['road']:
                                    if (625, 187.5) not in coords and (4, 3) not in data.occupied:
                                        coords += [(625, 187.5)]
                    if i == (1, 2):
                        if (267.5, 93.75) in data.p2Ex['road']:
                            if (1, 1) not in data.occupied:
                                if (332.5, 93.75) in data.p2Ex['road']:
                                    if (365, 112.5) not in coords and (2, 2) not in data.occupied:
                                        coords += [(365, 112.5)]
                        if (235, 150) in data.p2Ex['road']:
                            if (1, 3) not in data.occupied:
                                if (202.5, 206.25) in data.p2Ex['road']:
                                    if (170, 225) not in coords and (1, 4) not in data.occupied:
                                        coords += [(170, 225)]
                                if (267.5, 206.25) in data.p2Ex['road']:
                                    if (300, 225) not in coords and (2, 4) not in data.occupied:
                                        coords += [(300, 225)]
                    if i == (2, 2):
                        if (332.5, 93.75) in data.p2Ex['road']:
                            if (1, 1) not in data.occupied:
                                if (267.5, 93.75) in data.p2Ex['road']:
                                    if coordConverter((1, 2)) not in coords and (1, 2) not in data.occupied:
                                        coords += [coordConverter((1, 2))]
                        if (397.5, 93.75) in data.p2Ex['road']:
                            if (2, 1) not in data.occupied:
                                if (462.5, 93.75) in data.p2Ex['road']:
                                    if coordConverter((3, 2)) not in coords and (3, 2) not in data.occupied:
                                        coords += [coordConverter((3, 2))]
                        if (365, 150) in data.p2Ex['road']:
                            if (2, 3) not in data.occupied:
                                if (332.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                                if (397.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                    if i == (3, 2):
                        if (462.5, 93.75) in data.p2Ex['road']:
                            if (2, 1) not in data.occupied:
                                if (397.5, 93.75) in data.p2Ex['road']:
                                    if coordConverter((2, 2)) not in coords and (2, 2) not in data.occupied:
                                        coords += [coordConverter((2, 2))]
                        if (527.5, 93.75) in data.p2Ex['road']:
                            if (3, 1) not in data.occupied:
                                if (592.5, 93.75) in data.p2Ex['road']:
                                    if coordConverter((4, 2)) not in coords and (4, 2) not in data.occupied:
                                        coords += [coordConverter((4, 2))]
                        if (495, 150) in data.p2Ex['road']:
                            if (3, 3) not in data.occupied:
                                if (462.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                                if (527.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                    if i == (4, 2):
                        if (592.5, 93.75) in data.p2Ex['road']:
                            if (3, 1) not in data.occupied:
                                if (527.5, 93.75) in data.p2Ex['road']:
                                    if coordConverter((3, 2)) not in coords and (3, 2) not in data.occupied:
                                        coords += [coordConverter((3, 2))]
                        if (625, 150) in data.p2Ex['road']:
                            if (4, 3) not in data.occupied:
                                if (592.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                                if (657.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((5, 4)) not in coords and (5, 4) not in data.occupied:
                                        coords += [coordConverter((5, 4))]
                    if i == (1, 3):
                        if (235, 150) in data.p2Ex['road']:
                            if (1, 2) not in data.occupied:
                                if (267.5, 93.75) in data.p2Ex['road']:
                                    if coordConverter((1, 1)) not in coords and (1, 1) not in data.occupied:
                                        coords += [coordConverter((1, 1))]
                        if (202.5, 206.25) in data.p2Ex['road']:
                            if (1, 4) not in data.occupied:
                                if (170, 262.5) in data.p2Ex['road']:
                                    if coordConverter((1, 5)) not in coords and (1, 5) not in data.occupied:
                                        coords += [coordConverter((1, 5))]
                        if (267.5, 206.25) in data.p2Ex['road']:
                            if (2, 4) not in data.occupied:
                                if (332.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((2, 3)) not in coords and (2, 3) not in data.occupied:
                                        coords += [coordConverter((2, 3))]
                                if (300, 262.5) in data.p2Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                    if i == (2, 3):
                        if (365, 150) in data.p2Ex['road']:
                            if (2, 2) not in data.occupied:
                                if (332.5, 93.75) in data.p2Ex['road']:
                                    if coordConverter((1, 1)) not in coords and (1, 1) not in data.occupied:
                                        coords += [coordConverter((1, 1))]
                                if (397.5, 93.75) in data.p2Ex['road']:
                                    if coordConverter((2, 1)) not in coords and (2, 1) not in data.occupied:
                                        coords += [coordConverter((2, 1))]
                        if (332.5, 206.25) in data.p2Ex['road']:
                            if (2, 4) not in data.occupied:
                                if (267.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((1, 3)) not in coords and (1, 3) not in data.occupied:
                                        coords += [coordConverter((1, 3))]
                                if (300, 262.5) in data.p2Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                        if (397.5, 206.25) in data.p2Ex['road']:
                            if (3, 4) not in data.occupied:
                                if (462.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((3, 3)) not in coords and (3, 3) not in data.occupied:
                                        coords += [coordConverter((3, 3))]
                                if (430, 262.5) in data.p2Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                    if i == (3, 3):
                        if (495, 150) in data.p2Ex['road']:
                            if (3, 2) not in data.occupied:
                                if (462.5, 93.75) in data.p2Ex['road']:
                                    if coordConverter((2, 1)) not in coords and (2, 1) not in data.occupied:
                                        coords += [coordConverter((2, 1))]
                                if (527.5, 93.75) in data.p2Ex['road']:
                                    if coordConverter((3, 1)) not in coords and (3, 1) not in data.occupied:
                                        coords += [coordConverter((3, 1))]
                        if (462.5, 206.25) in data.p2Ex['road']:
                            if (3, 4) not in data.occupied:
                                if (397.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((2, 3)) not in coords and (2, 3) not in data.occupied:
                                        coords += [coordConverter((2, 3))]
                                if (430, 262.5) in data.p2Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                        if (527.5, 206.25) in data.p2Ex['road']:
                            if (4, 4) not in data.occupied:
                                if (592.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((4, 3)) not in coords and (4, 3) not in data.occupied:
                                        coords += [coordConverter((4, 3))]
                                if (560, 262.5) in data.p2Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                    if i == (4, 3):
                        if (625, 150) in data.p2Ex['road']:
                            if (4, 2) not in data.occupied:
                                if (592.5, 93.75) in data.p2Ex['road']:
                                    if coordConverter((3, 1)) not in coords and (3, 1) not in data.occupied:
                                        coords += [coordConverter((3, 1))]
                        if (592.5, 206.25) in data.p2Ex['road']:
                            if (4, 4) not in data.occupied:
                                if (527.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((5, 3)) not in coords and (5, 3) not in data.occupied:
                                        coords += [coordConverter((5, 3))]
                                if (560, 262.5) in data.p2Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                        if (657.5, 206.25) in data.p2Ex['road']:
                            if (5, 4) not in data.occupied:
                                if (690, 262.5) in data.p2Ex['road']:
                                    if coordConverter((5, 5)) not in coords and (5, 5) not in data.occupied:
                                        coords += [coordConverter((5, 5))]
                    if i == (1, 4):
                        if (202.5, 206.25) in data.p2Ex['road']:
                            if (1, 3) not in data.occupied:
                                if (235, 150) in data.p2Ex['road']:
                                    if coordConverter((1, 2)) not in coords and (1, 2) not in data.occupied:
                                        coords += [coordConverter((1, 2))]
                                if (267.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                        if (170, 262.5) in data.p2Ex['road']:
                            if (1, 5) not in data.occupied:
                                if (137.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((1, 6)) not in coords and (1, 6) not in data.occupied:
                                        coords += [coordConverter((1, 6))]
                                if (202.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                    if i == (2, 4):
                        if (267.5, 206.25) in data.p2Ex['road']:
                            if (1, 3) not in data.occupied:
                                if (235, 150) in data.p2Ex['road']:
                                    if coordConverter((1, 2)) not in coords and (1, 2) not in data.occupied:
                                        coords += [coordConverter((1, 2))]
                                if (202.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((1, 4)) not in coords and (1, 4) not in data.occupied:
                                        coords += [coordConverter((1, 4))]
                        if (332.5, 206.25) in data.p2Ex['road']:
                            if (2, 3) not in data.occupied:
                                if (365, 150) in data.p2Ex['road']:
                                    if coordConverter((2, 2)) not in coords and (2, 2) not in data.occupied:
                                        coords += [coordConverter((2, 2))]
                                if (397.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                        if (300, 262.5) in data.p2Ex['road']:
                            if (2, 5) not in data.occupied:
                                if (267.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                                if (332.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                    if i == (3, 4):
                        if (397.5, 206.25) in data.p2Ex['road']:
                            if (2, 3) not in data.occupied:
                                if (365, 150) in data.p2Ex['road']:
                                    if coordConverter((2, 2)) not in coords and (2, 2) not in data.occupied:
                                        coords += [coordConverter((2, 2))]
                                if (332.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                        if (462.5, 206.25) in data.p2Ex['road']:
                            if (3, 3) not in data.occupied:
                                if (495, 150) in data.p2Ex['road']:
                                    if coordConverter((3, 2)) not in coords and (3, 2) not in data.occupied:
                                        coords += [coordConverter((3, 2))]
                                if (527.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                        if (430, 262.5) in data.p2Ex['road']:
                            if (3, 5) not in data.occupied:
                                if (397.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                                if (462.5, 318.75) in data.p2Ex['road']:
                                    if  coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                    if i == (4, 4):
                        if (527.5, 206.25) in data.p2Ex['road']:
                            if (3, 3) not in data.occupied:
                                if (495, 150) in data.p2Ex['road']:
                                    if coordConverter((3, 2)) not in coords and (3, 2) not in data.occupied:
                                        coords += [coordConverter((3, 2))]
                                if (462.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                        if (592.5, 206.25) in data.p2Ex['road']:
                            if (4, 3) not in data.occupied:
                                if (625, 150) in data.p2Ex['road']:
                                    if coordConverter((4, 2)) not in coords and (4, 2) not in data.occupied:
                                        coords += [coordConverter((4, 2))]
                                if (657.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((5, 4)) not in coords and (5, 4) not in data.occupied:
                                        coords += [coordConverter((5, 4))]
                        if (560, 262.5) in data.p2Ex['road']:
                            if (4, 5) not in data.occupied:
                                if (527.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                                if (592.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                    if i == (5, 4):
                        if (657.5, 206.25) in data.p2Ex['road']:
                            if (4, 3) not in data.occupied:
                                if (625, 150) in data.p2Ex['road']:
                                    if coordConverter((4, 2)) not in coords and (4, 2) not in data.occupied:
                                        coords += [coordConverter((4, 2))]
                                if (592.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                        if (690, 262.5) in data.p2Ex['road']:
                            if (5, 5) not in data.occupied:
                                if (657.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                                if (722.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((6, 6)) not in coords and (6, 6) not in data.occupied:
                                        coords += [coordConverter((6, 6))]
                    if i == (1, 5):
                        if (170, 262.5) in data.p2Ex['road']:
                            if (1, 4) not in data.occupied:
                                if (202.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((1, 3)) not in coords and (1, 3) not in data.occupied:
                                        coords += [coordConverter((1, 3))]
                        if (137.5, 318.75) in data.p2Ex['road']:
                            if (1, 6) not in data.occupied:
                                if (105, 375) in data.p2Ex['road']:
                                    if coordConverter((1, 7)) not in coords and (1, 7) not in data.occupied:
                                        coords += [coordConverter((1, 7))]
                        if (202.5, 318.75) in data.p2Ex['road']:
                            if (2, 6) not in data.occupied:
                                if (267.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                                if (235, 375) in data.p2Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                    if i == (2, 5):
                        if (300, 262.5) in data.p2Ex['road']:
                            if (2, 4) not in data.occupied:
                                if (267.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((1, 3)) not in coords and (1, 3) not in data.occupied:
                                        coords += [coordConverter((1, 3))]
                                if (332.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((2, 3)) not in coords and (2, 3) not in data.occupied:
                                        coords += [coordConverter((2, 3))]
                        if (267.5, 318.75) in data.p2Ex['road']:
                            if (2, 6) not in data.occupied:
                                if (202.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((1, 5)) not in coords and (1, 5) not in data.occupied:
                                        coords += [coordConverter((1, 5))]
                                if (235, 375) in data.p2Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                        if (332.5, 318.75) in data.p2Ex['road']:
                            if (3, 6) not in data.occupied:
                                if (397.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                                if (365, 375) in data.p2Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                    if i == (3, 5):
                        if (430, 262.5) in data.p2Ex['road']:
                            if (3, 4) not in data.occupied:
                                if (397.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((2, 3)) not in coords and (2, 3) not in data.occupied:
                                        coords += [coordConverter((2, 3))]
                                if (462.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((3, 3)) not in coords and (3, 3) not in data.occupied:
                                        coords += [coordConverter((3, 3))]
                        if (397.5, 318.75) in data.p2Ex['road']:
                            if (3, 6) not in data.occupied:
                                if (332.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                                if (365, 375) in data.p2Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                        if (462.5, 318.75) in data.p2Ex['road']:
                            if (4, 6) not in data.occupied:
                                if (527.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                                if (495, 375) in data.p2Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                    if i == (4, 5):
                        if (527.5, 318.75) in data.p2Ex['road']:
                            if (4, 6) not in data.occupied:
                                if (462.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                                if (495, 375) in data.p2Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                        if (560, 262.5) in data.p2Ex['road']:
                            if (4, 4) not in data.occupied:
                                if (527.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((3, 3)) not in coords and (3, 3) not in data.occupied:
                                        coords += [coordConverter((3, 3))]
                                if (592.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((4, 3)) not in coords and (4, 3) not in data.occupied:
                                        coords += [coordConverter((4, 3))]
                        if (592.5, 318.75) in data.p2Ex['road']:
                            if (5, 6) not in data.occupied:
                                if (657.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((5, 5)) not in coords and (5, 5) not in data.occupied:
                                        coords += [coordConverter((5, 5))]
                                if (625, 375) in data.p2Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                    if i == (5, 5):
                        if (690, 262.5) in data.p2Ex['road']:
                            if (5, 4) not in data.occupied:
                                if (657.5, 206.25) in data.p2Ex['road']:
                                    if coordConverter((4, 3)) not in coords and (4, 3) not in data.occupied:
                                        coords += [coordConverter((4, 3))]
                        if (657.5, 318.75) in data.p2Ex['road']:
                            if (5, 6) not in data.occupied:
                                if (592.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                                if (625, 375) in data.p2Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                        if (722.5, 318.75) in data.p2Ex['road']:
                            if (6, 6) not in data.occupied:
                                if (755, 375) in data.p2Ex['road']:
                                    if coordConverter((6, 7)) not in coords and (6, 7) not in data.occupied:
                                        coords += [coordConverter((6, 7))]
                    if i == (1, 6):
                        if (137.5, 318.75) in data.p2Ex['road']:
                            if (1, 5) not in data.occupied:
                                if (170, 262.5) in data.p2Ex['road']:
                                    if coordConverter((1, 4)) not in coords and (1, 4) not in data.occupied:
                                        coords += [coordConverter((1, 4))]
                                if (202.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                        if (105, 375) in data.p2Ex['road']:
                            if (1, 7) not in data.occupied:
                                if (137.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((1, 8)) not in coords and (1, 8) not in data.occupied:
                                        coords += [coordConverter((1, 8))]
                    if i == (2, 6):
                        if (202.5, 318.75) in data.p2Ex['road']:
                            if (1, 5) not in data.occupied:
                                if (170, 262.5) in data.p2Ex['road']:
                                    if coordConverter((1, 4)) not in coords and (1, 4) not in data.occupied:
                                        coords += [coordConverter((1, 4))]
                                if (137.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((1, 6)) not in coords and (1, 6) not in data.occupied:
                                        coords += [coordConverter((1, 6))]
                        if (267.5, 318.75) in data.p2Ex['road']:
                            if (2, 5) not in data.occupied:
                                if (300, 262.5) in data.p2Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                                if (332.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                        if (235, 375) in data.p2Ex['road']:
                            if (2, 7) not in data.occupied:
                                if (202.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((1, 8)) not in coords and (1, 8) not in data.occupied:
                                        coords += [coordConverter((1, 8))]
                                if (267.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                    if i == (3, 6):
                        if (332.5, 318.75) in data.p2Ex['road']:
                            if (2, 5) not in data.occupied:
                                if (300, 262.5) in data.p2Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                                if (267.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                        if (397.5, 318.75) in data.p2Ex['road']:
                            if (3, 5) not in data.occupied:
                                if (430, 262.5) in data.p2Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                                if (462.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                        if (365, 375) in data.p2Ex['road']:
                            if (3, 7) not in data.occupied:
                                if (332.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                                if (397.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                    if i == (4, 6):
                        if (462.5, 318.75) in data.p2Ex['road']:
                            if (3, 5) not in data.occupied:
                                if (430, 262.5) in data.p2Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                                if (397.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                        if (527.5, 318.75) in data.p2Ex['road']:
                            if (4, 5) not in data.occupied:
                                if (560, 262.5) in data.p2Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                                if (592.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                        if (495, 375) in data.p2Ex['road']:
                            if (4, 7) not in data.occupied:
                                if (462.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                                if (527.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                    if i == (5, 6):
                        if (592.5, 318.75) in data.p2Ex['road']:
                            if (4, 5) not in data.occupied:
                                if (560, 262.5) in data.p2Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                                if (527.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                        if (657.5, 318.75) in data.p2Ex['road']:
                            if (5, 5) not in data.occupied:
                                if (690, 262.5) in data.p2Ex['road']:
                                    if coordConverter((5, 4)) not in coords and (5, 4) not in data.occupied:
                                        coords += [coordConverter((5, 4))]
                                if (722.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((6, 6)) not in coords and (6, 6) not in data.occupied:
                                        coords += [coordConverter((6, 6))]
                        if (625, 375) in data.p2Ex['road']:
                            if (5, 7) not in data.occupied:
                                if (592.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                                if (657.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((5, 8)) not in coords and (5, 8) not in data.occupied:
                                        coords += [coordConverter((5, 8))]
                    if i == (6, 6):
                        if (722.5, 318.75) in data.p2Ex['road']:
                            if (5, 5) not in data.occupied:
                                if (690, 262.5) in data.p2Ex['road']:
                                    if coordConverter((5, 4)) not in coords and (5, 4) not in data.occupied:
                                        coords += [coordConverter((5, 4))]
                                if (657.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                        if (755, 375) in data.p2Ex['road']:
                            if (6, 7) not in data.occupied:
                                if (722.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((5, 8)) not in coords and (5, 8) not in data.occupied:
                                        coords += [coordConverter((5, 8))]
                    if i == (1, 7):
                        if (105, 375) in data.p2Ex['road']:
                            if (1, 6) not in data.occupied:
                                if (137.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((1, 5)) not in coords and (1, 5) not in data.occupied:
                                        coords += [coordConverter((1, 5))]
                        if (137.5, 431.25) in data.p2Ex['road']:
                            if (1, 8) not in data.occupied:
                                if (202.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                                if (170, 487.5) in data.p2Ex['road']:
                                    if coordConverter((1, 9)) not in coords and (1, 9) not in data.occupied:
                                        coords += [coordConverter((1, 9))]
                    if i == (2, 7):
                        if (235, 375) in data.p2Ex['road']:
                            if (2, 6) not in data.occupied:
                                if (202.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((1, 5)) not in coords and (1, 5) not in data.occupied:
                                        coords += [coordConverter((1, 5))]
                                if (267.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                        if (202.5, 431.25) in data.p2Ex['road']:
                            if (1, 8) not in data.occupied:
                                if (137.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((1, 7)) not in coords and (1, 7) not in data.occupied:
                                        coords += [coordConverter((1, 7))]
                                if (170, 487.5) in data.p2Ex['road']:
                                    if coordConverter((1, 9)) not in coords and (1, 9) not in data.occupied:
                                        coords += [coordConverter((1, 9))]
                        if (267.5, 431.25) in data.p2Ex['road']:
                            if (2, 8) not in data.occupied:
                                if (332.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                                if (300, 487.5) in data.p2Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                    if i == (3, 7):
                        if (365, 375) in data.p2Ex['road']:
                            if (3, 6) not in data.occupied:
                                if (332.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                                if (397.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                        if (332.5, 431.25) in data.p2Ex['road']:
                            if (2, 8) not in data.occupied:
                                if (267.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                                if (300, 487.5) in data.p2Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                        if (397.5, 431.25) in data.p2Ex['road']:
                            if (3, 8) not in data.occupied:
                                if (462.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                                if (430, 487.5) in data.p2Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                    if i == (4, 7):
                        if (495, 375) in data.p2Ex['road']:
                            if (4, 6) not in data.occupied:
                                if (462.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                                if (527.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                        if (462.5, 431.25) in data.p2Ex['road']:
                            if (3, 8) not in data.occupied:
                                if (397.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                                if (430, 487.5) in data.p2Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                        if (527.5, 431.25) in data.p2Ex['road']:
                            if (4, 8) not in data.occupied:
                                if (592.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                                if (560, 487.5) in data.p2Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                    if i == (5, 7):
                        if (625, 375) in data.p2Ex['road']:
                            if (5, 6) not in data.occupied:
                                if (592.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                                if (657.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((5, 5)) not in coords and (5, 5) not in data.occupied:
                                        coords += [coordConverter((5, 5))]
                        if (592.5, 431.25) in data.p2Ex['road']:
                            if (4, 8) not in data.occupied:
                                if (527.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                                if (560, 487.5) in data.p2Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                        if (657.5, 431.25) in data.p2Ex['road']:
                            if (5, 8) not in data.occupied:
                                if (722.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((6, 7)) not in coords and (6, 7) not in data.occupied:
                                        coords += [coordConverter((6, 7))]
                                if (690, 487.5) in data.p2Ex['road']:
                                    if coordConverter((5, 9)) not in coords and (5, 9) not in data.occupied:
                                        coords += [coordConverter((5, 9))]
                    if i == (6, 7):
                        if (755, 375) in data.p2Ex['road']:
                            if (6, 6) not in data.occupied:
                                if (722.5, 318.75) in data.p2Ex['road']:
                                    if coordConverter((5, 5)) not in coords and (5, 5) not in data.occupied:
                                        coords += [coordConverter((5, 5))]
                        if (722.5, 431.25) in data.p2Ex['road']:
                            if (5, 8) not in data.occupied:
                                if (657.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                                if (690, 487.5) in data.p2Ex['road']:
                                    if coordConverter((5, 9)) not in coords and (5, 9) not in data.occupied:
                                        coords += [coordCOnverter((5, 9))]
                    if i == (1, 8):
                        if (137.5, 431.25) in data.p2Ex['road']:
                            if (1, 7) not in data.occupied:
                                if (105, 375) in data.p2Ex['road']:
                                    if coordConverter((1, 6)) not in coords and (1, 6) not in data.occupied:
                                        coords += [coordConverter((1, 6))]
                        if (202.5, 431.25) in data.p2Ex['road']:
                            if (2, 7) not in data.occupied:
                                if (235, 375) in data.p2Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                                if (267.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                        if (170, 487.5) in data.p2Ex['road']:
                            if (1, 9) not in data.occupied:
                                if (202.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((1, 10)) not in coords and (1, 10) not in data.occupied:
                                        coords += [coordConverter((1, 10))]
                    if i == (2, 8):
                        if (267.5, 431.25) in data.p2Ex['road']:
                            if (2, 7) not in data.occupied:
                                if (235, 375) in data.p2Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                                if (202.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((1, 8)) not in coords and (1, 8) not in data.occupied:
                                        coords += [coordConverter((1, 8))]
                        if (332.5, 431.25) in data.p2Ex['road']:
                            if (3, 7) not in data.occupied:
                                if (365, 375) in data.p2Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                                if (397.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                        if (300, 487.5) in data.p2Ex['road']:
                            if (2, 9) not in data.occupied:
                                if (267.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((1, 10)) not in coords and (1, 10) not in data.occupied:
                                        coords += [coordConverter((1, 10))]
                                if (332.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                    if i == (3, 8):
                        if (397.5, 431.25) in data.p2Ex['road']:
                            if (3, 7) not in data.occupied:
                                if (332.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                                if (365, 375) in data.p2Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                        if (462.5, 431.25) in data.p2Ex['road']:
                            if (4, 7) not in data.occupied:
                                if (495, 375) in data.p2Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                                if (527.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                        if (430, 487.5) in data.p2Ex['road']:
                            if (3, 9) not in data.occupied:
                                if (397.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                                if (462.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                    if i == (4, 8):
                        if (527.5, 431.25) in data.p2Ex['road']:
                            if (4, 7) not in data.occupied:
                                if (495, 375) in data.p2Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                                if (462.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                        if (592.5, 431.25) in data.p2Ex['road']:
                            if (5, 7) not in data.occupied:
                                if (625, 375) in data.p2Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                                if (657.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((5, 8)) not in coords and (5, 8) not in data.occupied:
                                        coords += [coordConverter((5, 8))]
                        if (560, 487.5) in data.p2Ex['road']:
                            if (4, 9) not in data.occupied:
                                if (527.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                                if (592.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((4, 10)) not in coords and (4, 10) not in data.occupied:
                                        coords += [coordConverter((4, 10))]
                    if i == (5, 8):
                        if (657.5, 431.25) in data.p2Ex['road']:
                            if (5, 7) not in data.occupied:
                                if (625, 375) in data.p2Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                                if (592.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                        if (722.5, 431.25) in data.p2Ex['road']:
                            if (6, 7) not in data.occupied:
                                if (755, 375) in data.p2Ex['road']:
                                    if coordConverter((6, 6)) not in coords and (6, 6) not in data.occupied:
                                        coords += [coordConverter((6, 6))]
                        if (690, 487.5) in data.p2Ex['road']:
                            if (5, 9) not in data.p2Ex['road']:
                                if (657.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((4, 10)) not in coords and (4, 10) not in data.occupied:
                                        coords += [coordConverter((4, 10))]
                    if i == (1, 9):
                        if (170, 487.5) in data.p2Ex['road']:
                            if (1, 8) not in data.occupied:
                                if (137.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((1, 7)) not in coords and (1, 7) not in data.occupied:
                                        coords += [coordConverter((1, 7))]
                                if (202.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                        if (202.5, 543.75) in data.p2Ex['road']:
                            if (1, 10) not in data.occupied:
                                if (267.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                                if (235, 600) in data.p2Ex['road']:
                                    if coordConverter((1, 11)) not in coords and (1, 11) not in data.occupied:
                                        coords += [coordConverter((1, 11))]
                    if i == (2, 9):
                        if (300, 487.5) in data.p2Ex['road']:
                            if (2, 8) not in data.occupied:
                                if (267.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                                if (332.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                        if (267.5, 543.75) in data.p2Ex['road']:
                            if (1, 10) not in data.occupied:
                                if (202.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((1, 9)) not in coords and (1, 9) not in data.occupied:
                                        coords += [coordConverter((1, 9))]
                                if (235, 600) in data.p2Ex['road']:
                                    if coordConverter((1, 11)) not in coords and (1, 11) not in data.occupied:
                                        coords += [coordConverter((1, 11))]
                        if (332.5, 543.75) in data.p2Ex['road']:
                            if (2, 10) not in data.occupied:
                                if (397.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                                if (365, 600) in data.p2Ex['road']:
                                    if coordConverter((2, 11)) not in coords and (2, 11) not in data.occupied:
                                        coords += [coordConverter((2, 11))]
                    if i == (3, 9):
                        if (430, 487.5) in data.p2Ex['road']:
                            if (3, 8) not in data.occupied:
                                if (397.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                                if (462.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                        if (397.5, 543.75) in data.p2Ex['road']:
                            if (2, 10) not in data.occupied:
                                if (332.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                                if (365, 600) in data.p2Ex['road']:
                                    if coordConverter((2, 11)) not in coords and (2, 11) not in data.occupied:
                                        coords += [coordConverter((2, 11))]
                        if (462.5, 543.75) in data.p2Ex['road']:
                            if (3, 10) not in data.occupied:
                                if (527.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                                if (495, 600) in data.p2Ex['road']:
                                    if coordConverter((3, 11)) not in coords and (3, 11) not in data.occupied:
                                        coords += [coordConverter((3, 11))]
                    if i == (4, 9):
                        if (560, 487.5) in data.p2Ex['road']:
                            if (4, 8) not in data.occupied:
                                if (527.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                                if (592.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                        if (527.5, 543.75) in data.p2Ex['road']:
                            if (3, 10) not in data.occupied:
                                if (462.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                                if (495, 600) in data.p2Ex['road']:
                                    if coordConverter((3, 11)) not in coords and (3, 11) not in data.occupied:
                                        coords += [coordConverter((3, 11))]
                        if (592.5, 543.75) in data.p2Ex['road']:
                            if (4, 10) not in data.occupied:
                                if (657.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((5, 9)) not in coords and (5, 9) not in data.occupied:
                                        coords += [coordConverter((5, 9))]
                                if (625, 600) in data.p2Ex['road']:
                                    if coordConverter((4, 11)) not in coords and (4, 11) not in data.occupied:
                                        coords += [coordConverter((4, 11))]
                    if i == (5, 9):
                        if (690, 487.5) in data.p2Ex['road']:
                            if (5, 8) not in data.occupied:
                                if (657.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                                if (722.5, 431.25) in data.p2Ex['road']:
                                    if coordConverter((6, 7)) not in coords and (6, 7) not in data.occupied:
                                        coords += [coordConverter((6, 7))]
                        if (657.5, 543.75) in data.p2Ex['road']:
                            if (4, 10) not in data.occupied:
                                if (592.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                                if (625, 600) in data.p2Ex['road']:
                                    if coordConverter((4, 11)) not in coords and (4, 11) not in data.occupied:
                                        coords += [coordConverter((4, 11))]
                    if i == (1, 10):
                        if (202.5, 543.75) in data.p2Ex['road']:
                            if (1, 9) not in data.occupied:
                                if (170, 487.5) in data.p2Ex['road']:
                                    if coordConverter((1, 8)) not in coords and (1, 8) not in data.occupied:
                                        coords += [coordConverter((1, 8))]
                        if (267.5, 543.75) in data.p2Ex['road']:
                            if (2, 9) not in data.occupied:
                                if (300, 487.5) in data.p2Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                                if (332.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                        if (235, 600) in data.p2Ex['road']:
                            if (1, 11) not in data.occupied:
                                if (267.5, 656.25) in data.p2Ex['road']:
                                    if coordConverter((1, 12)) not in coords and (1, 12) not in data.occupied:
                                        coords += [coordConverter((1, 12))]
                    if i == (2, 10):
                        if (332.5, 543.75) in data.p2Ex['road']:
                            if (2, 9) not in data.occupied:
                                if (300, 487.5) in data.p2Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                                if (267.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((1, 10)) not in coords and (1, 10) not in data.occupied:
                                        coords += [coordConverter((1, 10))]
                        if (397.5, 543.75) in data.p2Ex['road']:
                            if (3, 9) not in data.occupied:
                                if (430, 487.5) in data.p2Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                                if (462.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                        if (365, 600) in data.p2Ex['road']:
                            if (2, 11) not in data.occupied:
                                if (332.5, 656.25) in data.p2Ex['road']:
                                    if coordConverter((1, 12)) not in coords and (1, 12) not in data.occupied:
                                        coords += [coordConverter((1, 12))]
                                if (397.5, 656.25) in data.p2Ex['road']:
                                    if coordConverter((2, 12)) not in coords and (2, 12) not in data.occupied:
                                        coords += [coordConverter((2, 12))]
                    if i == (3, 10):
                        if (462.5, 543.75) in data.p2Ex['road']:
                            if (3, 9) not in data.occupied:
                                if (430, 487.5) in data.p2Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                                if (397.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                        if (527.5, 543.75) in data.p2Ex['road']:
                            if (4, 9) not in data.occupied:
                                if (560, 487.5) in data.p2Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                                if (592.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((4, 10)) not in coords and (4, 10) not in data.occupied:
                                        coords += [coordConverter((4, 10))]
                        if (495, 600) in data.p2Ex['road']:
                            if (3, 11) not in data.occupied:
                                if (462.5, 656.25) in data.p2Ex['road']:
                                    if coordConverter((2, 12)) not in coords and (2, 12) not in data.occupied:
                                        coords += [coordConverter((2, 12))]
                                if (527.5, 656.25) in data.p2Ex['road']:
                                    if coordConverter((3, 12)) not in coords and (3, 12) not in data.occupied:
                                        coords += [coordConverter((3, 12))]
                    if i == (4, 10):
                        if (657.5, 543.75) in data.p2Ex['road']:
                            if (5, 9) not in data.occupied:
                                if (690, 487.5) in data.p2Ex['road']:
                                    if coordConverter((5, 8)) not in coords and (5, 8) not in data.occupied:
                                        coords += [coordConverter(5, 8)]
                        if (592.5, 543.75) in data.p2Ex['road']:
                            if (4, 9) not in data.occupied:
                                if (560, 487.5) in data.p2Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                                if (527.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                        if (625, 600) in data.p2Ex['road']:
                            if (4, 11) not in data.occupied:
                                if (592.5, 656.25) in data.p2Ex['road']:
                                    if coordConverter((3, 12)) not in coords and (3, 12) not in data.occupied:
                                        coords += [coordConverter((3, 12))]
                    if i == (1, 11):
                        if (235, 600) in data.p2Ex['road']:
                            if (1, 10) not in data.occupied:
                                if (202.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((1, 9)) not in coords and (1, 9) not in data.occupied:
                                        coords += [coordConverter((1, 9))]
                                if (267.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                        if (267.5, 656.25) in data.p2Ex['road']:
                            if (1, 12) not in data.occupied:
                                if (332.5, 656.25) in data.p2Ex['road']:
                                    if coordConverter((2, 11)) not in coords and (2, 11) not in data.occupied:
                                        coords += [coordConverter((2, 11))]
                    if i == (2, 11):
                        if (365, 600) in data.p2Ex['road']:
                            if (2, 10) not in data.occupied:
                                if (332.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                                if (397.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                        if (332.5, 656.25) in data.p2Ex['road']:
                            if (1, 12) not in data.occupied:
                                if (267.5, 656.25) in data.p2Ex['road']:
                                    if coordConverter((1, 11)) not in coords and (1, 11) not in data.occupied:
                                        coords += [coordConverter((1, 11))]
                        if (397.5, 656.25) in data.p2Ex['road']:
                            if (2, 12) not in data.occupied:
                                if (462.5, 656.25) in data.p2Ex['road']:
                                    if coordConverter((3, 11)) not in coords and (3, 11) not in data.occupied:
                                        coords += [coordConverter((3, 11))]
                    if i == (3, 11):
                        if (495, 600) in data.p2Ex['road']:
                            if (3, 10) not in data.occupied:
                                if (462.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                                if (527.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                        if (462.5, 656.25) in data.p2Ex['road']:
                            if (2, 12) not in data.occupied:
                                if (397.5, 656.25) in data.p2Ex['road']:
                                    if coordConverter((2, 11)) not in coords and (2, 11) not in data.occupied:
                                        coords += [coordConverter((2, 11))]
                        if (527.5, 656.25) in data.p2Ex['road']:
                            if (3, 12) not in data.occupied:
                                if (592.5, 656.25) in data.p2Ex['road']:
                                    if coordConverter((4, 11)) not in coords and (4, 11) not in data.occupied:
                                        coords += [coordConverter((4, 11))]
                    if i == (4, 11):
                        if (625, 600) in data.p2Ex['road']:
                            if (4, 10) not in data.occupied:
                                if (592.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                                if (657.5, 543.75) in data.p2Ex['road']:
                                    if coordConverter((5, 9)) not in coords and (5, 9) not in data.occupied:
                                        coords += [coordConverter((5, 9))]
                        if (592.5, 656.25) in data.p2Ex['road']:
                            if (3, 12) not in data.occupied:
                                if (527.5, 656.25) in data.p2Ex['road']:
                                    if coordConveter((3, 11)) not in coords and (3, 11) not in data.occupied:
                                        coords += [coordConveter((3, 11))]
                    if i == (1, 12):
                        if (267.5, 656.25) in data.p2Ex['road']:
                            if (1, 11) not in data.occupied:
                                if (235, 600) in data.p2Ex['road']:
                                    if coordConverter((1, 10)) not in coords and (1, 10) not in data.occupied:
                                        coords += [coordConverter((1, 10))]
                        if (332.5, 656.25) in data.p2Ex['road']:
                            if (2, 11) not in data.occupied:
                                if (365, 600) in data.p2Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                                if (397.5, 656.25) in data.p2Ex['road']:
                                    if coordConverter((2, 12)) not in coords and (2, 12) not in data.occupied:
                                        coords += [coordConverter((2, 12))]
                    if i == (2, 12):
                        if (397.5, 656.25) in data.p2Ex['road']:
                            if (2, 11) not in data.occupied:
                                if (332.5, 656.25) in data.p2Ex['road']:
                                    if coordConverter((1, 12)) not in coords and (1, 12) not in data.occupied:
                                        coords += [coordConverter((1, 12))]
                                if (365, 600) in data.p2Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                        if (462.5, 656.25) in data.p2Ex['road']:
                            if (3, 11) not in data.occupied:
                                if (495, 600) in data.p2Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                                if (527.5, 656.25) in data.p2Ex['road']:
                                    if coordConverter((3, 12)) not in coords and (3, 12) not in data.occupied:
                                        coords += [coordConverter((3, 12))]
                    if i == (3, 12):
                        if (527.5, 656.25) in data.p2Ex['road']:
                            if (3, 11) not in data.occupied:
                                if (495, 600) in data.p2Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                                if (462.5, 656.25) in data.p2Ex['road']:
                                    if coordConverter((2, 12)) not in coords and (2, 12) not in data.occupied:
                                        coords += [coordConverter((2, 12))]
                        if (592.5, 656.25) in data.p2Ex['road']:
                            if (4, 11) not in data.occupied:
                                if (625, 600) in data.p2Ex['road']:
                                    if coordConverter((4, 10)) not in coords and (4, 10) not in data.occupied:
                                        coords += [coordConverter((4, 10))]
    if data.turn == 3:
        for key in data.p3Ex:
            if key == 'city' or key == 'settle':
                for i in data.p3Ex[key]:
                    if i == (1, 1):
                        if (267.5, 93.75) in data.p3Ex['road']:
                            if (1, 2) not in data.occupied:
                                if (235, 150) in data.p3Ex['road']:
                                    if (235, 187.5) not in coords and (1, 3) not in data.occupied:
                                        coords += [(235, 187.5)]
                        if (332.5, 93.75) in data.p3Ex['road']:
                            if (2, 2) not in data.occupied:
                                if (397.5, 93.75) in data.p3Ex['road']:
                                    if (430, 75) not in coords and (2, 1) not in data.occupied:
                                        coords += [(430, 75)]
                                if (365, 150) in data.p3Ex['road']:
                                    if (365, 187.5) not in coords and (2, 3) not in data.occupied:
                                        coords += [(365, 187.5)]
                    if i == (2, 1):
                        if (397.5, 93.75) in data.p3Ex['road']:
                            if (2, 2) not in data.occupied:
                                if (332.5, 93.75) in data.p3Ex['road']:
                                    if (300, 75) not in coords and (1, 1) not in data.occupied:
                                        coords += [(300, 75)]
                                if (365, 150) in data.p3Ex['road']:
                                    if (365, 187.5) not in coords and (2, 3) not in data.occupied:
                                        coords += [(365, 187.5)]
                        if (462.5, 93.75) in data.p3Ex['road']:
                            if (3, 2) not in data.occupied:
                                if (527.5, 93.75) in data.p3Ex['road']:
                                    if (560, 75) not in coords and (3, 1) not in data.occupied:
                                        coords += [(560, 75)]
                                if (495, 150) in data.p3Ex['road']:
                                    if (495, 187.5) not in coords and (3, 3) not in data.occupied:
                                        coords += [(495, 187.5)]
                    if i == (3, 1):
                        if (527.5, 93.75) in data.p3Ex['road']:
                            if (3, 2) not in data.occupied:
                                if (462.5, 93.75) in data.p3Ex['road']:
                                    if (430, 75) not in coords and (2, 1) not in data.occupied:
                                        coords += [(430, 75)]
                                if (495, 150) in data.p3Ex['road']:
                                    if (495, 187.5) not in coords and (3, 3) not in data.occupied:
                                        coords += [(495, 187.5)]
                        if (592.5, 93.75) in data.p3Ex['road']:
                            if (4, 2) not in data.occupied:
                                if (625, 150) in data.p3Ex['road']:
                                    if (625, 187.5) not in coords and (4, 3) not in data.occupied:
                                        coords += [(625, 187.5)]
                    if i == (1, 2):
                        if (267.5, 93.75) in data.p3Ex['road']:
                            if (1, 1) not in data.occupied:
                                if (332.5, 93.75) in data.p3Ex['road']:
                                    if (365, 112.5) not in coords and (2, 2) not in data.occupied:
                                        coords += [(365, 112.5)]
                        if (235, 150) in data.p3Ex['road']:
                            if (1, 3) not in data.occupied:
                                if (202.5, 206.25) in data.p3Ex['road']:
                                    if (170, 225) not in coords and (1, 4) not in data.occupied:
                                        coords += [(170, 225)]
                                if (267.5, 206.25) in data.p3Ex['road']:
                                    if (300, 225) not in coords and (2, 4) not in data.occupied:
                                        coords += [(300, 225)]
                    if i == (2, 2):
                        if (332.5, 93.75) in data.p3Ex['road']:
                            if (1, 1) not in data.occupied:
                                if (267.5, 93.75) in data.p3Ex['road']:
                                    if coordConverter((1, 2)) not in coords and (1, 2) not in data.occupied:
                                        coords += [coordConverter((1, 2))]
                        if (397.5, 93.75) in data.p3Ex['road']:
                            if (2, 1) not in data.occupied:
                                if (462.5, 93.75) in data.p3Ex['road']:
                                    if coordConverter((3, 2)) not in coords and (3, 2) not in data.occupied:
                                        coords += [coordConverter((3, 2))]
                        if (365, 150) in data.p3Ex['road']:
                            if (2, 3) not in data.occupied:
                                if (332.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                                if (397.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                    if i == (3, 2):
                        if (462.5, 93.75) in data.p3Ex['road']:
                            if (2, 1) not in data.occupied:
                                if (397.5, 93.75) in data.p3Ex['road']:
                                    if coordConverter((2, 2)) not in coords and (2, 2) not in data.occupied:
                                        coords += [coordConverter((2, 2))]
                        if (527.5, 93.75) in data.p3Ex['road']:
                            if (3, 1) not in data.occupied:
                                if (592.5, 93.75) in data.p3Ex['road']:
                                    if coordConverter((4, 2)) not in coords and (4, 2) not in data.occupied:
                                        coords += [coordConverter((4, 2))]
                        if (495, 150) in data.p3Ex['road']:
                            if (3, 3) not in data.occupied:
                                if (462.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                                if (527.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                    if i == (4, 2):
                        if (592.5, 93.75) in data.p3Ex['road']:
                            if (3, 1) not in data.occupied:
                                if (527.5, 93.75) in data.p3Ex['road']:
                                    if coordConverter((3, 2)) not in coords and (3, 2) not in data.occupied:
                                        coords += [coordConverter((3, 2))]
                        if (625, 150) in data.p3Ex['road']:
                            if (4, 3) not in data.occupied:
                                if (592.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                                if (657.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((5, 4)) not in coords and (5, 4) not in data.occupied:
                                        coords += [coordConverter((5, 4))]
                    if i == (1, 3):
                        if (235, 150) in data.p3Ex['road']:
                            if (1, 2) not in data.occupied:
                                if (267.5, 93.75) in data.p3Ex['road']:
                                    if coordConverter((1, 1)) not in coords and (1, 1) not in data.occupied:
                                        coords += [coordConverter((1, 1))]
                        if (202.5, 206.25) in data.p3Ex['road']:
                            if (1, 4) not in data.occupied:
                                if (170, 262.5) in data.p3Ex['road']:
                                    if coordConverter((1, 5)) not in coords and (1, 5) not in data.occupied:
                                        coords += [coordConverter((1, 5))]
                        if (267.5, 206.25) in data.p3Ex['road']:
                            if (2, 4) not in data.occupied:
                                if (332.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((2, 3)) not in coords and (2, 3) not in data.occupied:
                                        coords += [coordConverter((2, 3))]
                                if (300, 262.5) in data.p3Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                    if i == (2, 3):
                        if (365, 150) in data.p3Ex['road']:
                            if (2, 2) not in data.occupied:
                                if (332.5, 93.75) in data.p3Ex['road']:
                                    if coordConverter((1, 1)) not in coords and (1, 1) not in data.occupied:
                                        coords += [coordConverter((1, 1))]
                                if (397.5, 93.75) in data.p3Ex['road']:
                                    if coordConverter((2, 1)) not in coords and (2, 1) not in data.occupied:
                                        coords += [coordConverter((2, 1))]
                        if (332.5, 206.25) in data.p3Ex['road']:
                            if (2, 4) not in data.occupied:
                                if (267.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((1, 3)) not in coords and (1, 3) not in data.occupied:
                                        coords += [coordConverter((1, 3))]
                                if (300, 262.5) in data.p3Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                        if (397.5, 206.25) in data.p3Ex['road']:
                            if (3, 4) not in data.occupied:
                                if (462.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((3, 3)) not in coords and (3, 3) not in data.occupied:
                                        coords += [coordConverter((3, 3))]
                                if (430, 262.5) in data.p3Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                    if i == (3, 3):
                        if (495, 150) in data.p3Ex['road']:
                            if (3, 2) not in data.occupied:
                                if (462.5, 93.75) in data.p3Ex['road']:
                                    if coordConverter((2, 1)) not in coords and (2, 1) not in data.occupied:
                                        coords += [coordConverter((2, 1))]
                                if (527.5, 93.75) in data.p3Ex['road']:
                                    if coordConverter((3, 1)) not in coords and (3, 1) not in data.occupied:
                                        coords += [coordConverter((3, 1))]
                        if (462.5, 206.25) in data.p3Ex['road']:
                            if (3, 4) not in data.occupied:
                                if (397.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((2, 3)) not in coords and (2, 3) not in data.occupied:
                                        coords += [coordConverter((2, 3))]
                                if (430, 262.5) in data.p3Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                        if (527.5, 206.25) in data.p3Ex['road']:
                            if (4, 4) not in data.occupied:
                                if (592.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((4, 3)) not in coords and (4, 3) not in data.occupied:
                                        coords += [coordConverter((4, 3))]
                                if (560, 262.5) in data.p3Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                    if i == (4, 3):
                        if (625, 150) in data.p3Ex['road']:
                            if (4, 2) not in data.occupied:
                                if (592.5, 93.75) in data.p3Ex['road']:
                                    if coordConverter((3, 1)) not in coords and (3, 1) not in data.occupied:
                                        coords += [coordConverter((3, 1))]
                        if (592.5, 206.25) in data.p3Ex['road']:
                            if (4, 4) not in data.occupied:
                                if (527.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((5, 3)) not in coords and (5, 3) not in data.occupied:
                                        coords += [coordConverter((5, 3))]
                                if (560, 262.5) in data.p3Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                        if (657.5, 206.25) in data.p3Ex['road']:
                            if (5, 4) not in data.occupied:
                                if (690, 262.5) in data.p3Ex['road']:
                                    if coordConverter((5, 5)) not in coords and (5, 5) not in data.occupied:
                                        coords += [coordConverter((5, 5))]
                    if i == (1, 4):
                        if (202.5, 206.25) in data.p3Ex['road']:
                            if (1, 3) not in data.occupied:
                                if (235, 150) in data.p3Ex['road']:
                                    if coordConverter((1, 2)) not in coords and (1, 2) not in data.occupied:
                                        coords += [coordConverter((1, 2))]
                                if (267.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                        if (170, 262.5) in data.p3Ex['road']:
                            if (1, 5) not in data.occupied:
                                if (137.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((1, 6)) not in coords and (1, 6) not in data.occupied:
                                        coords += [coordConverter((1, 6))]
                                if (202.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                    if i == (2, 4):
                        if (267.5, 206.25) in data.p3Ex['road']:
                            if (1, 3) not in data.occupied:
                                if (235, 150) in data.p3Ex['road']:
                                    if coordConverter((1, 2)) not in coords and (1, 2) not in data.occupied:
                                        coords += [coordConverter((1, 2))]
                                if (202.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((1, 4)) not in coords and (1, 4) not in data.occupied:
                                        coords += [coordConverter((1, 4))]
                        if (332.5, 206.25) in data.p3Ex['road']:
                            if (2, 3) not in data.occupied:
                                if (365, 150) in data.p3Ex['road']:
                                    if coordConverter((2, 2)) not in coords and (2, 2) not in data.occupied:
                                        coords += [coordConverter((2, 2))]
                                if (397.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                        if (300, 262.5) in data.p3Ex['road']:
                            if (2, 5) not in data.occupied:
                                if (267.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                                if (332.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                    if i == (3, 4):
                        if (397.5, 206.25) in data.p3Ex['road']:
                            if (2, 3) not in data.occupied:
                                if (365, 150) in data.p3Ex['road']:
                                    if coordConverter((2, 2)) not in coords and (2, 2) not in data.occupied:
                                        coords += [coordConverter((2, 2))]
                                if (332.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                        if (462.5, 206.25) in data.p3Ex['road']:
                            if (3, 3) not in data.occupied:
                                if (495, 150) in data.p3Ex['road']:
                                    if coordConverter((3, 2)) not in coords and (3, 2) not in data.occupied:
                                        coords += [coordConverter((3, 2))]
                                if (527.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                        if (430, 262.5) in data.p3Ex['road']:
                            if (3, 5) not in data.occupied:
                                if (397.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                                if (462.5, 318.75) in data.p3Ex['road']:
                                    if  coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                    if i == (4, 4):
                        if (527.5, 206.25) in data.p3Ex['road']:
                            if (3, 3) not in data.occupied:
                                if (495, 150) in data.p3Ex['road']:
                                    if coordConverter((3, 2)) not in coords and (3, 2) not in data.occupied:
                                        coords += [coordConverter((3, 2))]
                                if (462.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                        if (592.5, 206.25) in data.p3Ex['road']:
                            if (4, 3) not in data.occupied:
                                if (625, 150) in data.p3Ex['road']:
                                    if coordConverter((4, 2)) not in coords and (4, 2) not in data.occupied:
                                        coords += [coordConverter((4, 2))]
                                if (657.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((5, 4)) not in coords and (5, 4) not in data.occupied:
                                        coords += [coordConverter((5, 4))]
                        if (560, 262.5) in data.p3Ex['road']:
                            if (4, 5) not in data.occupied:
                                if (527.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                                if (592.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                    if i == (5, 4):
                        if (657.5, 206.25) in data.p3Ex['road']:
                            if (4, 3) not in data.occupied:
                                if (625, 150) in data.p3Ex['road']:
                                    if coordConverter((4, 2)) not in coords and (4, 2) not in data.occupied:
                                        coords += [coordConverter((4, 2))]
                                if (592.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                        if (690, 262.5) in data.p3Ex['road']:
                            if (5, 5) not in data.occupied:
                                if (657.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                                if (722.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((6, 6)) not in coords and (6, 6) not in data.occupied:
                                        coords += [coordConverter((6, 6))]
                    if i == (1, 5):
                        if (170, 262.5) in data.p3Ex['road']:
                            if (1, 4) not in data.occupied:
                                if (202.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((1, 3)) not in coords and (1, 3) not in data.occupied:
                                        coords += [coordConverter((1, 3))]
                        if (137.5, 318.75) in data.p3Ex['road']:
                            if (1, 6) not in data.occupied:
                                if (105, 375) in data.p3Ex['road']:
                                    if coordConverter((1, 7)) not in coords and (1, 7) not in data.occupied:
                                        coords += [coordConverter((1, 7))]
                        if (202.5, 318.75) in data.p3Ex['road']:
                            if (2, 6) not in data.occupied:
                                if (267.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                                if (235, 375) in data.p3Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                    if i == (2, 5):
                        if (300, 262.5) in data.p3Ex['road']:
                            if (2, 4) not in data.occupied:
                                if (267.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((1, 3)) not in coords and (1, 3) not in data.occupied:
                                        coords += [coordConverter((1, 3))]
                                if (332.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((2, 3)) not in coords and (2, 3) not in data.occupied:
                                        coords += [coordConverter((2, 3))]
                        if (267.5, 318.75) in data.p3Ex['road']:
                            if (2, 6) not in data.occupied:
                                if (202.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((1, 5)) not in coords and (1, 5) not in data.occupied:
                                        coords += [coordConverter((1, 5))]
                                if (235, 375) in data.p3Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                        if (332.5, 318.75) in data.p3Ex['road']:
                            if (3, 6) not in data.occupied:
                                if (397.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                                if (365, 375) in data.p3Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                    if i == (3, 5):
                        if (430, 262.5) in data.p3Ex['road']:
                            if (3, 4) not in data.occupied:
                                if (397.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((2, 3)) not in coords and (2, 3) not in data.occupied:
                                        coords += [coordConverter((2, 3))]
                                if (462.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((3, 3)) not in coords and (3, 3) not in data.occupied:
                                        coords += [coordConverter((3, 3))]
                        if (397.5, 318.75) in data.p3Ex['road']:
                            if (3, 6) not in data.occupied:
                                if (332.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                                if (365, 375) in data.p3Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                        if (462.5, 318.75) in data.p3Ex['road']:
                            if (4, 6) not in data.occupied:
                                if (527.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                                if (495, 375) in data.p3Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                    if i == (4, 5):
                        if (527.5, 318.75) in data.p3Ex['road']:
                            if (4, 6) not in data.occupied:
                                if (462.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                                if (495, 375) in data.p3Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                        if (560, 262.5) in data.p3Ex['road']:
                            if (4, 4) not in data.occupied:
                                if (527.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((3, 3)) not in coords and (3, 3) not in data.occupied:
                                        coords += [coordConverter((3, 3))]
                                if (592.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((4, 3)) not in coords and (4, 3) not in data.occupied:
                                        coords += [coordConverter((4, 3))]
                        if (592.5, 318.75) in data.p3Ex['road']:
                            if (5, 6) not in data.occupied:
                                if (657.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((5, 5)) not in coords and (5, 5) not in data.occupied:
                                        coords += [coordConverter((5, 5))]
                                if (625, 375) in data.p3Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                    if i == (5, 5):
                        if (690, 262.5) in data.p3Ex['road']:
                            if (5, 4) not in data.occupied:
                                if (657.5, 206.25) in data.p3Ex['road']:
                                    if coordConverter((4, 3)) not in coords and (4, 3) not in data.occupied:
                                        coords += [coordConverter((4, 3))]
                        if (657.5, 318.75) in data.p3Ex['road']:
                            if (5, 6) not in data.occupied:
                                if (592.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                                if (625, 375) in data.p3Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                        if (722.5, 318.75) in data.p3Ex['road']:
                            if (6, 6) not in data.occupied:
                                if (755, 375) in data.p3Ex['road']:
                                    if coordConverter((6, 7)) not in coords and (6, 7) not in data.occupied:
                                        coords += [coordConverter((6, 7))]
                    if i == (1, 6):
                        if (137.5, 318.75) in data.p3Ex['road']:
                            if (1, 5) not in data.occupied:
                                if (170, 262.5) in data.p3Ex['road']:
                                    if coordConverter((1, 4)) not in coords and (1, 4) not in data.occupied:
                                        coords += [coordConverter((1, 4))]
                                if (202.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                        if (105, 375) in data.p3Ex['road']:
                            if (1, 7) not in data.occupied:
                                if (137.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((1, 8)) not in coords and (1, 8) not in data.occupied:
                                        coords += [coordConverter((1, 8))]
                    if i == (2, 6):
                        if (202.5, 318.75) in data.p3Ex['road']:
                            if (1, 5) not in data.occupied:
                                if (170, 262.5) in data.p3Ex['road']:
                                    if coordConverter((1, 4)) not in coords and (1, 4) not in data.occupied:
                                        coords += [coordConverter((1, 4))]
                                if (137.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((1, 6)) not in coords and (1, 6) not in data.occupied:
                                        coords += [coordConverter((1, 6))]
                        if (267.5, 318.75) in data.p3Ex['road']:
                            if (2, 5) not in data.occupied:
                                if (300, 262.5) in data.p3Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                                if (332.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                        if (235, 375) in data.p3Ex['road']:
                            if (2, 7) not in data.occupied:
                                if (202.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((1, 8)) not in coords and (1, 8) not in data.occupied:
                                        coords += [coordConverter((1, 8))]
                                if (267.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                    if i == (3, 6):
                        if (332.5, 318.75) in data.p3Ex['road']:
                            if (2, 5) not in data.occupied:
                                if (300, 262.5) in data.p3Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                                if (267.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                        if (397.5, 318.75) in data.p3Ex['road']:
                            if (3, 5) not in data.occupied:
                                if (430, 262.5) in data.p3Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                                if (462.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                        if (365, 375) in data.p3Ex['road']:
                            if (3, 7) not in data.occupied:
                                if (332.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                                if (397.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                    if i == (4, 6):
                        if (462.5, 318.75) in data.p3Ex['road']:
                            if (3, 5) not in data.occupied:
                                if (430, 262.5) in data.p3Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                                if (397.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                        if (527.5, 318.75) in data.p3Ex['road']:
                            if (4, 5) not in data.occupied:
                                if (560, 262.5) in data.p3Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                                if (592.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                        if (495, 375) in data.p3Ex['road']:
                            if (4, 7) not in data.occupied:
                                if (462.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                                if (527.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                    if i == (5, 6):
                        if (592.5, 318.75) in data.p3Ex['road']:
                            if (4, 5) not in data.occupied:
                                if (560, 262.5) in data.p3Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                                if (527.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                        if (657.5, 318.75) in data.p3Ex['road']:
                            if (5, 5) not in data.occupied:
                                if (690, 262.5) in data.p3Ex['road']:
                                    if coordConverter((5, 4)) not in coords and (5, 4) not in data.occupied:
                                        coords += [coordConverter((5, 4))]
                                if (722.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((6, 6)) not in coords and (6, 6) not in data.occupied:
                                        coords += [coordConverter((6, 6))]
                        if (625, 375) in data.p3Ex['road']:
                            if (5, 7) not in data.occupied:
                                if (592.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                                if (657.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((5, 8)) not in coords and (5, 8) not in data.occupied:
                                        coords += [coordConverter((5, 8))]
                    if i == (6, 6):
                        if (722.5, 318.75) in data.p3Ex['road']:
                            if (5, 5) not in data.occupied:
                                if (690, 262.5) in data.p3Ex['road']:
                                    if coordConverter((5, 4)) not in coords and (5, 4) not in data.occupied:
                                        coords += [coordConverter((5, 4))]
                                if (657.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                        if (755, 375) in data.p3Ex['road']:
                            if (6, 7) not in data.occupied:
                                if (722.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((5, 8)) not in coords and (5, 8) not in data.occupied:
                                        coords += [coordConverter((5, 8))]
                    if i == (1, 7):
                        if (105, 375) in data.p3Ex['road']:
                            if (1, 6) not in data.occupied:
                                if (137.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((1, 5)) not in coords and (1, 5) not in data.occupied:
                                        coords += [coordConverter((1, 5))]
                        if (137.5, 431.25) in data.p3Ex['road']:
                            if (1, 8) not in data.occupied:
                                if (202.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                                if (170, 487.5) in data.p3Ex['road']:
                                    if coordConverter((1, 9)) not in coords and (1, 9) not in data.occupied:
                                        coords += [coordConverter((1, 9))]
                    if i == (2, 7):
                        if (235, 375) in data.p3Ex['road']:
                            if (2, 6) not in data.occupied:
                                if (202.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((1, 5)) not in coords and (1, 5) not in data.occupied:
                                        coords += [coordConverter((1, 5))]
                                if (267.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                        if (202.5, 431.25) in data.p3Ex['road']:
                            if (1, 8) not in data.occupied:
                                if (137.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((1, 7)) not in coords and (1, 7) not in data.occupied:
                                        coords += [coordConverter((1, 7))]
                                if (170, 487.5) in data.p3Ex['road']:
                                    if coordConverter((1, 9)) not in coords and (1, 9) not in data.occupied:
                                        coords += [coordConverter((1, 9))]
                        if (267.5, 431.25) in data.p3Ex['road']:
                            if (2, 8) not in data.occupied:
                                if (332.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                                if (300, 487.5) in data.p3Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                    if i == (3, 7):
                        if (365, 375) in data.p3Ex['road']:
                            if (3, 6) not in data.occupied:
                                if (332.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                                if (397.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                        if (332.5, 431.25) in data.p3Ex['road']:
                            if (2, 8) not in data.occupied:
                                if (267.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                                if (300, 487.5) in data.p3Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                        if (397.5, 431.25) in data.p3Ex['road']:
                            if (3, 8) not in data.occupied:
                                if (462.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                                if (430, 487.5) in data.p3Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                    if i == (4, 7):
                        if (495, 375) in data.p3Ex['road']:
                            if (4, 6) not in data.occupied:
                                if (462.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                                if (527.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                        if (462.5, 431.25) in data.p3Ex['road']:
                            if (3, 8) not in data.occupied:
                                if (397.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                                if (430, 487.5) in data.p3Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                        if (527.5, 431.25) in data.p3Ex['road']:
                            if (4, 8) not in data.occupied:
                                if (592.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                                if (560, 487.5) in data.p3Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                    if i == (5, 7):
                        if (625, 375) in data.p3Ex['road']:
                            if (5, 6) not in data.occupied:
                                if (592.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                                if (657.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((5, 5)) not in coords and (5, 5) not in data.occupied:
                                        coords += [coordConverter((5, 5))]
                        if (592.5, 431.25) in data.p3Ex['road']:
                            if (4, 8) not in data.occupied:
                                if (527.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                                if (560, 487.5) in data.p3Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                        if (657.5, 431.25) in data.p3Ex['road']:
                            if (5, 8) not in data.occupied:
                                if (722.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((6, 7)) not in coords and (6, 7) not in data.occupied:
                                        coords += [coordConverter((6, 7))]
                                if (690, 487.5) in data.p3Ex['road']:
                                    if coordConverter((5, 9)) not in coords and (5, 9) not in data.occupied:
                                        coords += [coordConverter((5, 9))]
                    if i == (6, 7):
                        if (755, 375) in data.p3Ex['road']:
                            if (6, 6) not in data.occupied:
                                if (722.5, 318.75) in data.p3Ex['road']:
                                    if coordConverter((5, 5)) not in coords and (5, 5) not in data.occupied:
                                        coords += [coordConverter((5, 5))]
                        if (722.5, 431.25) in data.p3Ex['road']:
                            if (5, 8) not in data.occupied:
                                if (657.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                                if (690, 487.5) in data.p3Ex['road']:
                                    if coordConverter((5, 9)) not in coords and (5, 9) not in data.occupied:
                                        coords += [coordCOnverter((5, 9))]
                    if i == (1, 8):
                        if (137.5, 431.25) in data.p3Ex['road']:
                            if (1, 7) not in data.occupied:
                                if (105, 375) in data.p3Ex['road']:
                                    if coordConverter((1, 6)) not in coords and (1, 6) not in data.occupied:
                                        coords += [coordConverter((1, 6))]
                        if (202.5, 431.25) in data.p3Ex['road']:
                            if (2, 7) not in data.occupied:
                                if (235, 375) in data.p3Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                                if (267.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                        if (170, 487.5) in data.p3Ex['road']:
                            if (1, 9) not in data.occupied:
                                if (202.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((1, 10)) not in coords and (1, 10) not in data.occupied:
                                        coords += [coordConverter((1, 10))]
                    if i == (2, 8):
                        if (267.5, 431.25) in data.p3Ex['road']:
                            if (2, 7) not in data.occupied:
                                if (235, 375) in data.p3Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                                if (202.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((1, 8)) not in coords and (1, 8) not in data.occupied:
                                        coords += [coordConverter((1, 8))]
                        if (332.5, 431.25) in data.p3Ex['road']:
                            if (3, 7) not in data.occupied:
                                if (365, 375) in data.p3Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                                if (397.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                        if (300, 487.5) in data.p3Ex['road']:
                            if (2, 9) not in data.occupied:
                                if (267.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((1, 10)) not in coords and (1, 10) not in data.occupied:
                                        coords += [coordConverter((1, 10))]
                                if (332.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                    if i == (3, 8):
                        if (397.5, 431.25) in data.p3Ex['road']:
                            if (3, 7) not in data.occupied:
                                if (332.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                                if (365, 375) in data.p3Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                        if (462.5, 431.25) in data.p3Ex['road']:
                            if (4, 7) not in data.occupied:
                                if (495, 375) in data.p3Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                                if (527.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                        if (430, 487.5) in data.p3Ex['road']:
                            if (3, 9) not in data.occupied:
                                if (397.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                                if (462.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                    if i == (4, 8):
                        if (527.5, 431.25) in data.p3Ex['road']:
                            if (4, 7) not in data.occupied:
                                if (495, 375) in data.p3Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                                if (462.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                        if (592.5, 431.25) in data.p3Ex['road']:
                            if (5, 7) not in data.occupied:
                                if (625, 375) in data.p3Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                                if (657.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((5, 8)) not in coords and (5, 8) not in data.occupied:
                                        coords += [coordConverter((5, 8))]
                        if (560, 487.5) in data.p3Ex['road']:
                            if (4, 9) not in data.occupied:
                                if (527.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                                if (592.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((4, 10)) not in coords and (4, 10) not in data.occupied:
                                        coords += [coordConverter((4, 10))]
                    if i == (5, 8):
                        if (657.5, 431.25) in data.p3Ex['road']:
                            if (5, 7) not in data.occupied:
                                if (625, 375) in data.p3Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                                if (592.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                        if (722.5, 431.25) in data.p3Ex['road']:
                            if (6, 7) not in data.occupied:
                                if (755, 375) in data.p3Ex['road']:
                                    if coordConverter((6, 6)) not in coords and (6, 6) not in data.occupied:
                                        coords += [coordConverter((6, 6))]
                        if (690, 487.5) in data.p3Ex['road']:
                            if (5, 9) not in data.p3Ex['road']:
                                if (657.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((4, 10)) not in coords and (4, 10) not in data.occupied:
                                        coords += [coordConverter((4, 10))]
                    if i == (1, 9):
                        if (170, 487.5) in data.p3Ex['road']:
                            if (1, 8) not in data.occupied:
                                if (137.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((1, 7)) not in coords and (1, 7) not in data.occupied:
                                        coords += [coordConverter((1, 7))]
                                if (202.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                        if (202.5, 543.75) in data.p3Ex['road']:
                            if (1, 10) not in data.occupied:
                                if (267.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                                if (235, 600) in data.p3Ex['road']:
                                    if coordConverter((1, 11)) not in coords and (1, 11) not in data.occupied:
                                        coords += [coordConverter((1, 11))]
                    if i == (2, 9):
                        if (300, 487.5) in data.p3Ex['road']:
                            if (2, 8) not in data.occupied:
                                if (267.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                                if (332.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                        if (267.5, 543.75) in data.p3Ex['road']:
                            if (1, 10) not in data.occupied:
                                if (202.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((1, 9)) not in coords and (1, 9) not in data.occupied:
                                        coords += [coordConverter((1, 9))]
                                if (235, 600) in data.p3Ex['road']:
                                    if coordConverter((1, 11)) not in coords and (1, 11) not in data.occupied:
                                        coords += [coordConverter((1, 11))]
                        if (332.5, 543.75) in data.p3Ex['road']:
                            if (2, 10) not in data.occupied:
                                if (397.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                                if (365, 600) in data.p3Ex['road']:
                                    if coordConverter((2, 11)) not in coords and (2, 11) not in data.occupied:
                                        coords += [coordConverter((2, 11))]
                    if i == (3, 9):
                        if (430, 487.5) in data.p3Ex['road']:
                            if (3, 8) not in data.occupied:
                                if (397.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                                if (462.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                        if (397.5, 543.75) in data.p3Ex['road']:
                            if (2, 10) not in data.occupied:
                                if (332.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                                if (365, 600) in data.p3Ex['road']:
                                    if coordConverter((2, 11)) not in coords and (2, 11) not in data.occupied:
                                        coords += [coordConverter((2, 11))]
                        if (462.5, 543.75) in data.p3Ex['road']:
                            if (3, 10) not in data.occupied:
                                if (527.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                                if (495, 600) in data.p3Ex['road']:
                                    if coordConverter((3, 11)) not in coords and (3, 11) not in data.occupied:
                                        coords += [coordConverter((3, 11))]
                    if i == (4, 9):
                        if (560, 487.5) in data.p3Ex['road']:
                            if (4, 8) not in data.occupied:
                                if (527.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                                if (592.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                        if (527.5, 543.75) in data.p3Ex['road']:
                            if (3, 10) not in data.occupied:
                                if (462.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                                if (495, 600) in data.p3Ex['road']:
                                    if coordConverter((3, 11)) not in coords and (3, 11) not in data.occupied:
                                        coords += [coordConverter((3, 11))]
                        if (592.5, 543.75) in data.p3Ex['road']:
                            if (4, 10) not in data.occupied:
                                if (657.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((5, 9)) not in coords and (5, 9) not in data.occupied:
                                        coords += [coordConverter((5, 9))]
                                if (625, 600) in data.p3Ex['road']:
                                    if coordConverter((4, 11)) not in coords and (4, 11) not in data.occupied:
                                        coords += [coordConverter((4, 11))]
                    if i == (5, 9):
                        if (690, 487.5) in data.p3Ex['road']:
                            if (5, 8) not in data.occupied:
                                if (657.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                                if (722.5, 431.25) in data.p3Ex['road']:
                                    if coordConverter((6, 7)) not in coords and (6, 7) not in data.occupied:
                                        coords += [coordConverter((6, 7))]
                        if (657.5, 543.75) in data.p3Ex['road']:
                            if (4, 10) not in data.occupied:
                                if (592.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                                if (625, 600) in data.p3Ex['road']:
                                    if coordConverter((4, 11)) not in coords and (4, 11) not in data.occupied:
                                        coords += [coordConverter((4, 11))]
                    if i == (1, 10):
                        if (202.5, 543.75) in data.p3Ex['road']:
                            if (1, 9) not in data.occupied:
                                if (170, 487.5) in data.p3Ex['road']:
                                    if coordConverter((1, 8)) not in coords and (1, 8) not in data.occupied:
                                        coords += [coordConverter((1, 8))]
                        if (267.5, 543.75) in data.p3Ex['road']:
                            if (2, 9) not in data.occupied:
                                if (300, 487.5) in data.p3Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                                if (332.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                        if (235, 600) in data.p3Ex['road']:
                            if (1, 11) not in data.occupied:
                                if (267.5, 656.25) in data.p3Ex['road']:
                                    if coordConverter((1, 12)) not in coords and (1, 12) not in data.occupied:
                                        coords += [coordConverter((1, 12))]
                    if i == (2, 10):
                        if (332.5, 543.75) in data.p3Ex['road']:
                            if (2, 9) not in data.occupied:
                                if (300, 487.5) in data.p3Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                                if (267.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((1, 10)) not in coords and (1, 10) not in data.occupied:
                                        coords += [coordConverter((1, 10))]
                        if (397.5, 543.75) in data.p3Ex['road']:
                            if (3, 9) not in data.occupied:
                                if (430, 487.5) in data.p3Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                                if (462.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                        if (365, 600) in data.p3Ex['road']:
                            if (2, 11) not in data.occupied:
                                if (332.5, 656.25) in data.p3Ex['road']:
                                    if coordConverter((1, 12)) not in coords and (1, 12) not in data.occupied:
                                        coords += [coordConverter((1, 12))]
                                if (397.5, 656.25) in data.p3Ex['road']:
                                    if coordConverter((2, 12)) not in coords and (2, 12) not in data.occupied:
                                        coords += [coordConverter((2, 12))]
                    if i == (3, 10):
                        if (462.5, 543.75) in data.p3Ex['road']:
                            if (3, 9) not in data.occupied:
                                if (430, 487.5) in data.p3Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                                if (397.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                        if (527.5, 543.75) in data.p3Ex['road']:
                            if (4, 9) not in data.occupied:
                                if (560, 487.5) in data.p3Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                                if (592.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((4, 10)) not in coords and (4, 10) not in data.occupied:
                                        coords += [coordConverter((4, 10))]
                        if (495, 600) in data.p3Ex['road']:
                            if (3, 11) not in data.occupied:
                                if (462.5, 656.25) in data.p3Ex['road']:
                                    if coordConverter((2, 12)) not in coords and (2, 12) not in data.occupied:
                                        coords += [coordConverter((2, 12))]
                                if (527.5, 656.25) in data.p3Ex['road']:
                                    if coordConverter((3, 12)) not in coords and (3, 12) not in data.occupied:
                                        coords += [coordConverter((3, 12))]
                    if i == (4, 10):
                        if (657.5, 543.75) in data.p3Ex['road']:
                            if (5, 9) not in data.occupied:
                                if (690, 487.5) in data.p3Ex['road']:
                                    if coordConverter((5, 8)) not in coords and (5, 8) not in data.occupied:
                                        coords += [coordConverter(5, 8)]
                        if (592.5, 543.75) in data.p3Ex['road']:
                            if (4, 9) not in data.occupied:
                                if (560, 487.5) in data.p3Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                                if (527.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                        if (625, 600) in data.p3Ex['road']:
                            if (4, 11) not in data.occupied:
                                if (592.5, 656.25) in data.p3Ex['road']:
                                    if coordConverter((3, 12)) not in coords and (3, 12) not in data.occupied:
                                        coords += [coordConverter((3, 12))]
                    if i == (1, 11):
                        if (235, 600) in data.p3Ex['road']:
                            if (1, 10) not in data.occupied:
                                if (202.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((1, 9)) not in coords and (1, 9) not in data.occupied:
                                        coords += [coordConverter((1, 9))]
                                if (267.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                        if (267.5, 656.25) in data.p3Ex['road']:
                            if (1, 12) not in data.occupied:
                                if (332.5, 656.25) in data.p3Ex['road']:
                                    if coordConverter((2, 11)) not in coords and (2, 11) not in data.occupied:
                                        coords += [coordConverter((2, 11))]
                    if i == (2, 11):
                        if (365, 600) in data.p3Ex['road']:
                            if (2, 10) not in data.occupied:
                                if (332.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                                if (397.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                        if (332.5, 656.25) in data.p3Ex['road']:
                            if (1, 12) not in data.occupied:
                                if (267.5, 656.25) in data.p3Ex['road']:
                                    if coordConverter((1, 11)) not in coords and (1, 11) not in data.occupied:
                                        coords += [coordConverter((1, 11))]
                        if (397.5, 656.25) in data.p3Ex['road']:
                            if (2, 12) not in data.occupied:
                                if (462.5, 656.25) in data.p3Ex['road']:
                                    if coordConverter((3, 11)) not in coords and (3, 11) not in data.occupied:
                                        coords += [coordConverter((3, 11))]
                    if i == (3, 11):
                        if (495, 600) in data.p3Ex['road']:
                            if (3, 10) not in data.occupied:
                                if (462.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                                if (527.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                        if (462.5, 656.25) in data.p3Ex['road']:
                            if (2, 12) not in data.occupied:
                                if (397.5, 656.25) in data.p3Ex['road']:
                                    if coordConverter((2, 11)) not in coords and (2, 11) not in data.occupied:
                                        coords += [coordConverter((2, 11))]
                        if (527.5, 656.25) in data.p3Ex['road']:
                            if (3, 12) not in data.occupied:
                                if (592.5, 656.25) in data.p3Ex['road']:
                                    if coordConverter((4, 11)) not in coords and (4, 11) not in data.occupied:
                                        coords += [coordConverter((4, 11))]
                    if i == (4, 11):
                        if (625, 600) in data.p3Ex['road']:
                            if (4, 10) not in data.occupied:
                                if (592.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                                if (657.5, 543.75) in data.p3Ex['road']:
                                    if coordConverter((5, 9)) not in coords and (5, 9) not in data.occupied:
                                        coords += [coordConverter((5, 9))]
                        if (592.5, 656.25) in data.p3Ex['road']:
                            if (3, 12) not in data.occupied:
                                if (527.5, 656.25) in data.p3Ex['road']:
                                    if coordConveter((3, 11)) not in coords and (3, 11) not in data.occupied:
                                        coords += [coordConveter((3, 11))]
                    if i == (1, 12):
                        if (267.5, 656.25) in data.p3Ex['road']:
                            if (1, 11) not in data.occupied:
                                if (235, 600) in data.p3Ex['road']:
                                    if coordConverter((1, 10)) not in coords and (1, 10) not in data.occupied:
                                        coords += [coordConverter((1, 10))]
                        if (332.5, 656.25) in data.p3Ex['road']:
                            if (2, 11) not in data.occupied:
                                if (365, 600) in data.p3Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                                if (397.5, 656.25) in data.p3Ex['road']:
                                    if coordConverter((2, 12)) not in coords and (2, 12) not in data.occupied:
                                        coords += [coordConverter((2, 12))]
                    if i == (2, 12):
                        if (397.5, 656.25) in data.p3Ex['road']:
                            if (2, 11) not in data.occupied:
                                if (332.5, 656.25) in data.p3Ex['road']:
                                    if coordConverter((1, 12)) not in coords and (1, 12) not in data.occupied:
                                        coords += [coordConverter((1, 12))]
                                if (365, 600) in data.p3Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                        if (462.5, 656.25) in data.p3Ex['road']:
                            if (3, 11) not in data.occupied:
                                if (495, 600) in data.p3Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                                if (527.5, 656.25) in data.p3Ex['road']:
                                    if coordConverter((3, 12)) not in coords and (3, 12) not in data.occupied:
                                        coords += [coordConverter((3, 12))]
                    if i == (3, 12):
                        if (527.5, 656.25) in data.p3Ex['road']:
                            if (3, 11) not in data.occupied:
                                if (495, 600) in data.p3Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                                if (462.5, 656.25) in data.p3Ex['road']:
                                    if coordConverter((2, 12)) not in coords and (2, 12) not in data.occupied:
                                        coords += [coordConverter((2, 12))]
                        if (592.5, 656.25) in data.p3Ex['road']:
                            if (4, 11) not in data.occupied:
                                if (625, 600) in data.p3Ex['road']:
                                    if coordConverter((4, 10)) not in coords and (4, 10) not in data.occupied:
                                        coords += [coordConverter((4, 10))]
    if data.turn == 4:
        for key in data.p4Ex:
            if key == 'city' or key == 'settle':
                for i in data.p4Ex[key]:
                    if i == (1, 1):
                        if (267.5, 93.75) in data.p4Ex['road']:
                            if (1, 2) not in data.occupied:
                                if (235, 150) in data.p4Ex['road']:
                                    if (235, 187.5) not in coords and (1, 3) not in data.occupied:
                                        coords += [(235, 187.5)]
                        if (332.5, 93.75) in data.p4Ex['road']:
                            if (2, 2) not in data.occupied:
                                if (397.5, 93.75) in data.p4Ex['road']:
                                    if (430, 75) not in coords and (2, 1) not in data.occupied:
                                        coords += [(430, 75)]
                                if (365, 150) in data.p4Ex['road']:
                                    if (365, 187.5) not in coords and (2, 3) not in data.occupied:
                                        coords += [(365, 187.5)]
                    if i == (2, 1):
                        if (397.5, 93.75) in data.p4Ex['road']:
                            if (2, 2) not in data.occupied:
                                if (332.5, 93.75) in data.p4Ex['road']:
                                    if (300, 75) not in coords and (1, 1) not in data.occupied:
                                        coords += [(300, 75)]
                                if (365, 150) in data.p4Ex['road']:
                                    if (365, 187.5) not in coords and (2, 3) not in data.occupied:
                                        coords += [(365, 187.5)]
                        if (462.5, 93.75) in data.p4Ex['road']:
                            if (3, 2) not in data.occupied:
                                if (527.5, 93.75) in data.p4Ex['road']:
                                    if (560, 75) not in coords and (3, 1) not in data.occupied:
                                        coords += [(560, 75)]
                                if (495, 150) in data.p4Ex['road']:
                                    if (495, 187.5) not in coords and (3, 3) not in data.occupied:
                                        coords += [(495, 187.5)]
                    if i == (3, 1):
                        if (527.5, 93.75) in data.p4Ex['road']:
                            if (3, 2) not in data.occupied:
                                if (462.5, 93.75) in data.p4Ex['road']:
                                    if (430, 75) not in coords and (2, 1) not in data.occupied:
                                        coords += [(430, 75)]
                                if (495, 150) in data.p4Ex['road']:
                                    if (495, 187.5) not in coords and (3, 3) not in data.occupied:
                                        coords += [(495, 187.5)]
                        if (592.5, 93.75) in data.p4Ex['road']:
                            if (4, 2) not in data.occupied:
                                if (625, 150) in data.p4Ex['road']:
                                    if (625, 187.5) not in coords and (4, 3) not in data.occupied:
                                        coords += [(625, 187.5)]
                    if i == (1, 2):
                        if (267.5, 93.75) in data.p4Ex['road']:
                            if (1, 1) not in data.occupied:
                                if (332.5, 93.75) in data.p4Ex['road']:
                                    if (365, 112.5) not in coords and (2, 2) not in data.occupied:
                                        coords += [(365, 112.5)]
                        if (235, 150) in data.p4Ex['road']:
                            if (1, 3) not in data.occupied:
                                if (202.5, 206.25) in data.p4Ex['road']:
                                    if (170, 225) not in coords and (1, 4) not in data.occupied:
                                        coords += [(170, 225)]
                                if (267.5, 206.25) in data.p4Ex['road']:
                                    if (300, 225) not in coords and (2, 4) not in data.occupied:
                                        coords += [(300, 225)]
                    if i == (2, 2):
                        if (332.5, 93.75) in data.p4Ex['road']:
                            if (1, 1) not in data.occupied:
                                if (267.5, 93.75) in data.p4Ex['road']:
                                    if coordConverter((1, 2)) not in coords and (1, 2) not in data.occupied:
                                        coords += [coordConverter((1, 2))]
                        if (397.5, 93.75) in data.p4Ex['road']:
                            if (2, 1) not in data.occupied:
                                if (462.5, 93.75) in data.p4Ex['road']:
                                    if coordConverter((3, 2)) not in coords and (3, 2) not in data.occupied:
                                        coords += [coordConverter((3, 2))]
                        if (365, 150) in data.p4Ex['road']:
                            if (2, 3) not in data.occupied:
                                if (332.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                                if (397.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                    if i == (3, 2):
                        if (462.5, 93.75) in data.p4Ex['road']:
                            if (2, 1) not in data.occupied:
                                if (397.5, 93.75) in data.p4Ex['road']:
                                    if coordConverter((2, 2)) not in coords and (2, 2) not in data.occupied:
                                        coords += [coordConverter((2, 2))]
                        if (527.5, 93.75) in data.p4Ex['road']:
                            if (3, 1) not in data.occupied:
                                if (592.5, 93.75) in data.p4Ex['road']:
                                    if coordConverter((4, 2)) not in coords and (4, 2) not in data.occupied:
                                        coords += [coordConverter((4, 2))]
                        if (495, 150) in data.p4Ex['road']:
                            if (3, 3) not in data.occupied:
                                if (462.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                                if (527.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                    if i == (4, 2):
                        if (592.5, 93.75) in data.p4Ex['road']:
                            if (3, 1) not in data.occupied:
                                if (527.5, 93.75) in data.p4Ex['road']:
                                    if coordConverter((3, 2)) not in coords and (3, 2) not in data.occupied:
                                        coords += [coordConverter((3, 2))]
                        if (625, 150) in data.p4Ex['road']:
                            if (4, 3) not in data.occupied:
                                if (592.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                                if (657.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((5, 4)) not in coords and (5, 4) not in data.occupied:
                                        coords += [coordConverter((5, 4))]
                    if i == (1, 3):
                        if (235, 150) in data.p4Ex['road']:
                            if (1, 2) not in data.occupied:
                                if (267.5, 93.75) in data.p4Ex['road']:
                                    if coordConverter((1, 1)) not in coords and (1, 1) not in data.occupied:
                                        coords += [coordConverter((1, 1))]
                        if (202.5, 206.25) in data.p4Ex['road']:
                            if (1, 4) not in data.occupied:
                                if (170, 262.5) in data.p4Ex['road']:
                                    if coordConverter((1, 5)) not in coords and (1, 5) not in data.occupied:
                                        coords += [coordConverter((1, 5))]
                        if (267.5, 206.25) in data.p4Ex['road']:
                            if (2, 4) not in data.occupied:
                                if (332.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((2, 3)) not in coords and (2, 3) not in data.occupied:
                                        coords += [coordConverter((2, 3))]
                                if (300, 262.5) in data.p4Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                    if i == (2, 3):
                        if (365, 150) in data.p4Ex['road']:
                            if (2, 2) not in data.occupied:
                                if (332.5, 93.75) in data.p4Ex['road']:
                                    if coordConverter((1, 1)) not in coords and (1, 1) not in data.occupied:
                                        coords += [coordConverter((1, 1))]
                                if (397.5, 93.75) in data.p4Ex['road']:
                                    if coordConverter((2, 1)) not in coords and (2, 1) not in data.occupied:
                                        coords += [coordConverter((2, 1))]
                        if (332.5, 206.25) in data.p4Ex['road']:
                            if (2, 4) not in data.occupied:
                                if (267.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((1, 3)) not in coords and (1, 3) not in data.occupied:
                                        coords += [coordConverter((1, 3))]
                                if (300, 262.5) in data.p4Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                        if (397.5, 206.25) in data.p4Ex['road']:
                            if (3, 4) not in data.occupied:
                                if (462.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((3, 3)) not in coords and (3, 3) not in data.occupied:
                                        coords += [coordConverter((3, 3))]
                                if (430, 262.5) in data.p4Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                    if i == (3, 3):
                        if (495, 150) in data.p4Ex['road']:
                            if (3, 2) not in data.occupied:
                                if (462.5, 93.75) in data.p4Ex['road']:
                                    if coordConverter((2, 1)) not in coords and (2, 1) not in data.occupied:
                                        coords += [coordConverter((2, 1))]
                                if (527.5, 93.75) in data.p4Ex['road']:
                                    if coordConverter((3, 1)) not in coords and (3, 1) not in data.occupied:
                                        coords += [coordConverter((3, 1))]
                        if (462.5, 206.25) in data.p4Ex['road']:
                            if (3, 4) not in data.occupied:
                                if (397.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((2, 3)) not in coords and (2, 3) not in data.occupied:
                                        coords += [coordConverter((2, 3))]
                                if (430, 262.5) in data.p4Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                        if (527.5, 206.25) in data.p4Ex['road']:
                            if (4, 4) not in data.occupied:
                                if (592.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((4, 3)) not in coords and (4, 3) not in data.occupied:
                                        coords += [coordConverter((4, 3))]
                                if (560, 262.5) in data.p4Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                    if i == (4, 3):
                        if (625, 150) in data.p4Ex['road']:
                            if (4, 2) not in data.occupied:
                                if (592.5, 93.75) in data.p4Ex['road']:
                                    if coordConverter((3, 1)) not in coords and (3, 1) not in data.occupied:
                                        coords += [coordConverter((3, 1))]
                        if (592.5, 206.25) in data.p4Ex['road']:
                            if (4, 4) not in data.occupied:
                                if (527.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((5, 3)) not in coords and (5, 3) not in data.occupied:
                                        coords += [coordConverter((5, 3))]
                                if (560, 262.5) in data.p4Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                        if (657.5, 206.25) in data.p4Ex['road']:
                            if (5, 4) not in data.occupied:
                                if (690, 262.5) in data.p4Ex['road']:
                                    if coordConverter((5, 5)) not in coords and (5, 5) not in data.occupied:
                                        coords += [coordConverter((5, 5))]
                    if i == (1, 4):
                        if (202.5, 206.25) in data.p4Ex['road']:
                            if (1, 3) not in data.occupied:
                                if (235, 150) in data.p4Ex['road']:
                                    if coordConverter((1, 2)) not in coords and (1, 2) not in data.occupied:
                                        coords += [coordConverter((1, 2))]
                                if (267.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                        if (170, 262.5) in data.p4Ex['road']:
                            if (1, 5) not in data.occupied:
                                if (137.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((1, 6)) not in coords and (1, 6) not in data.occupied:
                                        coords += [coordConverter((1, 6))]
                                if (202.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                    if i == (2, 4):
                        if (267.5, 206.25) in data.p4Ex['road']:
                            if (1, 3) not in data.occupied:
                                if (235, 150) in data.p4Ex['road']:
                                    if coordConverter((1, 2)) not in coords and (1, 2) not in data.occupied:
                                        coords += [coordConverter((1, 2))]
                                if (202.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((1, 4)) not in coords and (1, 4) not in data.occupied:
                                        coords += [coordConverter((1, 4))]
                        if (332.5, 206.25) in data.p4Ex['road']:
                            if (2, 3) not in data.occupied:
                                if (365, 150) in data.p4Ex['road']:
                                    if coordConverter((2, 2)) not in coords and (2, 2) not in data.occupied:
                                        coords += [coordConverter((2, 2))]
                                if (397.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                        if (300, 262.5) in data.p4Ex['road']:
                            if (2, 5) not in data.occupied:
                                if (267.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                                if (332.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                    if i == (3, 4):
                        if (397.5, 206.25) in data.p4Ex['road']:
                            if (2, 3) not in data.occupied:
                                if (365, 150) in data.p4Ex['road']:
                                    if coordConverter((2, 2)) not in coords and (2, 2) not in data.occupied:
                                        coords += [coordConverter((2, 2))]
                                if (332.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                        if (462.5, 206.25) in data.p4Ex['road']:
                            if (3, 3) not in data.occupied:
                                if (495, 150) in data.p4Ex['road']:
                                    if coordConverter((3, 2)) not in coords and (3, 2) not in data.occupied:
                                        coords += [coordConverter((3, 2))]
                                if (527.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                        if (430, 262.5) in data.p4Ex['road']:
                            if (3, 5) not in data.occupied:
                                if (397.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                                if (462.5, 318.75) in data.p4Ex['road']:
                                    if  coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                    if i == (4, 4):
                        if (527.5, 206.25) in data.p4Ex['road']:
                            if (3, 3) not in data.occupied:
                                if (495, 150) in data.p4Ex['road']:
                                    if coordConverter((3, 2)) not in coords and (3, 2) not in data.occupied:
                                        coords += [coordConverter((3, 2))]
                                if (462.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                        if (592.5, 206.25) in data.p4Ex['road']:
                            if (4, 3) not in data.occupied:
                                if (625, 150) in data.p4Ex['road']:
                                    if coordConverter((4, 2)) not in coords and (4, 2) not in data.occupied:
                                        coords += [coordConverter((4, 2))]
                                if (657.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((5, 4)) not in coords and (5, 4) not in data.occupied:
                                        coords += [coordConverter((5, 4))]
                        if (560, 262.5) in data.p4Ex['road']:
                            if (4, 5) not in data.occupied:
                                if (527.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                                if (592.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                    if i == (5, 4):
                        if (657.5, 206.25) in data.p4Ex['road']:
                            if (4, 3) not in data.occupied:
                                if (625, 150) in data.p4Ex['road']:
                                    if coordConverter((4, 2)) not in coords and (4, 2) not in data.occupied:
                                        coords += [coordConverter((4, 2))]
                                if (592.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                        if (690, 262.5) in data.p4Ex['road']:
                            if (5, 5) not in data.occupied:
                                if (657.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                                if (722.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((6, 6)) not in coords and (6, 6) not in data.occupied:
                                        coords += [coordConverter((6, 6))]
                    if i == (1, 5):
                        if (170, 262.5) in data.p4Ex['road']:
                            if (1, 4) not in data.occupied:
                                if (202.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((1, 3)) not in coords and (1, 3) not in data.occupied:
                                        coords += [coordConverter((1, 3))]
                        if (137.5, 318.75) in data.p4Ex['road']:
                            if (1, 6) not in data.occupied:
                                if (105, 375) in data.p4Ex['road']:
                                    if coordConverter((1, 7)) not in coords and (1, 7) not in data.occupied:
                                        coords += [coordConverter((1, 7))]
                        if (202.5, 318.75) in data.p4Ex['road']:
                            if (2, 6) not in data.occupied:
                                if (267.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                                if (235, 375) in data.p4Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                    if i == (2, 5):
                        if (300, 262.5) in data.p4Ex['road']:
                            if (2, 4) not in data.occupied:
                                if (267.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((1, 3)) not in coords and (1, 3) not in data.occupied:
                                        coords += [coordConverter((1, 3))]
                                if (332.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((2, 3)) not in coords and (2, 3) not in data.occupied:
                                        coords += [coordConverter((2, 3))]
                        if (267.5, 318.75) in data.p4Ex['road']:
                            if (2, 6) not in data.occupied:
                                if (202.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((1, 5)) not in coords and (1, 5) not in data.occupied:
                                        coords += [coordConverter((1, 5))]
                                if (235, 375) in data.p4Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                        if (332.5, 318.75) in data.p4Ex['road']:
                            if (3, 6) not in data.occupied:
                                if (397.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                                if (365, 375) in data.p4Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                    if i == (3, 5):
                        if (430, 262.5) in data.p4Ex['road']:
                            if (3, 4) not in data.occupied:
                                if (397.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((2, 3)) not in coords and (2, 3) not in data.occupied:
                                        coords += [coordConverter((2, 3))]
                                if (462.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((3, 3)) not in coords and (3, 3) not in data.occupied:
                                        coords += [coordConverter((3, 3))]
                        if (397.5, 318.75) in data.p4Ex['road']:
                            if (3, 6) not in data.occupied:
                                if (332.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                                if (365, 375) in data.p4Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                        if (462.5, 318.75) in data.p4Ex['road']:
                            if (4, 6) not in data.occupied:
                                if (527.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                                if (495, 375) in data.p4Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                    if i == (4, 5):
                        if (527.5, 318.75) in data.p4Ex['road']:
                            if (4, 6) not in data.occupied:
                                if (462.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                                if (495, 375) in data.p4Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                        if (560, 262.5) in data.p4Ex['road']:
                            if (4, 4) not in data.occupied:
                                if (527.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((3, 3)) not in coords and (3, 3) not in data.occupied:
                                        coords += [coordConverter((3, 3))]
                                if (592.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((4, 3)) not in coords and (4, 3) not in data.occupied:
                                        coords += [coordConverter((4, 3))]
                        if (592.5, 318.75) in data.p4Ex['road']:
                            if (5, 6) not in data.occupied:
                                if (657.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((5, 5)) not in coords and (5, 5) not in data.occupied:
                                        coords += [coordConverter((5, 5))]
                                if (625, 375) in data.p4Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                    if i == (5, 5):
                        if (690, 262.5) in data.p4Ex['road']:
                            if (5, 4) not in data.occupied:
                                if (657.5, 206.25) in data.p4Ex['road']:
                                    if coordConverter((4, 3)) not in coords and (4, 3) not in data.occupied:
                                        coords += [coordConverter((4, 3))]
                        if (657.5, 318.75) in data.p4Ex['road']:
                            if (5, 6) not in data.occupied:
                                if (592.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                                if (625, 375) in data.p4Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                        if (722.5, 318.75) in data.p4Ex['road']:
                            if (6, 6) not in data.occupied:
                                if (755, 375) in data.p4Ex['road']:
                                    if coordConverter((6, 7)) not in coords and (6, 7) not in data.occupied:
                                        coords += [coordConverter((6, 7))]
                    if i == (1, 6):
                        if (137.5, 318.75) in data.p4Ex['road']:
                            if (1, 5) not in data.occupied:
                                if (170, 262.5) in data.p4Ex['road']:
                                    if coordConverter((1, 4)) not in coords and (1, 4) not in data.occupied:
                                        coords += [coordConverter((1, 4))]
                                if (202.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                        if (105, 375) in data.p4Ex['road']:
                            if (1, 7) not in data.occupied:
                                if (137.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((1, 8)) not in coords and (1, 8) not in data.occupied:
                                        coords += [coordConverter((1, 8))]
                    if i == (2, 6):
                        if (202.5, 318.75) in data.p4Ex['road']:
                            if (1, 5) not in data.occupied:
                                if (170, 262.5) in data.p4Ex['road']:
                                    if coordConverter((1, 4)) not in coords and (1, 4) not in data.occupied:
                                        coords += [coordConverter((1, 4))]
                                if (137.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((1, 6)) not in coords and (1, 6) not in data.occupied:
                                        coords += [coordConverter((1, 6))]
                        if (267.5, 318.75) in data.p4Ex['road']:
                            if (2, 5) not in data.occupied:
                                if (300, 262.5) in data.p4Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                                if (332.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                        if (235, 375) in data.p4Ex['road']:
                            if (2, 7) not in data.occupied:
                                if (202.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((1, 8)) not in coords and (1, 8) not in data.occupied:
                                        coords += [coordConverter((1, 8))]
                                if (267.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                    if i == (3, 6):
                        if (332.5, 318.75) in data.p4Ex['road']:
                            if (2, 5) not in data.occupied:
                                if (300, 262.5) in data.p4Ex['road']:
                                    if coordConverter((2, 4)) not in coords and (2, 4) not in data.occupied:
                                        coords += [coordConverter((2, 4))]
                                if (267.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                        if (397.5, 318.75) in data.p4Ex['road']:
                            if (3, 5) not in data.occupied:
                                if (430, 262.5) in data.p4Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                                if (462.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                        if (365, 375) in data.p4Ex['road']:
                            if (3, 7) not in data.occupied:
                                if (332.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                                if (397.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                    if i == (4, 6):
                        if (462.5, 318.75) in data.p4Ex['road']:
                            if (3, 5) not in data.occupied:
                                if (430, 262.5) in data.p4Ex['road']:
                                    if coordConverter((3, 4)) not in coords and (3, 4) not in data.occupied:
                                        coords += [coordConverter((3, 4))]
                                if (397.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                        if (527.5, 318.75) in data.p4Ex['road']:
                            if (4, 5) not in data.occupied:
                                if (560, 262.5) in data.p4Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                                if (592.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                        if (495, 375) in data.p4Ex['road']:
                            if (4, 7) not in data.occupied:
                                if (462.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                                if (527.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                    if i == (5, 6):
                        if (592.5, 318.75) in data.p4Ex['road']:
                            if (4, 5) not in data.occupied:
                                if (560, 262.5) in data.p4Ex['road']:
                                    if coordConverter((4, 4)) not in coords and (4, 4) not in data.occupied:
                                        coords += [coordConverter((4, 4))]
                                if (527.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                        if (657.5, 318.75) in data.p4Ex['road']:
                            if (5, 5) not in data.occupied:
                                if (690, 262.5) in data.p4Ex['road']:
                                    if coordConverter((5, 4)) not in coords and (5, 4) not in data.occupied:
                                        coords += [coordConverter((5, 4))]
                                if (722.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((6, 6)) not in coords and (6, 6) not in data.occupied:
                                        coords += [coordConverter((6, 6))]
                        if (625, 375) in data.p4Ex['road']:
                            if (5, 7) not in data.occupied:
                                if (592.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                                if (657.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((5, 8)) not in coords and (5, 8) not in data.occupied:
                                        coords += [coordConverter((5, 8))]
                    if i == (6, 6):
                        if (722.5, 318.75) in data.p4Ex['road']:
                            if (5, 5) not in data.occupied:
                                if (690, 262.5) in data.p4Ex['road']:
                                    if coordConverter((5, 4)) not in coords and (5, 4) not in data.occupied:
                                        coords += [coordConverter((5, 4))]
                                if (657.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                        if (755, 375) in data.p4Ex['road']:
                            if (6, 7) not in data.occupied:
                                if (722.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((5, 8)) not in coords and (5, 8) not in data.occupied:
                                        coords += [coordConverter((5, 8))]
                    if i == (1, 7):
                        if (105, 375) in data.p4Ex['road']:
                            if (1, 6) not in data.occupied:
                                if (137.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((1, 5)) not in coords and (1, 5) not in data.occupied:
                                        coords += [coordConverter((1, 5))]
                        if (137.5, 431.25) in data.p4Ex['road']:
                            if (1, 8) not in data.occupied:
                                if (202.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                                if (170, 487.5) in data.p4Ex['road']:
                                    if coordConverter((1, 9)) not in coords and (1, 9) not in data.occupied:
                                        coords += [coordConverter((1, 9))]
                    if i == (2, 7):
                        if (235, 375) in data.p4Ex['road']:
                            if (2, 6) not in data.occupied:
                                if (202.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((1, 5)) not in coords and (1, 5) not in data.occupied:
                                        coords += [coordConverter((1, 5))]
                                if (267.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                        if (202.5, 431.25) in data.p4Ex['road']:
                            if (1, 8) not in data.occupied:
                                if (137.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((1, 7)) not in coords and (1, 7) not in data.occupied:
                                        coords += [coordConverter((1, 7))]
                                if (170, 487.5) in data.p4Ex['road']:
                                    if coordConverter((1, 9)) not in coords and (1, 9) not in data.occupied:
                                        coords += [coordConverter((1, 9))]
                        if (267.5, 431.25) in data.p4Ex['road']:
                            if (2, 8) not in data.occupied:
                                if (332.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                                if (300, 487.5) in data.p4Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                    if i == (3, 7):
                        if (365, 375) in data.p4Ex['road']:
                            if (3, 6) not in data.occupied:
                                if (332.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((2, 5)) not in coords and (2, 5) not in data.occupied:
                                        coords += [coordConverter((2, 5))]
                                if (397.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                        if (332.5, 431.25) in data.p4Ex['road']:
                            if (2, 8) not in data.occupied:
                                if (267.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                                if (300, 487.5) in data.p4Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                        if (397.5, 431.25) in data.p4Ex['road']:
                            if (3, 8) not in data.occupied:
                                if (462.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                                if (430, 487.5) in data.p4Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                    if i == (4, 7):
                        if (495, 375) in data.p4Ex['road']:
                            if (4, 6) not in data.occupied:
                                if (462.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((3, 5)) not in coords and (3, 5) not in data.occupied:
                                        coords += [coordConverter((3, 5))]
                                if (527.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                        if (462.5, 431.25) in data.p4Ex['road']:
                            if (3, 8) not in data.occupied:
                                if (397.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                                if (430, 487.5) in data.p4Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                        if (527.5, 431.25) in data.p4Ex['road']:
                            if (4, 8) not in data.occupied:
                                if (592.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                                if (560, 487.5) in data.p4Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                    if i == (5, 7):
                        if (625, 375) in data.p4Ex['road']:
                            if (5, 6) not in data.occupied:
                                if (592.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((4, 5)) not in coords and (4, 5) not in data.occupied:
                                        coords += [coordConverter((4, 5))]
                                if (657.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((5, 5)) not in coords and (5, 5) not in data.occupied:
                                        coords += [coordConverter((5, 5))]
                        if (592.5, 431.25) in data.p4Ex['road']:
                            if (4, 8) not in data.occupied:
                                if (527.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                                if (560, 487.5) in data.p4Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                        if (657.5, 431.25) in data.p4Ex['road']:
                            if (5, 8) not in data.occupied:
                                if (722.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((6, 7)) not in coords and (6, 7) not in data.occupied:
                                        coords += [coordConverter((6, 7))]
                                if (690, 487.5) in data.p4Ex['road']:
                                    if coordConverter((5, 9)) not in coords and (5, 9) not in data.occupied:
                                        coords += [coordConverter((5, 9))]
                    if i == (6, 7):
                        if (755, 375) in data.p4Ex['road']:
                            if (6, 6) not in data.occupied:
                                if (722.5, 318.75) in data.p4Ex['road']:
                                    if coordConverter((5, 5)) not in coords and (5, 5) not in data.occupied:
                                        coords += [coordConverter((5, 5))]
                        if (722.5, 431.25) in data.p4Ex['road']:
                            if (5, 8) not in data.occupied:
                                if (657.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                                if (690, 487.5) in data.p4Ex['road']:
                                    if coordConverter((5, 9)) not in coords and (5, 9) not in data.occupied:
                                        coords += [coordCOnverter((5, 9))]
                    if i == (1, 8):
                        if (137.5, 431.25) in data.p4Ex['road']:
                            if (1, 7) not in data.occupied:
                                if (105, 375) in data.p4Ex['road']:
                                    if coordConverter((1, 6)) not in coords and (1, 6) not in data.occupied:
                                        coords += [coordConverter((1, 6))]
                        if (202.5, 431.25) in data.p4Ex['road']:
                            if (2, 7) not in data.occupied:
                                if (235, 375) in data.p4Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                                if (267.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                        if (170, 487.5) in data.p4Ex['road']:
                            if (1, 9) not in data.occupied:
                                if (202.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((1, 10)) not in coords and (1, 10) not in data.occupied:
                                        coords += [coordConverter((1, 10))]
                    if i == (2, 8):
                        if (267.5, 431.25) in data.p4Ex['road']:
                            if (2, 7) not in data.occupied:
                                if (235, 375) in data.p4Ex['road']:
                                    if coordConverter((2, 6)) not in coords and (2, 6) not in data.occupied:
                                        coords += [coordConverter((2, 6))]
                                if (202.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((1, 8)) not in coords and (1, 8) not in data.occupied:
                                        coords += [coordConverter((1, 8))]
                        if (332.5, 431.25) in data.p4Ex['road']:
                            if (3, 7) not in data.occupied:
                                if (365, 375) in data.p4Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                                if (397.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                        if (300, 487.5) in data.p4Ex['road']:
                            if (2, 9) not in data.occupied:
                                if (267.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((1, 10)) not in coords and (1, 10) not in data.occupied:
                                        coords += [coordConverter((1, 10))]
                                if (332.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                    if i == (3, 8):
                        if (397.5, 431.25) in data.p4Ex['road']:
                            if (3, 7) not in data.occupied:
                                if (332.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                                if (365, 375) in data.p4Ex['road']:
                                    if coordConverter((3, 6)) not in coords and (3, 6) not in data.occupied:
                                        coords += [coordConverter((3, 6))]
                        if (462.5, 431.25) in data.p4Ex['road']:
                            if (4, 7) not in data.occupied:
                                if (495, 375) in data.p4Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                                if (527.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                        if (430, 487.5) in data.p4Ex['road']:
                            if (3, 9) not in data.occupied:
                                if (397.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                                if (462.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                    if i == (4, 8):
                        if (527.5, 431.25) in data.p4Ex['road']:
                            if (4, 7) not in data.occupied:
                                if (495, 375) in data.p4Ex['road']:
                                    if coordConverter((4, 6)) not in coords and (4, 6) not in data.occupied:
                                        coords += [coordConverter((4, 6))]
                                if (462.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                        if (592.5, 431.25) in data.p4Ex['road']:
                            if (5, 7) not in data.occupied:
                                if (625, 375) in data.p4Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                                if (657.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((5, 8)) not in coords and (5, 8) not in data.occupied:
                                        coords += [coordConverter((5, 8))]
                        if (560, 487.5) in data.p4Ex['road']:
                            if (4, 9) not in data.occupied:
                                if (527.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                                if (592.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((4, 10)) not in coords and (4, 10) not in data.occupied:
                                        coords += [coordConverter((4, 10))]
                    if i == (5, 8):
                        if (657.5, 431.25) in data.p4Ex['road']:
                            if (5, 7) not in data.occupied:
                                if (625, 375) in data.p4Ex['road']:
                                    if coordConverter((5, 6)) not in coords and (5, 6) not in data.occupied:
                                        coords += [coordConverter((5, 6))]
                                if (592.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                        if (722.5, 431.25) in data.p4Ex['road']:
                            if (6, 7) not in data.occupied:
                                if (755, 375) in data.p4Ex['road']:
                                    if coordConverter((6, 6)) not in coords and (6, 6) not in data.occupied:
                                        coords += [coordConverter((6, 6))]
                        if (690, 487.5) in data.p4Ex['road']:
                            if (5, 9) not in data.p4Ex['road']:
                                if (657.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((4, 10)) not in coords and (4, 10) not in data.occupied:
                                        coords += [coordConverter((4, 10))]
                    if i == (1, 9):
                        if (170, 487.5) in data.p4Ex['road']:
                            if (1, 8) not in data.occupied:
                                if (137.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((1, 7)) not in coords and (1, 7) not in data.occupied:
                                        coords += [coordConverter((1, 7))]
                                if (202.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                        if (202.5, 543.75) in data.p4Ex['road']:
                            if (1, 10) not in data.occupied:
                                if (267.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                                if (235, 600) in data.p4Ex['road']:
                                    if coordConverter((1, 11)) not in coords and (1, 11) not in data.occupied:
                                        coords += [coordConverter((1, 11))]
                    if i == (2, 9):
                        if (300, 487.5) in data.p4Ex['road']:
                            if (2, 8) not in data.occupied:
                                if (267.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((2, 7)) not in coords and (2, 7) not in data.occupied:
                                        coords += [coordConverter((2, 7))]
                                if (332.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                        if (267.5, 543.75) in data.p4Ex['road']:
                            if (1, 10) not in data.occupied:
                                if (202.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((1, 9)) not in coords and (1, 9) not in data.occupied:
                                        coords += [coordConverter((1, 9))]
                                if (235, 600) in data.p4Ex['road']:
                                    if coordConverter((1, 11)) not in coords and (1, 11) not in data.occupied:
                                        coords += [coordConverter((1, 11))]
                        if (332.5, 543.75) in data.p4Ex['road']:
                            if (2, 10) not in data.occupied:
                                if (397.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                                if (365, 600) in data.p4Ex['road']:
                                    if coordConverter((2, 11)) not in coords and (2, 11) not in data.occupied:
                                        coords += [coordConverter((2, 11))]
                    if i == (3, 9):
                        if (430, 487.5) in data.p4Ex['road']:
                            if (3, 8) not in data.occupied:
                                if (397.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((3, 7)) not in coords and (3, 7) not in data.occupied:
                                        coords += [coordConverter((3, 7))]
                                if (462.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                        if (397.5, 543.75) in data.p4Ex['road']:
                            if (2, 10) not in data.occupied:
                                if (332.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                                if (365, 600) in data.p4Ex['road']:
                                    if coordConverter((2, 11)) not in coords and (2, 11) not in data.occupied:
                                        coords += [coordConverter((2, 11))]
                        if (462.5, 543.75) in data.p4Ex['road']:
                            if (3, 10) not in data.occupied:
                                if (527.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                                if (495, 600) in data.p4Ex['road']:
                                    if coordConverter((3, 11)) not in coords and (3, 11) not in data.occupied:
                                        coords += [coordConverter((3, 11))]
                    if i == (4, 9):
                        if (560, 487.5) in data.p4Ex['road']:
                            if (4, 8) not in data.occupied:
                                if (527.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((4, 7)) not in coords and (4, 7) not in data.occupied:
                                        coords += [coordConverter((4, 7))]
                                if (592.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                        if (527.5, 543.75) in data.p4Ex['road']:
                            if (3, 10) not in data.occupied:
                                if (462.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                                if (495, 600) in data.p4Ex['road']:
                                    if coordConverter((3, 11)) not in coords and (3, 11) not in data.occupied:
                                        coords += [coordConverter((3, 11))]
                        if (592.5, 543.75) in data.p4Ex['road']:
                            if (4, 10) not in data.occupied:
                                if (657.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((5, 9)) not in coords and (5, 9) not in data.occupied:
                                        coords += [coordConverter((5, 9))]
                                if (625, 600) in data.p4Ex['road']:
                                    if coordConverter((4, 11)) not in coords and (4, 11) not in data.occupied:
                                        coords += [coordConverter((4, 11))]
                    if i == (5, 9):
                        if (690, 487.5) in data.p4Ex['road']:
                            if (5, 8) not in data.occupied:
                                if (657.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((5, 7)) not in coords and (5, 7) not in data.occupied:
                                        coords += [coordConverter((5, 7))]
                                if (722.5, 431.25) in data.p4Ex['road']:
                                    if coordConverter((6, 7)) not in coords and (6, 7) not in data.occupied:
                                        coords += [coordConverter((6, 7))]
                        if (657.5, 543.75) in data.p4Ex['road']:
                            if (4, 10) not in data.occupied:
                                if (592.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                                if (625, 600) in data.p4Ex['road']:
                                    if coordConverter((4, 11)) not in coords and (4, 11) not in data.occupied:
                                        coords += [coordConverter((4, 11))]
                    if i == (1, 10):
                        if (202.5, 543.75) in data.p4Ex['road']:
                            if (1, 9) not in data.occupied:
                                if (170, 487.5) in data.p4Ex['road']:
                                    if coordConverter((1, 8)) not in coords and (1, 8) not in data.occupied:
                                        coords += [coordConverter((1, 8))]
                        if (267.5, 543.75) in data.p4Ex['road']:
                            if (2, 9) not in data.occupied:
                                if (300, 487.5) in data.p4Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                                if (332.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                        if (235, 600) in data.p4Ex['road']:
                            if (1, 11) not in data.occupied:
                                if (267.5, 656.25) in data.p4Ex['road']:
                                    if coordConverter((1, 12)) not in coords and (1, 12) not in data.occupied:
                                        coords += [coordConverter((1, 12))]
                    if i == (2, 10):
                        if (332.5, 543.75) in data.p4Ex['road']:
                            if (2, 9) not in data.occupied:
                                if (300, 487.5) in data.p4Ex['road']:
                                    if coordConverter((2, 8)) not in coords and (2, 8) not in data.occupied:
                                        coords += [coordConverter((2, 8))]
                                if (267.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((1, 10)) not in coords and (1, 10) not in data.occupied:
                                        coords += [coordConverter((1, 10))]
                        if (397.5, 543.75) in data.p4Ex['road']:
                            if (3, 9) not in data.occupied:
                                if (430, 487.5) in data.p4Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                                if (462.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                        if (365, 600) in data.p4Ex['road']:
                            if (2, 11) not in data.occupied:
                                if (332.5, 656.25) in data.p4Ex['road']:
                                    if coordConverter((1, 12)) not in coords and (1, 12) not in data.occupied:
                                        coords += [coordConverter((1, 12))]
                                if (397.5, 656.25) in data.p4Ex['road']:
                                    if coordConverter((2, 12)) not in coords and (2, 12) not in data.occupied:
                                        coords += [coordConverter((2, 12))]
                    if i == (3, 10):
                        if (462.5, 543.75) in data.p4Ex['road']:
                            if (3, 9) not in data.occupied:
                                if (430, 487.5) in data.p4Ex['road']:
                                    if coordConverter((3, 8)) not in coords and (3, 8) not in data.occupied:
                                        coords += [coordConverter((3, 8))]
                                if (397.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                        if (527.5, 543.75) in data.p4Ex['road']:
                            if (4, 9) not in data.occupied:
                                if (560, 487.5) in data.p4Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                                if (592.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((4, 10)) not in coords and (4, 10) not in data.occupied:
                                        coords += [coordConverter((4, 10))]
                        if (495, 600) in data.p4Ex['road']:
                            if (3, 11) not in data.occupied:
                                if (462.5, 656.25) in data.p4Ex['road']:
                                    if coordConverter((2, 12)) not in coords and (2, 12) not in data.occupied:
                                        coords += [coordConverter((2, 12))]
                                if (527.5, 656.25) in data.p4Ex['road']:
                                    if coordConverter((3, 12)) not in coords and (3, 12) not in data.occupied:
                                        coords += [coordConverter((3, 12))]
                    if i == (4, 10):
                        if (657.5, 543.75) in data.p4Ex['road']:
                            if (5, 9) not in data.occupied:
                                if (690, 487.5) in data.p4Ex['road']:
                                    if coordConverter((5, 8)) not in coords and (5, 8) not in data.occupied:
                                        coords += [coordConverter(5, 8)]
                        if (592.5, 543.75) in data.p4Ex['road']:
                            if (4, 9) not in data.occupied:
                                if (560, 487.5) in data.p4Ex['road']:
                                    if coordConverter((4, 8)) not in coords and (4, 8) not in data.occupied:
                                        coords += [coordConverter((4, 8))]
                                if (527.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                        if (625, 600) in data.p4Ex['road']:
                            if (4, 11) not in data.occupied:
                                if (592.5, 656.25) in data.p4Ex['road']:
                                    if coordConverter((3, 12)) not in coords and (3, 12) not in data.occupied:
                                        coords += [coordConverter((3, 12))]
                    if i == (1, 11):
                        if (235, 600) in data.p4Ex['road']:
                            if (1, 10) not in data.occupied:
                                if (202.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((1, 9)) not in coords and (1, 9) not in data.occupied:
                                        coords += [coordConverter((1, 9))]
                                if (267.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                        if (267.5, 656.25) in data.p4Ex['road']:
                            if (1, 12) not in data.occupied:
                                if (332.5, 656.25) in data.p4Ex['road']:
                                    if coordConverter((2, 11)) not in coords and (2, 11) not in data.occupied:
                                        coords += [coordConverter((2, 11))]
                    if i == (2, 11):
                        if (365, 600) in data.p4Ex['road']:
                            if (2, 10) not in data.occupied:
                                if (332.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((2, 9)) not in coords and (2, 9) not in data.occupied:
                                        coords += [coordConverter((2, 9))]
                                if (397.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                        if (332.5, 656.25) in data.p4Ex['road']:
                            if (1, 12) not in data.occupied:
                                if (267.5, 656.25) in data.p4Ex['road']:
                                    if coordConverter((1, 11)) not in coords and (1, 11) not in data.occupied:
                                        coords += [coordConverter((1, 11))]
                        if (397.5, 656.25) in data.p4Ex['road']:
                            if (2, 12) not in data.occupied:
                                if (462.5, 656.25) in data.p4Ex['road']:
                                    if coordConverter((3, 11)) not in coords and (3, 11) not in data.occupied:
                                        coords += [coordConverter((3, 11))]
                    if i == (3, 11):
                        if (495, 600) in data.p4Ex['road']:
                            if (3, 10) not in data.occupied:
                                if (462.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((3, 9)) not in coords and (3, 9) not in data.occupied:
                                        coords += [coordConverter((3, 9))]
                                if (527.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                        if (462.5, 656.25) in data.p4Ex['road']:
                            if (2, 12) not in data.occupied:
                                if (397.5, 656.25) in data.p4Ex['road']:
                                    if coordConverter((2, 11)) not in coords and (2, 11) not in data.occupied:
                                        coords += [coordConverter((2, 11))]
                        if (527.5, 656.25) in data.p4Ex['road']:
                            if (3, 12) not in data.occupied:
                                if (592.5, 656.25) in data.p4Ex['road']:
                                    if coordConverter((4, 11)) not in coords and (4, 11) not in data.occupied:
                                        coords += [coordConverter((4, 11))]
                    if i == (4, 11):
                        if (625, 600) in data.p4Ex['road']:
                            if (4, 10) not in data.occupied:
                                if (592.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((4, 9)) not in coords and (4, 9) not in data.occupied:
                                        coords += [coordConverter((4, 9))]
                                if (657.5, 543.75) in data.p4Ex['road']:
                                    if coordConverter((5, 9)) not in coords and (5, 9) not in data.occupied:
                                        coords += [coordConverter((5, 9))]
                        if (592.5, 656.25) in data.p4Ex['road']:
                            if (3, 12) not in data.occupied:
                                if (527.5, 656.25) in data.p4Ex['road']:
                                    if coordConveter((3, 11)) not in coords and (3, 11) not in data.occupied:
                                        coords += [coordConveter((3, 11))]
                    if i == (1, 12):
                        if (267.5, 656.25) in data.p4Ex['road']:
                            if (1, 11) not in data.occupied:
                                if (235, 600) in data.p4Ex['road']:
                                    if coordConverter((1, 10)) not in coords and (1, 10) not in data.occupied:
                                        coords += [coordConverter((1, 10))]
                        if (332.5, 656.25) in data.p4Ex['road']:
                            if (2, 11) not in data.occupied:
                                if (365, 600) in data.p4Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                                if (397.5, 656.25) in data.p4Ex['road']:
                                    if coordConverter((2, 12)) not in coords and (2, 12) not in data.occupied:
                                        coords += [coordConverter((2, 12))]
                    if i == (2, 12):
                        if (397.5, 656.25) in data.p4Ex['road']:
                            if (2, 11) not in data.occupied:
                                if (332.5, 656.25) in data.p4Ex['road']:
                                    if coordConverter((1, 12)) not in coords and (1, 12) not in data.occupied:
                                        coords += [coordConverter((1, 12))]
                                if (365, 600) in data.p4Ex['road']:
                                    if coordConverter((2, 10)) not in coords and (2, 10) not in data.occupied:
                                        coords += [coordConverter((2, 10))]
                        if (462.5, 656.25) in data.p4Ex['road']:
                            if (3, 11) not in data.occupied:
                                if (495, 600) in data.p4Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                                if (527.5, 656.25) in data.p4Ex['road']:
                                    if coordConverter((3, 12)) not in coords and (3, 12) not in data.occupied:
                                        coords += [coordConverter((3, 12))]
                    if i == (3, 12):
                        if (527.5, 656.25) in data.p4Ex['road']:
                            if (3, 11) not in data.occupied:
                                if (495, 600) in data.p4Ex['road']:
                                    if coordConverter((3, 10)) not in coords and (3, 10) not in data.occupied:
                                        coords += [coordConverter((3, 10))]
                                if (462.5, 656.25) in data.p4Ex['road']:
                                    if coordConverter((2, 12)) not in coords and (2, 12) not in data.occupied:
                                        coords += [coordConverter((2, 12))]
                        if (592.5, 656.25) in data.p4Ex['road']:
                            if (4, 11) not in data.occupied:
                                if (625, 600) in data.p4Ex['road']:
                                    if coordConverter((4, 10)) not in coords and (4, 10) not in data.occupied:
                                        coords += [coordConverter((4, 10))]
    return coords