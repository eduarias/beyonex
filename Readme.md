# QA Technical Task for Beyonnex

## Implementation details
The test cases are implemented using Robot Framework with Selenium. They can
be run using docker or directly by console.

In order to meet the requirements of having a selector of temperature for
moisturizers or sunscreens depending on the current temperature and keep a
ATDD style, what have been done is having two test cases, one for moisturizers and
another one for sunscreens, but one of them will be skipped depending on
the temperature value.

The tests have been implemented using page objects for each web page of the
site and a service file where the keywords for the tests are implemented, that
are in the `resources`folder. The test cases are in `tests`folder on
file `tests.robot`.

## Run the test locally
In practice, it is easiest to install Robot Framework and SeleniumLibrary along 
with its dependencies using pip package manager. Once you have pip installed,
all you need to do is running this command:

`$ pip install -r requirements.txt`

To execute the test:

`$ python -m robot tests/tests.robot`
or
`$ robot tests`

In order to do this you should also need to have chromedriver installed on
the machine. (https://chromedriver.chromium.org/downloads)

## Run the test using Docker
Right now by default, running tests will be successful for macbooks with ARM-based chips (M1 or M2). If you use macbooks with intel chips or use any other hardware, 
please first modify the docker-compose.yml file.

To build the docker image for testing:

`$ docker compose build`

To execute the tests:

`$ docker compose up --abort-on-container-exit`

Note that if you get an error like this: (which is related to docker itself)

`error getting credentials - err: exec: "docker-credential-desktop": executable file not found in $PATH, out: '' `

One solution is that in ~/.docker/config.json change credsStore to credStore.

### Read results
Once tests are executed for the first time and `output` folder should be
created where report and log can be found. 

The report (`output/report.html`) just have information about the test execution results, one 
should be skipped due to the temperature selector and the other one should 
pass or fail.

The log (`output/log.html`) contains a detailed log of each step of the test
with the status of each one and screenshots of the final payment page or
the failing step, and also useful debug information.
