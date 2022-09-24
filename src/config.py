# File with all configurations
class Config:
	DEBUG = True

	# SETTINGS OF CRM
	SECRET_KEY = "randomstringstep"
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/restapi'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	# SETTINGS OF HALOPSA SERVICE
	RESOURCE_URI = 'https://restapi.halopsa.com/api'
	AUTHORISATION_URI = 'https://eu-trial.halopsa.com/token?tenant=restapi'
	AUTHORISATION_TYPE = 'Basic NDg0NTk2MDAtNWI5Yi00ZGJiLTkwNmItZGY0NTA0ZjhhY2I1OjhhNTM3OWUwLTAyNTYtNDQ1ZC1hMjAxLTY5YjVkZGUyODQ1ZS1hOGI1YjFiZS04ODVhLTQ3NjYtOGNmNC1iZDg2MDBlZGYzMTE='
	CLIENT_ID = "48459600-5b9b-4dbb-906b-df4504f8acb5"
	CLIENT_SECRET = "8a5379e0-0256-445d-a201-69b5dde2845e-a8b5b1be-885a-4766-8cf4-bd8600edf311"

	# SETTINGS OF TICKETS AND USERS

	# TICKETS
	STANDARD_TITLE = "Standard title"
	STANDARD_INFO = "Standard info about the ticket"
	STANDARD_USER_ID = 1

	# USERS
