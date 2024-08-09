# Comments added by ChatGPT
import random  # For generating random positions for the apple
import time    # For managing game timing
import curses  # For creating a terminal-based user interface

# Define constants for the different elements in the game
empty = "."       # Represents an empty space on the grid
snake_body = "●"  # Represents the body of the snake
snake_head = "@"  # Represents the head of the snake
apple = "■"       # Represents the apple

# Initialize the snake's position on the grid as a list of [row, col] pairs
snake = [[7, 1], [7, 2], [7, 3], [7, 4]]
# Initialize the apple's position on the grid
app_exists = [7, 12]
# Initialize the direction of the snake's movement
direction = "NONE"
# Initialize the game running status
running = True

def draw_snake(snake, grid):
    """
    Draw the snake on the grid.
    The body of the snake is drawn first, followed by the head.
    
    :param snake: List of [row, col] pairs representing the snake's position.
    :param grid: 2D list representing the game grid.
    :return: Updated grid with the snake drawn on it.
    """
    # Draw the snake's body (all parts except the head)
    for row, col in snake[:-1]:
        grid[row][col] = snake_body

    # Draw the snake's head
    head_row, head_col = snake[-1]
    grid[head_row][head_col] = snake_head
    
    return grid

def update_snake(snake, direction):
    """
    Update the snake's position based on the current direction.
    
    :param snake: List of [row, col] pairs representing the snake's position.
    :param direction: The current direction of the snake's movement.
    :return: Updated snake list and a boolean indicating if the snake is still alive.
    """
    # Copy the current head of the snake
    head = snake[-1].copy()

    # Move the head in the specified direction
    if direction == "UP":
        head[0] -= 1
    elif direction == "DOWN":
        head[0] += 1
    elif direction == "LEFT":
        head[1] -= 1
    elif direction == "RIGHT":
        head[1] += 1
    else:
        # If no valid direction, return the snake unchanged and still alive
        return snake, True

    # Check for collisions with the snake's body or the grid boundaries
    if head in snake or head[0] < 0 or head[0] >= 15 or head[1] < 0 or head[1] >= 17:
        return snake, False  # Collision detected, snake is not alive

    # Update the snake by adding the new head position and removing the tail
    snake.append(head)
    snake.pop(0)
    
    return snake, True  # Snake is still alive

def check_apple(grid, snake, app_exists):
    """
    Check if the snake has eaten the apple and generate a new apple if necessary.
    
    :param grid: 2D list representing the game grid.
    :param snake: List of [row, col] pairs representing the snake's position.
    :param app_exists: [row, col] pair representing the apple's position.
    :return: Updated grid and the new apple position.
    """
    # Check if the snake's head is on the apple
    if snake[-1] == app_exists:
        # Generate a new apple position that is not on the snake
        while True:
            col = random.randint(0, 16)
            row = random.randint(0, 14)
            if [row, col] not in snake:
                app_exists = [row, col]
                break
    
    # Place the apple on the grid
    grid[app_exists[0]][app_exists[1]] = apple
    
    return grid, app_exists

def initialize():
    """
    Initialize the game grid with empty spaces.
    
    :return: 2D list representing the initialized game grid.
    """
    grid = [[empty] * 17 for _ in range(15)]
    return grid

def main(stdscr):
    """
    Main function to handle the game loop and rendering.
    
    :param stdscr: The main screen object provided by curses.wrapper.
    """
    global direction, snake, running, app_exists

    # Initialize timing for movement and FPS calculation
    start_time = time.time()
    fps_start = time.time()

    # Initialize the grid and set up the terminal
    grid = initialize()
    stdscr.clear()
    stdscr.addstr(0, 0, "Press arrow keys (up, down, left, right). Press 'q' to exit.")
    curses.curs_set(0)
    stdscr.nodelay(True)  # Make getch non-blocking
    runs = 0  # To count the number of iterations for FPS calculation

    while running:
        key = stdscr.getch()  # Get the pressed key
        runs += 1

        # Change direction based on the pressed key, avoiding reverse direction
        if key == curses.KEY_UP and direction != "DOWN":
            direction = "UP"
        elif key == curses.KEY_DOWN and direction != "UP":
            direction = "DOWN"
        elif key == curses.KEY_LEFT and direction != "RIGHT" and direction != "NONE":
            direction = "LEFT"
        elif key == curses.KEY_RIGHT and direction != "LEFT":
            direction = "RIGHT"
        elif key == ord('q'):  # Exit the game if 'q' is pressed
            break
        
        # Update the snake's position at regular intervals
        if time.time() - start_time >= 0.2:
            snake, alive = update_snake(snake, direction)
            if not alive:  # End the game if the snake is not alive
                running = False
            start_time = time.time()

        # Get the terminal's size
        height, width = stdscr.getmaxyx()

        # Re-initialize the grid and update it with the apple and snake
        grid = initialize()
        grid, app_exists = check_apple(grid, snake, app_exists)
        grid = draw_snake(snake, grid)

        # Clear the screen and render the grid
        stdscr.clear()
        start_col = 0
        for i, row in enumerate(grid, start=4):
            start_col = (width - len(" ".join(row))) // 2  # Center the grid horizontally
            stdscr.addstr(i + 2, start_col, " ".join(row))

        # Calculate and display the FPS
        fps = f"fps: {str(int(runs / (time.time() - fps_start)))}"
        stdscr.addstr(1, (width - len(fps)) // 2, fps)
        stdscr.refresh()

    # Display the game over message
    stdscr.addstr(len(grid) + 6, 0, "Game Over!")
    stdscr.refresh()
    time.sleep(2)

if __name__ == '__main__':
    curses.wrapper(main)
