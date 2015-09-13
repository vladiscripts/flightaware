# flightaware - Python RESTful API for FlightAware.com

This is a python based wrapper which simplifies communication with the FlightAware.com RESTful APIs.  Documentation for the APIs can be found at:  http://flightaware.com/commercial/flightxml/explorer

In order to use these APIs, you'll need to be a commercial subscriber to the FlightAware.com service, have a user name, and an API key.

Special thanks to fredpalmer and queenvictoria for getting this project kicked off.

## FlightAware.com API access
In order to use the flightaware module, you'll need to have FlightAware username and api_key.  You can get these from http://flightaware.com/commercial/flightxml.  Note, that you'll need to sign up for the service.  There is a free tier of service, but not all of the APIs are supported and the unit tests, described below, may fail.

## Installation
This is only available via source at the moment.  Clone this repository, and install the flightaware software on your system using the following command.
```
git clone https://github.com/icedawn/flightaware
cd flightaware
python setup.py install
```
This will install the flightaware module on your system.

## Unit testing
In order to unit test the flightaware module, you will need to create a file called ```developer.cfg``` in the ```tests``` directory within the ```flightaware``` source tree.

```
cd tests
cat > developer.cfg << EOF
[test settings]
username = your-flightaware-username
api_key = your-flightaware-api-key
EOF
```
And then to actually run the unit tests, you'll issue the standard python unit test command:
```
python -m unittest flightaware_tests
```
### Unit testing notes
FlightAware.com is a live service, with historical records.  It is possible that some of the unit tests will fail because some of the hardcoded inputs are no longer valid.  The unit tests could use some work to find current flights to base subsequent unit test API calls on, instead of relying on hardcoded values.

Here's an example unit test run that shows a failure because an inbound flight has arrived and is no longer available for that API.  This also shows a bug in  the FlightAware.com service itself (reported 9/12/2015) where certain API calls will fail intermittently.
```
$ python -m unittest flightaware_tests
Using username => icedawn
Using api_key => xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
...................F.............F.......
======================================================================
FAIL: test_inbound_flight_info (flightaware_tests.TestSequenceFunctions)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "flightaware_tests.py", line 158, in test_inbound_flight_info
    self.assertNotIn("error", results)
AssertionError: 'error' unexpectedly found in {u'error': u'Inbound flight is not known'}

======================================================================
FAIL: test_search_birdseye_positions (flightaware_tests.TestSequenceFunctions)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "flightaware_tests.py", line 285, in test_search_birdseye_positions
    self.assertNotIn("error", results)
AssertionError: 'error' unexpectedly found in {'text': u'Operation failed: list element in braces followed by "}" instead of space\n', 'error': 'internal server error'}

----------------------------------------------------------------------
Ran 41 tests in 38.163s

FAILED (failures=2)
```
The unit tests should handle the first case, but the second case is reported correctly -- the test case failed because the FlightAware.com service call failed unexpectedly.
