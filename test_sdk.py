from real_nex_sync_api_data_facade import RealNexSyncApiDataFacade

# Initialize the SDK with a mock API key (replace with actual if needed)
sdk = RealNexSyncApiDataFacade(api_key="your-api-key", timeout=10000)

# Example usage: print available client details
result = sdk.client.get_user(api_version="1.0")
print(result)
