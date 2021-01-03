import configparser
config = configparser.RawConfigParser()
config.read("C:\\Users\\rohit\\PycharmProjects\\NOPCOM\\Configurations\\config.ini")

class Readconfig():
    @staticmethod
    def getAppURL():
        url =config.get('common info','baseURL')
        return url
    @staticmethod
    def getUseName():
        user =config.get('common info','username')
        return user
    @staticmethod
    def getPassWord():
        pwd =config.get('common info','password')
        return pwd

