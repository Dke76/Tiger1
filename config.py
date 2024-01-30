import os

API_ID = API_ID = 20319884

API_HASH = os.environ.get("API_HASH", "637e3ba6357aa3ba2f3bf5742e0fd066")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6739364046:AAEgyFVJ5DUzWEDJKOD90oHPtjqksjGFhZ8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6913130519))

LOG = -1002127021404

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


