#!/usr/bin/env python3
"""
Scheduler for running NeetCode automation tasks.
Supports daily, weekly, or custom scheduling intervals.
"""

import schedule
import time
import subprocess
import sys
import logging
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scheduler.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class NeetCodeScheduler:
    def __init__(self):
        self.script_dir = Path(__file__).parent
        
    def run_script(self, script_name: str) -> bool:
        """Run a Python script and return success status."""
        try:
            script_path = self.script_dir / script_name
            logger.info(f"Running {script_name}...")
            
            result = subprocess.run(
                [sys.executable, str(script_path)],
                cwd=self.script_dir,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            
            if result.returncode == 0:
                logger.info(f"{script_name} completed successfully")
                if result.stdout:
                    logger.info(f"Output: {result.stdout.strip()}")
                return True
            else:
                logger.error(f"{script_name} failed with code {result.returncode}")
                if result.stderr:
                    logger.error(f"Error: {result.stderr.strip()}")
                return False
                
        except subprocess.TimeoutExpired:
            logger.error(f"{script_name} timed out after 5 minutes")
            return False
        except Exception as e:
            logger.error(f"Failed to run {script_name}: {e}")
            return False
    
    def generate_cards(self):
        """Generate Anki cards from solutions."""
        success = self.run_script("generate.py")
        if success:
            logger.info("Cards generated successfully")
            # Optionally push to Anki immediately
            # self.run_script("push_to_anki.py")
        else:
            logger.error("Card generation failed")
    
    def validate_solutions(self):
        """Run solution validation."""
        success = self.run_script("test_solutions.py")
        if success:
            logger.info("Solution validation passed")
        else:
            logger.warning("Solution validation found issues")
    
    def setup_daily_schedule(self):
        """Run tasks daily at 9 AM."""
        logger.info("Setting up daily schedule (9:00 AM)")
        schedule.every().day.at("09:00").do(self.generate_cards)
        schedule.every().day.at("09:30").do(self.validate_solutions)
    
    def setup_weekly_schedule(self):
        """Run tasks weekly on Sunday at 10 AM."""
        logger.info("Setting up weekly schedule (Sunday 10:00 AM)")
        schedule.every().sunday.at("10:00").do(self.generate_cards)
        schedule.every().sunday.at("10:30").do(self.validate_solutions)
    
    def setup_custom_schedule(self, interval_hours: int = 6):
        """Run tasks every N hours."""
        logger.info(f"Setting up custom schedule (every {interval_hours} hours)")
        schedule.every(interval_hours).hours.do(self.generate_cards)
        schedule.every(interval_hours).hours.do(self.validate_solutions)
    
    def run_once(self):
        """Run all tasks once immediately."""
        logger.info("Running all tasks once")
        self.generate_cards()
        self.validate_solutions()
    
    def start_scheduler(self, schedule_type: str = "daily"):
        """Start the scheduler with specified schedule type."""
        logger.info(f"Starting NeetCode scheduler with {schedule_type} schedule")
        
        if schedule_type == "daily":
            self.setup_daily_schedule()
        elif schedule_type == "weekly":
            self.setup_weekly_schedule()
        elif schedule_type.startswith("every_"):
            try:
                hours = int(schedule_type.split("_")[1])
                self.setup_custom_schedule(hours)
            except (IndexError, ValueError):
                logger.error("Invalid custom schedule format. Use: every_N where N is hours")
                return
        else:
            logger.error(f"Unknown schedule type: {schedule_type}")
            return
        
        logger.info("Scheduler started. Press Ctrl+C to stop.")
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            logger.info("Scheduler stopped by user")

def main():
    if len(sys.argv) < 2:
        print("Usage: python scheduler.py [daily|weekly|every_N|once]")
        print("Examples:")
        print("  python scheduler.py daily    # Run daily at 9 AM")
        print("  python scheduler.py weekly   # Run weekly on Sunday at 10 AM")
        print("  python scheduler.py every_6  # Run every 6 hours")
        print("  python scheduler.py once     # Run all tasks once immediately")
        sys.exit(1)
    
    schedule_type = sys.argv[1]
    scheduler = NeetCodeScheduler()
    
    if schedule_type == "once":
        scheduler.run_once()
    else:
        scheduler.start_scheduler(schedule_type)

if __name__ == "__main__":
    main()
