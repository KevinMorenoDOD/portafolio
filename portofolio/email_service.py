import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def send_contact_email(name: str, email: str, message: str) -> dict:
    """
    Send an email from the contact form to the portfolio owner.

    Args:
        name: Sender's name
        email: Sender's email address
        message: The message content

    Returns:
        dict with 'success' (bool) and 'error' (str or None)
    """
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_password = os.getenv("SMTP_PASSWORD", "")
    recipient = os.getenv("RECIPIENT_EMAIL", "kevin.dev.dod@gmail.com")

    if not smtp_user or not smtp_password or smtp_password == "TU_APP_PASSWORD_AQUI":
        return {
            "success": False,
            "error": "El servicio de correo no está configurado. Configure SMTP_USER y SMTP_PASSWORD en el archivo .env",
        }

    # Build the email
    msg = MIMEMultipart()
    msg["From"] = f"{name} <{smtp_user}>"
    msg["To"] = recipient
    msg["Subject"] = f"Portfolio Contact: {name}"
    msg["Reply-To"] = email

    body = f"""
Nombre: {name}
Correo: {email}

Mensaje:
{message}
"""
    msg.attach(MIMEText(body, "plain", "utf-8"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port, timeout=15) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, recipient, msg.as_string())
        return {"success": True, "error": None}
    except smtplib.SMTPAuthenticationError:
        return {
            "success": False,
            "error": "Error de autenticación. Verifica tu App Password en .env",
        }
    except smtplib.SMTPException as e:
        return {"success": False, "error": f"Error SMTP: {str(e)}"}
    except Exception as e:
        return {"success": False, "error": f"Error al enviar: {str(e)}"}
