#!/bin/bash

# Launch the NFL Football Game

# Set the game path (assuming the game is in the current directory)
GAME_PATH="./nfl-football-game"

# Check if the game directory exists
if [ -d "$GAME_PATH" ]; then
    cd "$GAME_PATH" && ./run_game.sh
else
    echo "Game directory not found!"
fi
