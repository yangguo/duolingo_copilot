# Duolingo Copilot 🤖

An AI-powered bot that uses browser automation to complete Duolingo Japanese learning tests automatically. Built with [browser-use](https://github.com/browser-use/browser-use) for intelligent browser control.

> **Quick Start**: See [QUICKSTART.md](QUICKSTART.md) for a 5-minute setup guide!

## Features

- 🧠 **AI-Powered**: Uses advanced language models to understand and answer Japanese learning questions
- 🌐 **Browser Automation**: Leverages browser-use library for reliable browser control
- 🎯 **Japanese Learning**: Specifically designed for Japanese language lessons on Duolingo
- 📚 **Multiple Question Types**: Handles multiple choice, translation, listening, and matching questions
- 🔐 **Secure**: Credentials stored in environment variables

## Prerequisites

- Python 3.11 or higher
- A Duolingo account
- One of the following:
  - Browser Use API key (get free $10 credits at [Browser Use Cloud](https://cloud.browser-use.com/new-api-key))
  - OpenAI API key or any OpenAI-compatible API endpoint

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yangguo/duolingo_copilot.git
   cd duolingo_copilot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Chromium browser** (required by browser-use):
   ```bash
   python -m playwright install chromium
   ```

4. **Configure environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your credentials:
   
   **Option 1: Browser Use Cloud (Recommended)**
   - `BROWSER_USE_API_KEY`: Get from [Browser Use Cloud](https://cloud.browser-use.com/new-api-key)
   
   **Option 2: OpenAI or OpenAI-compatible API**
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `OPENAI_BASE_URL`: (Optional) Custom base URL for OpenAI-compatible APIs (e.g., `https://api.openai.com/v1`)
   - `OPENAI_MODEL`: (Optional) Model name to use (default: `gpt-4`)
   
   **Duolingo Credentials (Optional)**
   - `DUOLINGO_USERNAME`: Your Duolingo email/username (optional)
   - `DUOLINGO_PASSWORD`: Your Duolingo password (optional)
   
   **Browser Configuration (Optional)**
   - `CHROME_CDP_URL`: Connect to existing Chrome browser with remote debugging
   - `CHROME_USER_DATA_DIR`: Use persistent Chrome profile to maintain login sessions

## Usage

### Basic Usage

Run the copilot to complete a Japanese lesson:

```bash
python duolingo_copilot.py
```

The bot will:
1. Log in to Duolingo (if credentials are provided)
2. Navigate to the Japanese course
3. Start and complete a lesson using AI
4. Answer all questions until the lesson is complete

### Using Existing Browser Session

If you already have Chrome open with Duolingo logged in, you can connect to it instead of launching a new browser:

**Method 1: Remote Debugging (Recommended)**

Use the provided helper script to start Chrome with remote debugging:

```bash
# Linux/macOS
./start_chrome_debug.sh

# Windows
start_chrome_debug.bat
```

Or start Chrome manually:
```bash
# Windows
chrome.exe --remote-debugging-port=9222

# macOS
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

# Linux
google-chrome --remote-debugging-port=9222
```

Then:
1. Log in to Duolingo manually in the browser
2. In another terminal, run:
   ```bash
   python duolingo_copilot.py --cdp-url http://localhost:9222 --skip-login
   ```
   
   Or set in `.env`:
   ```bash
   CHROME_CDP_URL=http://localhost:9222
   ```

**Method 2: Persistent Browser Profile**

Use a Chrome user data directory to maintain login sessions:

```bash
python duolingo_copilot.py --user-data-dir /path/to/chrome/profile
```

Or set in `.env`:
```bash
CHROME_USER_DATA_DIR=/path/to/chrome/profile
```

### Manual Login

If you prefer not to store your credentials, you can skip the automatic login:
1. Don't set `DUOLINGO_USERNAME` and `DUOLINGO_PASSWORD` in `.env`
2. Run the script
3. Manually log in to Duolingo when the browser opens
4. The bot will wait 30 seconds before proceeding with the lesson

### Command Line Options

```bash
python duolingo_copilot.py --help
```

Options:
- `--cdp-url URL`: Chrome DevTools Protocol URL (e.g., `http://localhost:9222`)
- `--user-data-dir PATH`: Chrome user data directory path
- `--skip-login`: Skip login step (use with existing session)

### Advanced Usage

You can modify `duolingo_copilot.py` to:
- Complete multiple lessons in sequence
- Practice specific skills
- Run on a schedule using cron/task scheduler
- Customize the AI's behavior

See `advanced_example.py` for more examples.

## Testing

Run the comprehensive test suite to verify everything works:

```bash
python test_copilot.py
```

This will run unit tests, integration checks, and identify any issues. See [TESTING.md](TESTING.md) for detailed testing documentation.

For a quick installation check:

```bash
python test_setup.py
```

## How It Works

The Duolingo Copilot uses the browser-use library, which combines:
- **Playwright**: For browser automation
- **AI Vision**: To understand the page content
- **Language Models**: To intelligently answer questions

The AI agent:
1. Navigates the Duolingo interface
2. Reads and understands each question
3. Uses Japanese language knowledge to select correct answers
4. Continues until the lesson is complete

## Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `BROWSER_USE_API_KEY` | No* | API key from Browser Use Cloud |
| `OPENAI_API_KEY` | No* | OpenAI API key or compatible API key |
| `OPENAI_BASE_URL` | No | Custom base URL for OpenAI-compatible APIs |
| `OPENAI_MODEL` | No | Model name (default: gpt-4) |
| `CHROME_CDP_URL` | No | Chrome DevTools Protocol URL for existing browser |
| `CHROME_USER_DATA_DIR` | No | Path to Chrome user data directory |
| `DUOLINGO_USERNAME` | No | Your Duolingo email/username |
| `DUOLINGO_PASSWORD` | No | Your Duolingo password |

*Either `BROWSER_USE_API_KEY` or `OPENAI_API_KEY` must be set.

### LLM Configuration

**Browser Use Cloud** (Default option)

This project uses Browser Use Cloud's LLM service by default, which is optimized for browser automation tasks. New signups get $10 in free credits.

**OpenAI or OpenAI-compatible APIs**

You can also use OpenAI or any OpenAI-compatible API (such as Azure OpenAI, local LLMs, or other providers):

```bash
# .env file example for OpenAI
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4

# .env file example for Azure OpenAI
OPENAI_API_KEY=your-azure-key
OPENAI_BASE_URL=https://your-resource.openai.azure.com/openai/deployments/your-deployment
OPENAI_MODEL=gpt-4

# .env file example for local LLM (like LM Studio)
OPENAI_API_KEY=lm-studio
OPENAI_BASE_URL=http://localhost:1234/v1
OPENAI_MODEL=local-model
```

## Troubleshooting

### "Either OPENAI_API_KEY or BROWSER_USE_API_KEY must be set"
- Make sure you've created a `.env` file from `.env.example`
- Add either your Browser Use API key from https://cloud.browser-use.com/new-api-key
- Or add your OpenAI API key (or compatible API credentials)

### Browser doesn't open
- Install Chromium: `python -m playwright install chromium`
- Check that Playwright is properly installed

### Login fails
- Verify your Duolingo credentials are correct
- Try manual login instead (leave credentials empty)
- Check if Duolingo requires additional verification

### Questions answered incorrectly
- The AI does its best but isn't perfect
- It learns from Duolingo's corrections
- You may need to review and redo some lessons

## Limitations

- The AI may not answer every question correctly
- Some question types (like speaking) may be challenging
- Duolingo's UI changes may require updates to the task prompts
- Rate limiting may apply based on your API usage

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This tool is for educational purposes. Please use responsibly and in accordance with Duolingo's Terms of Service. The goal is to assist with learning, not to cheat or bypass the learning process.

## License

MIT License - See LICENSE file for details

## Acknowledgments

- [browser-use](https://github.com/browser-use/browser-use) - For the amazing browser automation library
- [Duolingo](https://www.duolingo.com) - For making language learning accessible
- The open-source community

## Support

If you encounter any issues or have questions:
1. Check the [browser-use documentation](https://docs.browser-use.com)
2. Open an issue on GitHub
3. Join the [browser-use Discord](https://link.browser-use.com/discord) for community support