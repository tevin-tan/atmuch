# -*- coding: UTF-8 -*-
import subprocess
import os

class RunTests(object):
    def __init__(self):
        t_dir = os.path.dirname(os.getcwd())
        pah = t_dir + "\\case\\"
        self.pah = pah
        self.testcaselistfile = "testcases.txt"

    def LoadAndRunTestCases(self):
        f = open(self.testcaselistfile)
        testfiles = [test for test in f.readlines() if not test.startswith("#")]
        f.close()
        for item in testfiles:
            print(item)
            # 	subprocess.call("nosetests -s \\" + str(item).replace("\\n", ""), shell=True)
            subprocess.call("nosetests -s " + self.pah + str(item), shell=True)


if __name__ == "__main__":
    newrun = RunTests()
    newrun.LoadAndRunTestCases()
