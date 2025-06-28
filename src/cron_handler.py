import random
import string
from datetime import datetime
from pathlib import Path
from fastapi import APIRouter

router = APIRouter()

def write_single_log_entry():
    """Write a single log entry - designed for cron job execution"""
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
        return {"status": "success", "message": log_entry.strip()}
        
    except Exception as e:
        print(f"Error writing log entry: {e}")
        return {"status": "error", "message": str(e)}

@router.post("/cron/write-log")
async def cron_write_log():
    """Endpoint for Vercel cron job to call"""
    return write_single_log_entry()

@router.get("/cron/write-log")
async def manual_write_log():
    """Manual trigger endpoint for testing"""
    return write_single_log_entry() 