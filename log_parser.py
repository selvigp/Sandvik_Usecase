import aiofiles
from config import LOG_PATTERN, USER_PATTERN, API_ERROR_PATTERN, DATA

async def process_log_line(line):
    """Parses a single line from a log file and updates global data."""
    match = LOG_PATTERN.match(line)
    if match:
        timestamp, server, level, message = match.groups()
        DATA["log_counts"][level] += 1

        user_match = USER_PATTERN.search(message)
        if user_match:
            user = user_match.group(1)
            if user not in DATA["user_activity"]:
                DATA["user_activity"][user] = {"last_seen": timestamp, "actions": 0}
            DATA["user_activity"][user]["last_seen"] = timestamp
            DATA["user_activity"][user]["actions"] += 1

        if API_ERROR_PATTERN.search(message):
            DATA["api_errors"]["failed_requests"] += 1

async def process_log_file(file_path):
    """Reads and processes an entire log file asynchronously."""
    async with aiofiles.open(file_path, mode='r') as f:
        async for line in f:
            await process_log_line(line)
