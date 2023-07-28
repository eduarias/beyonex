# QA Technical Task for Beyonex

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

## Run the test using Docker
To build the docker image for testing:

`$ docker compose build`

To execute the tests:

`$ docker compose up --abort-on-container-exit`

### Read results
Once tests are executed for the first time and `output` folder should be
created where report and log can be found. 

The report (`output/report.html`) just have information about the test execution results, one 
should skipped due to the temperature selector and the other one should 
pass or fail.

The log (`output/log.html`) contains a detailed log of each step of the test
with the status of each one and screenshots of the final payment page or
the failing step, and also useful debug information.