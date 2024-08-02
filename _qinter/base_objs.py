import dataclasses

from PySide6.QtWidgets import QWidget


@dataclasses.dataclass
class QTkWidgetWrapper():
  _inner: QWidget
