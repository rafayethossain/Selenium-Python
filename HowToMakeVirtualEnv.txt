Try Creating Virtual Environment on Windows PowerShell

Step 1: Creating Directory:

$ mkdir python-webui-testing
$ cd python-webui-testing

Step 2: Istalling Pip environment:

$ pip install pipenv

Step 3: Istalling PyTest environment:

$ pipenv install pytest --dev

Step 4: Creating new directory:

$ mkdir tests
$ cd tests


Step 5: Creating new file name test_math.py and paste this code snippet:

def test_addition():
  assert 1 + 1 == 2

Step 6: Run test. Change directory back to the project root, and invoke the pytest module:

$ cd ..
$ pipenv run python -m pytest


Step 7: Verify that ChromeDriver works from the command line:

$ chromedriver

Step 8: install Python’s selenium package into our environment:

$ pipenv install selenium --dev