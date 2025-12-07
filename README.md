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
- Browser Use API key (get free $10 credits at [Browser Use Cloud](https://cloud.browser-use.com/new-api-key))

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
   - `BROWSER_USE_API_KEY`: Get from [Browser Use Cloud](https://cloud.browser-use.com/new-api-key)
   - `DUOLINGO_USERNAME`: Your Duolingo email/username (optional)
   - `DUOLINGO_PASSWORD`: Your Duolingo password (optional)

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

### Manual Login

If you prefer not to store your credentials, you can skip the automatic login:
1. Don't set `DUOLINGO_USERNAME` and `DUOLINGO_PASSWORD` in `.env`
2. Run the script
3. Manually log in to Duolingo when the browser opens
4. The bot will wait 30 seconds before proceeding with the lesson

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
| `BROWSER_USE_API_KEY` | Yes | API key from Browser Use Cloud |
| `DUOLINGO_USERNAME` | No | Your Duolingo email/username |
| `DUOLINGO_PASSWORD` | No | Your Duolingo password |

### Browser Use Cloud

This project uses Browser Use Cloud's LLM service, which is optimized for browser automation tasks. New signups get $10 in free credits.

Alternatively, you can use other LLM providers (OpenAI, Anthropic, etc.) by modifying the code to use a different LLM. See [browser-use documentation](https://docs.browser-use.com) for details.

## Troubleshooting

### "BROWSER_USE_API_KEY not found"
- Make sure you've created a `.env` file from `.env.example`
- Add your API key from https://cloud.browser-use.com/new-api-key

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