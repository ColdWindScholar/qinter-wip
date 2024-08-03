from PySide6.QtWidgets import QMainWindow

from qinter.utils import _unpack_tk_geometry


class QTkMainWindowImpl(QMainWindow):
  _DFLT_W = 200
  _DFLT_H = 200
  _DFLT_TITLE = 'tk'

  def __init__(self):
    QMainWindow.__init__(self)

    self.setWindowTitle(self._DFLT_TITLE)
    self.resize(self._DFLT_W, self._DFLT_H)
    self.show()

  def geometry(self, s: str):
    self.resize(*_unpack_tk_geometry(s))

  def title(self, s: str):
    self.setWindowTitle(s)
