# Cookie Clicker Web Application

A simple, responsive interactive web application featuring a centered cookie button and a counter that increments with every click.

## Features

- **Centered Cookie UI**: A styled chocolate chip cookie centered on the screen with interactive hover and click animations.
- **Click Counter**: Displays the total number of times the cookie has been clicked.
- **Interactive Visual Effects**: Generates floating `+1` text animations at the point of interaction whenever the cookie is clicked.
- **Persistent State**: Utilizes browser `localStorage` to save your click score so progress is preserved across page reloads.
- **Reset Functionality**: Includes a reset button to restore the click counter back to zero anytime.

## How to Run

1. Simply open `index.html` in any modern web browser (e.g., Double-click `index.html` or open via browser).
2. Alternatively, serve the files using a local HTTP server such as `npx serve .` or Python's `python3 -m http.server 8000`.

## Project Structure

- `index.html`: Contains the layout, inline CSS styles, cookie design elements, and interactive JavaScript logic.
- `README.md`: Documentation for the project.
