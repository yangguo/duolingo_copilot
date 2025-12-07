# Contributing to Duolingo Copilot

Thank you for your interest in contributing to Duolingo Copilot! This document provides guidelines and instructions for contributing.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/duolingo_copilot.git
   cd duolingo_copilot
   ```
3. **Set up the development environment**:
   ```bash
   pip install -r requirements.txt
   cp .env.example .env
   # Add your API keys to .env
   ```
4. **Run the test script** to verify setup:
   ```bash
   python test_setup.py
   ```

## Development Guidelines

### Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and concise

### Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** with clear, focused commits

3. **Test your changes** thoroughly:
   - Verify syntax: `python -m py_compile your_file.py`
   - Test functionality manually
   - Ensure no regressions

4. **Update documentation** if needed:
   - Update README.md for new features
   - Add docstrings to new functions
   - Update examples if applicable

### Commit Messages

Use clear, descriptive commit messages:
- Start with a verb (Add, Fix, Update, Remove, etc.)
- Keep the first line under 72 characters
- Add details in the body if needed

Examples:
```
Add support for multiple language courses

Fix login error when special characters in password

Update README with troubleshooting section
```

## Types of Contributions

### Bug Fixes

If you find a bug:
1. Check if it's already reported in Issues
2. If not, create a new issue with:
   - Description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment (OS, Python version, etc.)
3. Submit a PR with the fix

### New Features

Before working on a new feature:
1. Open an issue to discuss it
2. Wait for maintainer feedback
3. Implement the feature
4. Submit a PR with:
   - Clear description
   - Examples of usage
   - Updated documentation

### Documentation

Documentation improvements are always welcome:
- Fix typos or unclear explanations
- Add examples
- Improve setup instructions
- Add troubleshooting tips

## Pull Request Process

1. **Update your branch** with the latest main:
   ```bash
   git checkout main
   git pull upstream main
   git checkout your-feature-branch
   git merge main
   ```

2. **Push your changes**:
   ```bash
   git push origin your-feature-branch
   ```

3. **Create a Pull Request** on GitHub:
   - Use a clear, descriptive title
   - Describe what changes you made and why
   - Reference any related issues
   - Include screenshots for UI changes (if applicable)

4. **Address review feedback**:
   - Make requested changes
   - Push additional commits
   - Respond to comments

## Testing

Currently, testing is manual due to the nature of browser automation:

1. Test with a real Duolingo account
2. Verify all lesson types work correctly
3. Check error handling
4. Test with and without credentials

Future: We plan to add automated tests using mocked responses.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Provide constructive feedback
- Focus on the code, not the person

## Questions?

If you have questions:
1. Check existing issues and documentation
2. Open a new issue with the `question` label
3. Join the browser-use Discord for community help

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🎉
