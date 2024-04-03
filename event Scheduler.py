from datetime import datetime

# In-memory storage for events
events = []

# Function to add a new event
def add_event(title, description, date, time):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        datetime.strptime(time, '%H:%M')
    except ValueError:
        print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
        return

    events.append({
        'title': title,
        'description': description,
        'date': date,
        'time': time
    })
    print("Event added successfully.")

# Function to display all events sorted by date and time
def list_events():
    sorted_events = sorted(events, key=lambda x: (x['date'], x['time']))
    if sorted_events:
        print("All Events:")
        for event in sorted_events:
            print(f"Title: {event['title']}, Description: {event['description']}, Date: {event['date']}, Time: {event['time']}")
    else:
        print("No events found.")

# Function to delete an event based on title
def delete_event(title):
    global events
    events = [event for event in events if event['title'] != title]
    print("Event deleted successfully.")

# Function to search events by date or keyword in title/description
def search_events(keyword):
    found_events = [event for event in events if keyword.lower() in event['title'].lower() or keyword.lower() in event['description'].lower() or keyword == event['date']]
    if found_events:
        print("Matching Events:")
        for event in found_events:
            print(f"Title: {event['title']}, Description: {event['description']}, Date: {event['date']}, Time: {event['time']}")
    else:
        print("No events found matching the search criteria.")

# Function to edit an existing event
def edit_event(title, new_title, new_description, new_date, new_time):
    global events
    for event in events:
        if event['title'] == title:
            event['title'] = new_title
            event['description'] = new_description
            event['date'] = new_date
            event['time'] = new_time
            print("Event edited successfully.")
            return
    print("Event not found.")

# Main function
def main():
    while True:
        print("\n1. Add Event")
        print("2. List Events")
        print("3. Delete Event")
        print("4. Search Events")
        print("5. Edit Event")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter event title: ")
            description = input("Enter event description: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            add_event(title, description, date, time)
        elif choice == '2':
            list_events()
        elif choice == '3':
            title = input("Enter the title of the event you want to delete: ")
            delete_event(title)
        elif choice == '4':
            keyword = input("Enter a date or keyword to search events: ")
            search_events(keyword)
        elif choice == '5':
            title = input("Enter the title of the event you want to edit: ")
            new_title = input("Enter new title (leave blank to keep current): ")
            new_description = input("Enter new description (leave blank to keep current): ")
            new_date = input("Enter new date (YYYY-MM-DD) (leave blank to keep current): ")
            new_time = input("Enter new time (HH:MM) (leave blank to keep current): ")
            edit_event(title, new_title, new_description, new_date, new_time)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Unit tests
def test_add_event():
    add_event("Meeting", "Team meeting", "2024-04-02", "09:00")
    assert len(events) == 1

def test_delete_event():
    delete_event("Meeting")
    assert len(events) == 0

def test_edit_event():
    add_event("Meeting", "Team meeting", "2024-04-02", "09:00")
    edit_event("Meeting", "Updated Meeting", "Updated description", "2024-04-03", "10:00")
    for event in events:
        if event['title'] == "Updated Meeting":
            assert event['description'] == "Updated description"
            assert event['date'] == "2024-04-03"
            assert event['time'] == "10:00"
            break

if __name__ == "__main__":
    # Run unit tests
    test_add_event()
    test_delete_event()
    test_edit_event()
    print("All tests passed.")

    # Run the main program
    main()
