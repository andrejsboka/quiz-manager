# Installation Guide

## For Windows Users (Recommended Method)

### Step 1: Install Python

1. Go to https://www.python.org/downloads/
2. Download the latest Python 3.x version
3. **Run the installer**
4. ⚠️ **CRITICAL**: Check the box "Add Python to PATH"
5. Click "Install Now"
6. Wait for installation to complete

### Step 2: Verify Python Installation

1. Press `Win + R`
2. Type `cmd` and press Enter
3. Type: `python --version`
4. You should see something like: `Python 3.11.0`

### Step 3: Download Quiz Manager

**Option A: Download ZIP (Easiest)**
1. Click the green "Code" button at the top of this page
2. Click "Download ZIP"
3. Extract the ZIP to a folder (e.g., `C:\Users\YourName\Documents\quiz-manager`)

**Option B: Git Clone**
```bash
git clone https://github.com/andrejsboka/quiz-manager.git
```

### Step 4: Run the Application

1. Navigate to the extracted folder
2. **Double-click `quiz_app.pyw`**
3. The Quiz Manager window will open!

**Troubleshooting:**
- If nothing happens, right-click → "Open with" → Select Python
- If a black window appears, make sure the file is `.pyw` not `.py`

### Step 5: (Optional) Create Desktop Shortcut

1. Right-click `quiz_app.pyw`
2. Select "Send to" → "Desktop (create shortcut)"
3. Now you can launch from your Desktop!

## For macOS Users

### Step 1: Install Python

Python is usually pre-installed on macOS. Check version:
```bash
python3 --version
```

If not installed or outdated, install via Homebrew:
```bash
brew install python3
```

### Step 2: Download Quiz Manager
```bash
cd ~/Documents
git clone https://github.com/andrejsboka/quiz-manager.git
cd quiz-manager
```

### Step 3: Run the Application
```bash
python3 quiz_app.pyw
```

Or double-click `quiz_app.pyw` in Finder.

## For Linux Users

### Step 1: Install Python and Tkinter

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install python3 python3-tk
```

**Fedora:**
```bash
sudo dnf install python3 python3-tkinter
```

### Step 2: Download Quiz Manager
```bash
cd ~/Documents
git clone https://github.com/andrejsboka/quiz-manager.git
cd quiz-manager
```

### Step 3: Run the Application
```bash
python3 quiz_app.pyw
```

### Step 4: (Optional) Make it Executable
```bash
chmod +x quiz_app.pyw
./quiz_app.pyw
```

## Common Issues

### Issue: "Python is not recognized"

**Windows:**
- Python not in PATH
- Reinstall Python and check "Add Python to PATH"

### Issue: "No module named tkinter"

**Windows/macOS:**
- Reinstall Python with default options

**Linux:**
```bash
sudo apt-get install python3-tk
```

### Issue: Double-clicking opens text editor

**Windows:**
- Right-click file → "Open with" → Choose Python
- Check "Always use this app"

### Issue: Nothing happens when double-clicking

**Debug mode:**
```bash
# Open terminal/cmd in the folder
python quiz_app.pyw
# This will show any error messages
```

## Next Steps

After installation:
1. Import `sample_questions.json` to get started
2. Add your own questions
3. Take a test!

## Need Help?

- Create an issue on GitHub
- Check existing issues for solutions
- Email: a@boka.lv
```

## 📂 Final Project Structure (Updated)
```
quiz-manager/
│
├── quiz_app.pyw                # Main application (no console window)
├── sample_questions.json       # Example questions (in progress)
├── README.md                   # Main documentation
├── INSTALL.md                  # Detailed installation guide
├── LICENSE                     # (in progress)
