import json
import requests


class HaloTickets:

    def __init__(self):
        self.bearer = ''
        # self.resource_uri = 'https://testflask.halopsa.com/api'
        self.resource_uri = 'https://tatooleh2.halopsa.com/api'
        # self.authorisation_uri = 'https://uk-trial.halopsa.com/token?tenant=testflask'
        self.authorisation_uri = 'https://uk-trial.halopsa.com/token?tenant=tatooleh2'
        self.client_id = "91c3dfe0-99a9-4558-a15f-915a3fee5af3"
        self.client_secret = "04117c7b-f8a0-4245-a914-8fb30d6e9dbb-dce46485-f36d-4dbe-b84f-b3386076e92b"

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
        print(response.text)
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
        self.check_auth()
        headers = {
            'Authorization': 'Bearer ' + self.bearer,
            'Content-Type': 'application/json'
        }
        response = requests.request("DELETE", self.resource_uri + '/tickets', headers=headers)
        print(response.text)
        return f"Ticket {id} was deleted"
# не працює


class HaloCustomer:

    def __init__(self):
        self.endpoint = "dgyueiw"
