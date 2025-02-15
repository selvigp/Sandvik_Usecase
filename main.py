import asyncio
from log_aggregator import aggregate_logs

if __name__ == "__main__":
    asyncio.run(aggregate_logs("server_logs"))
