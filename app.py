"""Clinic Appointment Application."""

DOCTORS = ["Dr. Mehta", "Dr. Shah", "Dr. Patel"]


def list_doctors():
    return DOCTORS


def main():
    print("Clinic Appointment Application")
    print("Doctors:", ", ".join(list_doctors()))


if __name__ == "__main__":
    main()
