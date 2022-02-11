import pygame 

#INITIALIZE PYGAME
pygame.init()

#WINDOW VARIABLES
WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode ((WIDTH, HEIGHT))
pygame.display.set_caption("GABE MADE ME DO THIS!")
FPS = 60

#COLOR
WHITE = (255, 255, 255)
BLACK = (0,0,0)
GREEN =(122, 186, 122)
YELLOW = (255, 217, 0)
GRAY = (192, 192, 192)

#FONT
TITLE_FONT = pygame.font.SysFont ("comicsans", 60)
KEYBOARD_LETTER_FONT = pygame.font.SysFont ("comicsans", 15)
GRID_LETTER_FONT = pygame.font.SysFont ("comicsans", 40)

#GAME GRID SETTINGS
grid = []
GRID_DIMENSION = 50
GAP = 20
startx = round ((WIDTH - 8*GAP - 5*GRID_DIMENSION)/2)
starty = 125    

for i in range (30):
    x = startx + GAP*2 + ((GRID_DIMENSION + GAP)) * (i%5)
    y = starty + ((i//5)) * (GAP + GRID_DIMENSION) 
    grid.append ([x,y])

#KEYBOARD SETTINGS
first_Row =[]
letters_First_Row = 10
second_Row =[]
letters_Second_Row = 9
third_Row =[]
letters_Third_Row = 7
enter_Key = []
backspace_Key = []

letter_Width = 30
letter_Height = 40

gap_Letter = 10

startx_First_Row = round ((WIDTH - 10*gap_Letter - 11*letter_Width)/2)
starty_First_Row = 525

letter_First_Representation = ""

for i in range (letters_First_Row):
    first_row_x = startx_First_Row + gap_Letter*2 + ((letter_Width + gap_Letter))* (i%letters_First_Row)
    first_row_y = starty_First_Row + gap_Letter + letter_Height 
    if i == 0: letter_First_Representation = "Q"
    elif i == 1: letter_First_Representation = "W"
    elif i == 2: letter_First_Representation = "E"
    elif i == 3: letter_First_Representation = "R"
    elif i == 4: letter_First_Representation = "T"
    elif i == 5: letter_First_Representation = "Y"
    elif i == 6: letter_First_Representation = "U"
    elif i == 7: letter_First_Representation = "I"
    elif i == 8: letter_First_Representation = "0"
    elif i == 9: letter_First_Representation = "P"
    first_Row.append ([first_row_x, first_row_y, letter_First_Representation])

print (first_Row)

startx_Second_Row = round ((WIDTH - 10*gap_Letter - 9.5*letter_Width)/2)
starty_Second_Row = 525 + letter_Height + gap_Letter

letter_Second_Representation = ""

for i in range (letters_Second_Row):
    second_row_x = startx_Second_Row + gap_Letter*2 + ((letter_Width + gap_Letter))* (i%letters_Second_Row)
    second_row_y = starty_Second_Row + gap_Letter + letter_Height 
    if i == 0: letter_Second_Representation = "A"
    if i == 1: letter_Second_Representation = "S"
    if i == 2: letter_Second_Representation = "D"
    if i == 3: letter_Second_Representation = "F"
    if i == 4: letter_Second_Representation = "G"
    if i == 5: letter_Second_Representation = "H"
    if i == 6: letter_Second_Representation = "J"
    if i == 7: letter_Second_Representation = "K"
    if i == 8: letter_Second_Representation = "L"
    
    second_Row.append ([second_row_x, second_row_y, letter_Second_Representation])

print (second_Row)

startx_Third_Row = round ((WIDTH - 11*gap_Letter - 6.5*letter_Width)/2)
starty_Third_Row = 525 + (letter_Height + gap_Letter) * 2

letter_Third_Representation = ""

for i in range (letters_Third_Row):
    third_row_x = startx_Third_Row + gap_Letter*2 + ((letter_Width + gap_Letter))* (i%letters_Third_Row)
    third_row_y = starty_Third_Row + gap_Letter + letter_Height 
    
    if i == 0: letter_Third_Representation = "Z"
    if i == 1: letter_Third_Representation = "X"
    if i == 2: letter_Third_Representation = "C"
    if i == 3: letter_Third_Representation = "V"
    if i == 4: letter_Third_Representation = "B"
    if i == 5: letter_Third_Representation = "N"
    if i == 6: letter_Third_Representation = "M"
    
    third_Row.append ([third_row_x, third_row_y, letter_Third_Representation])

print (third_Row)

backspace_Width = enter_Width = 1.5 * letter_Width + 0.5 * gap_Letter
backspace_Height = enter_Height = 40
enter = []
backspace = []

startx_Enter = round ((WIDTH - 10.5*gap_Letter - 6*letter_Width)/2) - enter_Width
starty_Enter = 525 + (letter_Height + gap_Letter) * 3
enter_word = "Enter"
enter.append ([startx_Enter, starty_Enter, enter_word])

startx_Backspace = round ((WIDTH + 11.5*gap_Letter + 6*letter_Width)/2) 
starty_Backspace = 525 + (letter_Height + gap_Letter) * 3
backspace_word = "Delete"
backspace.append ([startx_Backspace, starty_Backspace, backspace_word])

#PRINT LETTERS ONTO GRID
guessed_Word = []


#COMPUTER GENERATED WORD
generated_Word = "skill"


#DISPLAYS GAME SCREEN 
def display_Screen():
    WINDOW.fill (BLACK)

    #DISPLAY TITLE 
    text = TITLE_FONT.render ("WELCOME TO WORDLE", 1, WHITE)
    WINDOW.blit (text, (WIDTH/2 - text.get_width()/2, 20))

    #DISPLAY 5 COLUMNNS, 6 ROWS: THE GAME GRID
    for letter in grid:
        x, y = letter
        pygame.draw.rect (WINDOW, GREEN, pygame.Rect(x, y, GRID_DIMENSION, GRID_DIMENSION))

    
    #DISPLAY KEYBOARD
    #display first row of keyboard
    for first_keys in first_Row:
        first_row_x, first_row_y, letter_First_Representation = first_keys
        pygame.draw.rect (WINDOW, YELLOW, pygame.Rect(first_row_x, first_row_y, letter_Width, letter_Height))
        text = KEYBOARD_LETTER_FONT.render (letter_First_Representation, 1, BLACK)
        WINDOW.blit (text ,(first_row_x, first_row_y))
    
    #display second row of keyboard
    for second_keys in second_Row:
        second_row_x, second_row_y, letter_Second_Representation = second_keys
        pygame.draw.rect (WINDOW, YELLOW, pygame.Rect(second_row_x, second_row_y, letter_Width, letter_Height))
        text = KEYBOARD_LETTER_FONT.render (letter_Second_Representation, 1, BLACK)
        WINDOW.blit (text ,(second_row_x, second_row_y))

    #display third row of keyboard
    for third_keys in third_Row:
        third_row_x, third_row_y, letter_Third_Representation = third_keys
        pygame.draw.rect (WINDOW, YELLOW, pygame.Rect(third_row_x, third_row_y, letter_Width, letter_Height))
        text = KEYBOARD_LETTER_FONT.render (letter_Third_Representation, 1, BLACK)
        WINDOW.blit (text ,(third_row_x, third_row_y))

    #display enter and backspace keys
    for enter_ky in enter:
            startx_Enter, starty_Enter, enter_word = enter_ky
            pygame.draw.rect (WINDOW, WHITE, pygame.Rect(startx_Enter, starty_Enter, enter_Width, enter_Height))
            text = KEYBOARD_LETTER_FONT.render (enter_word, 1, BLACK)
            WINDOW.blit (text ,(startx_Enter, starty_Enter))
        
    for backspace_ky in backspace:
            startx_Backspace, starty_Backspace, backspace_word = backspace_ky
            pygame.draw.rect (WINDOW, GREEN, pygame.Rect(startx_Backspace, starty_Backspace, backspace_Width, backspace_Height)) 
            text = KEYBOARD_LETTER_FONT.render (backspace_word, 1, BLACK)
            WINDOW.blit (text ,(startx_Backspace, starty_Backspace))
    
    pygame.display.update()


#display guessed_Word into a new 6x5 grid overlaying the Grid two-dimensional array
def display_Word (guessed_Word,  delete):
    for i in range (len(guessed_Word)):
        x = startx + GAP*2 + ((GRID_DIMENSION + GAP)) * (i%5)
        y = starty + ((i//5)) * (GAP + GRID_DIMENSION) 
        text = GRID_LETTER_FONT.render (guessed_Word[i], 1, BLACK)
        WINDOW.blit (text, (x,y))
        if delete:
            x = startx + GAP*2 + ((GRID_DIMENSION + GAP)) * (len(guessed_Word)%5)
            y = starty  
            pygame.draw.rect (WINDOW, GREEN, pygame.Rect(x, y, GRID_DIMENSION, GRID_DIMENSION))
    if len(guessed_Word) ==  0 and delete:
        x = startx + 2*GAP
        y = starty  
        pygame.draw.rect (WINDOW, GREEN, pygame.Rect(x, y, GRID_DIMENSION, GRID_DIMENSION))
    
    pygame.display.update()

    



#check to see if the guessed_Word matches the computer generated word
#change color of original grid according to the rules (using another 2 dimensional array to layer on top of Grid?)

check_Guess = []
#correct letter, right space = 0
#correct letter, wrong space = 1
#wrong letter = 2
def check_Word (guessed_Word):
    print (generated_Word.upper())
    for i in range (len(generated_Word)):
        if guessed_Word [i] in generated_Word.upper()[i:i+1]:
            check_Guess.append (0)
        elif guessed_Word [i] in generated_Word.upper():
            check_Guess.append (1)
        else: 
            check_Guess.append (2)   



#color the grid the appropriate color based on values
#def color_Grid ()


def main ():
    run = True
    clock = pygame.time.Clock()
    row = 0
    delete = False

    display_Screen()

    while run: 
        clock.tick (FPS)
        pressed_Key = ""
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_Position_X, mouse_Position_Y = pygame.mouse.get_pos()
                for first_keys in first_Row:
                    x, y, letter = first_keys
                    if (mouse_Position_X >= x and mouse_Position_X <= x + letter_Width and mouse_Position_Y >= y and mouse_Position_Y <= y + letter_Height):
                        pressed_Key = letter
                        if len (guessed_Word) <5: 
                            guessed_Word.append (pressed_Key)
                for second_keys in second_Row:
                    x, y, letter = second_keys
                    if (mouse_Position_X >= x and mouse_Position_X <= x + letter_Width and mouse_Position_Y >= y and mouse_Position_Y <= y + letter_Height):
                        pressed_Key = letter
                        if len (guessed_Word) <5:
                            guessed_Word.append (pressed_Key)
                for third_keys in third_Row:
                    x, y, letter = third_keys
                    if (mouse_Position_X >= x and mouse_Position_X <= x + letter_Width and mouse_Position_Y >= y and mouse_Position_Y <= y + letter_Height):
                        pressed_Key = letter
                        if len (guessed_Word) <5:
                            guessed_Word.append (pressed_Key)
                for enter_ky in enter:
                    x, y, enter_word = enter_ky
                    if (mouse_Position_X >= x and mouse_Position_X <= x + enter_Width and mouse_Position_Y >= y and mouse_Position_Y <= y + enter_Height):
                        pressed_Key = enter_word
                        if len(guessed_Word) == 5:
                            check_Word (guessed_Word) 



                            print (check_Guess)
                            #color the grid the appropriate color based on values
                            #color_Grid ()



                            guessed_Word.clear()
                for backspace_ky in backspace:
                    x, y, backspace_word = backspace_ky
                    if (mouse_Position_X >= x and mouse_Position_X <= x + backspace_Width and mouse_Position_Y >= y and mouse_Position_Y <= y + backspace_Height):
                        pressed_Key = backspace_word
                        if len(guessed_Word) > 0:
                            if len(guessed_Word) == 1: guessed_Word.clear()
                            else: guessed_Word.pop()
                            delete = True

                print (f"Guessed word: {guessed_Word} + Guess: {row}")
                
                display_Word (guessed_Word, delete)

                #reset the delete variable to false
                delete = False

    pygame.quit()

if __name__ == "__main__":
    main()
