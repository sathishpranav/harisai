
import logging

class LoG:
    @staticmethod
    def log_gen():

        # logging.basicConfig(filename="C://Users//rohit//PycharmProjects//nopcommerce//Log//auto_log.log",
        #               format='%(asctime)s: %(levelname)s:%(message)s',
        #               datefmt='%m%d%Y %I:%M:%S $p',
        #               )
        # getLogger() method takes the test case name as input
        Logger_object = logging.getLogger(__name__)
        # FileHandler() method takes location and path of log file
        fhandler = logging.FileHandler(filename="C:\\Users\\rohit\\PycharmProjects\\NOPCOM\\Logs\\auto_logs.log", mode='a')
        # Formatter() method takes care of the log file formatting
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        # addHandler() method takes fileHandler object as parameter
        Logger_object.addHandler(fhandler)
        # setting the logger level
        Logger_object.setLevel(logging.DEBUG)
        return Logger_object



