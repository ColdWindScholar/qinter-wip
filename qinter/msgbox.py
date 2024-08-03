from PySide6.QtWidgets import QMessageBox

_R_OK = 'ok'


def _showxxx_func(fn):
    def inner(title: str = '',
              message: str = '') -> str:
        fn(None, title, message)
        return _R_OK

    return inner


showinfo_impl = _showxxx_func(QMessageBox.information)
showwarning_impl = _showxxx_func(QMessageBox.warning)
showerror_impl = _showxxx_func(QMessageBox.critical)
