import requests
import json

# Your Facebook App ID and App Secret
app_id = "1126862121803807"
app_secret = "0d670b095d87aa3d1a91d4c01cac5f81"

# The target user ID and password
target_user_id = "61552076792138"
target_password = "mrefatnothere"

# Generate an access token
token_url = f"https://graph.facebook.com/oauth/access_token?client_id={app_id}&client_secret={app_secret}&grant_type=client_credentials"
response = requests.get(token_url)
if response.status_code == 20:
    access_token = response.json()["access_token"]
else:
    print(f"Error: {response.status_code} - Unable to generate access token.")

# Search for the target user
search_url = f"https://graph.facebook.com/v15.0/search?q={target_user_id}&type=user&access_token={access_token}"
response = requests.get(search_url)
if response.status_code == 20:
    user_data = json.loads(response.text)

    # Check if the target user ID exists in the search results
    if len(user_data["data"]) > 0:
        for user in user_data["data"]:
            # Compare the target user ID and password
            if user["id"] == target_user_id and user["password"] == target_password:
                print(f"Found the target user: {user['id']} - {user['name']}")

            else:
                print(f"No match found for the target user ID: {user['id']}")

    else:
        print(f"No match found for the target user ID: {target_user_id}")

else:
    print(f"Error: {response.status_code} - Unable to search for the target user.")
