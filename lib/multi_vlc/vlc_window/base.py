import logging

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from multi_vlc.qobjects.settings import settings
from multi_vlc.qobjects.time_status_bar import TimeStatusBar
from multi_vlc.qobjects.widget.model_count import ModelCountWidget
from multi_vlc.ui.ui_vlc import Ui_VlcMainWindow
from multi_vlc.vlc_model import VlcModel
from pyqt_settings.action import SettingDialogAction
from pyqt_utils.slot_decorator import SlotDecorator

logger = logging.getLogger(__name__)


class BaseWindow(QMainWindow, Ui_VlcMainWindow,
                 metaclass=SlotDecorator):

    def __init__(self, *args):
        super().__init__(*args)
        self.setupUi(self)
        self.retranslateUi(self)

        self.menuBar().addAction(SettingDialogAction(
            settings, icon=QIcon(), parent=self.menuBar()))

        self.model = VlcModel(self)
        self.model.dirtyChanged.connect(self.setWindowModified)
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(VlcModel.COL_FILES, 400)
        self.tableView.selectionModel().selectionChanged.connect(self._showSelectedCount)

        sb = TimeStatusBar(self)
        sb.addPermanentWidget(ModelCountWidget(self.model))
        self.setStatusBar(sb)

        self.__basePostInit = False
        self.__post_init__()
        assert self.__basePostInit, "You need to call 'super().__post_init__()'"

    def __post_init__(self):
        self.__basePostInit = True

    def _showSelectedCount(self):
        rows = len(self.tableView.selectionModel().selectedRows())
        self.statusBar().showMessage(f"Selected {rows} rows")
