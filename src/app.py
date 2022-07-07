from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from classes.halo import HaloTickets
from datetime import datetime
from config import Config
import json

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class Tickets(db.Model):
    __tablename__ = "tickets"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    info = db.Column(db.String(800), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    def all(self):
        return {
            "id":    self.id,
            "title": self.title,
            "info":  self.info
        }

    def __repr__(self):
        return {'id': self.id, 'title': self.title, 'info': self.info, 'user_id': self.user_id}

    def __str__(self):
        return 'Ticket(id=' + str(self.id) + ', title=' + self.title + ', info=' + self.info + ', user_id=' + str(self.user_id) + ')'


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)
    email = db.Column(db.String(80), unique=True)
    psw = db.Column(db.String(80))

    def __repr__(self):
        return '<Customer {}>'.format(self.id)


from classes.crm import CrmTickets

# app.config.from_object(Config)
ht = HaloTickets()
ct = CrmTickets(db, Tickets)


@app.route('/get-halo-tickets', methods=['GET'])
def halo_get_tickets():
    return ht.get_tickets()


@app.route('/get-halo-ticket/<ticket_id>', methods=['GET'])
def halo_get_ticket(ticket_id):
    return ht.get_ticket(ticket_id)


@app.route('/set-halo-ticket', methods=['GET'])
def halo_post_ticket():
    return ht.post_ticket(data={'summary': 'sum' + str(datetime),
                                'details': 'details'})


@app.route('/get-crm-tickets', methods=['GET'])
def crm_get_tickets():
    return ct.get_tickets()


@app.route('/get-crm-ticket/<ticket_id>', methods=['GET'])
def crm_get_ticket(ticket_id):
    return ct.get_ticket(ticket_id)


@app.route('/create-crm-ticket', methods=['GET'])
def crm_create_ticket():
    return ct.create_ticket(data={'user_id': 1, 'title': 'sum' + str(datetime), 'info': 'details'})


@app.route('/set-crm-ticket', methods=['GET'])
def crm_post_ticket():
    return ct.post_ticket(data={'id': 1, 'title': 'sum' + str(datetime),
                                'info': 'details'})


@app.route('/exportTickets', methods=['GET'])
def export_tickets():
    internal_tickets_list = ct.getTickets()
    # Данная функция находится в классе в файле Crm
    return ht.update_tickets(internal_tickets_list)


if __name__ == '__main__':
    app.run()
