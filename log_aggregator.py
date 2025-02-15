import os
import asyncio
import aiofiles
import json
from config import DATA
from log_parser import process_log_file

async def aggregate_logs(log_dir):
    """Aggregates logs from all log files in a directory."""
    tasks = [process_log_file(os.path.join(log_dir, file))
             for file in os.listdir(log_dir) if file.endswith(".log")]
    
    await asyncio.gather(*tasks)

    # Compute API error rate
    failed = DATA["api_errors"]["failed_requests"]
    total = DATA["api_errors"]["total_requests"]
    DATA["api_errors"]["error_rate"] = f"{(failed / total) * 100:.2f}%"

    # Store processed logs
    async with aiofiles.open("processed_logs.json", "w") as f:
        await f.write(json.dumps(DATA, indent=2))
