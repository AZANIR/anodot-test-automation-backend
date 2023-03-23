# Automation Framework with Playwright and pytest

## Manual steps:
### 1. Install environment:

```bash
run: |
  python -m pip install --upgrade pip
  pip install -r requirements.txt
```

### 2. Run all playwright tests:
reopen terminal and run:
```bash
pytest
```

### 3. To run tests with HTML report:
```bash
pytest tests/ --html-report=./report --title='PYTEST REPORT'
```

# Test Plan 

To design and implement a test plan for the PyTemp package, we can use the pytest library in Python.

Here's a sample test plan to cover the basic functionality of the package:

Test the basic functionality of the temperature conversion functions for Fahrenheit to Celsius and vice versa.

- *Test if the conversion from Fahrenheit to Celsius is accurate
Test if the conversion from Celsius to Fahrenheit is accurate
Test the functionality of the temperature conversion functions for Kelvin to Celsius and vice versa.*

- *Test if the conversion from Kelvin to Celsius is accurate
Test if the conversion from Celsius to Kelvin is accurate
Test the functionality of the temperature conversion functions for Kelvin to Fahrenheit and vice versa.*

- *Test if the conversion from Kelvin to Fahrenheit is accurate
Test if the conversion from Fahrenheit to Kelvin is accurate
Test the functionality of the temperature averaging functions for lists of temperatures.*


## Testing edge cases and error handling

For example, testing if the package can handle extremely high or low temperatures, or if it can handle invalid input values.
Testing the performance of the package

For example, testing how quickly the package can convert large lists of temperatures or handle a high volume of requests.
Testing the package with different Python versions and environments

For example, testing the package with different versions of Python or different operating systems to ensure compatibility.
In the future, tests should be added to cover these areas as well to ensure the reliability and robustness of the package.

