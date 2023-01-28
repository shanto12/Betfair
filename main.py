from betfairlightweight import APIClient
from CONSTS import *

# Instantiate the API client
client = APIClient(app_key=APPLICATION_KEY_1, username=USER_NAME, password=PASSWORD, certs=CERT_FILE_LOCAITON)

# Login to the API
client.login()

# Get a list of all live events
events = client.betting.list_event_types()

# Find the event of interest
event_name = "Soccer"
event_of_interest = next((x for x in events if x.event_type.name == event_name), None)

# Get the market_catalogue of the event
market_catalogue = client.betting.list_market_catalogue(filter={"eventTypeIds": [event_of_interest.event_type.id]})

# Get the percentage completion of the event
market_book = client.betting.list_market_book(market_ids=[market_catalogue[0].market_id])

print(f'{market_book[0].market_info.competition} is {market_book[0].market_info.percentage_complete}% completed')

# Logout from the API
client.logout()
