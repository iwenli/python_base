# !/usr/bin/python
# -*-coding: UTF-8 -*-
'''
@Author: iwenli
@License: Copyright © 2019 txooo.com Inc. All rights reserved.
@Github: https://github.com/iwenli
@Date: 2019-05-20 12:44:47
@LastEditors: iwenli
@LastEditTime: 2019-05-20 14:18:30
@Description: ...
'''
import io
import os
__author__ = 'iwenli'

root_path = os.path.abspath('.')
sub_path = os.path.join(root_path, 'sub')


def with_file():
    with open(
            'g:/0.Project/0.learn/Python/BaseDemo/python_base/0.example/0.base.py',
            'r',
            encoding='utf-8') as f:
        print(f.read())


def file_path():
    '''
    os.sep    可以取代操作系统特定的路径分隔符。windows下为 '\\'
    os.name    字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是 'posix'
    os.getcwd()    函数得到当前工作目录，即当前Python脚本工作的目录路径
    os.getenv()    获取一个环境变量，如果没有返回none
    os.putenv(key, value)    设置一个环境变量值
    os.listdir(path)    返回指定目录下的所有文件和目录名
    os.remove(path)    函数用来删除一个文件
    os.system(command)    函数用来运行shell命令
    os.linesep    字符串给出当前平台使用的行终止符。例如，Windows使用 '\r\n'，Linux使用 '\n' 而Mac使用 '\r'
    os.path.split(path)        函数返回一个路径的目录名和文件名
    os.path.isfile()    和os.path.isdir()函数分别检验给出的路径是一个文件还是目录
    os.path.exists()    函数用来检验给出的路径是否真地存在
    os.curdir        返回当前目录 ('.')
    os.mkdir(path)    创建一个目录
    os.makedirs(path)    递归的创建目录
    os.chdir(dirname)    改变工作目录到dirname          
    os.path.getsize(name)    获得文件大小，如果name是目录返回0L
    os.path.abspath(name)    获得绝对路径
    os.path.normpath(path)    规范path字符串形式
    os.path.splitext()        分离文件名与扩展名
    os.path.join(path,name)    连接目录与文件名或目录
    os.path.basename(path)    返回文件名
    os.path.dirname(path)    返回文件路径
    os.walk(top,topdown=True,onerror=None)        遍历迭代目录
    os.rename(src, dst)        重命名file或者directory src到dst 如果dst是一个存在的directory, 将抛出OSError. 在Unix, 如果dst在存且是一个file, 如果用户有权限的话，它将被安静的替换. 操作将会失败在某些Unix 中如果src和dst在不同的文件系统中. 如果成功, 这命名操作将会是一个原子操作 (这是POSIX 需要). 在 Windows上, 如果dst已经存在, 将抛出OSError，即使它是一个文件. 在unix，Windows中有效。
    os.renames(old, new)    递归重命名文件夹或者文件。像rename()
    # shutil 模块
    shutil.copyfile( src, dst)    从源src复制到dst中去。当然前提是目标地址是具备可写权限。抛出的异常信息为IOException. 如果当前的dst已存在的话就会被覆盖掉
    shutil.move( src, dst)        移动文件或重命名
    shutil.copymode( src, dst)    只是会复制其权限其他的东西是不会被复制的
    shutil.copystat( src, dst)    复制权限、最后访问时间、最后修改时间
    shutil.copy( src, dst)        复制一个文件到一个文件或一个目录
    shutil.copy2( src, dst)        在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西
    shutil.copy2( src, dst)        如果两个位置的文件系统是一样的话相当于是rename操作，只是改名；如果是不在相同的文件系统的话就是做move操作
    shutil.copytree( olddir, newdir, True/Flase)
    把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接
    shutil.rmtree( src )    递归删除一个目录以及目录内的所有内容
    '''
    print(os.name)  # 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
    # print(os.uname())  # win没有次函数
    print(os.environ)  # 环境变量
    print(root_path)  # 查看当前目录的绝对路径
    print(sub_path)
    print(os.mkdir(sub_path))
    # print(os.rmdir(sub_path))
    source_file = os.path.join(sub_path, '1.txt')
    with open(source_file, 'rw') as f:
        f.write(os.environ)
    print(os.path.splitext(source_file))
    os.rename(source_file, '1.1.txt')


def serialization():
    import pickle

    d = dict(name='json', age=20, score=99.99)
    print(d)
    print(pickle.dumps(d))
    file_name = os.path.join(sub_path, 'serializa.bak')
    with open(file_name, 'wb') as f:
        pickle.dump(d, f)

    with open(file_name, 'rb') as f:
        d1 = pickle.load(f)
    print(d1)

    # json
    import json
    print(json.dumps(d1))
    json_file_name = os.path.join(sub_path, 'serializa_json.txt')
    with open(json_file_name, 'w') as f:
        json.dump(d, f)

    with open(json_file_name, 'r') as f:
        d1 = json.load(f)
    print(d1)


if __name__ == '__main__':
    # # 文件读写
    # # with_file()

    # # StringIO和BytesIO
    # f = io.StringIO()
    # print(f.write('hello'))
    # print(f.write(' '))
    # print(f.write('world!'))
    # print(f.getvalue())

    # f1 = io.StringIO('Hello!\nHi!\nGoodbye!')
    # while True:
    #     s = f1.readline()
    #     if s == '':
    #         break
    #     print(s.strip())

    # # BytesIO
    # b1 = io.BytesIO()
    # b1.write("中国".encode('utf-8'))
    # print(b1.getvalue())
    # b2 = io.BytesIO(b'\xe4\xb8\xad\xe5\x9b\xbd')
    # print(f.read())

    # 操作文件和目录
    # file_path()

    # 序列化
    serialization()