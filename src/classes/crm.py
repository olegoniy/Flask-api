from flask import render_template
from abc import abstractclassmethod
import json
import jsonify


class CrmTickets:

    def __init__(self, db, Tickets):
        self.endpoint = ""
        self.db = db
        self.Tickets = Tickets

    def get_tickets(self, page: int, limit: int):
        res = []
        for item in self.db.session.query(self.Tickets).offset(page * limit).limit(limit).all():
            res.append((item.id, item.title, item.user_id))
        return json.dumps(res)

    def get_ticket(self, id):
        try:
            return json.dumps(self.db.session.query(self.Tickets).filter(self.Tickets.id == id).first().all())
        except:
            return "Wrong ticket ID"

    def get_data(self):
        data = {}
        data["title"] = ""
        data["info"] = ""
        data["user_id"] = 123
        return data

    def post_ticket(self, data):
        ticket = self.Tickets()
        ticket.id = self.db.session.query(self.Tickets).all()[-1].id + 1
        ticket.title = ""
        ticket.info = ""
        ticket.user_id = 123
        self.db.session.add(ticket)
        self.db.session.commit()
        return f"Ticket {ticket.id} was created"

    def filtration(self, data):
        pass

    def put_ticket(self, data):
        ticket = self.db.session.query(self.Tickets).filter(self.Tickets.id == data["id"]).first()
        try:
            ticket.title = data["title"]
        except:
            pass
        try:
            ticket.info = data["info"]
        except:
            pass
        try:
            ticket.user_id = data["user_id"]
        except:
            pass
        self.db.session.add(ticket)
        self.db.session.commit()
        return "Changes were applied \n" + str(ticket)

    def delete_ticket(self, id):
        if self.db.session.query(self.Tickets).filter(self.Tickets.id == id).all():
            self.db.session.query(self.Tickets).filter(self.Tickets.id == id).delete()
            for item in self.db.session.query(self.Tickets).filter(self.Tickets.id > id):
                item.id -= 1
            self.db.session.commit()
            return f"Ticket {id} was deleted"
        return "Wrong id"
