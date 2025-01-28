import time
import datetime

start_time = time.time()



def get_elapsed_time():
    elapsed_time = time.time() - start_time
    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    data = {
        "hours": int(hours),
        "minutes": int(minutes),
        "seconds": int(seconds)
    }
    return data


def get_time():
    now = datetime.datetime.now()
    return {"hours": now.hour, "minutes": now.minute, "seconds": now.second}