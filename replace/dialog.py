from tkinter import *
from tkinter.ttk import Progressbar
from mdlib import directory, article, picture
import os
import re


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.progress = None
        self.path_entry = None
        self.source_url = None
        self.target_url = None
        self.quitButton = None
        self.alertButton = None
        self.createWidgets()

    def createWidgets(self):
        Label(self.master, text='进度：', font=12, width=10).grid(row=1, column=0, pady=10)
        self.progress = Progressbar(self.master, length=200, cursor='spider',
                                    mode="determinate", orient=HORIZONTAL)
        self.progress.grid(row=1, column=1, pady=10)
        # 创建并添加Entry,用于接受用户输入
        self.path_entry = Entry(self.master, font=16)
        self.path_entry.grid(row=2, column=1, padx=5, pady=10)
        Label(self.master, text='文档目录：', font=12, width=10).grid(row=2, column=0)

        # 创建并添加Entry,用于接受用户输入
        self.source_url = Entry(self.master, font=16)
        self.source_url.grid(row=3, column=1, padx=5, pady=10)
        # 创建并添加Label
        Label(self.master, text='原始URL：', font=12, width=10).grid(row=3, column=0)
        # 创建并添加Entry,用于接受用户输入
        self.target_url = Entry(self.master, font=16)
        self.target_url.grid(row=4, column=1, padx=5, pady=10)
        # 创建并添加Label
        Label(self.master, text='替换URL：', font=12, width=10).grid(row=4, column=0)

        self.alertButton = Button(self, text='确认', width=5, command=self.type_pic_path)
        self.alertButton.grid(row=6, column=0, padx=10)
        self.quitButton = Button(self, text="退出", width=5, command=self.quit)
        self.quitButton.grid(row=6, column=10)
        self.grid(columnspan=10, pady=10)
        self.source_url.insert(0, r"")
        self.target_url.insert(0, r"")
        self.path_entry.insert(0, r"")

    def quit(self):
        quit()

    def increment(self, rate):
        self.progress["value"] = rate
        self.master.update()

    def type_pic_path(self):
        if len(self.source_url.get()) == 0 or len(self.path_entry.get()) == 0:
            self.quit()
        print(self.source_url.get())
        print(self.path_entry.get())
        print(self.target_url.get())
        replace(self)
        self.quit()


def replace(self):
    sub_path = directory.find_sub_path(self.path_entry.get())
    if len(sub_path) > 0:
        index = 0
        for path in sub_path:
            with open(path, "r+", encoding="UTF-8") as f:
                # 读取文件内容
                content = f.read()
                # 替换内容
                content = re.sub(self.source_url.get(), self.target_url.get(), content)
                # 将指针移动到文件开头
                f.seek(0)
                # 清空文件
                f.truncate()
                # 将修改后的内容写入文件
                f.write(content)
                # 关闭文件
                f.close()
            index = index + 1
            per = index / len(sub_path) * 100
            self.increment(round(per))



