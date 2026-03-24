# Contributing to Global Startup Explorer

Thank you for your interest in contributing to the **Global Startup Explorer**! 🌍

As an open-source initiative by [Genox Holdings](https://genoxholdings.com), we believe that every founder deserves access to global opportunities. This project relies on community contributions to keep our database of grants, accelerators, and perks up to date.

## How Can I Contribute?

### 1. Adding New Opportunities
Found a great government grant, corporate innovation program, or a startup cloud perk? You can add it directly to our database!

1. Open `data_mock.py` or `startup_crawler_global.py` depending on the scope of the program.
2. If it's a massive global program, add it to the `REAL_SOURCES` dictionary in `data_mock.py` or as a direct crawler target.
3. Use the following format:
   ```python
   ("Program Name", "Short description highlighting funding/perks.", "Category", "Industries", "Funding Amount", "Equity Taken", "Provider Name")
   ```
4. Categories must EXACTLY match one of: `Gov Grants`, `Corporate`, `VCs & Accelerators`, `Perks`, `Relocation/Growth`.

### 2. Fixing Bugs / UI Improvements
1. Fork the repository and create a new branch containing your feature or bug fix.
2. The UI is built with vanilla CSS (`templates/index.html`) to remain lightweight. Avoid adding heavy frontend frameworks without discussing in an issue first.
3. The backend is a lightweight Flask app `app.py`.

### 3. Local Development Setup
1. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/global-startup-dashboard.git
   cd global-startup-dashboard
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application (this will automatically seed SQLite and start the server):
   ```bash
   python app.py
   ```
4. Access at `http://localhost:5000`.

## Pull Request Process
1. Ensure your code conforms to standard Python formatting (PEP 8).
2. Update the `README.md` with details of changes to the interface or new massive endpoints.
3. Submit your PR with a clear title and description using the provided template.

## Need Help?
Contact us at `developer@genox.one` or open an issue string. 
