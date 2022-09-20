import json
import requests
from src.config import Config
from oauthlib.oauth2 import BackendApplicationClient

# Class for tickets in HaloPSA (not finished because of support)
class HaloTickets:

    def __init__(self):
        self.bearer = ''
        self.resource_uri = Config.RESOURCE_URI
        self.authorisation_uri = Config.AUTHORISATION_URI
        self.client_id = Config.CLIENT_ID
        self.client_secret = Config.CLIENT_SECRET

    # Authentication in HaloPSA service to gt access
    def auth(self):
        payload = 'grant_type=client_credentials&client_id=48459600-5b9b-4dbb-906b-df4504f8acb5&client_secret=8a5379e0-0256-445d-a201-69b5dde2845e-a8b5b1be-885a-4766-8cf4-bd8600edf311'
        headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json'
             }

        client = BackendApplicationClient(self.client_id)
        # data = client.prepare_request_body(refresh_token = None )
        res = requests.request("POST", self.authorisation_uri,headers=headers,  data=payload)
        client.parse_request_body_response(res.text)
        self.bearer = client.token['access_token']
        # headers = {
        #     'Content-Type': 'application/x-www-form-urlencoded',
        #     'Accept': 'application/json'
        # }
        # payload = 'grant_type=client_credentials&client_id=' + self.client_id + '&client_secret=' + self.client_secret
        # res = requests.request("POST", self.authorisation_uri, headers=headers, data=payload)
        # print(str(res))
        # self.bearer = json.loads(res.text)['access_token']

    # Returns list of tickets (doesn't work(problems with access))
    def get_tickets(self):
        self.auth()
        payload = {}
        headers = {
            'Authorization': 'Bearer ' + self.bearer,
            'Accept': 'application/json'
        }
        response = requests.request("GET", self.resource_uri + '/tickets', headers=headers, data=payload)
        return response.status_code

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
