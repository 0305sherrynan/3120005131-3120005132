import math


class compare:
    originfile = "",
    student_file = "",
    write_file = "",
    correct_index=list(),
    false_index=list()

    def __init__(self):
        self.originfile = open("./file_box/answerfile.txt", 'r', encoding='utf-8')
        self.student_file = open("./file_box/student_answer.txt", 'r', encoding='utf-8')
        self.write_file = open("./file_box/grade.txt", 'w', encoding='utf-8')
        self.correct_index = list()

    def compare_correct(self):
        i = 1
        str = self.read_file_origin()
        while str != "":
            str1 = self.read_file_student()
            str = str.replace('\n','')
            str1 = str1.replace('\n','')
            print(str+"-"+"("+str1+")")
            judge = math.isclose(eval(str+"-"+"("+str1+")"),0)
            # lingshi = ""+i
            if judge :
                self.correct_index.append(i)
            else :
                self.false_index.append(i)
            str = self.read_file_origin()
            i += 1

    def write_info(self):
        str11 = " ".join(map(str,self.correct_index))
        str12 = " ".join(map(str,self.false_index))
        self.write_file.write(str11+"\n")
        self.write_file.write(str12)
        self.write_file.close()
        self.student_file.close()
        self.originfile.close()

    def read_file_origin(self):
        str = self.originfile.readline()
        return str

    def read_file_student(self):
        str = self.student_file.readline()
        return str

