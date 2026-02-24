# Time handling for word counter
from datetime import datetime

def get_current_iso_time():
    #Returns current time in ISO format
    return datetime.now().isoformat()

