class HelpDesk:
    def __init__(self):
        self.tickets = {}

    def create_ticket(self, ticket_id, issue):
        self.tickets[ticket_id] = {'issue': issue, 'status': 'open'}

    def resolve_ticket(self, ticket_id):
        if ticket_id in self.tickets:
            self.tickets[ticket_id]['status'] = 'resolved'
        else:
            print("Ticket not found.")

    def check_ticket(self, ticket_id):
        return self.tickets.get(ticket_id, "Ticket not found.")

helpdesk_system = HelpDesk()
helpdesk_system.create_ticket(101, "Internet connectivity issue.")
helpdesk_system.create_ticket(102, "Password reset request.")
helpdesk_system.resolve_ticket(101)
print(helpdesk_system.check_ticket(101))
print(helpdesk_system.check_ticket(102))
