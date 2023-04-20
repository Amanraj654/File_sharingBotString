#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @
STRING_SESSION = os.environ.get("STRING_SESSION", "BQFyB34ACLmo_IMSCNqu0PettGOuwZmOGf7ENp552A0jmDEuUvppQ6Udz-M1acSifqb6JnlgOQrVqtc4yWzm7JzN7nD4rq7mz6nZb66P-89EsamC4LJfoz8Rpav0nJqXdk6YUQYDa7SLea9bWlvObkdHn9CNHCXONrGl2wietweL3Ht-UTqqf2T4B_XeVHdJD4zzNIU-Ttl6nsvD7n5DIpHGyRO-fSjA8DHIB_VgUVuUVFj4M3NsIrwk6WTHMnfu1k4x-F8N-JTItMdUO0Y0eQ2kg4GBXGzzZfRr7Zq_GJzjfo4iAiPldoCzKLr5HynLKPYkFUI_2yK46WMQ6-gOxV5JpdwtqAAAAAFyLQZFAQ")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24250238"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "cb3f118ce5553dc140127647edcf3720")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001151586439"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6175650047"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Rajkumar:Rajkumar654@cluster0.ay3mov2.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexjjot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5757528547").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
