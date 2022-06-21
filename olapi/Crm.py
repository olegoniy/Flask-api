from flask_sqlalchemy import SQLAlchemy
from app import db
from config import Config


engine = create_engine(DATABASE)


class crm_tickets:

    def __init__(self):
        self.endpoint = "fdfdfd"

    def getTickets(self):
        pass

    def getTickets(self, id):
        pass

    def postTicket(self, data):
        pass

    def deleteTicket(self, id):
        pass