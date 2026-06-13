# Contributing to Awesome Startup Global Explorer

First off, thank you for considering contributing to Awesome Startup Global Explorer! It's people like you that make this global ecosystem possible. Whether you are adding a regional micro-VC, fixing a translation, or improving the crawler, your help is incredibly valuable.

## 🌟 Help Wanted! (Good First Issues)

We are actively looking for contributions in the following areas:
- **Adding Local Grants & VCs:** If your country is missing specific grants or accelerators, please add them to `data_vcs_massive.py`!
- **Translations:** Improving the Arabic, Spanish, or Chinese translations in our `messages.po` files.
- **Frontend Optimization:** Enhancing the glassmorphism UI or optimizing data tables for mobile.

## How Can I Contribute?

### Reporting Bugs
- Use the GitHub Issues tracker.
- Describe the bug clearly. Provide steps to reproduce it.
- Include OS, browser, and Python versions.

### Suggesting Enhancements
- Open an Issue with the `enhancement` label.
- Clearly describe the feature and how it benefits global founders.

### Pull Requests
1. Fork the repo and create your branch from `main`.
2. If you've added new VCs or Grants, ensure they follow the tuple structure in the crawler.
3. Ensure the test suite passes (`pytest test_frontend.py`).
4. Update the README or documentation if your change alters behavior.
5. Submit your PR! We usually review within 24 hours.

## Coding Standards
- We follow standard Python PEP 8 guidelines.
- Frontend modifications must adhere to the Genox "Serious Dark" UI/UX standard (No emojis on primary UI elements, `#050505` background).
- All new dependencies must be approved by maintainers to prevent bloat.

## Translation
We use `Flask-Babel` for i18n. If you want to add or fix a translation, please submit a PR modifying the `.po` files in the `translations/` directory.

## Spread the Word
If you can't code right now, you can still contribute immensely by **giving the repo a Star ⭐** and sharing it with other founders, Hacker News, or on Twitter!
