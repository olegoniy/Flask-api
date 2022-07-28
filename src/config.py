# File with all configurations
class Config:
    DEBUG = True

    # SETTINGS OF CRM
    SECRET_KEY = "randomstringstep"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/restapi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SETTINGS OF HALOPSA SERVICE
    RESOURCE_URI = 'https://olehtest.halopsa.com/api'
    AUTHORISATION_URI = 'https://eu-trial.halopsa.com/token?tenant=olehtest'
    CLIENT_ID = "01401278-cd57-4418-b485-6c5998bdb663"
    CLIENT_SECRET = "31aab08b-e566-4c85-bdd0-786795aa3e48-26abd3be-9b9f-44be-871a-52128e154528"

    # SETTINGS OF TICKETS AND USERS

    # TICKETS
    STANDARD_TITLE = "Standard title"
    STANDARD_INFO = "Standard info about the ticket"
    STANDARD_USER_ID = 1

    # USERS
