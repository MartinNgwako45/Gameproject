

import pygame # We are importing a game library thta will allows us to use specicfic functions in our library.
import random # Importing random in order to generate random numbers.

# Initializing pygame module in order to start everything.

pygame.init() 

# We need to set a width and height for the game screen.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player, enemies and prize and attributes chosen images to them.

player = pygame.image.load("player1.jpg")
enemy = pygame.image.load("ghost.png")
enemy2 = pygame.image.load("enemy11.jpg")
enemy3 = pygame.image.load("green_ghost.jpg")
prize = pygame.image.load("prize33.jpg")

# Get the width and height of the images in order to do boundary detection and make sure the image does not pass the screen and to know when it does.

image_height = player.get_height()
image_width = player.get_width()

enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()


print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Storing the positions of the players, enemies and prize so the variables can constantly change. 

playerXPosition = 500
playerYPosition = 50

# Making the enemy start off screen and at a random y position.

enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)

enemy2xposition = screen_width
enemy2yposition = random.randint(0, screen_height - enemy2_height)

enemy3xposition = 20
enemy3yposition = random.randint(0, screen_height - enemy3_height)

prizexposition = 10
prizeyposition = random.randint(0, screen_height - prize_height)

# This checks if the up or down or left or right key is pressed.
# Right now they are not so we make them false 

keyUp= False
keyDown = False
keyleft =False
keyright = False

# This is the game loop.

while 1:

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. 
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy2, (enemy2xposition, enemy2yposition))
    screen.blit(enemy3, (enemy3xposition, enemy3yposition))
    screen.blit(prize, (prizexposition, prizeyposition))
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True

            if event.key == pygame.K_LEFT:
                keyleft = True
            if event.key == pygame.K_RIGHT:
                keyright = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False

            if event.key == pygame.K_LEFT:
                keyleft = False
            if event.key == pygame.K_RIGHT:
                keyright = False

    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if want the player to move up we have to increase the y value 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1

    if keyleft == True:       
        if playerXPosition > 0 :
            playerXPosition -= 1

    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1

    if keyright == True:
        if playerXPosition < screen_width - image_width:
            playerXPosition += 1

    # Checking for collision of the enemies with the player.
    # To do this we need bounding boxes around the pictures of the player and enemies.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding boxes for the enemies:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition
    
    enemy2box = pygame.Rect(enemy2.get_rect())
    enemy2box.top = enemy2yposition
    enemy2box.left = enemy2xposition

    enemy3box = pygame.Rect(enemy3.get_rect())
    enemy3box.top = enemy3yposition
    enemy3box.left = enemy3xposition

    prizebox = pygame.Rect(prize.get_rect())
    prizebox.top = prizeyposition
    prizebox.left = prizexposition


    # Test collision of the boxes:
    
    if playerBox.colliderect(enemyBox):

        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy2box):

        print("You lose!")

        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy3box):

        print("You lose!")
        
        pygame.quit()
        exit(0)
        
    # If one the enemies is off the screen the user wins the game:
    
    if enemyXPosition < 0 - enemy_width:

        print("You win!")

        pygame.quit()
        
        exit(0)
        
    if enemy2xposition < 0 - enemy_width:
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
    
    if enemy3xposition > 1040:

     print("You win!")
         
     pygame.quit()
        
     exit(0)

    if playerBox.colliderect(prizebox):
    
     print("You win!")
        
        # Quite game and exit window: 
     pygame.quit()
       
     exit(0)
    
    
    # Make enemies approach the player in different speeds.
    
    enemyXPosition -= 0.60
    enemy2xposition -= 0.90
    enemy3xposition += 0.15
    prizexposition += 0.50
    

  

