# Auto1_automation_framework
Automation tests written in Python 3.7 with the use of Behave library for Gherkin scripts

To run the tests, you need to have Python 3.7 and chromedriver installed on your machine. Both need to have their paths added 
to the PATH system variables. 

After this:

The tests suite runs best on PyCharm IDE Professional version(that version is the only one that provides
plugins for BDD scenarios and Behave configurations used in this suite).

Once you have that installed, move to the root level of the project directory and run the "pip install -r requirements.txt" command from
PyCharm command line. This will install all the dependecies necessary to run the test.

Once this is done, go to the settings page and select a Python interpreter that will allow you to run the test suite.

Next, go to configurations dropdown(top right area of the UI) and create a new Behave configuration for the test suite.
In the configuration panel, set the "Features files or folders" input to the integration_tests/features directory in the project.
Next select your project interpreter and set the "Working directory" input to the top level of the project folder.

Then run the tests.
