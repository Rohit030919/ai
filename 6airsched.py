class AirlineScheduler:
    def __init__(self):
        self.flights = {}
        self.cargo = {}

    def schedule_flight(self, flight_number, departure_time, arrival_time):
        self.flights[flight_number] = {'departure': departure_time, 'arrival': arrival_time}

    def schedule_cargo(self, cargo_id, flight_number, weight):
        self.cargo[cargo_id] = {'flight_number': flight_number, 'weight': weight}

    def get_flight_schedule(self, flight_number):
        return self.flights.get(flight_number, "Flight not scheduled.")

    def get_cargo_schedule(self, cargo_id):
        return self.cargo.get(cargo_id, "Cargo not scheduled.")

scheduler = AirlineScheduler()
scheduler.schedule_flight("AA123", "2023-05-05 10:00", "2023-05-05 12:00")
scheduler.schedule_cargo("CARGO001", "AA123", 500)

print(scheduler.get_flight_schedule("AA123"))
print(scheduler.get_cargo_schedule("CARGO001"))
