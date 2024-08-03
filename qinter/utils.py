from qinter.exceptions import TclError


def _bad_geometry(s: str):
  return TclError(f'bad geometry specifier "{s}"')


def _unpack_tk_geometry(s: str) -> (int, int):
  v = s.split('x', 1)
  try:
    w = int(v[0])
    h = int(v[1])
  except (IndexError, ValueError) as e:
    raise _bad_geometry(s) from e
  if w < 0 or h < 0:
    raise _bad_geometry(s)
  return w, h
