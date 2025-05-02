import requests
from requests.auth import HTTPBasicAuth

razor_pay_credentials_dict = {
    'RAZOR_PAY_KEY_ID': 'rzp_live_k9VzCZ3QDoLFVG',
    'RAZOR_PAY_KEY_SECRET': '8LBAMU8pxZTw2NYn1ssbyJEz',
    'RAZOR_PAY_API_BASE_URL': 'https://api.razorpay.com/v1',
    'RAZOR_PAY_WEBHOOK_SECRET': 'hIQiGhb0eBYFtKzrnjndmfMgVECgKhUy',
    'RAZOR_PAY_ACCOUNT_NUMBER': '4564560568203166',
}
create_contact_payload = {
    "name": "Akash Kumar",
    "email": "test@example.com",
    "contact": "9984698008",
    "type": "vendor",
    "reference_id": "1234",
    "notes": {
        "note_key": "Beam me up Scotty Updated"
    }
}


def _razor_pay_auth():
    return HTTPBasicAuth(
        username=razor_pay_credentials_dict["RAZOR_PAY_KEY_ID"],
        password=razor_pay_credentials_dict["RAZOR_PAY_KEY_SECRET"]
    )


def create_contact(cc_payload):
    response = requests.post(
        'https://api.razorpay.com/v1/contacts',
        json=cc_payload,
        auth=_razor_pay_auth()
    )
    return response


resp_create_contact = create_contact(create_contact_payload)
print("creating_contact :- ", create_contact(create_contact_payload).json())
c_id = resp_create_contact.json()["id"]

print(c_id)

funds_account = {
    "contact_id": c_id,
    "account_type": "bank_account",
    "bank_account": {
        "name": "Akash Kumar",
        "ifsc": "SBIN0011179",
        "account_number": "32876387119"
    }
}


def create_fund_accounts(cc_payload):
    response = requests.post(
        'https://api.razorpay.com/v1/fund_accounts',
        json=cc_payload,
        auth=_razor_pay_auth()
    )
    return response


resp_fund_accounts = create_fund_accounts(funds_account)
print("Creating_fund_accounts :- ", resp_fund_accounts.json())
f_id = resp_fund_accounts.json()["id"]
print(f_id)

# validating back accounts

validation_account = {
    "account_number": razor_pay_credentials_dict['RAZOR_PAY_ACCOUNT_NUMBER'],
    "fund_account": {
        "id": f_id
    },
    "amount": 200,
    "currency": "INR",
    "notes": {
        "random_key_1": "Make it so.",
        "random_key_2": "Tea. Earl Grey. Hot."
    }
}


def fund_accounts_validation(cc_payload):
    print("cc_payload", cc_payload)
    response = requests.post(
        'https://api.razorpay.com/v1/fund_accounts/validations',
        json=cc_payload,
        auth=_razor_pay_auth()
    )
    return response


def validate_accounts(name):
    resp_fund_accounts_validation = fund_accounts_validation(validation_account)
    print("Validating fund Accounts :- ", resp_fund_accounts_validation.json())
    return "TT"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    validate_accounts("Validation")
