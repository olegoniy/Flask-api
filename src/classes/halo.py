import json
import requests


class HaloTickets:

    def __init__(self):
        self.bearer = ''
        # self.resource_uri = 'https://testflask.halopsa.com/api'
        self.resource_uri = 'https://tatooleh.halopsa.com/api'
        # self.authorisation_uri = 'https://uk-trial.halopsa.com/token?tenant=testflask'
        self.authorisation_uri = 'https://uk-trial.halopsa.com/token?tenant=tatooleh'
        self.client_id = "b19e739f-5495-4e7c-8f7b-65fe995a4406"
        self.client_secret = "1bda024e-5bf3-4dd7-8264-d392f41aa5b9-974abdca-1cc4-4a41-bc5c-5391c899fb70"

    def auth(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        payload = 'grant_type=client_credentials&client_id=' + self.client_id + '&client_secret=' + self.client_secret
        res = requests.request("POST", self.authorisation_uri, headers=headers, data=payload)
        self.bearer = json.loads(res.text)['access_token']

    def check_auth(self):
        self.auth()

    def get_tickets(self):
        self.check_auth()
        payload = {}
        headers = {
            'Authorization': 'Bearer ' + self.bearer,
            'Accept': 'application/json'
        }

        response = requests.request("GET", self.resource_uri + '/tickets', headers=headers, data=payload)

        # print(response.text)
        return response.status_code

    def get_ticket(self, ticket_id):
        self.check_auth()
        payload = {}
        headers = {
            'Authorization': 'Bearer ' + self.bearer,
            'Accept': 'application/json'
        }

        response = requests.request("GET", self.resource_uri + '/tickets/' + ticket_id, headers=headers, data=payload)

        print(response.text)
        return response.status_code

    def post_ticket(self, data):
        self.check_auth()
        payload = json.dumps([
            data])
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
        self.endpoint = "dgyueiw"
