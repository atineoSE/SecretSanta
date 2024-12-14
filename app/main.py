import logging
import sys

from app.email_client import EmailClient
from app.participants import exclusions, participants
from app.randomizer import get_pairs

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)

if __name__ == "__main__":
    email_client = EmailClient()
    logging.info(
        f"Getting pairs for {len(participants)} participants with {len(exclusions)} exclusions."
    )
    pairs = get_pairs(participants, exclusions)
    if not pairs:
        raise ValueError(
            "Could not find any matched pairs of giver-receiver. "
            + "Have you entered participants?"
        )

    logging.info(f"Sending emails to {len(pairs)} participants.")
    for giver_name, receiver_name in pairs.items():
        email_client.send_email(
            giver_name=giver_name,
            giver_email=participants[giver_name],
            receiver_name=receiver_name,
        )
    email_client.close()

    logging.info(
        f"SUCCESS: Secret Santa emails were sent to {len(pairs)} participants."
    )
