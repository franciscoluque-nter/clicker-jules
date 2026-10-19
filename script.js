// Helper functions to manage browser HTTP cookies
function setCookie(name, value, days = 365) {
  const date = new Date();
  date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
  const expires = "expires=" + date.toUTCString();
  document.cookie = `${name}=${encodeURIComponent(value)}; ${expires}; path=/; SameSite=Lax`;
}

function getCookie(name) {
  const nameEQ = name + "=";
  const ca = document.cookie.split(';');
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i].trim();
    if (c.indexOf(nameEQ) === 0) {
      return decodeURIComponent(c.substring(nameEQ.length, c.length));
    }
  }
  return null;
}

document.addEventListener('DOMContentLoaded', () => {
  const clickCountEl = document.getElementById('click-count');
  const cookieBtn = document.getElementById('cookie-btn');
  const resetBtn = document.getElementById('reset-btn');

  // Retrieve count from HTTP cookie or default to 0
  const savedCount = getCookie('cookieClickCount');
  let count = savedCount !== null ? parseInt(savedCount, 10) : 0;
  if (isNaN(count)) count = 0;

  clickCountEl.textContent = count;

  // Cookie click handler
  cookieBtn.addEventListener('click', (event) => {
    count++;
    clickCountEl.textContent = count;
    setCookie('cookieClickCount', count);

    // Create floating +1 effect
    createFloatingText(event);
  });

  // Create floating +1 text animation
  function createFloatingText(event) {
    const rect = cookieBtn.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    const floatEl = document.createElement('div');
    floatEl.className = 'floating-text';
    floatEl.textContent = '+1';

    // Position relative to cookie wrapper
    floatEl.style.left = `${x}px`;
    floatEl.style.top = `${y}px`;

    cookieBtn.appendChild(floatEl);

    // Remove element after animation completes
    floatEl.addEventListener('animationend', () => {
      floatEl.remove();
    });
  }

  // Reset button handler
  resetBtn.addEventListener('click', () => {
    count = 0;
    clickCountEl.textContent = count;
    setCookie('cookieClickCount', count);
  });

  // Client-side protections to discourage opening Developer Tools
  // Prevent right-click context menu
  document.addEventListener('contextmenu', (event) => {
    event.preventDefault();
  });

  // Prevent keyboard shortcuts for DevTools (F12, Ctrl+Shift+I/J/C, Ctrl+U, Cmd+Opt+I/J/C)
  document.addEventListener('keydown', (event) => {
    const isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;
    const isInspectShortcut =
      event.key === 'F12' ||
      ((event.ctrlKey || (isMac && event.metaKey)) &&
        event.shiftKey &&
        ['I', 'J', 'C', 'i', 'j', 'c'].includes(event.key)) ||
      ((event.ctrlKey || (isMac && event.metaKey)) &&
        ['U', 'u'].includes(event.key));

    if (isInspectShortcut) {
      event.preventDefault();
      event.stopPropagation();
    }
  });
});
