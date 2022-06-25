# discord token
# use https://pcstrike.com/how-to-get-discord-token/ to get your discord token
TOKEN = "NTk0MDc4NzQ1NjE5NTk1MjY0.GrkCX_.OtzID81jcnt6Jnpl6L49A72dBSBeDHt7Tody7M"

# dict from process name to tuple of status and emoji
PROCESS = {
    "pycharm.sh": ("I'm working pydudes", "👨‍💻"),
    "metaeditor64.ex": ("I'm working dudes. MQL SUCKS!", "🤑"),
}

# daily quotes list
QUOTES = [
    "“We Make The World What It Is, By What We Do. All Of Us.” – Iron Mike",
    "“So Get Up. Dust Yourself Off. Try Again.” – Deacon",
    "“Do You Know Why We Keep Going? Because What The Hell Else Are We Gonna Do?” – Deacon",
    "There is nothing permanent, except change.",
    "Careful, he's American. The metric system makes him angry.",
    "When you deal with the best, you die like the rest!",
    "If Mama ain't happy, nobody happy! So you'd better make Mama happy!",
    "I don't know how I'm gonna fix this, but I'm sure as hell gonna try. - Kyle Crane",
    "“Dreams have a nasty habit of going bad when you’re not looking.” – Max Payne",
    "“Did I ever tell you the definition of insanity?” – Far Cry 3",
    "“Waka Waka Waka” – Pacman",
    "“The cake is a lie” – Portal",
    "RUOK?",
]

# maximum number of allowed error
MAX_ERROR = 10


URL = "https://discord.com/api/v9/users/@me/settings"

HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "authorization": TOKEN,
    "content-type": "application/json",
    "origin": "https://discord.com",
    "referer": "https://discord.com/channels/@me",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "cache-control": "no-cache",
}
