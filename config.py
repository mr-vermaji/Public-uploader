import os

# ✅ Required API credentials (replace default values or use environment variables)
API_ID = int(os.environ.get("API_ID", "28947698"))  # Replace 123456 with your real API ID
API_HASH = os.environ.get("API_HASH", "181af3baf73a37c24a429ca08e3f34f8")  # Replace with your real API hash
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8181530454:AAHSFvK44JpTiniQXMrGcZTduCwauz_7BYs")  # Replace with your real bot token

# ✅ Optional: database or pass value
PASS_DB = int(os.environ.get("PASS_DB", "721"))  # Default is 721 if not set

# ✅ Owner Telegram ID
OWNER = int(os.environ.get("OWNER", "7035612796"))  # Replace with your Telegram user ID

# ✅ Log chat ID (for logging bot activities)
LOG = int(os.environ.get("LOG", "-1002586433753"))  # Replace with the group/channel/chat ID where logs should go

# ✅ Optional: update group ID (uncomment if used)
# UPDATE_GRP = int(os.environ.get("UPDATE_GRP", "-1002586433753"))

# ✅ Admins list (space-separated IDs in ENV or hardcoded here)
ADMINS = []
for x in os.environ.get("ADMINS", "7035612796").split():
    try:
        ADMINS.append(int(x))
    except ValueError:
        raise ValueError("Invalid admin ID in ADMINS environment variable.")

# ✅ Ensure OWNER is in the admins list
if OWNER not in ADMINS:
    ADMINS.append(OWNER)

# ✅ Optional: join link
join = os.environ.get("JOIN", "https://t.me/TgRawanExtractor")  # Replace with your real link

# ✅ Premium logs channel or group
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", LOG))  # Defaults to LOG if not set
