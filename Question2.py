# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_new_ticket(ticket_id, customer, issue):
    " Open a new service ticket."
    if ticket_id in service_tickets:
        print(f"Ticket ID {ticket_id} already exists.")
    else:
        service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
        print(f"Ticket {ticket_id} has been opened.")

def update_ticket_status(ticket_id, status):
    "Update the status of an existing ticket."
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status
        print(f"Ticket {ticket_id} status has been updated to {status}.")
    else:
        print(f"Ticket ID {ticket_id} not found.")

def display_tickets(filter_status=None):
    "Display all tickets or filter by status."
    for ticket_id, details in service_tickets.items():
        if filter_status is None or details["Status"] == filter_status:
            print(f"ID: {ticket_id}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")

open_new_ticket("Ticket003", "Charlie", "Account locked")

update_ticket_status("Ticket001", "closed")

print("\nAll tickets:")
display_tickets()

print("\nOpen tickets:")
display_tickets(filter_status="open")
