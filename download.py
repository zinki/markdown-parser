import directory
import picture
import article
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.path_entry = None
        self.name_entry = None
        self.quitButton = None
        self.alertButton = None
        self.createWidgets()

    def createWidgets(self):
        # 创建并添加Label
        Label(self.master, text='文档根目录：', font=12, width=10).grid(row=1, column=0)
        # 创建并添加Entry,用于接受用户输入
        self.name_entry = Entry(self.master, font=16)
        self.name_entry.grid(row=1, column=1, padx=5, pady=10)
        # 创建并添加Label
        Label(self.master, text='图片路径：', font=12, width=10).grid(row=2, column=0)
        # 创建并添加Entry,用于接受用户输入
        self.path_entry = Entry(self.master, font=16)
        self.path_entry.grid(row=2, column=1, padx=5, pady=10)

        self.alertButton = Button(self, text='确认', width=5, command=self.type_pic_path)
        self.alertButton.grid(row=3, column=0, padx=10)
        self.quitButton = Button(self, text="退出", width=5, command=self.quit)
        self.quitButton.grid(row=3, column=10)
        self.grid(columnspan=10, pady=10)

    def type_pic_path(self):
        if len(self.name_entry.get()) == 0 or len(self.path_entry.get()) == 0:
            self.quit()
        print(self.name_entry.get())
        print(self.path_entry.get())
        sub_path = directory.find_sub_path(self.name_entry.get())
        if len(sub_path) <= 0:
            self.quit()
        for path in sub_path:
            pics = article.find_pics(path)
            if len(pics) > 0:
                picture.start_download_pic(self.path_entry.get(), pics)
        self.quit()

    def quit(self):
        quit()


def main():
    root = Tk()
    root.geometry('380x300')
    root.title("请输入图片保存位置")
    Application(root)
    root.mainloop()


main()
