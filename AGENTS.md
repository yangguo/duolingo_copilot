# Repository Guidelines

## Project Structure & Module Organization
- Core agent logic lives in `duolingo_copilot.py`; `advanced_example.py` shows extended flows and parameters.
- Tests: `test_copilot.py` (comprehensive) and `test_setup.py` (installation check); keep new tests alongside these unless a new module warrants its own file.
- Scripts: `start_chrome_debug.sh` / `.bat` start Chrome with remote debugging; docs in `README.md`, `QUICKSTART.md`, and `TESTING.md` hold usage details.
- Environment: `.env.example` lists required keys; never commit your filled `.env`.

## Build, Test, and Development Commands
- Install deps: `pip install -r requirements.txt`; install browser runtime once: `python -m playwright install chromium`.
- Run the copilot: `python duolingo_copilot.py [--cdp-url URL | --user-data-dir PATH | --skip-login]`.
- Installation smoke test: `python test_setup.py`.
- Full suite (unit + async + integration checks): `python test_copilot.py`.
- Quick syntax check: `python -m py_compile duolingo_copilot.py advanced_example.py`.

## Coding Style & Naming Conventions
- Follow PEP 8 with 4-space indentation; keep functions/classes documented with concise docstrings (match existing style in `duolingo_copilot.py`).
- Naming: classes in `PascalCase`, functions/variables in `snake_case`, flags in `--kebab-case`, environment variables UPPER_SNAKE.
- Keep console output purposeful and emoji-light; prefer clear status messages over verbose logging.

## Testing Guidelines
- Use `unittest` and `unittest.IsolatedAsyncioTestCase` patterns already in `test_copilot.py`; name test methods `test_*` with descriptive intent.
- Cover configuration handling (env vars, wait times), async flows (login, lesson, practice), and error paths when adding features.
- Run `python test_copilot.py` before submitting; note manual checks (e.g., real browser runs) in your PR if applicable.

## Commit & Pull Request Guidelines
- Commit messages: short, imperative, and under ~72 chars (e.g., `Add configurable login wait`, `Fix test setup check`).
- PRs should describe the change, list test commands run, and reference related issues. Include screenshots only when UI/browser output is relevant.
- Update docs (`README.md`, `QUICKSTART.md`, `TESTING.md`) when behavior or setup steps change; keep examples runnable.

## Security & Configuration Tips
- Store secrets only in `.env`; avoid echoing credentials in prints, logs, or recorded sessions.
- When using remote debugging (`--cdp-url`) or user data dirs, ensure the target Chrome profile is trusted and closed after runs to prevent credential leakage.
