# 更新简述

 - 2018年4月29日 15:17:22
>       build 3165

 - 2018年4月25日 14:09:11
>       install Insert Nums  (ctrl + alt + n)

 - 2018年4月11日 16:47:21
>       install more layout  (alt+shift + 670QW)
>       install Packages UI  ( 管理包很好用 )
>       install Console Wrap ( ctrl+shift+(+alt)+q 输出日志)
>       install SideBarEnhancements 
>~~cancel:   
>       install LaTeXTools~~

 - 2018年4月10日 21:28:27
>       install CUDA Snippets
>       install docBlockr_Python 
>~~cancel:   
>       install docBlockr  
>       install clang-format(need clang-format.exe)  
>       install FileHeader~~  

 - 2018年4月1日 22:38:24
>       汉化完成 
>   原理见Sublime_Text\Data\Packages\Default\汉化原理.md

 - 2018年3月31日 23:13:45  
>       git ignore *.sublime-build
>   优化多用户使用体验 一些不需要同步的东西ignore掉  
 
 - 2018年3月31日 22:40:41
>       更新至Dev版本 解决字体异常问题
>       未包含License 请自行注册使用
>       更新了编译器位置 移动至Data\Packages\User\Compiler\
>   todo:  
>       自己汉化一下 之前的汉化插件不是很好维护  
>       菜单那些功能加回来 比如右键e 右键c什么的  
>       todo.tdl文件的字体还是有点怪 有的字斜体有的字不是  

 - 2018年3月31日 20:47:56
>       删除了git上与个人用户相关的文件

 - 2018年3月31日 01:33:37
>       增加了显示抗锯齿
>       修复了md编辑时的显示异常
>   但导致字体变了。。


 - 2018年3月30日 20:45:13 
>       install PlainTasks

 - 2018年3月26日 10:42:24
>       install compare side-by-side
>       remove  filediffs  


 - 2018年3月20日 11:47:55
>       remove   SublimeCodeIntel
>       remove   AutoPEP8 
>       install  Anaconda

# 一、Python路径配置
>**编译Python的话 要修改文件**   
>**Sublime_Text\Data\Packages\User\Compiler\python2.sublime-build**   
>**Sublime_Text\Data\Packages\User\Compiler\python3.sublime-build**   
>**将文件中的python路径改为正确安装路径**   
---------------------------------------------------------    
# 二、已添加修改的sublime功能
## 1.增加的编译系统
>**---菜单栏->工具->编译系统->python2与python3**  
>**编译系统默认(自动)的时候 运行python时是用系统的默认python版本**  
>**要切换版本在这里改**  
>**注意编译MarkDown为HTML的时候 要把编译系统改回自动**  
---------------------------------------------------------    

## 2.编辑区快捷键
>**右键c  复制当前文件路径 python处理文本时会用到**  
>**右键e  打开当前文件所在路径**  
>**右键t  光标位置添加书签 (F2与shift+F2在书签间快速跳转)**  
---------------------------------------------------------    
## 3.标签栏
>**右键c 右键e  同编辑区**  
>**右键Q 克隆文件-代码长时双屏奇效**  
---------------------------------------------------------    
## 4.左侧工程列表右键菜单
>**注意区别删除文件、删除文件夹与从工程中移除**  
>**删除是真的删掉了 2333**  
>**coding时有时会输出测试文件 右键把输出的文件删掉比较方便。**  
>**emm可能是强迫症吧**  
---------------------------------------------------------    
>**左侧少些功能 暂时没加上去 不过影响不大 有空再加**
>**右键某文件夹后在explorer中打开(现在只能右键打开所在文件夹)**  
>**右键某文件直接运行**  
---------------------------------------------------------    

# 三、已安装的部分Package
## 1.编辑
AlignTab

>**选中多行后，ctrl+alt+a自动对齐**  
>**可配置多种对齐方式**  


按键       | 功能
---        | ---
ctrl+alt+a | 按第一个=  =>  : 丨import对齐
ctrl+alt+; | 按第一个;对齐
ctrl+alt+= | 按第一个=对齐
ctrl+alt+. | 按第一个.对齐
ctrl+alt+; | 按第一个:对齐
ctrl+alt+\ | 按所有的丨 对齐
ctrl+alt+7 | 按所有&对齐
ctrl+alt+' | 按第一个"对齐，小心使用，这个对齐后会在前后添加空格 有时候会改变字符串

大概就是对齐什么按什么  
想自定义对齐方式可以到`首选项->快捷键设置`里拓展

## 2.工具
cmd-caller
>ctrl+shift+x，在当前文件位置呼出git-bash 需在快捷键设置中 配置gitbash路径

sublimeGit 未详细配置  
## 3.MarkDown
- MarkDown Editing
>**F1 build a.md to a.html**  
>**支持[toc]自动生成目录**  

- OmniMarkupPreviwer  
>**ctrl+alt+o,在浏览器实时预览markdown**  

## 4.语言相关支持包
>**verilog**  
>**vhdl**  

## 5.主题与配色
>**Seti_UI**  
>**Seti_UX**  
# 四、sublime的原生常用功能
## 1.选择
按键       |功能
---        |---    
shift+右键 |花式多选 试试
ctrl+D     |选择下一个相同项
ALT+F3     |选择所有相同项
Ctrl+L     |选择整行（按住l继续选择下行）

## 2.分屏
按键       |功能
---        |---    
Alt+Shift+1| 恢复默认1屏
Alt+Shift+2| 左右分屏-2列
Alt+Shift+8| 垂直分屏-2屏

## 3.跳转
按键    |功能
---     |---      
Ctrl+P  |搜索文件预览并跳转 （esc取消 回车跳转)
Ctrl+R  |快速列出/跳转到某个函数 (等同于Ctrl+P后输入@)
Ctrl+G  |跳转到相应的行(等同于Ctrl+P后输入:)
F2      |下一个书签
shiftF2 |上一个书签

## 4.大小写转换
按键    |功能
---     |---  
Ctrl+K+U|改为大写(按住ctrl 按一下K再按一下U)
Ctrl+K+L|改为小写

## 5.编辑
按键                | 功能
---                 | ---
ctrl+shift+d        | 复制并粘贴光标所在整行，如果已经选中了文本会复制并粘贴选中项
ctrl+c              | 光标未选中文本时，复制所在行
ctrl+x              | 光标未选中文本时，剪切所在行（经常拿来当删除用）
ctrl+[ 或 ]         | 增加或减少缩进
选中多行后TAB       | 增加缩进
选中多行后shift+TAB | 增加缩进
ctrl+/              | 注释（可选多行
ctrl+shift+up/down  | 行间换行


# 五、更新

#### 2018年3月30日 20:45:13
    install PlainTasks
---------------------------------------------------------    
>**一个很好用的todolist工具**  
>**再也不用写什么`todo.md` `todolist.md`之类的东西了**  
>**拯救`拖延症`、`健忘症`、`我是谁我在哪综合症`**  
>**[[用法点我点我]](https://github.com/aziz/PlainTasks)**  
>**与github作者的示例不同  可能是mac字符集和win的不太一样**  
>**字符做了修改 在我的win7上运行正常**  
---------------------------------------------------------    
#### 2018年3月26日 10:42:24
    install compare side-by-side
    remove  filediffs  
---------------------------------------------------------    

>**发现这个插件之后 觉得filediffs有点蠢**  

---------------------------------------------------------    

#### 2018年3月20日 11:47:55
    remove   SublimeCodeIntel
    remove   AutoPEP8 
    install  Anaconda
---------------------------------------------------------    
>**用Anaconda替代原来的两个插件**

---------------------------------------------------------    

#### 2018年3月14日 02:25:00
    install MarkdownLivePreview
---------------------------------------------------------    

>**功能：markdown下，ALT+M，调出实时预览界面**
>
>**已知缺陷：**  
>**1.代码段不明显，不过这个是css的问题**  
>**2.设置中的update_preview_every设置过小时，会导致很卡**  
>**3.不支持表格**  
>**4.会下载图片生成存，且下载的比较慢**  
>
>**以下来自知乎**
>**实时预览需要浏览器内核渲染。**  
>**但是目前sublime和浏览器交互比较困难。**  
>**所以虽然这个功能很多人找。但是一直都没开发出来。**  
>  
>**emmm看起来很稀有所以这个插件先留着吧**  
---------------------------------------------------------    

