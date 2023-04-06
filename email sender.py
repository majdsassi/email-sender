from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = 'HNE T7OT EL KEY ELI 5THITOU FIL API SECTION'

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
subject = "hne subject "
html_content = "<html><body><h1hne tekteb el email t7eb tab3thou </h1></body></html>"
sender = {"name":"hne el name eli t7ebou yodher ","email":"hne t7ot el mail eli t7b yodher 3la asses b3thet meno"}
to = [{"email":"hne el bch tb3thlou el mail","name":"hne esmou"}]
headers = {"Some-Custom-Name":"unique-id-1234"}
params = {"parameter":"My param value","subject":"devoir"}
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, headers=headers, html_content=html_content, sender=sender, subject=subject)

try:
    api_response = api_instance.send_transac_email(send_smtp_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
