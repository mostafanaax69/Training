class Logger:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance
    
    def log(self, message, log_type='info'):
        if log_type == 'info':
            self._log_info(message)
        elif log_type == 'warning':
            self._log_warning(message)
        elif log_type == 'error':
            self._log_error(message)
        else:
            print(f"Invalid log type: {log_type}")

    def _log_info(self, message):
         print(f"[INFO] {message}")

    def _log_warning(self, message):
        print(f"[WARNING] {message}")

    def _log_error(self, message):
        print(f"[ERROR] {message}")





# Example usage:
logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)  # This should print True, indicating that there is only one instance of the logger

logger1.log("This is an information message.", log_type='info')
logger1.log("This is a warning message.", log_type='warning')
logger1.log("This is an error message.", log_type='error')
