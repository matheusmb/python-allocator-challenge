import re

class NameValidator:
    @staticmethod
    def hasValidHostType(host_type):
        pattern = r"^[a-z]+$"
        return re.match(pattern, host_type) is not None

    @staticmethod
    def hasValidHostName(host_name):
        pattern = r"^[a-z]+[1-9]+[0-9]*"
        return re.match(pattern, host_name) is not None

    @staticmethod
    def parseTypeFrom(host_name):
        pattern = r"[a-z]+"
        return re.search(pattern, host_name).group()

    @staticmethod
    def parseIdFrom(host_name):
        pattern = r"\d+"
        id = re.search(pattern, host_name).group()
        return int(id)

    @staticmethod
    def parseTypeIdFrom(host_name):
        return NameValidator.parseTypeFrom(host_name), NameValidator.parseIdFrom(
            host_name
        )
