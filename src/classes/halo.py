import json
import requests
from src.config import Config

# Class for tickets in HaloPSA (not finished because of support)
class HaloTickets:

    def __init__(self):
        self.bearer = ''
        self.resource_uri = Config.RESOURCE_URI
        self.authorisation_uri = Config.AUTHORISATION_URI
        self.authorisation_type = Config.AUTHORISATION_TYPE
        self.client_id = Config.CLIENT_ID
        self.client_secret = Config.CLIENT_SECRET

    # Authentication in HaloPSA service to gt access
    def auth(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        payload = {
            'grant_type': 'client_credentials',
            'scope': 'all',
            'token_type': 'Bearer',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        res = requests.request("POST", self.authorisation_uri, headers=headers, data=payload)
        self.bearer = json.loads(res.text)['access_token']

    # Returns list of tickets (doesn't work(problems with access))
    def get_tickets(self):
        self.auth()
        payload = {}
        headers = {
            'Authorization': 'Bearer ' + self.bearer,
            'Accept': 'application/json'
        }
        response = requests.request("GET", self.resource_uri + '/tickets', headers=headers, data=payload)
        return json.loads(response.text)

    # Returns info about ticket (doesn't work(problems with access))
    def get_ticket(self, ticket_id):
        self.auth()
        payload = {}
        headers = {
            'Authorization': 'Bearer ' + self.bearer,
            'Accept': 'application/json'
        }

        response = requests.request("GET", self.resource_uri + '/tickets/' + ticket_id, headers=headers, data=payload)
        return response.status_code

    # Creating of ticket (works for some reason)
    def post_ticket(self, data):
        self.auth()
        payload = json.dumps([data])
        headers = {
            'Authorization': 'Bearer ' + self.bearer,
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", self.resource_uri + '/tickets', headers=headers, data=payload)
        print(response.text)
        return str(json.loads(response.content)['id'])

    def delete_ticket(self, id):
        pass


class HaloCustomer:

    def __init__(self):
        pass
