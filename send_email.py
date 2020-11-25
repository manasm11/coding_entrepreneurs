from smtplib import SMTP

username = "laozimishra@gmail.com"
password = "R@ndumP@ssword"


def send_email(message=None, subject=None, to_emails=None, from_name=None, verbose=False):
    # ASSERTIONS TO CHECK INPUT VALUES
    verbose and print("INSIDE: send_email")
    _e = f" in '{__file__}'"
    assert isinstance(message, str), "'message' not string" + _e
    assert isinstance(subject, str), "'subject' not string" + _e
    assert isinstance(to_emails, list), "'to_emails' not list" + _e
    assert isinstance(to_emails[0], str), "'to_emails' elements not string"+_e
    # ASSERTIONS END
    # Sorry for wrong indentation below, but I couldn't find a fix for this...
    email_message_template = f"""from: {from_name if from_name else username}"""+"""
to: {to_email}"""+f"""
subject: {subject}

{message}"""

    # SENDING EMAIL
    with SMTP("smtp.gmail.com", 587) as conn:
        _response = conn.ehlo()
        verbose and print("[*] conn.ehlo():", _response)
        _response = conn.starttls()
        verbose and print("[*] conn.starttls():", _response)
        _response = conn.login(user=username, password=password)
        verbose and print("[*] conn.login():", _response)
        for to_email in to_emails:
            message = email_message_template.format(to_email=to_email)
            verbose and print("[*] message =", message)
            verbose and print("[*] sending to", to_email)
            _response = conn.sendmail(
                from_addr=username, to_addrs=to_email, msg=message.encode("utf-8"))
            verbose and print("[*] conn.sendmail():", _response)
        verbose and print("[+] all mails sent")


if __name__ == "__main__":
    send_email(
        message="HELLO",
        to_emails=[
            "f20170546@pilani.bits-pilani.ac.in",
            "manas.m22@gmail.com"
        ],
        subject="Testing",
        from_name="Manas Mishra",
        verbose=True
    )
