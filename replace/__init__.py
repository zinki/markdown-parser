from tkinter import *
import dialog


def main():
    root = Tk()
    root.geometry('380x300')
    root.title("请输入图片URL")
    dialog.Application(root)
    root.mainloop()


main()
