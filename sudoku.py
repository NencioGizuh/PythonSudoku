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

def GenerateCellen(sudokuCounter):
    cellenOptions = [1,2,3,4,5,6,7,8,9]
    randomInt = 8
    celOption = 0
    cellen = {}
    counter = 0
    while len(cellen) < 9:
        if(counter == 9):
            break
        filledOrNotFilled = random.randint(0,1)
        if filledOrNotFilled == 0:
            cel = {counter: ""}
            cellen.update(cel)
            counter += 1
            continue
        elif filledOrNotFilled == 1:
            randomNumber = random.randint(0,randomInt)
            randomInt -= 1
            celOption = cellenOptions[randomNumber]
            cellenOptions.remove(cellenOptions[randomNumber])
            cel = {counter: str(celOption)}
            cellen.update(cel)
            counter += 1
            continue
    #print(cellenOptions)
    #print(cellen)
    sudoku[sudokuCounter] = cellen
    sudokuCounter += 1
    return cellen

def GenerateSudoku():
    GenerateCellen(0)
    GenerateCellen(1)
    GenerateCellen(2)
    GenerateCellen(4)
    GenerateCellen(5)
    GenerateCellen(6)
    GenerateCellen(7)
    GenerateCellen(8)
    print(sudoku)
    return sudoku

GenerateSudoku()


def CheckHorizontal():
    return

def CheckVertical():
    return

def CheckNineCells():
    return

