import logging
def test_loggingDemo():
    #it will get any object for logging features
    logger=logging.getLogger(__name__) #__name__ it will capture your file name
    fileHandler = logging.FileHandler("logfile.log")

    formatHandler = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatHandler)

    logger.addHandler(fileHandler)  #filehandler object
    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happened")
    logger.critical("Critical issue")