import json
import requests


class HaloTickets:

    def __init__(self):
        self.bearer = ''
        self.resource_uri = 'https://olehtest.halopsa.com/api'
        self.authorisation_uri = 'https://uk-trial.halopsa.com/token?tenant=olehtest'
        self.client_id = "01401278-cd57-4418-b485-6c5998bdb663"
        self.client_secret = "31aab08b-e566-4c85-bdd0-786795aa3e48-26abd3be-9b9f-44be-871a-52128e154528"

    def auth(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        payload = 'grant_type=client_credentials&client_id=' + self.client_id + '&client_secret=' + self.client_secret
        res = requests.request("POST", self.authorisation_uri, headers=headers, data=payload)
        print(str(res))
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
        return response.status_code

    def post_ticket(self, data):
        self.check_auth()
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
        self.endpoint = "dgyueiw"
