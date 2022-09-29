import re
from  fractions import Fraction
class calculation:
    originfile = "",
    write_file = "",
    current_text = ""
    def __init__(self):
        self.originfile = open("./file_box/exercises.txt", 'r', encoding='utf-8')
        self.write_file = open("./file_box/answerfile.txt",'w',encoding='utf-8')

    # 将当行表达式处理
    def dealwith_singleline(self):
        # 处理带分数
         while self.read_file() == 1:
            self.exchange_fraction()
            self.update_to_fraction()
            self.use_eval()
         self.originfile.close()
         self.write_file.close()

    #将分数转为Fraction()
    def update_to_fraction(self):
        i = 0
        str = []

        str = re.findall(r"(\d+)\s*[/](\d+)",self.current_text)
        if len(str) == 0:
            return 1
        while i<len(str):
            str1 = ""
            fenzi = int(str[i][0])
            fenmu = int(str[i][1])
            str1 = '{}{}'.format(str1,"Fraction(")
            str1 = '{}{}'.format(str1, fenzi)
            str1 = '{}{}'.format(str1, ",")
            str1 = '{}{}'.format(str1, fenmu)
            str1 = '{}{}'.format(str1, ")")
            yuanbiaodashi = str[i][0]+"/"+str[i][1]
            self.current_text = self.current_text.replace(yuanbiaodashi,str1)
            i += 1
            # print(self.current_text)

    # 将带分数转化为假分数，用于eval计算
    def exchange_fraction(self):
        i = 0
        str = []
        # 单个带分数
        yuanbiaodashi = ""
        # str2列表存放每一个变化后的假分数
        str2 = []
        number = 0
        # 匹配到所有带分数 形如 [('10','81','10'),('3','1','3')]
        # print(self.current_text)
        str = re.findall(r"(\d+)\s*[\'](\d+)\s*[/](\d+)",self.current_text)
        # print(len(str))
        # 不存在带分数，直接结束接下来的工作
        if len(str) == 0 :
            return 1
        while i< len(str):
            # print(1)
            str1 = ""
            # 分子与分母
            fenzi = int(str[i][0])*int(str[i][2])+int(str[i][1])
            fenmu = int(str[i][2])
            # 单个带分数
            yuanbiaodashi = str[i][0]+"'"+str[i][1]+"/"+str[i][2]
            str1  = '{}{}'.format(str1,fenzi)
            str1 += '/'
            str1 = '{}{}'.format(str1, fenmu)
            # str2列表存放每一个变化后的假分数
            str2.append(str1)
            # 将当前表达式转化成功
            self.current_text = self.current_text.replace(yuanbiaodashi,str2[i])
            i += 1


    def use_eval(self):
        f = Fraction()
        print(self.current_text)
        print()
        x = eval(self.current_text)
        # 将浮点数转为负数存入答案中，分母为100
        if type(x) == float:
            print(1)
            f = Fraction(*x.as_integer_ratio())
            f = f.limit_denominator(100)
            self.write_file.write(str(f)+"\n")
        else:
            self.write_file.write(str(x)+"\n")
    # 读取单行文件表达式
    def read_file(self):
        self.current_text = self.originfile.readline()
        if self.current_text == "":
            return 0
        else: return 1