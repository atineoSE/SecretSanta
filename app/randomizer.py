import logging
import random


def get_pairs(participants, exclusions):
    pairs = {}
    assigned_participants = []
    for giver in participants:
        excluded = [e.strip() for e in exclusions.get(giver, "").split(",")]
        eligible_receivers = [
            receiver
            for receiver in participants
            if receiver not in [giver] + assigned_participants + excluded
        ]
        try:
            receiver = random.choice(eligible_receivers)
            pairs[giver] = receiver
            assigned_participants.append(receiver)
        except IndexError as exc:
            logging.error(
                "Could not find matching pairs. Try again or reduce number of exclusions."
            )
            raise exc

    return pairs
