# Snake Game

This is a simple implementation of the classic Snake game using Python and the `curses` library to create a terminal-based user interface.

## Features

- **Snake Movement**: Control the snake using the arrow keys (up, down, left, right).
- **Apple Collection**: The snake collects apples that appear randomly on the grid.
- **Dynamic Grid Rendering**: The game grid dynamically updates with the snake's position and the apple.
- **Game Over Condition**: The game ends when the snake collides with itself or the boundaries of the grid.
- **FPS Display**: The game displays the current frames per second (FPS) during gameplay.

## How to Play

1. **Controls**:
    - Use the arrow keys to change the direction of the snake:
      - `Up Arrow`: Move the snake up.
      - `Down Arrow`: Move the snake down.
      - `Left Arrow`: Move the snake left.
      - `Right Arrow`: Move the snake right.
    - Press `q` to quit the game at any time.

2. **Objective**:
    - Guide the snake to eat the apple (`■`) that appears randomly on the grid.
    - Each time the snake eats an apple, it grows longer.
    - Avoid running into the snake's own body or the edges of the grid, as this will result in a game over.

3. **Game Over**:
    - The game ends when the snake collides with itself or the grid's boundaries.
    - A "Game Over" message will be displayed, and the game will exit after a short delay.

## Installation and Setup

1. **Requirements**:
    - Python 3.x
    - `curses` library (pre-installed with Python on Unix-based systems, but may require installation on Windows)

2. **Running the Game**:
    - Clone or download the repository containing the game code.
    - Navigate to the directory containing the game script.
    - Run the game using the following command:
      ```bash
      python snake_game.py
      ```

## Customization

- **Grid Size**: The grid size is currently set to 15 rows by 17 columns. You can modify the grid size by changing the initialization in the `initialize()` function.
- **Snake Speed**: The snake's speed is controlled by the time interval (`0.2` seconds) in the `main()` loop. You can adjust this value to make the game faster or slower.
- **Symbols**: The symbols for the snake, apple, and empty spaces can be customized by modifying the `snake_body`, `snake_head`, `apple`, and `empty` variables.

## License

This project is open-source and available under the MIT License.

## Acknowledgments

- The `curses` library documentation for providing guidance on creating text-based user interfaces in Python.
