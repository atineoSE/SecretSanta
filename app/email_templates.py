import time

year = time.strftime("%Y", time.gmtime())

title_template_ES = f"El sorteo del amigo invisible de {year}"
body_template_ES = """
<html><head></head><body>
<style type="text/css"></style>
<p>Buenos d&iacute;as {giver_name}</p>
<p>Tu amigo/a invisible este a&ntilde;o es <b>{receiver_name}</b>.
<p>Este correo ha sido generado autom&aacute;ticamente.
Las respuestas no ser&aacute;n monitorizadas.
Si hay alg&uacute;n problema, contacta con {admin_email}.</p>
<p>-- La mano inocente</p>
</body></html>
"""

title_template_EN = f"Your Secret Santa draw for {year}"
body_template_EN = """
<html><head></head><body>
<style type="text/css"></style>
<p>Good day {giver_name}</p>
<p>You should get a present for <b>{receiver_name}</b>.
<p>This email has been generated automatically.
Replies won't be monitored.
If there is any problem, please reach out to {admin_email}.</p>
<p>-- The Hand of Fate</p>
</body></html>
"""


def get_template(lang, giver_name, receiver_name, admin_email):
    # Add more languages, as needed. For now, only ES for Spanish and EN for English are supported.
    if lang not in ["ES", "EN"]:
        raise ValueError(f"Language not supported. Got {lang} but expected ES or EN.")

    body_template = body_template_ES if lang == "ES" else body_template_EN
    title_template = title_template_ES if lang == "ES" else title_template_EN
    return (
        title_template,
        body_template.format(
            giver_name=giver_name, receiver_name=receiver_name, admin_email=admin_email
        ),
    )
