# Changelog

## [Unreleased]

### Added - Existing Browser Support

#### New Features
- **Connect to Existing Browser**: Use Chrome DevTools Protocol (CDP) to connect to already-running Chrome browsers
- **Persistent Browser Profiles**: Use `--user-data-dir` to maintain login sessions across runs
- **Skip Login Option**: `--skip-login` flag to bypass automatic login when using existing sessions
- **Environment Variables**: `CHROME_CDP_URL` and `CHROME_USER_DATA_DIR` for configuration
- **Helper Scripts**: 
  - `start_chrome_debug.sh` for Linux/macOS
  - `start_chrome_debug.bat` for Windows
- **Comprehensive Documentation**: New `USING_EXISTING_BROWSER.md` guide

#### Command Line Options
```bash
python duolingo_copilot.py --cdp-url http://localhost:9222 --skip-login
python duolingo_copilot.py --user-data-dir /path/to/profile
python duolingo_copilot.py --help
```

### Added - OpenAI API Support

#### New Features
- **OpenAI API Integration**: Support for OpenAI and OpenAI-compatible APIs
- **Custom Base URL**: Configure custom endpoints (Azure OpenAI, local LLMs, etc.)
- **Model Selection**: Choose any model via `OPENAI_MODEL` environment variable
- **Environment Variables**:
  - `OPENAI_API_KEY`: Your OpenAI API key
  - `OPENAI_BASE_URL`: Custom base URL (optional)
  - `OPENAI_MODEL`: Model name (default: gpt-4)

#### Examples
```bash
# Standard OpenAI
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4-turbo

# Azure OpenAI
OPENAI_API_KEY=your-azure-key
OPENAI_BASE_URL=https://your-resource.openai.azure.com/openai/deployments/your-deployment
OPENAI_MODEL=gpt-4

# Local LLM (e.g., LM Studio)
OPENAI_API_KEY=lm-studio
OPENAI_BASE_URL=http://localhost:1234/v1
OPENAI_MODEL=local-model
```

### Changed
- **LLM Initialization**: Now supports both Browser Use Cloud and OpenAI-compatible APIs
- **Error Messages**: More informative error messages when API keys are missing
- **Documentation**: Updated README.md, QUICKSTART.md with new features
- **Advanced Examples**: Added example for using existing browser sessions

### Files Modified
- `duolingo_copilot.py`: Added CDP URL and OpenAI API support
- `.env.example`: Added new environment variables
- `README.md`: Updated with OpenAI and existing browser documentation
- `QUICKSTART.md`: Added quick examples for new features
- `advanced_example.py`: Added existing browser example

### Files Added
- `start_chrome_debug.sh`: Helper script for Linux/macOS
- `start_chrome_debug.bat`: Helper script for Windows
- `USING_EXISTING_BROWSER.md`: Comprehensive guide for existing browser usage
- `CHANGELOG.md`: This file

### Benefits
1. **Flexibility**: Use any OpenAI-compatible LLM provider
2. **Cost Control**: Choose models based on cost and performance needs
3. **Session Persistence**: Maintain login state across runs
4. **Easier 2FA**: Handle multi-factor authentication manually once
5. **Development**: Easier debugging with visible browser window
6. **Privacy**: Option to use local LLMs
