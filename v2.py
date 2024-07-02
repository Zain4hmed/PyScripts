import pandas as pd
from faker import Faker
from faker.providers import DynamicProvider
import uuid
import random
from datetime import datetime, timedelta

# Fake details generator using English language
f = Faker(["en_US"])

# Dynamic providers for protocol, state, and return message
p_pro = DynamicProvider(provider_name="protocol", elements=["HTTP", "SFTP", "AdHOC", "routing"])
f.add_provider(p_pro)

s_pro = DynamicProvider(provider_name="state", elements=['SUBMITTED', 'FAILED', 'TO_EXECUTE', 'RECEIVING', 'POST_PROC', 'ARCHIVED', 'RECEIVED', 'SENT', 'AVAILABLE'])
f.add_provider(s_pro)

r_pro = DynamicProvider(provider_name="return_message", elements=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
f.add_provider(r_pro)

# List of 50 fake emails generated using the Faker library
email = [f.email() for _ in range(50)]

# Dynamic provider for email
rid_pro = DynamicProvider(provider_name="rid", elements=email)
f.add_provider(rid_pro)

# Monthly distribution percentages
monthly_distribution = [13, 12, 6, 4, 4, 11, 9, 9, 5, 4, 9, 14]

# Function to generate synthetic data based on monthly distributions
def generate_synthetic_data(entries, monthly_dist):
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

    # Distribute events across months
    monthly_counts = distribute_events(entries, monthly_dist)
    
    event_dates = []
    for month in range(1, 13):
        num_events_month = monthly_counts[month - 1]
        # Correctly handle all days in the month
        month_start = datetime(2021, month, 1)
        month_end = (month_start.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
        month_dates = pd.date_range(start=month_start, end=month_end).tolist()

        # Distributing events across days within the month
        daily_counts = distribute_events(num_events_month, [100 / len(month_dates)] * len(month_dates))
        for day, day_date in enumerate(month_dates):
            num_events_day = daily_counts[day]
            event_dates.extend([day_date] * num_events_day)
    
    # Randomly shuffle event_dates to distribute events more naturally
    random.shuffle(event_dates)
    
    # Populate EventTimeStamp and EventTime with these dates
    for i, event_date in enumerate(event_dates):
        synthetic.at[i, 'EventTimeStamp'] = event_date.timestamp()
        synthetic.at[i, 'EventTime'] = event_date.strftime('%Y-%m-%d %H:%M:%S')

    # Convert EventTime to datetime for easier manipulation
    synthetic['EventTime'] = pd.to_datetime(synthetic['EventTime'])

    return synthetic

# Function to calculate weekly representation
def calculate_weekly_representation(data):
    # Use .copy() to avoid SettingWithCopyWarning
    data = data.copy()
    # Group by month and week
    data['YearWeek'] = data['EventTime'].dt.strftime('%Y-%U')
    weekly_counts = data.groupby('YearWeek').size()
    weekly_percentages = (weekly_counts / data.shape[0]) * 100

    # Prepare the weekly representation
    weekly_representation = []
    month_grouped = data.groupby(data['EventTime'].dt.to_period('M'))
    for month, month_data in month_grouped:
        month_name = month_data['EventTime'].dt.strftime('%B').iloc[0]
        week_grouped = month_data.groupby(month_data['EventTime'].dt.strftime('%U'))
        for week, week_data in week_grouped:
            week_number = int(week) + 1
            percentage = (week_data.shape[0] / month_data.shape[0]) * 100
            week_summary = f"{month_name} : weekNumber{week_number}  [{', '.join(map(lambda x: f'%{x}', range(int(percentage), int(percentage) + 7)))}]"
            weekly_representation.append(week_summary)

    return weekly_representation

# Generate synthetic data using the provided distributions
entries = 5000
synthetic_data = generate_synthetic_data(entries, monthly_distribution)

# Monthly representation
monthly_counts = synthetic_data.groupby(synthetic_data['EventTime'].dt.to_period('M')).size()
monthly_percentages = (monthly_counts / monthly_counts.sum()) * 100
monthly_summary = pd.concat([monthly_counts, monthly_percentages], axis=1, keys=['Counts', 'Percentage'])

# Compute total transfers and total percentage
total_transfers = monthly_summary['Counts'].sum()
total_percentage = monthly_summary['Percentage'].sum()

# Append totals to monthly summary
monthly_summary.loc['Total'] = [total_transfers, total_percentage]

# Print the monthly representation with totals
print("\nMonthly Representation (Counts and Percentages):")
print(monthly_summary.to_string())

# Calculate weekly representation for each month
monthly_weekly_representation = {}
for month in synthetic_data['EventTime'].dt.to_period('M').sort_values().unique():
    monthly_data = synthetic_data[synthetic_data['EventTime'].dt.to_period('M') == month]
    monthly_weekly_representation[str(month)] = calculate_weekly_representation(monthly_data)

# Print the weekly representation for each month
for month, weekly_repr in monthly_weekly_representation.items():
    print(f"\nWeekly Representation for {month}:")
    for week_rep in weekly_repr:
        print(week_rep)

# Print the complete table of 5000 entries
print("\nComplete Data:")
print(synthetic_data)

# Optional: Save the data to CSV for a more comprehensive view
synthetic_data.to_csv("synthetic_data.csv", index=False)
