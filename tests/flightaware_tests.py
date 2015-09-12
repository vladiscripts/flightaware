import unittest
import pytz
from pprint import pprint
from datetime import datetime, timedelta
from flightaware.client import Client

import ConfigParser

config = ConfigParser.RawConfigParser()
config.read("developer.cfg")
username = config.get("test settings", "username")
api_key = config.get("test settings", "api_key")
verbose = config.getboolean("test settings", "verbose")

print "Using username => %s" % username
print "Using api_key => %s" % api_key


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.client = Client(username=username, api_key=api_key)

    def tearDown(self):
        pass

    #
    # Combined API tests
    #

    def test_basic_calls(self):
        results = self.client.all_airlines()
        self.assertNotIn("error", results)
        results = self.client.all_airports()
        self.assertNotIn("error", results)
        results = self.client.count_airport_operations("BNA")
        self.assertNotIn("error", results)

    def weather_calls(self):
        results = self.client.ntaf("BNA")
        self.assertNotIn("error", results)
        results = self.client.taf("BNA")
        self.assertNotIn("error", results)

    #
    # Individual API tests
    #

    def test_aircraft_type(self):
        results = self.client.aircraft_type("GALX")
        self.assertNotIn("error", results)

    def test_airline_insight(self):
        results = self.client.airline_insight("BNA", "ATL")
        self.assertNotIn("error", results)

    def test_airline_info(self):
        results = self.client.airline_info("SWA")
        self.assertNotIn("error", results)

    def test_airport_info(self):
        results = self.client.airport_info("KasdfBNA")
        self.assertIn("error", results)

        results = self.client.airport_info("BNA")
        self.assertNotIn("error", results)

        results = self.client.airport_info("KBNA")
        self.assertNotIn("error", results)
        if verbose: print results

    def test_all_airlines(self):
        results = self.client.all_airlines()
        self.assertNotIn("error", results)

    def test_all_airports(self):
        results = self.client.all_airports()
        self.assertNotIn("error", results)

    def test_count_airport_operations(self):
        results = self.client.count_airport_operations("BNA")
        self.assertNotIn("error", results)

    def test_decode_route(self):
        results = self.client.decode_route("KSQL", "SJC V334 SAC SWR", "KTRK")
        if verbose: pprint(results)
        self.assertNotIn("error", results)

    def test_fleet_arrived(self):
        results = self.client.fleet_arrived("URF")
        if verbose: pprint(results)
        self.assertNotIn("error", results)

    def test_fleet_scheduled(self):
        results = self.client.fleet_scheduled("URF")
        if verbose: pprint(results)
        self.assertNotIn("error", results)

    def test_flight_info(self):
        results = self.client.flight_info("N415PW")
        if verbose: pprint(results)
        self.assertNotIn("error", results)

    def test_flight_info_ex(self):
        results = self.client.flight_info_ex("N415PW")
        if verbose: pprint(results)
        self.assertNotIn("error", results)

    def test_get_flight_id(self):
        results = self.client.get_flight_id("N415PW", 1442008560)
        if verbose: pprint(results)
        self.assertNotIn("error", results)

        results = self.client.get_flight_id("N415PW", datetime.fromtimestamp(1442008560, tz=pytz.utc))
        if verbose: pprint(results)
        self.assertNotIn("error", results)

    def test_get_flight_info(self):
        start = datetime.now(tz=pytz.utc) + timedelta(days=2)
        end = datetime.now(tz=pytz.utc) + timedelta(days=3)
        results = self.client.airline_flight_schedules(
            start_date=start,
            end_date=end,
            origin="BNA",
            destination="ATL",
        )
        if verbose: print results
        self.assertNotIn("error", results)

        for result in results:
            self.assertIn("arrival_time", result)
            self.assertIn("departure_time", result)

    def test_metar(self):
        results = self.client.metar("BNA")
        self.assertNotIn("error", results)

    def test_metar_ex(self):
        results = self.client.metar_ex("BNA")
        self.assertNotIn("error", results)

    def test_zipcode_info(self):
        results = self.client.zipcode_info("37221")
        self.assertNotIn("error", results)

