import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv

# Load environment variables from .env file (local development).
load_dotenv()

BREVO_API_URL = "https://api.brevo.com/v3/smtp/email"
DEFAULT_RECIPIENT = "kevin.dev.dod@gmail.com"


def _sender_email() -> str:
    """Email address the message is sent from (must be verified in Brevo)."""
    return (
        os.getenv("SENDER_EMAIL", "").strip()
        or os.getenv("SMTP_USER", "").strip()
    )


def _recipient_email() -> str:
    """Email address that receives the contact messages."""
    return os.getenv("RECIPIENT_EMAIL", "").strip() or DEFAULT_RECIPIENT


def _email_body(name: str, email: str, message: str) -> str:
    return f"Nombre: {name}\nCorreo: {email}\n\nMensaje:\n{message}\n"


def _send_via_brevo(name: str, email: str, message: str) -> dict:
    """
    Send the contact email through Brevo's HTTPS API.

    Render (free tier) blocks outbound SMTP ports (25/465/587), so email must be
    sent over HTTPS (port 443) using an API instead of SMTP.
    """
    import requests

    api_key = os.getenv("BREVO_API_KEY", "").strip()
    sender = _sender_email()
    recipient = _recipient_email()

    if not sender:
        return {
            "success": False,
            "error": "Falta configurar SENDER_EMAIL (remitente verificado en Brevo).",
        }

    payload = {
        "sender": {"name": "Portafolio | Kevin Moreno", "email": sender},
        "to": [{"email": recipient}],
        "replyTo": {"email": email, "name": name},
        "subject": f"Portafolio | Nuevo contacto de {name}",
        "textContent": _email_body(name, email, message),
    }

    try:
        response = requests.post(
            BREVO_API_URL,
            json=payload,
            headers={
                "accept": "application/json",
                "api-key": api_key,
                "content-type": "application/json",
            },
            timeout=20,
        )
    except requests.RequestException as exc:
        return {"success": False, "error": f"Error de red al enviar: {exc}"}

    if response.status_code in (200, 201, 202):
        return {"success": True, "error": None}

    return {
        "success": False,
        "error": f"Error de Brevo ({response.status_code}): {response.text[:200]}",
    }


def _send_via_smtp(name: str, email: str, message: str) -> dict:
    """Send the contact email via SMTP (works locally or on paid hosting)."""
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_password = os.getenv("SMTP_PASSWORD", "")
    recipient = _recipient_email()

    msg = MIMEMultipart()
    msg["From"] = f"{name} <{smtp_user}>"
    msg["To"] = recipient
    msg["Subject"] = f"Portfolio Contact: {name}"
    msg["Reply-To"] = email
    msg.attach(MIMEText(_email_body(name, email, message), "plain", "utf-8"))

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
    except smtplib.SMTPException as exc:
        return {"success": False, "error": f"Error SMTP: {exc}"}
    except Exception as exc:
        return {"success": False, "error": f"Error al enviar: {exc}"}


def send_contact_email(name: str, email: str, message: str) -> dict:
    """
    Send an email from the contact form to the portfolio owner.

    Uses Brevo's HTTPS API when BREVO_API_KEY is set (required on Render free
    tier, where SMTP ports are blocked), otherwise falls back to SMTP.

    Args:
        name: Sender's name
        email: Sender's email address
        message: The message content

    Returns:
        dict with 'success' (bool) and 'error' (str or None)
    """
    if os.getenv("BREVO_API_KEY", "").strip():
        return _send_via_brevo(name, email, message)

    smtp_user = os.getenv("SMTP_USER", "")
    smtp_password = os.getenv("SMTP_PASSWORD", "")
    if smtp_user and smtp_password and smtp_password != "TU_APP_PASSWORD_AQUI":
        return _send_via_smtp(name, email, message)

    return {
        "success": False,
        "error": (
            "El servicio de correo no está configurado. Configure BREVO_API_KEY "
            "(recomendado) o SMTP_USER y SMTP_PASSWORD en las variables de entorno."
        ),
    }
