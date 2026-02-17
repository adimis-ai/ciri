# Deep Web Research

CIRI's `web_researcher` agent isn't just a simple scraper—it uses your real browser to navigate the web, bypass bot detection, and access authenticated content.

## Chrome/Edge Integration

Ciri connects to your browser via the **Chrome DevTools Protocol (CDP)**. This means:
- It uses your existing cookies and sessions (e.g., it can research inside your private GitHub or AWS console).
- It renders JavaScript-heavy pages exactly as you see them.
- It can perform complex multi-step interactions (filling forms, clicking buttons).

## How to Enable

If you see a warning that "CDP port 9222 did not open":

1. **Close all browser windows**.
2. **Launch your browser with remote debugging enabled**:
   - **Linux/macOS**: `/usr/bin/google-chrome --remote-debugging-port=9222`
   - **Windows**: `chrome.exe --remote-debugging-port=9222`
3. **Restart CIRI**.

## Safety & Privacy

- Ciri only uses the browser when explicitly delegated by the `web_researcher` agent.
- You can provide specialized browser profiles via the `/change-browser-profile` command.
- Per security restrictions (Chrome v136+), Ciri may work with a *copy* of your profile to ensure safe CDP communication.
