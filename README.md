# Secret Santa python app

Send private Secret Santa emails, assigning a random friend to give a present to.

Benefits:
* 😤 Fully private: No more sharing your friends' emails with dodgy websites.
* 💆‍♀️ Simple and lightweight: No need for configuring email servers or dedicated hosting.
* 😎 Reuse your Gmail account: Emails are sent from your Gmail account, so no suspicious-looking senders.

## What is Secret Santa?

As described on [Wikipedia](https://en.wikipedia.org/wiki/Secret_Santa):

> Secret Santa is a Western Christmas or Saint Nicholas tradition in which members of a group or community are randomly assigned a person to whom they give a gift. The identity of the gift giver is to remain a secret and should not be revealed.

You can use the Secret Santa python app to calculate random pairs of givers and receivers among the list of participants, making sure that everyone gets a present without knowing who the giver is.

An email will be sent to each individual participant, so that they know who they have to get a present for.

There are free apps that do this but they require that you hand over your friends' emails and names for data harvesting purposes 😵

The Secret Santa python app runs on your computer and is therefore fully private. You won't be giving away your personal details, nor those from your friends.

## How does the Secret Santa python app actually work?

Say we have 5 friends, Bob, Sally, Scott, Jess and Oliver, and they want to play Secret Santa.

We can enter their names and emails like so (full details below):
```
participants = {
    "Bob": "bob@dummy.com",
    "Sally": "sally@dummy.com",
    "Scott": "scott@dummy.com",
    "Jess": "jess@dummy.com",
    "Oliver": "oliver@dummy.com"
}
```

We can even consider some exclusions. Say that Bob and Sally live together and it's difficult for them to get presents for each other without the other one noticing. In that case, we'd want Bob and Sally to have other friends to give presents to instead. We can capture that through the following exclusions:
```
exclusions = {
    "Bob": "Sally",
    "Sally": "Bob"
}
```

With this information, we can run the Secret Santa python app, which could come up with the following pairing:
```
Bob should give a present to Scott.
Sally should give a present to Jess.
Scott should give a present to Bob.
Jess should give a present to Oliver.
Oliver should give a present to Sally.
```

The app will send an email to each individual person, letting them know who they should get a present for, without disclosing any further pairing information.

## Sending emails via your Gmail account

The Secret Santa python app works by sending emails on behalf of an existing Gmail user. This means you don't need to set up any email server. You just need to do a simple configuration, and emails will be sent as if you had sent them through your own Gmail account.

You don't need to see the emails though, so it can all happen without anyone knowing what the random pairs are.

A log will be created in your computer with the pairs, in case you need to audit the process at some point.

## How to use the Secret Santa python app

1. Clone this repo.
1. Install dependencies with `pip install -r requirements.txt` (a [virtual environment](https://virtualenv.pypa.io/en/latest/) is recommended).
1. Add your Google account details in the environment: `ADMIN_USER` and `APP_PASSWORD`. You can use a `.env` file at the root directory for convenience.
    - `ADMIN_USER` is your Google account username. Emails will be sent as if written by this user.
    - `APP_PASSWORD` is your app-specific password. See instructions below on how to get your own app password.
1. Add your desired language to the environment variable `LANG`. Only "ES" (for Spanish) and "EN" (for English) are supported. Default is "ES".
1. Customize the email template at `app/email_templates.py`, if needed. This will be the format of the email sent to the participants.
1. Add participant names and emails in `app/participants.py`. Follow the example there. It is recommended that you copy and paste email addresses directly from your address book, to avoid typos.
1. Add exclusions in `app/participants.py`, if needed. An exclusion is a person or group of people that one participant should not have to give presents to. For instance, if we want Bob to be able to give presents to everyone except Anna or Scott, then we can add `"Bob": "Anna, Scott"` to the exclusions dictionary. If too many exclusions are given, it may not be possible to find matching pairs for all participants. If not all participants can be matched, an error will be raised. If that happens, try to reduce exclusions.
1. Run the app from the terminal with ``PYTHONPATH=`pwd` python app/main.py``

## Getting your app password

1. Go to the [app passwords page](https://myaccount.google.com/apppasswords) of your Google account (if you can't access it, refer to this [help page](https://support.google.com/accounts/answer/185833?hl=en) for support).
1. Choose a name and create a new password.
1. A new random password will be generated. Copy it to your environment as `APP_PASSWORD` (be sure to remove the spaces, if present).

It is recommended that you revoke the password after sending the emails, for added security. You can easily generate a new one if needed.

## How to audit the process

Every time you run the Secret Santa python app, a new log file will be generated in the `logs` directory. It will reveal who was assigned to whom and to what email the information was sent.

This is helpful if you need to audit the process, for instance if someone says they didn't get their email.

Don't look at this file if you are participating in the Secret Santa game yourself, or it will ruin the fun!

## How to test the Secret Santa python app

It is recommended that you do a test run first, to make sure that you got all names and email addresses right, and that you are happy with the email format and formulation.

You can trigger a test run against a test email by setting the `TEST_EMAIL` environment variable. All messages will be sent to the test email rather than to the real recipients' emails.

To perform a real run, just remove the `TEST_EMAIL` variable from the environment.

## Contributing

We welcome and encourage contributions 🫶 Before sending in any changes though, please, open an issue and let us discuss the fitness and scope of your proposal first.

Don't forget to go over the open issues. You may find one you'd be interested to solve!

Here some areas where we welcome contributions:
* improved email templates
* more languages
* streamlined configuration
* improved error handling
* additional email providers, as long as they can be configured without additional hosting or containerization or any other complex setup scenarios

The following points are out of scope for this project:
* making a UI to enter participants information
* integrating complex email solutions

## License

See the LICENSE file for license rights and limitations (GPL-3.0).
