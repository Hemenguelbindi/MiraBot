from datetime import datetime

def create_error_message(err: Exception) -> str:
    return f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}||{err.__class__}||{err}"