import socket
from tkinter import Tk, Label, Entry, Button, Frame, Scrollbar, W, EW, E, Text, \
    DISABLED, Y, BOTH, NORMAL, END
from threading import Thread


class PortScanner():

    stop = False
    url = "google.com"
    start_port = 70
    end_port = 85

    def __init__(self, root):
        self.root = root
        self.create_gui()

    def on_scan_button_clicked(self):
        self.empty_console()
        self.scan_in_a_new_thread()

    def empty_console(self):
        self.console_text.config(state=NORMAL)
        self.console_text.delete("1.0", END)
        self.console_text.config(state=DISABLED)

    def scan_in_a_new_thread(self):
        url = self.host_entry.get()
        start_port = int(self.start_port_entry.get())
        end_port = int(self.end_port_entry.get())
        thread = Thread(target=self.start_scan,
                        args=(url, start_port, end_port))
        thread.start()
