import pandas as pd  
from faker import Faker
from faker.providers import DynamicProvider
import uuid
import random
from datetime import datetime, timedelta

# Fake details generator in the English region US 
f = Faker(["en_US"])

# Dynamic providers for protocol, state, and return message
p_pro = DynamicProvider(provider_name="protocol", elements=["HTTP", "SFTP", "AdHOC", "routing"])
f.add_provider(p_pro)

s_pro = DynamicProvider(provider_name="state", elements=['SUBMITTED','FAILED', 'TO_EXECUTE', 'RECEIVING', 'POST_PROC', 'ARCHIVED', 'RECEIVED', 'SENT', 'AVAILABLE'])
f.add_provider(s_pro)

r_pro = DynamicProvider(provider_name="return_message", elements=['a','b','c','d','e','f','g','h','i','j'])
f.add_provider(r_pro)

# List of 50 fake emails generated using the Faker library
email = [f.email() for _ in range(50)]

# Dynamic provider for email
rid_pro = DynamicProvider(provider_name="rid", elements=email)
f.add_provider(rid_pro)

# Creating the DataFrame
entries = 5000
synthetic = pd.DataFrame({
    'EventId': [uuid.uuid4() for _ in range(entries)],
    'EventTimeStamp': [None] * entries,  # Placeholder for timestamps
    'EventTime': [None] * entries,  # Placeholder for event times
    'Protocol': [f.protocol() for _ in range(entries)],
    'FileSize': random.sample(range(1000, 100000), entries),
    'State': [f.state() for _ in range(entries)],
    'UserId': [f.rid() for _ in range(entries)],
    'SenderId': [f.rid() for _ in range(entries)],
    'ReceiverId': [f.rid() for _ in range(entries)],
    'ClientName': [f.name() for _ in range(entries)],
    'ReturnMessage': [f.return_message() for _ in range(entries)], 
    'CycleId': [uuid.uuid4() for _ in range(entries)],
    'CoreId': [uuid.uuid4() for _ in range(entries)],
})

# Generating a list of all dates in the year 2021
start_date = datetime(2021, 1, 1)
end_date = datetime(2021, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date).tolist()

# Randomly distribute 5000 events across these dates
event_dates = random.choices(date_range, k=entries)

# Populate EventTimeStamp and EventTime with these dates
for i, event_date in enumerate(event_dates):
    synthetic.at[i, 'EventTimeStamp'] = event_date.timestamp()
    synthetic.at[i, 'EventTime'] = event_date.strftime('%Y-%m-%d %H:%M:%S')

print(synthetic)
