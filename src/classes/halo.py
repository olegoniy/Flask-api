import json
import requests
from config import Config

# Class for tickets in HaloPSA (not finished because of support)
class HaloTickets:

	def __init__(self):
		self.bearer = ''
		self.resource_uri = Config.RESOURCE_URI
		self.authorisation_uri = Config.AUTHORISATION_URI
		self.authorisation_type = Config.AUTHORISATION_TYPE
		self.client_id = Config.CLIENT_ID
		self.client_secret = Config.CLIENT_SECRET

	# Authentication in HaloPSA service to get access
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

	# Returns list of tickets
	def get_tickets(self, page, limit):
		self.auth()
		payload = {
				'pegeinate': True,
				'page_size': limit,
				'page_no': page
				}
		headers = {
			'Authorization': 'Bearer ' + self.bearer,
			'Accept': 'application/json'
		}
		response = requests.request("GET", self.resource_uri + '/tickets', headers=headers, data=payload)
		return json.loads(response.text)

	# Returns info about ticket 
	def get_ticket(self, ticket_id):
		self.auth()
		payload = {}
		headers = {
			'Authorization': 'Bearer ' + self.bearer,
			'Accept': 'application/json'
		}
		
		response = requests.request("GET", self.resource_uri + '/tickets/' + ticket_id, headers=headers, data=payload)
		try:
			return json.loads(response.text)
		except: 
			return "There is no ticket with such id"

	# Creating of ticket
	def post_ticket(self, data):
		self.auth()
		payload = json.dumps([data])
		headers = {
			'Authorization': 'Bearer ' + self.bearer,
			'Content-Type': 'application/json'
		}
		response = requests.request("POST", self.resource_uri + '/tickets', headers=headers, data=payload)
		return str(json.loads(response.content)['id'])
	
	# Changing info about a ticket
	def put_ticket(self, ticket_id, data):
		self.auth()
		data['id'] = ticket_id
		payload = json.dumps([data])
		headers = {
			'Authorization': 'Bearer ' + self.bearer,
			'Content-Type': 'application/json'
		}
		response = requests.request("POST", self.resource_uri + '/tickets', headers=headers, data=payload)

	# deleting of ticket
	def delete_ticket(self, ticket_id, data):
		self.auth()
		payload = json.dumps([data])
		headers = {
			'Authorization': 'Bearer ' + self.bearer,
			'Content-Type': 'application/json'
		}
		try:
			response = requests.request("DELETE", self.resource_uri + f'/tickets/{ticket_id}', headers=headers, data=payload)
		except:
			return "There is no ticket with such id"
		return f"The ticket {ticket_id} was deleted"


class HaloCustomer:

	def __init__(self):
		self.bearer = ''
		self.resource_uri = Config.RESOURCE_URI
		self.authorisation_uri = Config.AUTHORISATION_URI
		self.authorisation_type = Config.AUTHORISATION_TYPE
		self.client_id = Config.CLIENT_ID
		self.client_secret = Config.CLIENT_SECRET

	# Authentication in HaloPSA service to get access
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

	def get_users(self, page, limit):
		self.auth()
		payload = {
				'pegeinate': True,
				'page_size': limit,
				'page_no': page
				}
		headers = {
			'Authorization': 'Bearer ' + self.bearer,
			'Accept': 'application/json'
		}
		response = requests.request("GET", self.resource_uri + '/Users', headers=headers, data=payload)
		return json.loads(response.text)

	def get_user(self, user_id):
		self.auth()
		payload = {}
		headers = {
			'Authorization': 'Bearer ' + self.bearer,
			'Accept': 'application/json'
		}
		
		response = requests.request("GET", self.resource_uri + '/Users/' + user_id, headers=headers, data=payload)
		try:
			return json.loads(response.text)
		except: 
			return "There is no user with such id"
			
	def post_user(self, data):
		self.auth()
		payload = json.dumps([data])
		headers = {
			'Authorization': 'Bearer ' + self.bearer,
			'Content-Type': 'application/json'
		}
		response = requests.request("POST", self.resource_uri + '/Users', headers=headers, data=payload)
		return str(json.loads(response.content)['id'])
		
	def delete_user(self, user_id, data):
		self.auth()
		payload = {}
		headers = {
			'Authorization': 'Bearer ' + self.bearer,
			'Content-Type': 'application/json'
		}
		try:
			response = requests.request("DELETE", self.resource_uri + f'/Users/{user_id}', headers=headers, data=payload)
		except:
			return "There is no user with such id"
		return f"The user with id {user_id} was deleted"
