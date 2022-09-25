from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from classes.halo import HaloTickets
import datetime
from config import Config


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
			"id": self.id,
			"title": self.title,
			"info": self.info
		}

	def __repr__(self):
		return {
				'id': self.id,
				'title': self.title,
				'info': self.info,
				'user_id': self.user_id
				}

	def __str__(self):
		return 'Ticket(id=' + str(self.id) + ', title= "' + self.title + '", info=' + self.info + ', user_id=' + str(
			self.user_id) + ')'


class Customers(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(25), unique=True)
	email = db.Column(db.String(80), unique=True)
	psw = db.Column(db.String(80))

	def __repr__(self):
		return '<Customer {}>'.format(self.id)


from classes.crm import CrmTickets


ht = HaloTickets()
ct = CrmTickets(db, Tickets)


# routes to CRM functions (ready and work)
@app.route('/get-crm-tickets', methods=['GET'])
def crm_get_tickets():
	page = request.args.get('page', default=1, type=int) - 1
	limit = request.args.get('limit', default=10, type=int)
	return ct.get_tickets(page, limit)


@app.route('/get-crm-ticket/<ticket_id>', methods=['GET'])
def crm_get_ticket(ticket_id):
	return ct.get_ticket(id=ticket_id)


@app.route('/set-crm-ticket', methods=['POST'])
def crm_create_ticket():
	return ct.post_ticket()


@app.route('/filter-crm-tickets', methods=['PUT'])
def filter_crm_tickets():
	data = request.get_json()
	return ct.filtration(data)


@app.route('/put-crm-ticket', methods=['PUT'])
def crm_edit_ticket():
	data = request.get_json()
	return ct.put_ticket(data)


@app.route('/delete-crm-ticket/<ticket_id>', methods=['GET'])
def crm_delete_ticket(ticket_id):
	return ct.delete_ticket(id=ticket_id)


# routes for HaloPSA functions (don't work (problem with access))
@app.route('/get-halo-tickets', methods=['GET'])
def halo_get_tickets():
	return ht.get_tickets()


@app.route('/get-halo-ticket/<ticket_id>', methods=['GET'])
def halo_get_ticket(ticket_id):
	return ht.get_ticket(ticket_id)


@app.route('/set-halo-ticket', methods=['GET'])
def halo_post_ticket():
	return ht.post_ticket(data={
								'summary': 'sum' + str(datetime.date.today()),
								'details': 'details'
								})

@app.route('/put-halo-ticket/<ticket_id>', methods=['PUT'])
def halo_edit_ticket(ticket_id):
	data = request.get_json()
	return ht.put_ticket(ticket_id, data)


@app.route('/delete-halo-ticket/<ticket_id>', methods=['DELETE'])
def halo_delete_ticket(ticket_id):
	data = request.get_json()
	return ht.delete_ticket(ticket_id, data)


# route for communication of CRM and HaloPSA
@app.route('/exportTickets', methods=['GET'])
def export_tickets():
	internal_tickets_list = ct.getTickets()
	return ht.update_tickets(internal_tickets_list)


if __name__ == '__main__':
	app.run()
 
