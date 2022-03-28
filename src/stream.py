import logging
from kiteconnect import KiteTicker
from dotenv import load_dotenv

import utils

# while starting up the streamer, make sure to load in the env files
load_dotenv()

# make sure the following envs exist
try:
    API_KEY = utils.read_env("API_KEY")
    ACCESS_TOKEN = utils.read_env("ACCESS_TOKEN")
except LookupError:
    print("Crucial Required Variables are missing. Please set them.")
    exit(1)

logging.basicConfig(level=logging.DEBUG)

# Initialise
kws = KiteTicker(API_KEY, ACCESS_TOKEN)


def on_ticks(ws, ticks):
    # Callback to receive ticks.
    logging.debug("Ticks: {}".format(ticks))


def on_connect(ws, response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    ws.subscribe([738561, 5633])

    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_FULL, [738561])


def on_close(ws, code, reason):
    # On connection close stop the main loop
    # Reconnection will not happen after executing `ws.stop()`
    ws.stop()


# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect()
