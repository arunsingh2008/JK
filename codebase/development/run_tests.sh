


#!/bin/bash

# Configure test environment
export FLASK_ENV=testing

# Run unit tests
python -m unittest discover -s . -p "test_*.py"

# Review test results
if [ $? -eq 0 ]
then
  echo "All tests passed."
else
  echo "Some tests failed."
fi


