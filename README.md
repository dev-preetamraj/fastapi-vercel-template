# FastAPI Deployment on Vercel

This is a FastAPI application template optimized for deployment on Vercel.

## Background Tasks on Vercel

### The Problem
Vercel serverless functions don't support long-running background tasks because:
- Functions timeout after a few seconds
- Each function invocation is stateless
- No persistent processes are maintained

### The Solution
This template uses **Vercel Cron Jobs** to handle background tasks:

1. **Cron Job Configuration**: The `vercel.json` file includes a cron job that runs every 5 minutes:
   ```json
   "crons": [
     {
       "path": "/api/cron/write-log",
       "schedule": "*/5 * * * *"
     }
   ]
   ```

2. **Cron Endpoint**: The `/api/cron/write-log` endpoint writes a single log entry when triggered.

3. **Manual Testing**: You can manually trigger the log writing by calling:
   - `GET /api/cron/write-log` - Manual trigger
   - `POST /api/cron/write-log` - Cron job trigger

### Local Development
For local development, you can still use the original background task approach in `src/example_bg_task.py`.

### Deployment
1. Deploy to Vercel using `vercel` CLI or GitHub integration
2. The cron job will automatically start running every 5 minutes
3. Check your Vercel dashboard to monitor cron job execution

## API Endpoints

- `GET /` - Health check
- `GET /api/cron/write-log` - Manual log entry trigger
- `POST /api/cron/write-log` - Cron job endpoint (automatically called)

## Files Structure

- `src/main.py` - Main FastAPI application
- `src/cron_handler.py` - Cron job handler for background tasks
- `src/example_bg_task.py` - Original background task (for local development)
- `vercel.json` - Vercel configuration with cron jobs
