# Distributed Log Processing System

This is the step-by-step instructions to setup, run and test the scripts from scratch.

## Python Scripts

- `main.py` - This script will read logs from `server_logs` folder, extract key data and stored the results in processed_logs.json
- `config.py` - This script stores global configurations, regex patterns for log parsing and data structures used in processing.
- `api.py` - This is a FastAPI-based server scripts that provides an endpoint (/logs) to fetch processed log data via Web browser.
- `log_aggregator.py` - This script processes the multiple log files asynchronously, calculates error rates, and saves the processed data. 
- `log_parser.py` - This script used to read and parse individual log lines, extracting useful details like timestamps, log levels, user actions, and API errors.

## Prerequisites
- Installed Python v3.7(or later)
- Install pip 
- Required dependencies :- fastapi, aiofiles, uvicorn (ref requirements.txt) 
    
## Installation
- Clone the repository url

    - git clone <https://github_repo_url>
    - pip install -r requirements.txt
- Make sure that `server_logs` folder contains logs file for processing.

## Run Log Processing
To process logs and generate `processed_logs.json`, run below command.
```
python3 main.py
```
## Run API Server
To start the API server, run below command
```
uvicorn api:app --host 0.0.0.0 --port 8000 --reload
```
## Test the API Server via WebBrowser
```
http://localhost:8000/logs
```
