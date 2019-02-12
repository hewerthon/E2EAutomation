
import configparser


def read_config_data(section, key):
    """
    :param section:
    :param key:
    :return:
    """
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Config.cfg")
    return config.get(section, key)

def fetch_element_locators(section, key):
    """
    :param section:
    :param key:
    :return:
    """
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Elements.cfg")
    return config.get(section, key)
