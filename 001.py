import os

filename = 'student.txt'


def main():
    while True:
        menu()
        choice = int(input('请选择'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定要退出吗Y/N\n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用！！！')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menu():
    print('====================================学生信息管理系统=========================================')
    print('---------------------------------------主菜单----------------------------------------------')
    print('\t\t\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t\t\t6.统计学生人数')
    print('\t\t\t\t\t\t\t\t7.显示学生信息')
    print('\t\t\t\t\t\t\t\t0.退出系统')
    print('------------------------------------------------------------------------------------------')


def insert():
    student_list = []
    while True:
        id = int(input('请输入学号（例如：1001）:'))
        if not id:
            break

        name = input('请输入学生姓名:')
        if not name:
            break

        try:
            engilsh = int(input('请输入英语成绩:'))
            python = int(input('请输入Python成绩：'))
            java = int(input('请输入Java成绩：'))
        except:
            print('成绩无效，请重新输入：')
            continue

        student = {'id': id, 'name': name, 'english': engilsh, 'python': python, 'java': java}
        student_list.append(student)
        answer = input('是否继续添加Y/N\n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    save(student_list)
    print('学生信息录入成功。')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='UTF-8')
    except:
        stu_txt = open(filename, 'w', encoding='UTF-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = int(input('按ID查找请按1,按姓名查找请按2:'))
            if mode == 1:
                id = int(input('请输入学生ID：'))
            elif mode == 2:
                name = (input('请输入学生姓名：'))
            else:
                print('您的输入有误，请重新输入：')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            # 显示查询结果
            show_student(student_query)
            # 清空列表
            student_query.clear()
            answer = input('是否继续查询Y/N？\n')
            if answer == 'Y' or answer == 'y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息')
            return


def show_student(lst):
    if len(lst) == 0:
        print('无数据显示。')
        return
    else:
        # 定义标题显示格式
        format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
        print(format_title.format('id', '姓名', 'english', 'python', 'java', 'tatel'))
        # 定义内容显示格式
        format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
        for item in lst:
            print(format_data.format(item.get('id'), item.get('name'), item.get('english'), item.get('python'),
                                     item.get('java'),
                                     int(int(item.get('english')) + int(item.get('python')) + int(item.get('java')))))


def delete():
    while True:
        student_id = int(input('请输入要删除的学生ID:'))
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 标记是否删除

            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已经被删除')
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()  # 删除之后重新显示所有学生信息

            answer = input('是否继续删除学生信息Y/N?\n')
            if answer == 'Y' or answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):

        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        print('请先创建学生信息文件。')
        return
    student_id = (input('请输入要修改的学生id:'))
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if int(student_id) == int(d['id']):
                print('找到学生信息，开始修改。')
                while True:
                    try:
                        d['name'] = input('请输入学生姓名：')
                        d['english'] = input('请输入英语成绩；')
                        d['java'] = input('请输入java成绩；')
                        d['python'] = input('请输入Python成绩；')
                    except:
                        print('您的输入有误，请重新输入')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功')
            else:
                wfile.write(str(d) + '\n)')

                break
        answer = input('是否继续修改其他学生信息Y/N?\n')
        if answer == 'y' or answer == 'Y':
            modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
            student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)

    else:
        return
    asc = input('请选择升序（0）或者降序（1）:')
    if asc == '0':
        asc_bool = False
    elif asc == '1':
        asc_bool = True
    else:
        print('您的输入有误，请重新输入:')
        sort()
    mode = input('请选择排序方式（1：按英语成绩 2：按Python成绩 3：按照Java成绩 4：按照总成绩排序）:')
    if mode == '1':
        student_new.sort(key=lambda student_new: int(student_new['english']), reverse=asc_bool)
    elif mode == '2':
        student_new.sort(key=lambda student_new: int(student_new['python']), reverse=asc_bool)
    elif mode == '3':
        student_new.sort(key=lambda student_new: int(student_new['java']), reverse=asc_bool)
    elif mode == '4':
        student_new.sort(
            key=lambda student_new: int(student_new['english']) + int(student_new['python']) + int(student_new['java']),
            reverse=asc_bool)
    else:
        print('您的输入有误，请重新输入')
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student = rfile.readlines()
            if student:
                print(f'一共有{len(student)}名学生')
            else:
                print('暂未录入学生信息')

    else:
        print('暂未保存文件。')


def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student = rfile.readlines()
            for item in student:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
            else:
                print('暂未学生信息')
    else:
        print('暂未学生文件')


if __name__ == '__main__':
    main()
