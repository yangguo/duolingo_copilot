#!/bin/bash
# Helper script to start Chrome with remote debugging enabled
# This allows the Duolingo Copilot to connect to your existing browser session

PORT=${1:-9222}

echo "🌐 Starting Chrome with remote debugging on port $PORT..."
echo ""
echo "After Chrome starts:"
echo "1. Log in to Duolingo manually"
echo "2. In another terminal, run:"
echo "   python duolingo_copilot.py --cdp-url http://localhost:$PORT --skip-login"
echo ""

# Detect OS and start Chrome accordingly
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    if command -v google-chrome &> /dev/null; then
        google-chrome --remote-debugging-port=$PORT
    elif command -v chromium-browser &> /dev/null; then
        chromium-browser --remote-debugging-port=$PORT
    elif command -v chromium &> /dev/null; then
        chromium --remote-debugging-port=$PORT
    else
        echo "❌ Chrome/Chromium not found. Please install Google Chrome or Chromium."
        exit 1
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    if [ -d "/Applications/Google Chrome.app" ]; then
        /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=$PORT
    else
        echo "❌ Chrome not found at /Applications/Google Chrome.app"
        echo "Please install Google Chrome or run it manually with:"
        echo "  /path/to/Chrome --remote-debugging-port=$PORT"
        exit 1
    fi
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    # Windows (Git Bash, MSYS, Cygwin)
    if [ -f "$PROGRAMFILES/Google/Chrome/Application/chrome.exe" ]; then
        "$PROGRAMFILES/Google/Chrome/Application/chrome.exe" --remote-debugging-port=$PORT
    elif [ -f "$PROGRAMFILES(X86)/Google/Chrome/Application/chrome.exe" ]; then
        "$PROGRAMFILES(X86)/Google/Chrome/Application/chrome.exe" --remote-debugging-port=$PORT
    elif [ -f "$LOCALAPPDATA/Google/Chrome/Application/chrome.exe" ]; then
        "$LOCALAPPDATA/Google/Chrome/Application/chrome.exe" --remote-debugging-port=$PORT
    else
        echo "❌ Chrome not found. Please install Google Chrome or run it manually with:"
        echo "  chrome.exe --remote-debugging-port=$PORT"
        exit 1
    fi
else
    echo "❌ Unsupported operating system: $OSTYPE"
    exit 1
fi
