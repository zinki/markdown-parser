import os
import re

import picture


# 查找图片
def find_pics(article_path):
    # 打开md文件
    f = open(article_path, 'rb')
    content = f.read().decode('UTF-8')
    pics = []

    # 匹配正则 match ![]()
    results = re.findall(r"!\[(.+?)\)", content)

    for result in results:
        temp_pic = result.split("](")
        # 将图片加入到图片数组当中
        if len(temp_pic) == 2:
            basename = os.path.basename(article_path)
            pic = picture.image(basename, temp_pic[1])
            pics.append(pic)
    f.close()
    return pics
