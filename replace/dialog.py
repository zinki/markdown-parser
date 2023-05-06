from tkinter import *
from tkinter.ttk import Progressbar
from download import picture
from download import directory
from download import article


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.progress = None
        self.path_entry = None
        self.name_entry = None
        self.quitButton = None
        self.alertButton = None
        self.createWidgets()

    def createWidgets(self):
        Label(self.master, text='进度：', font=12, width=10).grid(row=1, column=0, pady=10)
        self.progress = Progressbar(self.master, length=200, cursor='spider',
                                    mode="determinate", orient=HORIZONTAL)
        self.progress.grid(row=1, column=1, pady=10)
        # 创建并添加Label
        Label(self.master, text='文档目录：', font=12, width=10).grid(row=2, column=0)
        # 创建并添加Entry,用于接受用户输入
        self.name_entry = Entry(self.master, font=16)
        self.name_entry.grid(row=2, column=1, padx=5, pady=10)
        # 创建并添加Label
        Label(self.master, text='目标URL：', font=12, width=10).grid(row=3, column=0)
        # 创建并添加Entry,用于接受用户输入
        self.path_entry = Entry(self.master, font=16)
        self.path_entry.grid(row=3, column=1, padx=5, pady=10)

        self.alertButton = Button(self, text='确认', width=5, command=self.type_pic_path)
        self.alertButton.grid(row=5, column=0, padx=10)
        self.quitButton = Button(self, text="退出", width=5, command=self.quit)
        self.quitButton.grid(row=5, column=10)
        self.grid(columnspan=10, pady=10)
        self.name_entry.insert(0, r"")
        self.path_entry.insert(0, r"")

    def quit(self):
        quit()

    def increment(self, rate):
        self.progress["value"] = rate
        self.master.update()

    def type_pic_path(self):
        if len(self.name_entry.get()) == 0 or len(self.path_entry.get()) == 0:
            self.quit()
        print(self.name_entry.get())
        print(self.path_entry.get())
        replace(self)
        self.quit()


def replace(self):
    sub_path = directory.find_sub_path(self.name_entry.get())
    if len(sub_path) > 0:
        index = 0
        for path in sub_path:
            pics = article.find_pics(path)
            if len(pics) > 0:
                picture.start_replace_pic(self.path_entry.get(), pics)
            index = index + 1
            per = index / len(sub_path) * 100
            self.increment(round(per))



