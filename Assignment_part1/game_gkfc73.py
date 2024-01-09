from medialib import *

# Initialize the medialib for game development
initialize()

# Define the initial background of the game
background = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', '_', '_', 'L', '_', '_', 'M', '_', '_', 'E', '_', '_', 'J', '_', '_', '_', '_', 'X'],
    ['X', '_', '_', '_', 'M', '_', 'B', '_', 'L', '_', '_', '_', '_', 'B', '_', 'J', '_', 'X'],
    ['X', '_', '_', 'B', '_', '_', '_', '_', '_', 'J', '_', '_', 'E', '_', 'L', '_', '_', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]
# Constants

x0 = 10
y0 = 200
tile_size = 30

avatar_position = [1, 1]  # Initial avatar position
clear(200, 200, 200)
points = 0
game_running = True

# Function to update and display the current points
def update_points(points):
    text(f"Current points: {points}", 1, 10, 18)  # Display the new points

# Function to display welcome message
def display_welcome_message(message):
    text(message, 1, 130, 18)  # Display welcome message

# Create a dictionary to map the tile characters to the airline names
airline_names = {
    'B': 'British Airways',
    'E': 'EasyJet',
    'L': 'Lufthansa',
    'J': 'Jet2'
}

# Main game loop
while game_running:
    # Clear the screen for redrawing
    #clear(200, 200, 200)

    # Redraw the background

    for i, row in enumerate(background):
        for j, tile in enumerate(row):
            image_file = f'{tile}.png' if tile != '_' else '_.png'
            full_image_path = f'Files for assignment Part 1/MazeGame_imgs/{image_file}'
            draw(full_image_path, x0 + j * tile_size, y0 + i * tile_size)

    # Redraw the avatar
    draw('Files for assignment Part 1/MazeGame_imgs/H.png', x0 + avatar_position[1] * tile_size,
         y0 + avatar_position[0] * tile_size)

    # Display game information
    text('Maze game', 300, 100, 20)
    text('You are a lost hero and have to find your way back home...', 10, 500, 16)
    text('When you collect 20 points, you can get back home!', 10, 520, 16)
    text('To play: press "a" and "d" keys to move left and right', 10, 540, 16)
    text('       press "w" and "s" keys to move upwards and downwards', 10, 560, 16)
    text('       press "q" to quit the game', 10, 580, 16)

    # Get key input from the player
    key = wait_key_press()  # Replace this with actual function to wait for a key press


    # Move the avatar based on user input and check boundary conditions
    if key == 'a' and avatar_position[1] > 0 and background[avatar_position[0]][avatar_position[1] - 1] != 'X':
        avatar_position[1] -= 1
    elif key == 'd' and avatar_position[1] < len(background[0]) - 1 and background[avatar_position[0]][
        avatar_position[1] + 1] != 'X':
        avatar_position[1] += 1
    elif key == 'w' and avatar_position[0] > 0 and background[avatar_position[0] - 1][avatar_position[1]] != 'X':
        avatar_position[0] -= 1
    elif key == 's' and avatar_position[0] < len(background) - 1 and background[avatar_position[0] + 1][
        avatar_position[1]] != 'X':
        avatar_position[0] += 1
    elif key == 'q':  # Quit game command
        game_running = False

    else:
        clear(200, 200, 200)
        welcome_message = f"illegal input"
        display_welcome_message(welcome_message)
        update_points(points)

    # Check for standing on an airline logo and increase points
    current_tile = background[avatar_position[0]][avatar_position[1]]
    if current_tile in ['E', 'J', 'L', 'B']:
        points += 1  # Increase points
        update_points(points)  # Update and display the new points

        airline_name = airline_names[current_tile]
        welcome_message = f"Welcome on board with {airline_name}! You just received 1 point!"
        print(welcome_message)  # Print to the terminal
        clear(200, 200, 200)
        display_welcome_message(welcome_message)  # Display welcome message on screen
        update_points(points)
        background[avatar_position[0]][avatar_position[1]] = '_'  # Change the tile to road after moving away

    # when meet monster
    if current_tile in ['M']:
        clear(200, 200, 200)
        game_running = False
        display_welcome_message("Game over!!!")

    # when get 20 points
    if points >= 20:
        clear(200, 200, 200)
        draw('Files for assignment Part 1/MazeGame_imgs/you_win.png', 100, 50)
        wait(3)
        break

    if not game_running:
        clear(200, 200, 200)
        print("Game over!!!")
        display_welcome_message("Game over!!!")  # Display game over message on screen
        break


    if current_tile == 'B':
        points += 0
        update_points(points)
        clear(200, 200, 200)
        display_welcome_message("Welcome on board with British Airways! You just received 1 point!")
        update_points(points)

        draw('Files for assignment Part 1/MazeGame_imgs/I.png', 10, 200)
        text('However, now British Airways has an employee work crisis.', 10, 480, 20)
        text('If you help them to make the decision, you can get extra points!', 10, 500, 20)
        text('Please make your decision by inputting "h" or "i"', 10, 560, 20)
        text('    h. Hire new staff', 10, 520, 20)
        text('    i. Increase existing staff pay', 10, 540, 20)

        while True:
            choice = wait_key_press()
            if choice == 'h':
                points += 3
                update_points(points)
                clear(200, 200, 200)
                update_points(points)
                display_welcome_message("Thank you for helping British Airways to hire new staff! You received extra 3 points!")
                break
            elif choice == 'i':
                points += 5
                update_points(points)
                clear(200, 200, 200)
                update_points(points)
                display_welcome_message("Thank you for helping to increase staff pay at British Airways! You received extra 5 points!")
                break

            else:
                text("illegal input",1, 50, 18)
                update_points(points)

        background[avatar_position[0]][avatar_position[1]] = '_'
        # when get 20 points
        if points >= 20:
            clear(200, 200, 200)
            draw('Files for assignment Part 1/MazeGame_imgs/you_win.png', 100, 50)
            wait(3)
            break

        background[avatar_position[0]][avatar_position[1]] = '_'


wait_mouse_leftclick()
all_done()