from apify_client import ApifyClient

def fetch_crypto_data(api_token, asset="bitcoin", limit=1000):
    print(f"Fetching {limit} bars of historical data for {asset}...")
    client = ApifyClient(api_token)
    
    try:
        run = client.actor("ar_scraper/Crypto-price-Fetch").call(
            run_input={"symbols": [asset], "limit": limit}
        )
        
        data = list(client.dataset(run.default_dataset_id).iterate_items())
        print("Data fetched successfully!")
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None