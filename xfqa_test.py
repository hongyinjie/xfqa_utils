import xfqa_utils
import datetime    
    
texts = [
    "你好",
    "今天星期几",
    "吃饭了没有",
    "明天北京天气怎么样",
    "1+4=",
    ]
def test():
    
    for text in texts:
        print("#" * 10)
        print(text)
        print (datetime.datetime.now())
        
        t0 = datetime.datetime.now()
        ans = xfqa_utils.QA(text)
        
        t1 = datetime.datetime.now()
        print("ans:" + str(ans))
        print(ans["intent"]["answer"]["text"])
        print(t1-t0)
    print (datetime.datetime.now())
    pass

cmds = [
    "echo $LD_LIBRARY_PATH",
    "export LD_LIBRARY_PATH=\".:/mnt/downloads/aiui/libs/x64\"",
    "echo $LD_LIBRARY_PATH",
    "source ~/.profile",
    "whoami",
    "echo $LD_LIBRARY_PATH",
    ]    
def test_call():
    for cmd in cmds:
        print("#" * 10)
        print(cmd)
        print (datetime.datetime.now())
        ans = xfqa_utils.my_call(cmd)
        print(ans)
        
    print (datetime.datetime.now())
    pass


if __name__ == '__main__':
#     confidence_test()
    test()
#     test_call()
    pass
