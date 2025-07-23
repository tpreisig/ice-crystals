# Ice Crystals Animation

## Overview

This is a Pygame-based application that creates an interactive animation of ice crystal-like structures. When the user clicks the mouse on the predefined screen, a branching crystal pattern is generated from a fixed starting point to the mouse position. The crystals have a fading effect with flickering brightness and play a feedback sound ( ➡️ beautiful and crystal clear piano arpeggios).

## Features

- **Interactive Crystal Generation**: Click anywhere on the screen to generate a new crystal pattern.
- **Branching Patterns**: Crystals grow with randomized branching, creating unique patterns each time.
- **Visual Effects**: Particles fade out over time with a flickering brightness effect.
- **Sound Effects**: Plays a crystal sound effect (`crystal.mp3`) on click, if the file is found.
- **Smooth Animation**: Runs at 60 FPS with a crosshair cursor for precise interaction.

## Requirements

- Python 3.x
- Pygame (`pip install pygame-ce`)
- Optional: The audio file provided named `crystal.mp3` in the `audio/` directory relative to the script for sound effects.

## Installation

1. Ensure Python is installed on your system.
2. Install Pygame:
   ```bash
   pip install pygame-ce
   ```
3. Place the `crystal.mp3` file provided in the `audio/` folder in the same directory as the script for sound effects.

3. **Controls**:
   - Click the mouse to generate a new crystal pattern from (450, 100) to the mouse position.
   - Press `ESC` or close the window to exit.
4. The application will display a dark blue background with animated crystal patterns.

## Code Structure

- **Initialization**: Sets up Pygame, the display (1200x600), and attempts to load the `crystal.mp3` sound.
- **Crystal Generation**: The `create_crystals` function generates a segmented line with randomized offsets and optional branching.
- **Particle System**: Each crystal consists of particles with position, lifetime, thickness, color, and brightness.
- **Main Loop**:
  - Handles mouse clicks to create new crystals.
  - Updates particle lifetimes, thickness, and brightness for fading and flickering effects.
  - Draws lines and glowing particles using additive blending.
  - Removes expired particles and empty crystal patterns.
- **Error Handling**: Checks for invalid particle data and handles missing audio files gracefully.

## Notes

- If the `crystal.mp3` file is not found, the application will run without sound and print a message to the console.
- The crystal patterns are drawn with a subtle glow effect using a semi-transparent surface (`circle_surf`).
- The application maintains a steady 60 FPS for smooth animation.


## License

This project is unlicensed and provided as-is for educational purposes.

