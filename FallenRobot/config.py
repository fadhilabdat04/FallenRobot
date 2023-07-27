class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 12857763
    API_HASH = "7b71e8bca0d5e1c6d8383ae818d9ec8d"

    CASH_API_KEY = "AL76C2F5UYMOVZKP"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://kprfogjs:z1cQQkrgTItmMGBVBbNQIJ3HWhY8kFRT@arjuna.db.elephantsql.com/kprfogjs"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001749511943)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://fadhilubot:fadhil123@cluster0.dxhbmhf.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph//file/8fffe9f061a0bd1fe1c3f.jpg"

    SUPPORT_CHAT = "SiArabSupport"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6031007486:AAFMxypvl32GLsci2OWJwleD1jfvlAPg9Ig"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "6I666ZYMGRHX"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1345594412  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [1345594412]  # User id of sudo users
    DEV_USERS = [1345594412]  # User id of dev users
    DEMONS = [1345594412]  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = [1345594412]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
