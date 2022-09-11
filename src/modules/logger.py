#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import uuid
from os import getenv


class Logger(object):
    """Class to do log."""

    def __init__(
        self, name: str, logname: str, logpath: str = None, level=logging.DEBUG
    ) -> None:
        """Constructor method, sets class variables.

        Args:
            name (str): Logger name.
            logname (str): Logfile name.
            logpath (str, optional): Log path. Defaults to None.
            level (object, optional): Logging level. Defaults to logging.DEBUG.
        """
        self._name = name
        self._logname = logname
        self._logpath = logpath if logpath is not None else getenv("LOG_PATH")
        self._level = level

    def get_logger(self) -> object:
        """Define logger object and set handlers if not defined.

        Args:
            name (str): Logger name.
            logname (str): Logfile path.
            level (object, optional): Logging level. Defaults to logging.DEBUG.

        Returns:
            logging.logger: Logger instance.
        """
        # get logger for 'name'
        logger = logging.getLogger(self._name)
        logpath = self._logpath + self._logname

        # avoid defining multiple handlers that will causes in duplicate logs
        if not logger.handlers:
            # define format
            formatter = logging.Formatter(
                "%(asctime)s,%(msecs)d %(levelname)s {0} {1}:%(lineno)d :%(funcName)s \
                %(message)s".format(
                    uuid.uuid4().hex, self._name
                )
            )

            # define file handler to the specified logpath
            file_handler = logging.FileHandler(logpath)
            file_handler.setFormatter(formatter)

            # set logging level and add file handler
            logger.addHandler(file_handler)
            logger.setLevel(self._level)

        return logger
