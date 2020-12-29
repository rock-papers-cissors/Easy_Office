from tkinter import *
import tkinter.filedialog
from mergePDF import mergePDF
import sys
import os

def main():
    root = Tk()
    root.title('Easy Office')
    root.geometry('450x450')

    filenames = []
    file_name_labels = []

    def on_add_file_button():
        filename = tkinter.filedialog.askopenfilename()
        filenames.append(filename)
        new_label = Label(root, text=filename, justify=LEFT, relief=GROOVE)
        new_label.grid(row=len(filenames)-1, column=2, columnspan=4, padx=10)
        file_name_labels.append(new_label)
        add_file_button.grid(row=len(filenames), column=3, columnspan=2, padx=10)
        merge_button.grid(row=len(filenames)+1, column=3, columnspan=2, padx=10)

    def on_merge_button():
        mergePDF(filenames)
        os.popen('evince merged.pdf')

    # add file button
    add_file_button = Button(root, text='添加文件', command=on_add_file_button)
    add_file_button.grid(row=0, column=3, columnspan=2,ipadx=10)

    merge_button = Button(root, text='合并文件', command=on_merge_button)
    merge_button.grid(row=1, column=3, columnspan=2, ipadx=10)
    root.mainloop()


if __name__ == '__main__':
    main()
