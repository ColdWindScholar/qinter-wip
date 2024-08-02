qinter
======

This project acts as a small transition layer mapping trivial Tkinter APIs into their PySide6 equivalents.

The main purpose of this project is to help beginners to get start with simple GUI programming but without some of the Tkinter's defects, including (but not limited to): Poor performance, not-portable (for example, Haiku OS and Android), poor appearance and integration under modern desktop environments by default.

## TODO

### Symbol availability

- [x] tkinter
  - [x] Tk()
    - [x] geometry(...)
    - [x] title(...)
    - [x] mainloop()
  - [x] Label(text)
  - [x] Button(text, command)
  - [x] messagebox
    - [x] showinfo(title, message)
    - [x] showwarning(title, message)
    - [x] showerror(title, message)
- [x] _tkinter
- [x] ttk

### Supported layout method

- [x] .place(x=..., y=...)


## License

[GLWTPL](LICENSE.txt)
