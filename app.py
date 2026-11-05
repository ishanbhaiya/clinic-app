"""Clinic Appointment Application."""

DOCTORS = ["Dr. Mehta", "Dr. Shah", "Dr. Patel"]
appointments = []


def list_doctors():
    return DOCTORS


def book_appointment(patient, doctor, time):
    """Book a slot, rejecting unknown doctors and double bookings."""
    if doctor not in DOCTORS:
        raise ValueError(f"Unknown doctor: {doctor}")
    for appointment in appointments:
        if appointment["doctor"] == doctor and appointment["time"] == time:
            raise ValueError(f"{doctor} is already booked at {time}")
    appointment = {"patient": patient, "doctor": doctor, "time": time}
    appointments.append(appointment)
    return appointment


def main():
    print("Clinic Appointment Application")
    print("Doctors:", ", ".join(list_doctors()))
    book_appointment("Ishan", "Dr. Mehta", "10:00")
    book_appointment("Riya", "Dr. Shah", "10:00")
    for a in appointments:
        print(f"Booked: {a['patient']} with {a['doctor']} at {a['time']}")


if __name__ == "__main__":
    main()
