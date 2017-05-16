# coding:utf-8
import os

# 定义文件目录
result_dir = "D:\workspace\Selenium2\chapter_07\project_test\log"

lists = os.listdir(result_dir)

# 重新按时间对目录下的文件进行排序
lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))

str = "最新的文件为:" + lists[-1]
print(str)
file = os.path.join(result_dir, lists[-1])
print(file)
