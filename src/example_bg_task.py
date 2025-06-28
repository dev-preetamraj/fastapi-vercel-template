import random
import asyncio
import string
from datetime import datetime
from pathlib import Path

# Global variable to control the background task
background_task_running = False

async def write_random_log():
    """Background task that writes random content to log.txt every 5 minutes"""
    global background_task_running
    background_task_running = True
    
    # Create log file path
    log_file = Path("log.txt")
    
    # Sample content for random generation
    sample_messages = [
        "System check completed successfully",
        "Database connection established",
        "Cache refreshed",
        "User authentication processed",
        "API request handled",
        "Background job executed",
        "Memory usage optimized",
        "Network connection stable",
        "Security scan completed",
        "Performance metrics recorded"
    ]
    
    while background_task_running:
        try:
            # Generate random content
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = random.choice(sample_messages)
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
            random_number = random.randint(1000, 9999)
            
            log_entry = f"[{timestamp}] {message} - ID: {random_string} - Value: {random_number}\n"
            
            # Write to log file
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)
            
            print(f"Log entry written: {log_entry.strip()}")
            
            # Wait for 5 minutes (300 seconds)
            await asyncio.sleep(30)
            
        except Exception as e:
            print(f"Error in background task: {e}")
            await asyncio.sleep(60)  # Wait 1 minute before retrying