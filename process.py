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
    textncode = ''
    swt = True
    for line in book:
        line = line.replace('\n', '')
        if re.search(r'^.[0-9].*?', line):
            if swt:
                line = '<p class="c"><a href="../index.html">' + \
                    line + '</a></p>' + '\n<hr />\n'
                textncode += line
                swt = False
            else:
                line = '<hr />\n<p class="c"><a href="../index.html">' + \
                    line + '</a></p>' + '\n<hr />\n'
                textncode += line
        elif len(line) <= 1:
            pass
        else:
            line = '<p>' + line + '</p>\n'
            textncode += line
    return textncode


def save(book, i):

    # book 格式化
    textncode = htmlFormat(book)
    # 与模板合并
    textncode = muban.header + textncode + muban.footer
    # 存储规则
    path = 'F:\\dvlp\\bibleshudu\\books\\' + str(i) + '.html'

    with open(path, 'w', encoding='utf-8') as f:
        f.write(textncode)

    exit()


def splitText(text):

    book = []
    i = 1
    for line in text:
        if not re.search(r'[0-9]. ', line):
            book.append(line)
        else:
            save(book, i)
            i += 1
            book = []


def main():
    # 定义项
    path = 'F:\\dvlp\\bibleshudu\\data.txt'

    # 获取文本存入列表
    text = get_content(path)

    # 切割文本放入模板
    splitText(text)


main()
