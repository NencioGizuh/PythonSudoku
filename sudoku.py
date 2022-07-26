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

def CheckHorizontal(sudokuSubList):
    cellenOptions = [1,2,3,4,5,6,7,8,9]
    for index,item in enumerate(sudokuSubList):
        if item == 0:
            continue
        elif item in cellenOptions:
            cellenOptions.remove(item)
        elif item not in cellenOptions:
            newNumber = random.randint(0, len(cellenOptions))
            sudokuSubList[index] = newNumber

    #dicthorizontalOne[0], dicthoriztonal[1], dicthorizontal[2] -> 
    
    #|-----------| # |---------|
    #|012|012|012|   |000111222|
    #|345|345|345|   |000111222| --> sudokuHorizontalOne[0,1,2]
    #|678|678|678|   |000111222|
    #|---|---|---|   |---------|
    #|012|012|012|   |333444555|
    #|345|345|345|   |333444555| --> sudokuHorizontalTwo[0,1,2]
    #|345|345|345|   |333444555|
    #|---|---|---|   |---------|
    #|012|012|012|   |666777888|
    #|345|345|345|   |666777888| --> sudokuHorizontalThree[6,7,8]
    #|678|678|678|   |666777888|
    #|-----------|   |---------|


    # We doen het per drie: 0,1,2 + 3,4,5 + 6,7,8
    # We checken elke keer deze sequenties 0,1,2,0,1,2,0,1,2 + 3,4,5,3,4,5,3,4,5 + 6,7,8,6,7,8,6,7,8

    #Dit wordt nu inefficient maar werk het eerst uit
    #Maak een functie waarin je een subsudoku meegeeft en de starting index zoals
def CreateHorizontalList(subHorizontal, horizontalListOne, horizontalListTwo, horizontalListThree):
    for value in subHorizontal.values():
        for sleutels, waardes in value.items():
            try:
                waarde = int(waardes)
            except:
                waarde = 0
            if sleutels == 0 or sleutels == 1 or sleutels == 2:
                horizontalListOne.append(waarde)
            elif sleutels == 3 or sleutels == 4 or sleutels == 5:
                horizontalListTwo.append(waarde)
            elif sleutels == 6 or sleutels == 7 or sleutels == 8:
                horizontalListThree.append(waarde)
    return horizontalListOne, horizontalListTwo, horizontalListThree

def GenerateSudoku():
    GenerateCellen(0)
    GenerateCellen(1)
    GenerateCellen(2)
    GenerateCellen(3)
    GenerateCellen(4)
    GenerateCellen(5)
    GenerateCellen(6)
    GenerateCellen(7)
    GenerateCellen(8)

    sudokuHorizontalListOne = []
    sudokuHorizontalListTwo = []
    sudokuHorizontalListThree = []
    sudokuHorizontalListFour = []
    sudokuHorizontalListFive = []
    sudokuHorizontalListSix = []
    sudokuHorizontalListSeven = []
    sudokuHorizontalListEight = []
    sudokuHorizontalListNine = []
    dictHorizontalOne = {}
    dictHorizontalTwo = {}
    dictHorizontalThree = {}
    dictHorizontalOne[0] = sudoku[0]
    dictHorizontalOne[1] = sudoku[1]
    dictHorizontalOne[2] = sudoku[2]
    dictHorizontalTwo[0] = sudoku[3]
    dictHorizontalTwo[1] = sudoku[4]
    dictHorizontalTwo[2] = sudoku[5]
    dictHorizontalThree[0] = sudoku[6]
    dictHorizontalThree[1] = sudoku[7]
    dictHorizontalThree[2] = sudoku[8]

    CreateHorizontalList(dictHorizontalOne, sudokuHorizontalListOne, sudokuHorizontalListTwo, sudokuHorizontalListThree)
    CreateHorizontalList(dictHorizontalTwo, sudokuHorizontalListFour, sudokuHorizontalListFive, sudokuHorizontalListSix)
    CreateHorizontalList(dictHorizontalThree, sudokuHorizontalListSeven, sudokuHorizontalListEight, sudokuHorizontalListNine)    
    CheckHorizontal(sudokuHorizontalListOne)
    CheckHorizontal(sudokuHorizontalListTwo)
    CheckHorizontal(sudokuHorizontalListThree)
    CheckHorizontal(sudokuHorizontalListFour)
    CheckHorizontal(sudokuHorizontalListFive)
    CheckHorizontal(sudokuHorizontalListSix)
    CheckHorizontal(sudokuHorizontalListSeven)
    CheckHorizontal(sudokuHorizontalListEight)
    CheckHorizontal(sudokuHorizontalListNine)
    print(sudokuHorizontalListOne)
    print(sudokuHorizontalListTwo)
    print(sudokuHorizontalListThree)
    print(sudokuHorizontalListFour)
    print(sudokuHorizontalListFive)
    print(sudokuHorizontalListSix)
    print(sudokuHorizontalListSeven)
    print(sudokuHorizontalListEight)
    print(sudokuHorizontalListNine)
    return sudoku

GenerateSudoku()

def CheckVertical(sudoku):
# We doen het per drie 0,3,6 + 1,4,7 + 2,5,8
# We checken elke keer deze sequenties 0,3,9,0,3,9,0,3,9 1,4,7,1,4,7,1,4,7 + 2,5,8,2,5,8,2,5,8
    return

