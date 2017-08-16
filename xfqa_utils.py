import subprocess
import json
    

def xfqa1(text): #老接口，调用命令行
    ans = None
    command_output = ""
    try:
        cmd = "./xfqa.run '{}'".format(text)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        command_output = process.stdout.read().decode('utf-8')
        
        ans = json.loads(command_output)
        return ans
    except Exception:
        print(command_output)
        return ans   
    
import xfqa
import datetime

#初始化函数
def xfqa_init():
    
    t0 = datetime.datetime.now()
    res = xfqa.init("59896876")
    t1 = datetime.datetime.now()
    print("xfqa_init takes (m): " + str(t1-t0))
    return res
xfqa_init()

def QA(text): #调用C库
    ans = None
    command_output = ""
    try:
        t0 = datetime.datetime.now()
        command_output = xfqa.qa(text)
        ans = json.loads(command_output)
        t1 = datetime.datetime.now()
        print("qa:" + text)
        print("\t takes (m): " + str(t1-t0))
        return ans
    except Exception:
        print("Exception output" + command_output)
        xfqa_init();
        return ans       

def my_call(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    command_output = process.stdout.read().decode('utf-8')
    return command_output