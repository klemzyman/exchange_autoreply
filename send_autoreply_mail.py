from exchangelib import DELEGATE, Account, Credentials, Message, HTMLBody, Configuration, NTLM
from exchangelib.queryset import Q
from datetime import datetime, timedelta
import pytz

# Uporabniško ime in geslo za prijavo v Exchange strežnik
username = "username"
password = "password"
credentials = Credentials(username, password)

# Konfiguracija strežnika
server = "mail.company.com"
config = Configuration(server=server, credentials=credentials, auth_type=NTLM)

# Poštni predal
mailbox = "user@company.com"

# Povezava z Exchange strežnikom
account = Account(primary_smtp_address=mailbox, config=config, autodiscover=False, access_type=DELEGATE)

# Preglej neprebana sporočila v zadnjih 20 minutah
timezone = pytz.timezone('Europe/Ljubljana')  # Adjust the timezone as needed
end_time = datetime.now(timezone)
start_time = end_time - timedelta(minutes=20)

# Pridobi vsa neprebana sporočila iz mape Prejeto, ki niso označena kategorijo 'replied'
inbox = account.inbox
unread_emails = inbox.filter(Q(is_read=False) & Q(datetime_received__gte=start_time) & ~Q(categories__contains='replied'))

email_addresses = set()

# Se sprehodi skozi vsa neprebana sporočila in doda naslove v seznam, sporočilo pa doda v kategorijo 'replied'
for email in unread_emails:
    email_addresses.add(email.sender.email_address)
    email.categories = ['replied']
    email.save()

# Vsem unikatnim naslovom pošlji odgovor
for email_address in email_addresses:    
    reply = Message(
        account=account,
        folder=inbox,
        subject="Zavrnjeno sporočilo",
        body=HTMLBody(f"Spoštovani!<br><br>Ta poštni naslov ni več aktiven. Prosimo, da vsa nadaljnja sporočila pošiljate na naslov <a href='mailto:racunovodstvo@ipf.si'>racunovodstvo@ipf.si</a>.<br><br>Lep pozdrav,<br>IPF, k.o."),
        to_recipients=[email_address]
    )
    reply.send()