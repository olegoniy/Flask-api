import json
import jsonify


class CrmTickets:

    def __init__(self, db, Tickets):
        self.endpoint = ""
        self.db = db
        self.Tickets = Tickets

    def get_tickets(self):
        res = []
        for item in self.db.session.query(self.Tickets).all():
            res.append((item.id, item.title, item.user_id))
        return json.dumps(res)

    def get_ticket(self, id):
        try:
            return json.dumps(self.db.session.query(self.Tickets).filter(self.Tickets.id == id).first().all())
        except:
            return "Wrong ticket ID"

    def create_ticket(self, data):
        ticket = self.Tickets()
        ticket.title = data['title']
        ticket.info = data['info']
        ticket.user_id = data['user_id']
        self.db.session.add(ticket)
        self.db.session.commit()
        return json.dumps(ticket.id)

    def post_ticket(self, data):
        ticket = self.db.session.query(self.Tickets).filter(self.Tickets.id == data.id).first()
        ticket.loads(data)
        self.db.session.add(ticket)
        self.db.session.commit()
        return ticket.id

    def delete_ticket(self, id):
        pass
