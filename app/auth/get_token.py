import os
import ..config
from auth0.v3.authentication import GetToken


domain = config.AUTH_CLIENT_DOMAIN
non_interactive_client_id = config.AUTH_CLIENT_ID
non_interactive_client_secret = config.AUTH_CLIENT_SECRET

get_token = GetToken(domain)
token = get_token.client_credentials(
    non_interactive_client_id, non_interactive_client_secret, 'https://{}/api/v2/'.format(domain))
mgmt_api_token = token['access_token']
