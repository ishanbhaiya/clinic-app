

import sys
from datetime import datetime

from app import DOCTORS

OPEN_HOUR = 9
CLOSE_HOUR = 17
SLOT_MINUTES = 30


def validate_slot(doctor, time, booked=()):
    """Return a list of problems with the slot (empty means valid)."""
    errors = []
    if doctor not in DOCTORS:
        errors.append(f"unknown doctor: {doctor}")
    try:
        parsed = datetime.strptime(time, "%H:%M")
    except ValueError:
        return errors + [f"invalid time format: {time}"]
    if not OPEN_HOUR <= parsed.hour < CLOSE_HOUR:
        errors.append(f"outside clinic hours: {time}")
    if parsed.minute % SLOT_MINUTES != 0:
        errors.append(f"not on a {SLOT_MINUTES}-minute boundary: {time}")
    if (doctor, time) in booked:
        errors.append(f"double booking: {doctor} at {time}")
    return errors


BOOKED = [("Dr. Mehta", "10:00")]

# (description, doctor, time, should_be_valid)
CASES = [
    ("opening slot", "Dr. Mehta", "09:00", True),
    ("half-hour slot", "Dr. Shah", "10:30", True),
    ("last slot of the day", "Dr. Patel", "16:30", True),
    ("same time, different doctor", "Dr. Shah", "10:00", True),
    ("before opening", "Dr. Mehta", "08:30", False),
    ("at closing time", "Dr. Mehta", "17:00", False),
    ("not a 30-minute slot", "Dr. Shah", "10:15", False),
    ("unknown doctor", "Dr. House", "11:00", False),
    ("malformed time", "Dr. Patel", "25:99", False),
    ("double booking", "Dr. Mehta", "10:00", False),
]


def main():
    failures = 0
    for description, doctor, time, should_be_valid in CASES:
        errors = validate_slot(doctor, time, BOOKED)
        passed = (not errors) == should_be_valid
        failures += not passed
        detail = "; ".join(errors) or "valid"
        print(f"{'PASS' if passed else 'FAIL'}: {description} -> {detail}")

    print(f"\n{len(CASES) - failures}/{len(CASES)} slot checks passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
