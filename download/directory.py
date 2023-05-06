import os
import os.path


def find_sub_path(path):
    # 初始化一个空的文章列表
    article_list = []
    if os.path.isfile(path):
        article_list.append(path)
    else:
        # 获取该文件夹下的所以子文件
        temp_files = os.listdir(path)
        # 遍历子文件
        for temp_file in temp_files:
            # 拼接该文件绝对路径
            full_path = os.path.join(path, temp_file)

            # 匹配.md文件
            if os.path.isfile(full_path) and os.path.splitext(full_path)[1] == ".md":
                # 如果是.md文件 加入文章列表
                article_list.append(full_path)
            # 如果是文件夹 进行递归继续搜索
            elif os.path.isdir(full_path):
                # 将子文件夹中的文章列表拼接到上级目录的文章列表中
                article_list.extend(find_sub_path(full_path))
    return article_list
