import math
import random
class create_questions:
    # 生成个数
    question_count = 0
    # 范围
    boundary = 0
    # 生成自然数还是真分数，0代表自然数，1代表真分数
    nature_or_true = 0
    # 运算符的个数
    signal_opration_count = 0

    # 构造函数
    def __init__(self,question_count,boundary):
        self.question_count = question_count
        self.boundary = boundary

    #判断是生成自然数还是真分数
    def random_nature_or_true(self):
        # 随机生成0~1的数
        randnum = random.randint(0,1)
        # 赋值给实例对象的属性
        self.nature_or_true = randnum

    # 生成操作符的数量
    def random_opration_count(self):
        # 随机生成0~3的数
        randnum = random.randint(0,3)
        print(randnum)
        self.signal_opration_count = randnum

    # 生成一个表达式
    def create_single_question(self):
        # 获得操作数
        self.random_opration_count()
        str = ""
        i = 0
        while i<=self.signal_opration_count:
            # 获得是生成自然数还是操作数
            self.random_nature_or_true()
            # 生成自然数
            if self.nature_or_true == 0:
                number = self.create_single_nature()
                str = '{}{}'.format(str,number)
            elif self.nature_or_true == 1:
                number_str = self.create_single_true()
                str = '{}{}'.format(str,number_str)
            # 生成一个运算符，最后一次不用生成运算符
            if i< self.signal_opration_count:
                operators = self.create_single_opration_signal()
                str += operators
            i += 1
        return str

    # 随机获得一个操作符
    def create_single_opration_signal(self):
        randnum = random.randint(1,4)
        choice = self.operators(randnum)
        return choice

    # 运算符
    def operators(self,choice):
        result={
            1 : '+',
            2 : '-',
            3 : '*',
            4 : '/'
        }
        return result.get(choice)

    # 随机生成一个自然数
    def create_single_nature(self):
         randnum = random.randint(1, self.boundary)
         # print(self.boundary)
         # print(randnum)
         return randnum


    # 随机生成一个分数
    def create_single_true(self):
        # 分子
        randnum = round(random.randint(1, 10))
        # print(randnum)
        # 分母
        randnum1 = round(random.randint(1, 10))
        # print(randnum1)
        str = ""
        # 判断分子比分母大的情况
        if randnum > randnum1:
            str = '{}{}'.format(str,int(randnum/randnum1))
            str += '’'
            str = '{}{}'.format(str,randnum%randnum1)
            str += '/'
            str = '{}{}'.format(str,randnum1)
        elif randnum <= randnum1:
            str += '1‘'
            str = '{}{}'.format(str,randnum)
            str += '/'
            str = '{}{}'.format(str,randnum1)
            # print(str)
        return str

    # 主运行函数
    def main_work(self):
        i = 1
        originfile = open("./file_box/exercises.txt", 'w', encoding='utf-8')
        # 清空文件内容
        originfile.truncate()
        # 要执行的次数，根据question_count
        while i<=self.question_count:
            str = self.create_single_question()
            originfile.write(str+'\n')
            i += 1
        # 关闭文件
        originfile.close()

