from typing import Optional, Callable

from PySide6.QtWidgets import QPushButton

from _qinter.widget import QTkWidgetBase


class ButtonImpl(QTkWidgetBase):
  _CB_TYPE = Callable[[], None]

  def __init__(self,
               parent: QTkWidgetBase,
               text: str = '',
               command: Optional[_CB_TYPE] = None):
    inner = QPushButton(parent._inner)
    inner.setText(text)

    if command:
      inner.clicked.connect(command)

    QTkWidgetBase.__init__(self, inner)
