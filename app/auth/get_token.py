from auth0.v3.management import Auth0
import set_auth

domain = set_auth.domain

mgmt_api_token = set_auth.mgmt_api_token

auth0 = Auth0(domain, mgmt_api_token)

auth0.connections.all()
