import json
import os
import threading
import urllib.request


# 图片类
class image:
    def __init__(self, article_name, image_url):
        # 图片链接
        self.image_url = image_url
        self.image_name = os.path.basename(image_url).split(".")[0]
        # 图片下载失败原因
        self.error_reason = None
        self.article_name = article_name


download_error_list = []


def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__)


# 开始下载
def start_download_pic(pic_path, images):
    for img in images:
        image_path = build_pic_name(pic_path, img)
        # 已存在则不重复下载
        if os.path.exists(image_path):
            print('article name:' + img.article_name)
            print('pic has existed:' + img.image_url)
            img.error_reason = "pic has existed:"
            download_pic_callback(img)
            return

        # 图片链接前缀不包含http
        if not img.image_url.startswith("https"):
            print('article name:' + img.article_name)
            print('pic has invalid url:' + img.image_url)
            img.error_reason = "pic has invalid url"
            download_pic_callback(img)
            return

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
            'Cookie': 'AspxAutoDetectCookieSupport=1',
        }

        # 下载图片
        request = urllib.request.Request(img.image_url, None, header)
        try:
            response = urllib.request.urlopen(request, timeout=10)
        # 下载失败
        except Exception as error:
            print('pic cannot download:' + img.image_url)
            img.error_reason = str(error)
            download_pic_callback(img)
            return

        # 保存图片
        try:
            fp = open(image_path, 'wb')
            fp.write(response.read())
            fp.close()
        # 保存失败
        except IOError as error:
            print(error)
            img.error_reason = str(error)
            download_pic_callback(img)
            return

        # 下载完成回调
        download_pic_callback(img)


# 组装图片名字
def build_pic_name(pic_path, img):
    # 剪去图片链接后的参数
    pic_url = os.path.basename(img.image_url)

    # 获取图片格式后缀 如果没有 默认jpg
    urls = pic_url.split(".")
    if len(urls) > 1:
        pic_type = urls[len(urls) - 1]
    else:
        pic_type = "jpg"

    # 组装图片命名
    pic_name = img.image_name + "." + pic_type

    pic_path = os.path.join(pic_path, pic_name)
    return pic_path


# 下载图片完成后的回调函数
def download_pic_callback(img):
    thread_lock = threading.Lock()
    # 获取线程锁
    thread_lock.acquire()
    # 如果下载失败 则保存到失败列表
    if img.error_reason is not None and len(img.error_reason) > 0:
        download_error_list.append(img)

    # 释放锁
    thread_lock.release()

def start_replace_pic(pic_path, images):
    for img in images:
        image_path = build_pic_name(pic_path, img)
        # 已存在则不重复下载
        if os.path.exists(image_path):
            print('article name:' + img.article_name)
            print('pic has existed:' + img.image_url)
            img.error_reason = "pic has existed:"
            download_pic_callback(img)
            return

        # 图片链接前缀不包含http
        if not img.image_url.startswith("https"):
            print('article name:' + img.article_name)
            print('pic has invalid url:' + img.image_url)
            img.error_reason = "pic has invalid url"
            download_pic_callback(img)
            return

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
            'Cookie': 'AspxAutoDetectCookieSupport=1',
        }

        # 下载图片
        request = urllib.request.Request(img.image_url, None, header)
        try:
            response = urllib.request.urlopen(request, timeout=10)
        # 下载失败
        except Exception as error:
            print('pic cannot download:' + img.image_url)
            img.error_reason = str(error)
            download_pic_callback(img)
            return

        # 保存图片
        try:
            fp = open(image_path, 'wb')
            fp.write(response.read())
            fp.close()
        # 保存失败
        except IOError as error:
            print(error)
            img.error_reason = str(error)
            download_pic_callback(img)
            return

        # 下载完成回调
        download_pic_callback(img)
