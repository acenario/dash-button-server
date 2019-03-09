class ConsoleColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[36m'
    OKGREEN = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    MAGENTA = '\033[35m'

    @staticmethod
    def get_question_string(str_input):
        return ConsoleColors.OKBLUE + str_input + ConsoleColors.ENDC

    @staticmethod
    def get_ok_string(str_input):
        return ConsoleColors.OKGREEN + str_input + ConsoleColors.ENDC

    @staticmethod
    def get_fail_string(str_input):
        return ConsoleColors.FAIL + str_input + ConsoleColors.ENDC

    @staticmethod
    def get_bold_string(str_input):
        return ConsoleColors.BOLD + str_input + ConsoleColors.ENDC

    @staticmethod
    def get_underline_string(str_input):
        return ConsoleColors.UNDERLINE + str_input + ConsoleColors.ENDC

    @staticmethod
    def get_info_string(str_input):
        return ConsoleColors.MAGENTA + str_input + ConsoleColors.ENDC