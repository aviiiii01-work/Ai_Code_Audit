#!/bin/bash

LOG_FILE="logs/validation.log"

timestamp() {
  date "+%Y-%m-%d %H:%M:%S"
}

echo "[$(timestamp)] Starting validation..." >> "$LOG_FILE"

# Check if src directory exists
if [ ! -d "src" ]; then
  echo "[$(timestamp)]  Error: src directory not found." >> "$LOG_FILE"
  exit 1
fi

# Check if config.json exists and is valid
if [ ! -f "config.json" ]; then
  echo "[$(timestamp)]  Error: config.json missing." >> "$LOG_FILE"
  exit 1
fi

if ! jq empty config.json 2>/dev/null; then
  echo "[$(timestamp)]  Error: Invalid JSON in config.json" >> "$LOG_FILE"
  exit 1
fi

echo "[$(timestamp)]  Validation passed." >> "$LOG_FILE"
exit 0
