import os
import sys
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

# Retrieve environment variables
site_url = os.environ.get('SHAREPOINT_SITE_URL')
username = os.environ.get('SHAREPOINT_USERNAME')
password = os.environ.get('SHAREPOINT_PASSWORD')

# Initialize credentials and context
credentials = UserCredential(username, password)
ctx = ClientContext(site_url).with_credentials(credentials)

# Define file details
file_url = "/sites/Insights-Intl/Shared Documents/Comscore_Data/Circuit_MS.parquet"
local_file_path = "Circuit_MS.parquet"

# Upload the file
with open(local_file_path, 'rb') as local_file:
    ctx.web.get_file_by_server_relative_url(file_url).upload(local_file).execute_query()
    print("File uploaded successfully.")
