import csv

with open("data/raw/StormEvents_details-ftp_v1.0_d2020_c20201216.csv", "r") as file:
    reader = csv.DictReader(file)
    line_count = 0
    event_types = set()
    empty_event_count = 0
    for row in reader:
        event = row["EVENT_TYPE"]
        if not event.strip():
            empty_event_count += 1
        event_types.add(event)
        line_count += 1
    empty_event_percentage = (
        (empty_event_count / line_count) * 100 if line_count > 0 else 0
    )
    print(reader.fieldnames)
    print(sorted(event_types))
    print("Event types count:", len(event_types))
    print("Line count:", line_count)
    print("Empty event count:", empty_event_count)
    print("Empty percentage:", empty_event_percentage)
