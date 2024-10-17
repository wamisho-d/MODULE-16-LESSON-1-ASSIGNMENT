# Task 1: Create a new feature branch named feature/tests.
git checkout -b feature/tests

# Task 2: Implement a new test in **app_test.py** to validate negative sum.

# app_test.py
import pytest

def sum(numbers):
    return sum(numbers)

def test_negative_sum():
    result = sum([-5, -10])
    assert result == -15, "The sum of -5 and -10 should be -15"

# Add more tests as necessary

# Task 4: Configure a CI/CD pipeline to build and test the feature/tests branch.
git add app_test.py .github/workflows/main.yml
git commit -m "Added negative sum test and updated pipeline for feature/tests branch"
git push origin feature/tests

# Task 5: Monitor the CI/CD pipeline to ensure that the build and tests pass successfully.
# Go to the "Actions" tab of your GitHub repository
# Check the progress of the pipeline for the feature/tests branch. Ensure all tests pass sucessfully
