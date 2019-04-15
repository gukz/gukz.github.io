technology stack need to be finished
2, markdown graphic
1, linux common useage  http://blog.leanote.com/post/freewalk/Markdown-%E8%AF%AD%E6%B3%95%E6%89%8B%E5%86%8C
4, the useage of git
7, the useage of gitlab
4, the useage of shell
8, the useage of docker
3, the useage of redis
6, the useage of celery
4, the useage of elastic
7, the useage of kubernetes

2, python3 函数中 import 是否会多次import
1, python3 gdb
4, 产品特性一定要写成文档
7, 评论达不到热门的要求就不显示热门或者按照点赞数排序
4, depolyment ingress
8,  from contextlib import contextmanager
    @contextmanager
    def mux_lock(v):
        print('enter')
        yield v**v
        print('finish')
    with mux_lock(2) as v:
        print('doing', v)
3, mac 安装homebrew ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
6, tmux的快捷键
       Ctrl+b " - 水平切分
       Ctrl+b % - 垂直切分
       Ctrl+b 方向键 - 移动窗口
       Ctrl+b c - 新窗口
       Ctrl+b n - 移动到下一个窗口
       Ctrl+b p - 移动到前一个窗口
       Ctrl+b & - 确认后退出
4, 设置系统默认shell chsh -s /usr/local/bin/zsh
7, chrome 获取cookie console里运行document.cookie

2, python3的包查找优先级, 安装了configs包, sea的查找路径就被替换了
    顺序: 1 判断是否为built-in模块
              如果是built-in模块, 正确找出, 其他路径被屏蔽
              如果不是,继续
          2 查找当前目录
          3 判断该包是否在site-packages下
    step1 built-in module
          step2 sys.path
1, pytest
4, celery
7,
4,
8,
