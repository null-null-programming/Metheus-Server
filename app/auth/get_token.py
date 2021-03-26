import os
from auth0.v3.authentication import GetToken

domain = 'myaccount.auth0.com'
non_interactive_client_id = 'exampleid'
non_interactive_client_secret = 'examplesecret'

get_token = GetToken(domain)
token = get_token.client_credentials(non_interactive_client_id,
                                     non_interactive_client_secret, 'https://{}/api/v2/'.format(domain))
mgmt_api_token = token['access_token']
