# xfqa_utils
讯飞AIUI的python接口

运行测试环境：
  gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4)
  python3.5
  gunicorn(可选)
  
  
具体使用可以参考 xfqa_test.py

可以执行web服务：
sh run_alt.sh

打开网页   http://127.0.0.1:5040/query?q=北京今天天气怎么样
在Postman测试，体验更好！


===核心：
生成 libs/x64/libxfqa.so 和 xfqa.py _xfqa.cpython-35m-x86_64-linux-gnu.so
其中： 
  libxfqa.so： 通过修改aiui_sample代码， 生成的so库
  xfqa.py _xfqa.cpython-35m-x86_64-linux-gnu.so  是用swig和python distutils 生成的。

接口
xfqa.init（appid）
xfqa.qa(text)

使用： 
1 讯飞平台注册，下载开发包（lib）
2 替换appid和lib包 （两者对应的）
3 平台应用设置（）
4 测试调用

