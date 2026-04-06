#!/bin/bash

# Configuration: Required variables from .env
REQUIRED_VARS=(
    "LOG_LEVEL"
    "RASA_URL"
    "RASA_TOKEN"
    # "ACTION_SERVER_URL"
    "MONGO_URL"
    "MONGO_DB"
    "MONGO_USERNAME"
    "MONGO_PASSWORD"
    "MONGO_AUTH_SOURCE"
    "MONGO_COLLECTION"
)

# Load local .env if it exists (for host-side validation)
[ -f .env ] && export $(grep -v '^#' .env | xargs)

# Check each required variable in the current environment
MISSING=0
for var in "${REQUIRED_VARS[@]}"; do
    if [ -z "${!var}" ]; then
        echo "[ERROR] MISSING: $var is not set in the environment."
        MISSING=$((MISSING + 1))
    fi
done

if [ $MISSING -gt 0 ]; then
    echo "[WARNING] Validation failed with $MISSING missing variable(s)."
    exit 1
else
    echo "[SUCCESS] All required environment variables are verified."
fi
