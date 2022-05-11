#!/usr/bin/env python3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json

data={
    "user" : "edgar.hernandezga@uanl.edu.mx"
    "passw" : "Para que quiere saber eso"
}

def EnviarCorreo(message, receipents )
    with open("passw.json") as f:
        data = json.load(f)
    # create and setup the parameters of the message
    email_msg = MIMEMultipart()
    email_msg["From"] = data["user"]
    receipents
    email_msg["To"] = ", ".join(receipents)
    email_msg["Subject"] = "Este es un mensaje de prueba"

    # add in the message body
    email_msg.attach(MIMEText(message, "plain"))

    # create server
    server = smtplib.SMTP("smtp.office365.com:587")
    server.starttls()
    # Login Credentials for sending the mail
    server.login(data["user"], data["passw"])


    # send the message via the server.
    server.sendmail(email_msg["From"], receipents, email_msg.as_string())
    server.quit()
    print("successfully sent email to %s:" % (email_msg["To"]))

def main():

    ayudarinfo =    ("Script diseñado para tener distintas herramientas de seguridad"
                    "\n Remitentes que quieres que le lleguen el mensaje -r"
                    "\n El mensaje que quieres mandar -m")


    analizar = argparse.ArgumentParser(ayudarinfo)
    analizar.add_argument('-r', '--remitente', type=str, 
                            help="Remitentes quieres que le lleguen el mensaje")
    analizar.add_argument('-m', '--mensaje', type=str, 
                            help="El mensaje que quieres mandar")
    argumentos = analizar.parse_args()

    if argumentos.remitente is not None:
        EnviarCorreo(argumentos.mensaje, argumentos.remitente)

if __name__ == "__main__":
    main()
