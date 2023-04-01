import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = "6144753157:AAHfsBvjQWdaOAI1My-6JVeB5zbdD9hWTXM"
    # The Telegram API things
    API_ID = 27885485
    API_HASH = "7dd9974c713787410beae4a295cc1e2d"
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 4097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    VIDEO_FORMATS = ["mp4", "mkv", "mov", "m4v", "avi", "unknown_video"]
    AUDIO_FORMATS = ["mp3", "flac", "m4a", "wav"]
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = 5663539940
    ADMINS = 5663539940
    SESSION_NAME = "URLUPLOADERBOT"
    # database uri (mongodb)
    DATABASE_URL = "mongodb+srv://sanmart02:sanmart02@uploader.qn5vziv.mongodb.net/?retryWrites=true&w=majority"
    DATABASE_NAME = "uploader"
    MAX_RESULTS = "50"
    #update channel
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL",)
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL",)
    #log channel
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
    
