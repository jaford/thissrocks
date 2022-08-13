#!/usr/bin/env python
import logging
import logging.handlers

logger = logging.getLogger(__name__)

null_handler = logging.NullHandler(level=logging.NOTSET)

logger.addHandler(null_handler)

