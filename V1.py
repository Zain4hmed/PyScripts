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

# Distributions provided in percentages
monthly_distribution = [13,12,6,4,4,11,9,9,5,4,9,14]
weekly_distribution = [40,30,20,10]
daily_distribution = [13,12,8,10,14,23,20]

# Function to generate synthetic data based on distributions
def generate_synthetic_data(entries, monthly_dist, weekly_dist, daily_dist):
    # Create the DataFrame
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

    # Function to distribute events based on percentage distribution
    def distribute_events(entries, distribution):
        counts = [int(entries * (percent / 100)) for percent in distribution]
        total = sum(counts)
        if total < entries:
            counts[-1] += entries - total
        return counts

    # Distributing events across months
    monthly_counts = distribute_events(entries, monthly_dist)
    
    event_dates = []
    for month in range(1, 13):
        num_events_month = monthly_counts[month - 1]
        # Correctly handle all days in the month
        month_start = datetime(2021, month, 1)
        month_end = (month_start.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
        month_dates = pd.date_range(start=month_start, end=month_end).tolist()

        # Distributing events across weeks within the month
        weekly_counts = distribute_events(num_events_month, weekly_dist)
        week_start = month_start
        for week in range(4):
            num_events_week = weekly_counts[week]
            week_end = week_start + timedelta(days=6)
            if week_end > month_end:
                week_end = month_end
            week_dates = pd.date_range(start=week_start, end=week_end).tolist()

            # Distributing events across days within the week
            daily_counts = distribute_events(num_events_week, daily_dist)
            for day, day_date in enumerate(week_dates):
                num_events_day = daily_counts[day % len(daily_counts)]
                event_dates.extend([day_date] * num_events_day)
            
            week_start = week_end + timedelta(days=1)
    
    # Randomly shuffle event_dates to distribute events more naturally
    event_dates = random.sample(event_dates, entries)
    
    # Populate EventTimeStamp and EventTime with these dates
    for i, event_date in enumerate(event_dates):
        synthetic.at[i, 'EventTimeStamp'] = event_date.timestamp()
        synthetic.at[i, 'EventTime'] = event_date.strftime('%Y-%m-%d %H:%M:%S')

    # Convert EventTime to datetime for easier manipulation
    synthetic['EventTime'] = pd.to_datetime(synthetic['EventTime'])

    return synthetic

# Generate synthetic data using the provided distributions
entries = 5000
synthetic_data = generate_synthetic_data(entries, monthly_distribution, weekly_distribution, daily_distribution)

# Yearly representation
yearly = synthetic_data.groupby(synthetic_data['EventTime'].dt.year).size()
print("Yearly Representation:")
print(yearly)

# Monthly representation
monthly_counts = synthetic_data.groupby(synthetic_data['EventTime'].dt.to_period('M')).size()
monthly_percentages = (monthly_counts / monthly_counts.sum()) * 100
monthly_summary = pd.concat([monthly_counts, monthly_percentages], axis=1, keys=['Counts', 'Percentage'])
print("\nMonthly Representation (Counts and Percentages):")
print(monthly_summary.to_string())

# Daily representation
daily_counts = synthetic_data.groupby(synthetic_data['EventTime'].dt.to_period('D')).size()
daily_percentages = (daily_counts / daily_counts.sum()) * 100
daily_summary = pd.concat([daily_counts, daily_percentages], axis=1, keys=['Counts', 'Percentage'])
print("\nDaily Representation (Counts and Percentages):")
print(daily_summary.to_string())

# Print the complete table of 5000 entries
print("\nComplete Data:")
print(synthetic_data)

# Optional: Save the data to CSV for a more comprehensive view
synthetic_data.to_csv("synthetic_data.csv", index=False)
