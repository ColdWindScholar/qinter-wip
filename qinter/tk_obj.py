from PySide6.QtWidgets import QApplication

from qinter.base_objs import QTkWidgetWrapper
from qinter.mainwindow import QTkMainWindowImpl


class TkImpl(QTkWidgetWrapper):
  def __init__(self):
    self._app = QApplication()
    self._root = QTkMainWindowImpl()

    QTkWidgetWrapper.__init__(self, self._root)

  def mainloop(self):
    self._app.exec()

  def geometry(self, s: str):
    self._root.geometry(s)

  def title(self, s: str):
    self._root.title(s)
