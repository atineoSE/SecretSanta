import logging
import sys
from app.participants import participants, exclusions
from app.randomizer import get_pairs
from app.email_client import EmailClient

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)

if __name__ == "__main__":
    email_client = EmailClient()
    pairs = get_pairs(participants, exclusions)
    if not pairs:
        raise ValueError(
            "Could not find any matched pairs of giver-receiver. "
            + "Have you entered participants?"
        )
    for giver_name, receiver_name in pairs.items():
        email_client.send_email(
            giver_name=giver_name,
            giver_email=participants[giver_name],
            receiver_name=receiver_name,
        )
    email_client.close()
    logging.info(f"Sent Secret Santa emails to {len(pairs)} participants.")
