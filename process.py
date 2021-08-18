import re
import muban


def get_content(path):
    f = open(path, encoding='utf-8')
    text = []
    i = 0
    for line in f.readlines():
        text.append(line)
    return text


def htmlFormat(book):
    fmt_1a = ''
    fmt_1b = ''
    return book


def save(book):

    # book 格式化
    book = htmlFormat(book)
    # 与模板合并
    # 存储规则
    pass


def splitText(text):

    book = ''
    for line in text:
        if not re.search(r'', line):
            book += line
        else:
            save(book)
            book = ''


def main():
    # 定义项
    path = 'D:\\dev\\bible_sudu\\data.txt'

    # 获取文本存入列表
    text = get_content(path)

    # 切割文本放入模板
    splitText(text)


main()
