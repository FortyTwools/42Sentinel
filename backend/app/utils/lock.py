import threading

user_locks = {}

def get_lock(user_id: int) -> threading.Lock:
    if user_id not in user_locks:
        user_locks[user_id] = threading.Lock()
    return user_locks[user_id]
