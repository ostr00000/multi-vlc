import logging
from pprint import pformat

import multi_vlc.managers
from multi_vlc.utils.dynamic_loader import loadClassFromPackage

logger = logging.getLogger(__name__)
# noinspection PyTypeChecker
classes = list(loadClassFromPackage(multi_vlc.managers))


class VlcWindow(*classes):
    pass


logger.debug(pformat(VlcWindow.mro()))