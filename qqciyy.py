import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
import jieba
import matplotlib.pyplot as plt
from scipy.misc import imread

newtext = []
# 打开E盘下的聊天记录文件tong.txt
for word in open('E:\\tong.txt', 'r', encoding='utf-8'):
    tmp = word[0:4]
    if (tmp == "2018" or tmp == "====" or tmp == "2019" or tmp == "2020"):  # 过滤掉聊天记录的时间和qq名称
        continue
    tmp = word[0:2]
    if (tmp[0] == '[' or tmp[0] == '/'or tmp[0] == '@'):  # 过滤掉图片和表情，例如[图片]，/滑稽
        continue
    newtext.append(word)
# 将过滤掉图片和表情和时间信息和qq名称剩下的文字重新写入E盘下的tong1.txt文件中去
with open('E:\\tong1.txt', 'w', encoding='utf-8') as f:
    for i in newtext:
        f.write(i)
 # 打开新生成的聊天记录文件
text = open('E:\\tong1.txt', 'r', encoding='utf-8').read()
word_jieba = jieba.cut(text, cut_all=True)
word_split = " ".join(word_jieba)

text = open("E:\\tong1.txt","rb").read()
#结巴分词
wordlist = jieba.cut(text,cut_all=True)
wl = " ".join(wordlist)

bg_pic =imread('E:\\background.png') 
 
#设置词云
wc = WordCloud(background_color = "White", #设置背景颜色
               mask=bg_pic,
               scale=1.5,
               width=1000,height=600,
               max_words = 2000, #设置最大显示的字数
               font_path='C:/Windows/Fonts/simhei.ttf',
               max_font_size = 80,
               stopwords={'表情','糊脸','拍桌','拍头','撤回','一条'}
    )

imColor = ImageColorGenerator(bg_pic)  
myword = wc.generate(wl)#生成词云
 
#展示词云图
plt.imshow(wc.recolor(color_func=imColor))
plt.axis("off")
plt.figure()
wc.to_file('E:\\tong.jpg') 