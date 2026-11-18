
class BookingRegistry:
    def __init__(self, movie, seat, subscription):
        self.movie = movie
        self.seat = seat
        self.subscription = subscription

class SeatOperations:
    def __init__(self):
        self.booked = set()

    def book(self, ticket):
        self.booked.add(ticket.seat)
        print("Ticket booked Successfully")

    def cancel(self, ticket):
        if ticket.seat not in self.booked:
            print("Ticket is not booked")
        else:
            self.booked.remove(ticket.seat)
            if ticket.subscription:
                print("Ticket Cancelled\nAmount Rs.200 will be credited")
            else:
                print("Ticket Cancelled\nAmount Rs.100 will be credited")

T1 = BookingRegistry('Ranabali', 34, True)
T2 = BookingRegistry('Ranabali', 30, False)

t = SeatOperations()
t.book(T1)
t.book(T2)
t.cancel(T1)
