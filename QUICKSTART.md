# Quick Start Guide

## 5-Minute Setup

### 1. Prerequisites
- Python 3.11+ installed
- A Duolingo account

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/yangguo/duolingo_copilot.git
cd duolingo_copilot

# Install dependencies
pip install -r requirements.txt

# Install Chromium browser
python -m playwright install chromium
```

### 3. Configuration

```bash
# Create your .env file
cp .env.example .env

# Edit .env and add your Browser Use API key
# Get it from: https://cloud.browser-use.com/new-api-key
```

Your `.env` should look like:
```bash
BROWSER_USE_API_KEY=bu_live_xxxxxxxxxxxxx
DUOLINGO_USERNAME=your-email@example.com  # Optional
DUOLINGO_PASSWORD=your-password            # Optional
```

### 4. Test Your Setup

```bash
python test_setup.py
```

You should see all tests pass except environment (if you haven't added your API key yet).

### 5. Run Your First Lesson

```bash
python duolingo_copilot.py
```

That's it! The bot will:
1. Open a browser
2. Log in to Duolingo (if credentials provided)
3. Navigate to Japanese course
4. Complete a lesson automatically

## Common Commands

```bash
# Basic usage - complete one lesson
python duolingo_copilot.py

# Use existing Chrome browser (already logged in)
# First, start Chrome with remote debugging:
./start_chrome_debug.sh   # Linux/macOS
# or
start_chrome_debug.bat    # Windows

# Then in another terminal:
python duolingo_copilot.py --cdp-url http://localhost:9222 --skip-login

# Use persistent browser profile (maintains login)
python duolingo_copilot.py --user-data-dir /path/to/chrome/profile

# Run advanced examples
python advanced_example.py

# Test installation
python test_setup.py
```

## What Happens When You Run It?

1. **Browser Opens**: You'll see a Chrome browser window open
2. **Navigation**: The bot navigates to Duolingo
3. **Login** (optional): Automatically logs in if credentials are provided
4. **Lesson Start**: Finds and starts a Japanese lesson
5. **AI Answers**: Uses AI to answer each question
6. **Completion**: Finishes the lesson and shows results

## Troubleshooting

### "Either OPENAI_API_KEY or BROWSER_USE_API_KEY must be set"
→ Create a `.env` file and add your API key from https://cloud.browser-use.com/new-api-key
  Or add your OpenAI API key

### "No module named 'browser_use'"
→ Run `pip install -r requirements.txt`

### Browser doesn't open
→ Run `python -m playwright install chromium`

### Login fails
→ Try manual login (leave credentials out of `.env`)

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Try [advanced_example.py](advanced_example.py) for more features
- Customize the task prompts for your needs
- Check [CONTRIBUTING.md](CONTRIBUTING.md) to contribute

## Getting Help

- Check the [browser-use documentation](https://docs.browser-use.com)
- Join the [browser-use Discord](https://link.browser-use.com/discord)
- Open an issue on GitHub

Happy learning! 🎉
