from typing import Optional

from qinter.base_objs import QTkWidgetWrapper


class QTkWidgetBase(QTkWidgetWrapper):
    def place(self,
              x: Optional[int] = None,
              y: Optional[int] = None):
        # FIXME: implement other methods
        if x is None:
            x = 0
        if y is None:
            y = 0
        geometry = self._inner.geometry()
        geometry.moveTo(x, y)
        self._inner.setGeometry(geometry)
        self._inner.show()
