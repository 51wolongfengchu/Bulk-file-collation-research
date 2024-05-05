import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import Listbox

# 定义一个函数来更新文件列表
def update_file_list(directory):
    # 清空当前的文件列表
    listbox_files.delete(0, tk.END)
    # 获取指定目录中的所有文件和文件夹
    try:
        file_list = os.listdir(directory)
    except FileNotFoundError:
        file_list = []
    # 将文件和文件夹添加到列表框中
    for file in file_list:
        listbox_files.insert(tk.END, file)

# 定义一个函数来组织文件
def organize_files():
    # 获取用户在GUI界面输入的源目录
    source_directory = entry_source.get()
    # 获取用户在GUI界面输入的目标目录，如果为空，则默认为目标目录为源目录
    target_directory = entry_target.get() or source_directory

    # 定义文件扩展名和对应的文件夹名称
    file_extensions = {
        '.pdf': 'PDF',
        '.ppt': 'PPT',
        '.pptx': 'PPT',
        '.doc': 'Word',
        '.docx': 'Word',
        '.xls': 'Excel',
        '.xlsx': 'Excel',
        '.png': '图片',
        '.jpg': '图片',
        '.jpeg': '图片',
        '.gif': '图片'
    }

    # 创建目标文件夹
    for folder in file_extensions.values():
        folder_path = os.path.join(target_directory, folder)  # 构建每个文件类型对应的文件夹路径
        if not os.path.exists(folder_path):  # 检查文件夹是否已经存在
            os.makedirs(folder_path)  # 如果不存在，则创建文件夹

    # 遍历源目录中的所有文件
    for filename in os.listdir(source_directory):
        file_extension = os.path.splitext(filename)[1]  # 获取文件的扩展名
        # 检查文件扩展名是否在定义的扩展名列表中
        if file_extension in file_extensions:
            # 获取对应的文件夹名称
            folder_name = file_extensions[file_extension]
            # 构建目标文件路径
            destination_folder = os.path.join(target_directory, folder_name)
            # 移动文件到目标文件夹
            shutil.move(os.path.join(source_directory, filename), destination_folder)

    # 弹出消息框显示整理完成的信息
    messagebox.showinfo("完成", "文件整理完成！")

# 创建主窗口
root = tk.Tk()
root.title("文件整理工具")  # 设置窗口标题

# 设置窗口大小
root.geometry("700x500")  # 设置窗口的宽度和高度

# 创建一个窗口来放置控件
window = tk.Frame(root)
window.pack()

# 添加标签和源目录输入框，设置背景颜色为浅绿色
label_source = tk.Label(window, text="源目录：")
label_source.pack()
entry_source = tk.Entry(window, width=50, bg="#90EE90")  # 设置bg参数为浅绿色
entry_source.pack()

# 添加按钮用于选择源目录
button_source = tk.Button(window, text="选择源目录", command=lambda: entry_source.insert(0, filedialog.askdirectory()))
button_source.pack()  # 将按钮添加到window窗口中

# 添加列表框用于显示文件目录
listbox_files = Listbox(window, height=10, width=50)
listbox_files.pack()

# 添加标签和目标目录输入框，设置背景颜色为浅绿色
label_target = tk.Label(window, text="目标目录:")
label_target.pack()
entry_target = tk.Entry(window, width=50, bg="#90EE90")  # 设置bg参数为浅绿色
entry_target.pack()

# 添加按钮用于选择目标目录
button_target = tk.Button(window, text="选择目标目录", command=lambda: entry_target.insert(0, filedialog.askdirectory()))
button_target.pack()  # 将按钮添加到window窗口中

# 添加整理文件按钮
button_organize = tk.Button(window, text="整理文件", command=organize_files)
button_organize.pack()  # 将按钮添加到window窗口中

# 添加按钮用于显示文件列表
button_show_files = tk.Button(window, text="显示文件列表", command=lambda: update_file_list(entry_source.get()))
button_show_files.pack()  # 将按钮添加到window窗口中

# 添加标签和搜索框，设置背景颜色为浅绿色
label_search = tk.Label(window, text="搜索文件:")
label_search.pack()
entry_search = tk.Entry(window, width=50, bg="#90EE90")  # 设置bg参数为浅绿色
entry_search.pack()



# 添加搜索并打开按钮
button_open_file = tk.Button(window, text="搜索并打开", command=lambda: open_file(entry_search.get(), entry_source.get()))
button_open_file.pack()


# 定义一个函数来搜索并打开文件
def open_file(search_term, directory):
    # 获取指定目录中的所有文件和文件夹
    try:
        file_list = os.listdir(directory)
    except FileNotFoundError:
        file_list = []

    # 遍历文件列表，查找包含搜索词的文件
    for file in file_list:
        if search_term.lower() in file.lower():
            # 构建文件的完整路径
            file_path = os.path.join(directory, file)
            # 打开文件
            os.startfile(file_path)
            return  # 如果找到了文件并成功打开，就返回

    # 如果没有找到文件，弹出消息框
    messagebox.showinfo("未找到", "没有找到包含搜索词的文件。")



# 运行主循环，显示GUI界面
root.mainloop()

