import pandas as pd
import requests
import datetime

# Define only the 'daily_sleep' endpoint
sleep_endpoint = 'https://api.ouraring.com/v2/usercollection/daily_sleep'

# Your authentication token (ensure this is kept secure!)
auth_token = 'test'

# Function to pull data from the 'daily_sleep' API endpoint
def pull_daily_sleep_data(start_date, end_date, auth_token):
    """
    Fetches data from the 'daily_sleep' Oura API endpoint.

    Parameters:
        start_date (datetime): Start date for data retrieval.
        end_date (datetime): End date for data retrieval.
        auth_token (str): Bearer token for authentication.

    Returns:
        pd.DataFrame or None: DataFrame containing the 'daily_sleep' data or None if not found.
    """
    params = {
        'start_date': start_date.strftime('%Y-%m-%d'),
        'end_date': end_date.strftime('%Y-%m-%d')
    }
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }

    try:
        response = requests.get(sleep_endpoint, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        response_data = response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred for {sleep_endpoint}: {http_err}")
        return None
    except Exception as err:
        print(f"Other error occurred for {sleep_endpoint}: {err}")
        return None

    # Normalize the JSON data into a DataFrame
    if 'data' in response_data:
        data = pd.json_normalize(response_data['data'])
        # Optionally, remove specific prefixes from column names
        data.rename(columns=lambda s: s.replace("contributors.", ""), inplace=True)
        return data
    else:
        print(f"No 'data' key in response from {sleep_endpoint}")
        return None

# Set the date range
start_date = datetime.datetime.strptime('2022-05-01', '%Y-%m-%d')
end_date = datetime.datetime.now()

# Fetch 'daily_sleep' data
daily_sleep_df = pull_daily_sleep_data(start_date, end_date, auth_token)

# Function to retrieve the sorted 'daily_sleep' DataFrame without passing any parameters
def get_sleep_data():
    """
    Retrieves and returns the sorted 'daily_sleep' DataFrame.

    Returns:
        pd.DataFrame: Sorted 'daily_sleep' DataFrame or an empty DataFrame if not found.
    """
    if daily_sleep_df is not None and not daily_sleep_df.empty:
        # Ensure the 'day' column exists
        if 'day' in daily_sleep_df.columns:
            sorted_sleep_df = daily_sleep_df.sort_values(by='day', ascending=False).reset_index(drop=True)
            return sorted_sleep_df
        else:
            print("The 'day' column is missing in the 'daily_sleep' DataFrame.")
            return pd.DataFrame()
    else:
        print("No 'daily_sleep' data available.")
        return pd.DataFrame()  # Return an empty DataFrame if 'daily_sleep' is not found