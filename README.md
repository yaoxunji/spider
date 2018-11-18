**doutuwang是爬去图片**<br>
**novelspider是爬取小说名和作者并入库**<br>
权当以后忘了参考
<br><br>

### Scrapy命令备忘

scrapy startproject name  创建项目 <br>
scrapy genspider name1 [网址] 创建爬虫模板<br>
scrapy crawl name1  启动爬虫<br>

scrapy shell 网址[不需要引号]<br>
requset 网址服务器相应请求，发回的相应信息（shell中）<br>
view（response）在浏览器中打开response中保存的网页数据（shell中）<br>
fetch（url）重新发送请求（shell中）<br>

### Scrapy项目文件

init.py ->保持默认，不许更改<br>
items.py ->自定义项目类的地方，爬虫获取数据之后传入管道文件的载体<br>
pipeline.py ->项目管道文件，对传入的项目类中的数据进行清理和入库<br>
settings.py ->项目的设置文件，例如下载延迟，项目管道文件中类的启用以及自定义中间件的启用和顺序<br>
middlewares.py ->中间件配置文件<br>
spider目录 ->里面只有一个init.py文件，（使用genspider之后会多），在该目录下定义爬虫类并继承<br>

### sqlite3链接操作在database.py中
补充一点查询的时候execute函数不会反回结果，提取结果需要 <br>
```
cu = conn.cursor //cursor是光标
all_results = cu.fetchall()
```
fetch只能执行一次，fetch 包括fetchone，fetchall，fetchmany（指定）<br>

