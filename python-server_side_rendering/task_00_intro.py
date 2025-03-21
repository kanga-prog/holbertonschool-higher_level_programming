import os

def generate_invitations(template, attendees):
    # Check if the template is a string and attendees is a list of dictionaries
    if not isinstance(template, str):
        print(f"Error: Expected a string for template, but got {type(template)}.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print(f"Error: Expected a list of dictionaries for attendees, but got {type(attendees)}.")
        return

    # Handle empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Handle empty list of attendees
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Iterate through each attendee and generate the invitation
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with the attendee's data, defaulting to 'N/A' if data is missing
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A") if attendee.get("event_date") else "N/A"
        event_location = attendee.get("event_location", "N/A")
        
        # Replace placeholders in the template
        invitation = template.format(name=name, event_title=event_title, event_date=event_date, event_location=event_location)
        
        # Define the output file path
        output_file = f"output_{index}.txt"
        
        # Ensure the file does not already exist before writing
        if os.path.exists(output_file):
            print(f"Error: {output_file} already exists.")
            continue
        
        # Write the invitation to a file
        try:
            with open(output_file, 'w') as file:
                file.write(invitation)
            print(f"Invitation for {name} saved to {output_file}.")
        except Exception as e:
            print(f"Error writing to {output_file}: {e}")

