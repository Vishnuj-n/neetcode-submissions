# NeetCode Scheduler with GitHub Integration

## Overview
The scheduler automatically fetches latest submissions from GitHub, validates solutions, and generates Anki flashcards.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Ensure Git repository is properly configured:**
   - Git must be installed on your system
   - The scheduler expects a remote named `origin`
   - Default branch is assumed to be `main` (adjust in `scheduler.py` if needed)

## Usage

### Scheduling Options

```bash
# Run once immediately
python scheduler.py once

# Daily schedule (9:00 AM)
python scheduler.py daily

# Weekly schedule (Sunday 10:00 AM)
python scheduler.py weekly

# Custom interval (every N hours)
python scheduler.py every_6  # Every 6 hours
python scheduler.py every_12 # Every 12 hours
```

### What It Does

1. **GitHub Sync:** Uses `git pull` to fetch latest changes from your NeetCode repository
2. **Solution Validation:** Runs syntax and structure checks on all submissions
3. **Card Generation:** Creates Anki flashcards from your solutions
4. **Logging:** All activities are logged to `scheduler.log`

### Workflow

For each scheduled run:
1. Fetch latest changes from GitHub
2. If new submissions are found, pull them locally
3. Validate all solutions (syntax, structure, instantiation)
4. Generate Anki cards from validated solutions
5. Log all activities and results

### Logs

Check `scheduler.log` for detailed information:
- GitHub sync status
- Validation results
- Card generation progress
- Any errors or warnings

### Branch Configuration

If your repository uses a different default branch (e.g., `master`), update line 64 in `scheduler.py`:

```python
# Change this line:
["git", "pull", "origin", "main"]

# To:
["git", "pull", "origin", "master"]
```

### Error Handling

- If GitHub sync fails, scheduler continues with local files
- Individual script failures don't stop the entire process
- All errors are logged with timestamps
- Timeouts prevent hanging processes (5-minute limit per script)

### Customization

You can modify the schedule times in the `setup_*_schedule()` methods:
- Daily: Change `"09:00"` to your preferred time
- Weekly: Change Sunday time or day
- Custom: Adjust the interval hours as needed
