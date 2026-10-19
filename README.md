# Cookie Clicker Web Application

A simple, responsive interactive web application featuring a centered cookie button and a counter that increments with every click.

## Features

- **Centered Cookie UI**: A styled chocolate chip cookie centered on the screen with interactive hover and click animations.
- **Click Counter**: Displays the total number of times the cookie has been clicked.
- **Interactive Visual Effects**: Generates floating `+1` text animations at the point of interaction whenever the cookie is clicked.
- **Cookie Persistence**: Utilizes browser HTTP cookies (`document.cookie`) to store your click count so progress is preserved across page reloads.
- **Reset Functionality**: Includes a reset button to restore the click counter back to zero anytime.
- **Client-Side DevTools Prevention**: Disables right-click context menus and intercepts common developer tools keyboard shortcuts (F12, `Ctrl+Shift+I/J/C`, `Ctrl+U`) to discourage basic client-side tampering (note: client-side restrictions are for user experience/guidance, as true web security relies on server-side logic).

## How to Run

1. Simply open `index.html` in any modern web browser (e.g., double-click `index.html` or open via browser).
2. Alternatively, serve the files using a local HTTP server such as `npx serve .` or Python's `python3 -m http.server 8000`.

## Project Structure

- `index.html`: Main HTML file containing the structure and styles for the web application.
- `script.js`: External JavaScript file containing counter logic, visual animations, and HTTP cookie management functions (`setCookie`, `getCookie`).
- `README.md`: Documentation for the project.
