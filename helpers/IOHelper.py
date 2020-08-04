class IOHelper:
    @staticmethod
    def ask_yes_no(message):
        """
        Ask a yes/no question, default being no.
        :param message: The message to display.
        :return: True if input is case insensitive "y" or "yes" else False.
        """
        print(message, "[y/N]", end="")
        choice = input().lower()
        return choice in ["y", "yes"]
