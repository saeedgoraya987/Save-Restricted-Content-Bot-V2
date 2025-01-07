# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24654535"))
API_HASH = getenv("API_HASH", "958dbfea3ee2f589e11a3d7c401d1a90")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6109365101").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://pegab42884:pegab42884@cluster0.0fgdr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002088316257")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002088316257"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "vnshortner.com")
AD_API = getenv("AD_API", "e1a6a5874210d8ef2ff3dddaf3dfa2c198e51771")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
