# Using Existing Browser Sessions

This guide explains how to use Duolingo Copilot with an existing browser session where you're already logged in to Duolingo.

## Why Use an Existing Browser?

- **Maintain Login State**: No need to log in repeatedly
- **Multi-Factor Authentication**: Easier to handle 2FA/MFA
- **Session Persistence**: Keep cookies, browsing history, and preferences
- **Development/Debugging**: Easier to debug and inspect what's happening

## Method 1: Remote Debugging (Recommended)

### Quick Start

**Windows:**
```cmd
start_chrome_debug.bat
```

**Linux/macOS:**
```bash
./start_chrome_debug.sh
```

Then in another terminal:
```bash
python duolingo_copilot.py --cdp-url http://localhost:9222 --skip-login
```

### Manual Setup

1. **Start Chrome with remote debugging:**

   **Windows:**
   ```cmd
   chrome.exe --remote-debugging-port=9222
   ```

   **macOS:**
   ```bash
   /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
   ```

   **Linux:**
   ```bash
   google-chrome --remote-debugging-port=9222
   ```

2. **Log in to Duolingo** in the browser window that opens

3. **Run the copilot:**
   ```bash
   python duolingo_copilot.py --cdp-url http://localhost:9222 --skip-login
   ```

### Using Environment Variables

Instead of passing `--cdp-url` every time, add to your `.env` file:

```bash
CHROME_CDP_URL=http://localhost:9222
```

Then simply run:
```bash
python duolingo_copilot.py --skip-login
```

## Method 2: Persistent Browser Profile

Use a Chrome user data directory to maintain sessions across runs:

```bash
python duolingo_copilot.py --user-data-dir ~/.chrome-duolingo
```

Or in `.env`:
```bash
CHROME_USER_DATA_DIR=/home/user/.chrome-duolingo
```

**Advantages:**
- Sessions persist between runs
- No need to start Chrome separately
- Simpler setup

**Note:** The first run will create a new profile. Log in to Duolingo, and subsequent runs will reuse that session.

## Command Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `--cdp-url URL` | Connect to existing Chrome browser | `--cdp-url http://localhost:9222` |
| `--user-data-dir PATH` | Use persistent Chrome profile | `--user-data-dir ~/.chrome-profile` |
| `--skip-login` | Skip automatic login | `--skip-login` |

## Using Different Ports

If port 9222 is already in use, you can use a different port:

```bash
# Start Chrome with custom port
chrome.exe --remote-debugging-port=9333

# Connect with custom port
python duolingo_copilot.py --cdp-url http://localhost:9333 --skip-login
```

## Troubleshooting

### "Failed to connect to browser"

**Solution 1:** Make sure Chrome is running with remote debugging:
```bash
# Check if Chrome is listening on the port
curl http://localhost:9222/json/version
```

**Solution 2:** Check firewall settings allow connections to localhost:9222

**Solution 3:** Try a different port (avoid common ports like 8080, 3000)

### "Browser already in use"

Only one process can connect to the CDP endpoint at a time. Make sure no other automation tools are connected.

### "Session expired"

If Duolingo logs you out, simply log back in manually in the Chrome window and run the script again.

## Advanced Usage

### With Advanced Examples

```bash
# Start Chrome with debugging
./start_chrome_debug.sh

# In another terminal, run advanced example
# Choose option 5 (Use existing browser session)
python advanced_example.py
```

### Programmatic Usage

```python
from duolingo_copilot import DuolingoCopilot
import asyncio

async def main():
    # Connect to existing browser
    copilot = DuolingoCopilot(cdp_url='http://localhost:9222')
    
    # Run without login
    await copilot.run_full_session(skip_login=True)

asyncio.run(main())
```

## Best Practices

1. **Keep Chrome Visible**: Don't minimize the browser window - some interactions may fail if elements aren't visible
2. **Use Dedicated Profile**: Create a separate Chrome profile just for automation
3. **Monitor Sessions**: Watch the browser to catch any issues early
4. **Handle Interruptions**: If Duolingo shows popups or notifications, close them manually
5. **Regular Restarts**: Restart Chrome periodically to avoid memory leaks

## Security Notes

- Remote debugging allows full access to the browser - only use on trusted networks
- Don't expose the debugging port to the internet
- Use localhost (127.0.0.1) only, not 0.0.0.0
- Close Chrome when done to stop the debugging server
