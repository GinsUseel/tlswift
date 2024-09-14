try:
    from telethon.errors import *
except ImportError as e:
    error_name = str(e).split("'")[1]
    raise ImportError(f"ImportError: {error_name} not found in telethon.errors module")
    
__all__ = [name for name in globals() if 'Error' in name]