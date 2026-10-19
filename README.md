# Cookie Clicker Web Application

A simple, responsive, and interactive Cookie Clicker web application built with HTML, CSS, and plain JavaScript.

## Features

- **Centered Interactive Cookie**: A styled CSS cookie complete with chocolate chips and interactive hover/active click scale effects.
- **Click Counter & Floating Popups**: Tracks total cookie clicks with an animated `+1` popup effect appearing at the cursor location on each click.
- **HTTP Cookie Persistence**: Uses standard browser cookies (`cookieClickCount`) to store click count across page reloads.
- **Achievement & Trophy System**: Unlocks trophy badges dynamically as click milestones are reached:
  - 🥉 **Bronze Cookie**: 10 Clicks
  - 🥈 **Silver Cookie**: 100 Clicks
  - 🥇 **Gold Cookie**: 1000 Clicks
- **Reset Functionality**: Includes a reset button to reset click count and trophy statuses back to zero.
- **DevTools Restrictions**: Intercepts context menu (right-click) and common Developer Tools hotkeys (`F12`, `Ctrl+Shift+I/J/C`, `Cmd+Option+I/J/C`, `Ctrl+U`) to prevent accidental or unauthorized cookie tampering.

## File Structure

```text
├── index.html             # Structure, CSS styling, and trophy achievement layout
├── script.js              # Click tracking, cookie helper functions, achievements logic, and DevTools blocking
├── README.md              # Project documentation
└── verification/          # Automated test scripts
    └── test_app.py        # Playwright test suite for app features and achievements
```

## How to Run

1. Open `index.html` in any web browser, or serve it using a local web server (e.g., `python3 -m http.server 8080`).
2. Click the cookie to increase your score and unlock trophies.

## Testing

Automated Playwright tests are located in the `verification/` folder:

```bash
# Run automated verification tests
python3 verification/test_app.py
```
