from PySide6.QtWidgets import QLabel

from qinter.widget import QTkWidgetBase


class LabelImpl(QTkWidgetBase):
  def __init__(self,
               parent: QTkWidgetBase,
               text: str = ''):
    inner = QLabel(parent._inner)
    inner.setText(text)

    QTkWidgetBase.__init__(self, inner)
