message_template = """Hello {name},
Thank you for joining '{website}'. We are very pleased to have you with us.
"""

def format_msg(name="Manas"):
    return message_template.format(name=name, website="laozi.in")
if __name__ == "__main__":
    recipients = ["Manas", "Divya", "Lakshya", "Naman"]
    for name in recipients:
        this_person_message = format_msg(name=name)
        print(this_person_message)