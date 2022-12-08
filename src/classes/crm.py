from flask import render_template
from abc import abstractclassmethod
import json
from config import Config


# Class for tickets in CRM (ready and works)
class CrmTickets:

	def __init__(self, db, Tickets):
		self.endpoint = ""
		self.db = db
		self.Tickets = Tickets

	# Returns list of all tickets in CRM (with pagination)
	def get_tickets(self, page: int, limit: int):
		res = []
		for item in self.db.session.query(self.Tickets).offset(page * limit).limit(limit).all():
			res.append((item.id, item.title, item.user_id))
		return json.dumps(res)

	# Returns info about ticket
	def get_ticket(self, id):
		try:
			return json.dumps(self.db.session.query(self.Tickets).filter(self.Tickets.id == id).first().all())
		except:
			return "Wrong ticket ID"

	# Creating of ticket with standard fields
	def post_ticket(self, data):
		ticket = self.Tickets()
		ticket.id = self.db.session.query(self.Tickets).all()[-1].id + 1
		ticket.title = Config.STANDARD_TITLE
		ticket.info = Config.STANDARD_INFO
		ticket.user_id = Config.STANDARD_USER_ID
		self.db.session.add(ticket)
		self.db.session.commit()
		return f"Ticket {ticket.id} was created"

	# Filtration of tickets by one or few keys (with pagination)
	def filtration(self, data):
		try:
			page = data['page']
		except:
			page = 0
		try:
			limit = data['limit']
		except:
			limit = 5

		def filter_check(data, ticket):
			filter = True
			try:
				filter = filter and self.Tickets.info.like("%" + data['info'] + "%")
			except:
				pass

			try:
				filter = filter and self.Tickets.info.like("%" + data['title'] + "%")
			except:
				pass

			try:
				filter = filter and self.Tickets.info.like("%" + data['user_id'] + "%")
			except:
				pass

			return filter

		res = []
		items = self.db.session.query(self.Tickets).filter(filter_check(data, self.Tickets)).offset(page * limit).limit(
			limit).all()
		for item in items:
			res.append((item.id, item.title, item.info, item.user_id))
		if res:
			return json.dumps(res)
		return "Wrong page or such ticket does not exist"

	# Editing of tickets fields
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

	def update_or_create_ticket(self, data):

		ticket = self.db.session.query(self.Tickets).filter(self.Tickets.id == data["id"]).first()
		if ticket is None:
			ticket = self.Tickets()

		for i in range(len(data)):
			value = data[i]
			if value is not None:
				key = self.Tickets.property_names[i]
				setattr(self, key, value)

		self.db.session.commit()