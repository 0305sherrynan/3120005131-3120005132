import argparse
# import random

from create_questions import create_questions
from calculation import  calculation
from compare import compare
def main_func():
    parser =argparse.ArgumentParser()
    # 控制生成题目的个数
    parser.add_argument('-n',type=int, help='控制生成题目的个数')
    # 控制题目中数值（自然数、真分数和真分数分母）的范围
    parser.add_argument('-r', type=int,help='控制题目中数值（自然数、真分数和真分数分母）的范围')
    # 将生成的题目输出到对应文件
    parser.add_argument('-e', default='exercisefile.txt',help='将生成的题目输出到对应文件')
    # 将统计结果输出到对应文件
    parser.add_argument('-a', default='answerfile.txt',help='将统计结果输出到对应文件')
    # 设置功能参数，是生成题目和答案还是对比答案
    parser.add_argument('-f',type=int,default=1,help='设置功能参数')
    # 获取参数
    args = parser.parse_args()
    #创建生成问题的类，传入生成的个数和范围
    if args.f == 1:
        create_questions1 = create_questions(args.n,args.r,args.e)
        create_questions1.main_work()
        calculation1 = calculation(args.e,args.a)
        calculation1.dealwith_singleline()
    elif args.f == 2:
        compare1 = compare(args.a)
        compare1.compare_correct()
        compare1.write_info()

    # 性能测试代码
    # create_questions1 = create_questions(10, 10)
    # create_questions1.main_work()
    # calculation1 = calculation()
    # calculation1.dealwith_singleline()



if __name__ == '__main__':
    main_func()
