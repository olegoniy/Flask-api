from models import Tickets, Customers


class CrmTickets:

    def __init__(self, db):
        self.endpoint = ""
        self.db = db

    def get_tickets(self):
        return self.db.session.query(Tickets).all()

    def get_ticket(self, id):
        return self.db.session.query(Tickets).filter(Tickets.id == id).first()

    def create_ticket(self, data):
        ticket = Tickets(data)
        self.db.session.add(ticket)
        self.db.session.commit()
        return ticket.id

    def post_ticket(self, data):
        ticket = self.db.session.query(Tickets).filter(Tickets.id == data.id).first()
        ticket = data
        self.db.session.add(ticket)
        self.db.session.commit()
        return ticket.id

    def delete_ticket(self, id):
        self.db.session.