#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import uuid
from os import getenv


class Logger:
    """Class to do log."""

    def __init__(self, name: str, logname: str, logpath: str = None, level=logging.DEBUG) -> None:
        """Object constructor.

        Args:
            name (str): Logger name.
            logname (str): Logfile name.
            logpath (str, optional): Log path. Defaults to None.
            level (object, optional): Logging level. Defaults to logging.DEBUG.
        """
        self._name = name
        self._logname = logname
        self._logpath = logpath if logpath is not None else getenv("LOGS_PATH", "default_path")
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
        logpath = os.path.join(self._logpath, self._logname)

        # avoid defining multiple handlers that will causes in duplicate logs
        if not logger.handlers:
            # define format
            formatter = logging.Formatter(
                f"%(asctime)s,%(msecs)d %(levelname)s {uuid.uuid4().hex} "
                f"{self._name}:%(lineno)d :%(funcName)s %(message)s"
            )

            # define file handler to the specified logpath
            file_handler = logging.FileHandler(logpath)
            file_handler.setFormatter(formatter)

            # set logging level and add file handler
            logger.addHandler(file_handler)
            logger.setLevel(self._level)

        return logger
