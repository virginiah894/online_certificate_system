import smtplib
from datetime import datetime as dt
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror

filename = "certificate.pdf"


def email_change(filename):

    time_p = dt.now()

    mon = time_p.strftime("%B")

    email_receivers = {
        "Virginiah": "virgyperry@gmail.com",
        
    }

    login = "veep460@gmail.com"

    password = "testingpassword@123"

    sender_email = login

    for name, email in email_receivers.items():

        receiver_email = email

        message = MIMEMultipart("alternative")

        message["Subject"] = "Important notice - Your Certificate"

        message["From"] = sender_email

        message["To"] = receiver_email

        # Add body to email

        try:
            body = html_2 = f"""\
                                    <html>
                                      <head></head>
                                      <body>
                                        <p> Good day!<br>
                                          <br>
                                          Kindly find attached your certificate.
                                          <p>
                                          Regards.
                                          
                                          </p>
                                          </br>
                                          <br>
                                            
                                          </br>
                                      
                                          </p> 
                                        </body>
                                    </html>
                                    """

            message.attach(MIMEText(body, "html"))

           # In same directory as script

            # Open  file in binary mode
            with open(filename, "rb") as attachment:
                # Add file as application/octet-stream

                # Email client can usually download this automatically as attachment

                part1 = MIMEBase("application", "octet-stream")

                part1.set_payload(attachment.read())

                # Encode file in ASCII characters to send by email

            encoders.encode_base64(part1)

            # Add header as key/value pair to attachment part
            part1.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            message.attach(part1)

            server = smtplib.SMTP("smtp.gmail.com", 587)

            server.starttls()

            server.ehlo()

            server.login(login, password)

            server.sendmail(sender_email, receiver_email, message.as_string())

            server.close()

            # telling the script to report if your message was sent or which errors need to be fixed

            print(f"Sent to {name}")

        except (gaierror, ConnectionRefusedError):

            print(
                f"Failed to connect to the server. Bad connection settings? Not sent to {name}, {email}"
            )

        except smtplib.SMTPServerDisconnected:

            print(
                f"Failed to connect to the server. Wrong user/password?Not sent to {name}, {email}"
            )

        except smtplib.SMTPException as e:

            print(f"SMTP error occurred {str(e)}  Not sent to {name}, {email}")


