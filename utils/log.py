class LogLevel:
    SUCCESS = '\033[92m[+]\033[0m'
    INFO = '\033[94m[*]\033[0m'
    WARN = '\033[93m[!]\033[0m'
    ERROR = '\033[91m[-]\033[0m'

class Logger:
    def success(self, msg, *args, **kwargs):
        if args or kwargs:
            formatted_msg = msg % args if args else msg.format(**kwargs)
        else:
            formatted_msg = msg
        print(f"{LogLevel.SUCCESS} {formatted_msg}")

    def info(self, msg, *args, **kwargs):
        if args or kwargs:
            formatted_msg = msg % args if args else msg.format(**kwargs)
        else:
            formatted_msg = msg
        print(f"{LogLevel.INFO} {formatted_msg}")

    def warn(self, msg, *args, **kwargs):
        if args or kwargs:
            formatted_msg = msg % args if args else msg.format(**kwargs)
        else:
            formatted_msg = msg
        print(f"{LogLevel.WARN} {formatted_msg}")

    def error(self, msg, *args, **kwargs):
        if args or kwargs:
            formatted_msg = msg % args if args else msg.format(**kwargs)
        else:
            formatted_msg = msg
        print(f"{LogLevel.ERROR} {formatted_msg}")

log = Logger()