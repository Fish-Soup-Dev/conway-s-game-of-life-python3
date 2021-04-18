import pygame
pygame.init()

# Screen size
width = 500
hight = 500
screen = pygame.display.set_mode([width, hight])

i = 0
squares = []
squares_freaze = []

# Make Array all 0's
while i != 25001:
    squares.append("0")
    squares_freaze.append("0")
    i = i + 1

print(25000, len(squares))

def count_around(count):
    num_of_alive = 0
    # left and right
    if count > 0:
        if squares_freaze[count - 1] == "1":
            num_of_alive += 1
    if count != 24999:
        if squares_freaze[count + 1] == "1":
            num_of_alive += 1
    # Top
    if count >= 49:
        if squares_freaze[count - 49] == "1":
            num_of_alive += 1
    if count >= 50:
        if squares_freaze[count - 50] == "1":
            num_of_alive += 1
    if count >= 51:
        if squares_freaze[count - 51] == "1":
            num_of_alive += 1
    # Bottom
    if count <= 24951:
        if squares_freaze[count + 49] == "1":
            num_of_alive += 1
    if count <= 24950:
        if squares_freaze[count + 50] == "1":
            num_of_alive += 1
    if count <= 24949:
        if squares_freaze[count + 51] == "1":
            num_of_alive += 1

    return num_of_alive

# Run until the user asks to quit
run = False
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Detect key and start or stop game
            if pygame.key.name(event.key) == 'g':
                run = True
            if pygame.key.name(event.key) == 's':
                run = False
            if pygame.key.name(event.key) == 'r':
                i = 0
                # Make Array all 0's
                while i != 25001:
                    squares[i] = "0"
                    i = i + 1

    # Set colors 
    screen.fill((100, 100, 100))

    i = 0

    while i != 25001:
        squares_freaze[i] = squares[i]
        i = i + 1

    if run == True:
        count = 0
        while count != (25000):
            
            # If its alive
            if squares[count] == "1":
                num_of_alive = 0
                
                num_of_alive = count_around(count)

                # Set square dead or alive based on sournding squares
                if num_of_alive == 3 or num_of_alive == 2:
                    squares[count] = "1"
                else:
                    squares[count] = "0"

            # If its dead
            if squares[count] == "0":
                num_of_alive = 0

                num_of_alive = count_around(count)

                # Set alive if 3 squares are near
                if num_of_alive == 3:
                    squares[count] = "1"

            count += 1
        
    i = 0
    x = 0
    y = 0

    # draw squares
    while i != len(squares):

        if squares[i] == "1":
            color = (0, 0, 0)
            pygame.draw.rect(screen, color, pygame.Rect(x * 10, y * 10, 9, 9))
        elif squares[i] == "0":
            color = (200, 200, 200)
            pygame.draw.rect(screen, color, pygame.Rect(x * 10, y * 10, 9, 9))

        i = i + 1
        x = x + 1

        if x == (width / 10):
            x = 0
            y = y + 1

    # Get mouse location and button pressed and update tiles
    if run == False:
        mousebutton = pygame.mouse.get_pressed()
        if mousebutton == (True, False, False):
            x, y = pygame.mouse.get_pos()
            x = int(x / 10)
            y = int(y / 10)

            out = x + (y * 50)

            ans = squares[out]

            if ans == "1":
                squares[out] = "1"
            if ans == "0":
                squares[out] = "1"

        if mousebutton == (False, False, True):
            x, y = pygame.mouse.get_pos()
            x = int(x / 10)
            y = int(y / 10)

            out = x + (y * 50)

            ans = squares[out]

            if ans == "1":
                squares[out] = "0"
            if ans == "0":
                squares[out] = "0"

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()