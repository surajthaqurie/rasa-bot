#!/bin/bash
set -e

# 1. Validate Environment
echo "Validating environment variables inside container..."
/app/scripts/validate_env.sh

# 2. Start Rasa
echo "Starting Rasa server..."
# Using exec to ensure signals (SIGTERM) are passed to the Rasa process
exec rasa "$@"
