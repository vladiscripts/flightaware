from flightaware.client import Client
from pprint import pprint

# App parameters
airport = 'KSFO'

# App configuration
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read("developer.cfg")
username = config.get("test settings", "username")
api_key = config.get("test settings", "api_key")

# Create the FlightAware.com API client ...
client = Client(username=username, api_key=api_key)

# Get the METAR information for San Francisco ...
results = client.metar(airport)
print "\n*** METAR information for:  ", airport
pprint(results)

# Get the extended METAR information for San Francisco ...
results = client.metar_ex(airport)
print "\n*** Extended METAR information for:  ", airport
pprint(results)

# Get the TAF (Terminal Aerodrome Forecast) for San Francisco ...
results = client.taf(airport)
print "\n*** TAF information for:  ", airport
pprint(results)

# Get the extended TAF (Terminal Aerodrome Forecast) for San Francisco ...
results = client.ntaf(airport)
print "\n*** Extended TAF information for:  ", airport
pprint(results)
