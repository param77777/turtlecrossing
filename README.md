# Turtle Crossing Game

A fun and interactive game built using Python's `turtle` module. The goal is to guide the player (a turtle) across the screen while avoiding cars. With each successful crossing, the difficulty increases, making the game more challenging and exciting.

---

## Features
- **Dynamic Car Generation**: Cars appear at random intervals and positions.
- **Player Movement**: The player can move upwards to reach the finish line.
- **Increasing Difficulty**: The speed of the cars increases with each level.
- **Game Over Detection**: The game ends if a car collides with the player.
- **Scoreboard**: Displays the current level and shows "Game Over" when the game ends.

---

## How to Play
1. Run the game.
2. Use the **Up Arrow Key** to move the turtle upward.
3. Avoid the cars coming from the right side of the screen.
4. Reach the top of the screen to complete a level.
5. Each level increases the speed of the cars.
6. The game ends when the turtle collides with a car.

---

## Installation and Setup
1. Ensure you have Python 3.x installed on your system.
2. Clone this repository or copy the code files.
3. Install any required dependencies (none required beyond Python's standard library).

---

## Running the Game
1. Open a terminal or command prompt.
2. Navigate to the directory containing the game files.
3. Run the following command:
   ```bash
   python main.py
   ```

---

## Files in the Project
- **`main.py`**: The main driver file that initializes the game loop.
- **`player.py`**: Handles the player's movement and position.
- **`car_manager.py`**: Manages car creation, movement, and speed.
- **`scoreboard.py`**: Displays the current level and game-over message.

---

## Future Improvements
- Add sound effects for collisions and level completions.
- Implement a scoring system based on time taken to complete levels.
- Add more levels with varying obstacles and challenges.

---

## Acknowledgments
- Inspired by classic arcade-style crossing games.
- Built with Python's `turtle` module for fun and learning.
