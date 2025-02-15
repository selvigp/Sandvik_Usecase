import re
from collections import defaultdict

# Regular expressions for log parsing
LOG_PATTERN = re.compile(r"\[(.*?)\] (.*?) (INFO|ERROR|WARN) (.*)")
USER_PATTERN = re.compile(r"User '(.*?)'")
API_ERROR_PATTERN = re.compile(r"API request failed")

# Global data structure
DATA = {
    "log_counts": defaultdict(int),
    "user_activity": {},
    "api_errors": {"total_requests": 100, "failed_requests": 0, "error_rate": "0.0%"},
}
