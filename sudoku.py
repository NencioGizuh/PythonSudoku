import random

#Genereer een sudoku
#Maak een frame/reeks van 8 elementen (0-9) die aangeven of ze gevuld zijn of niet
#De reden om te weten of het al gevuld is helpt later bij het oplossen
# {0:""}

#Sudoku strategieen
# Eerste strategie: Bekijk de opties die je kan passen in elk vak, als er maar een getal overblijft betekent dit
# dat dit nummer erin kan. 
# Dit doe je door verticaal, horizontaal en in de acht vakjes eromheen te checken voor de nummers
# Tweede strategie: X-wing en Y wing

sudoku = {}

def CheckForSameNumber(dictionary, nummer):
#We moeten checken in de dictionary of een key/value pair het nummer heeft wat we willen toevoegen
#Als het nummer gelijk is aan elkaar genereer dan een nieuw nummer tussen 1 en 9
    for key, value in dictionary.items():
        try:
            if int(value) == nummer:
                randomNumber = random.choice([i for i in range(0,9) if i not in [nummer]])
                print(randomNumber)
                #randomNumber = str(random.randint(1, 9))
                if randomNumber == nummer:
                    continue
                dictionary[key] = randomNumber
            else:
                continue
        except ValueError:
            continue
    return dictionary

CheckForSameNumber({1: "5"}, 5)

def GenerateCellen():
    cellen = {}
    counter = 0
    sudokuCounter = 0
    while len(cellen) <= 9:
        if(counter == 9):
            break
        filledOrNotFilled = random.randint(0,1)
        if filledOrNotFilled == 0:
            cel = {counter: ""}
            cellen.update(cel)
            counter += 1
            continue
        elif filledOrNotFilled == 1:
            randomNumber = str(random.randint(1, 9))
            CheckForSameNumber(cellen, randomNumber)
            cel = {counter: randomNumber}
            cellen.update(cel)
            counter += 1
            continue

    sudoku[sudokuCounter] = cellen
    sudokuCounter += 1
    if sudokuCounter == 9:
        sudokuCounter = 0
    return cellen

def GenerateSudoku():
    while len(sudoku) < 9:
        GenerateCellen()
    print(sudoku)
    return sudoku

#GenerateSudoku()



def CheckHorizontal():
    return

def CheckVertical():
    return

def CheckNineCells():
    return

