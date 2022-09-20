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
    CLIENT_ID = "48459600-5b9b-4dbb-906b-df4504f8acb5"
    # "8af729ce-5ec5-440c-89e4-45bd05b1dddd"
    CLIENT_SECRET = "8a5379e0-0256-445d-a201-69b5dde2845e-a8b5b1be-885a-4766-8cf4-bd8600edf311"
        #"d0f7da1e-3fc3-455a-8a32-ae26080bcc98-01ec7c9a-9293-4001-a0c9-ce360e644fa9"

    # SETTINGS OF TICKETS AND USERS

    # TICKETS
    STANDARD_TITLE = "Standard title"
    STANDARD_INFO = "Standard info about the ticket"
    STANDARD_USER_ID = 1

    # USERS
# 8a5379e0-0256-445d-a201-69b5dde2845e-a8b5b1be-885a-4766-8cf4-bd8600edf311
# 48459600-5b9b-4dbb-906b-df4504f8acb5