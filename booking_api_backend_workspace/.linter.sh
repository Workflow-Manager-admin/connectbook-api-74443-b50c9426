#!/bin/bash
cd /home/kavia/workspace/code-generation/connectbook-api-74443-b50c9426/booking_api_backend_workspace/booking_api_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

