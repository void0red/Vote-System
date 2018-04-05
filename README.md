# Vote-System

[demo](http://vote.void0red.me) 地址：vote.void0red.me

## Catalog

```
.
├── example.db
├── LICENSE
├── main.py
├── README.md
├── require.ini
├── static
│   ├── css
│   │   ├── bootstrap.min.css
│   │   ├── bootstrap.min.css.map
│   │   ├── index.css
│   │   ├── main.css
│   │   ├── manageBase.css
│   │   └── manager.css
│   ├── fonts
│   │   ├── glyphicons-halflings-regular.eot
│   │   ├── glyphicons-halflings-regular.svg
│   │   ├── glyphicons-halflings-regular.ttf
│   │   ├── glyphicons-halflings-regular.woff
│   │   └── glyphicons-halflings-regular.woff2
│   ├── js
│   │   ├── bootstrap.min.js
│   │   ├── check.js
│   │   ├── echarts.min.js
│   │   ├── httpPost.js
│   │   ├── jquery-3.3.1.min.js
│   │   ├── macarons.js
│   │   ├── manager.js
│   │   ├── md5.js
│   │   └── vote.js
│   └── pic
│       └── 404.jpg
├── templates
│   ├── 404.html
│   ├── index.html
│   ├── login.html
│   ├── manageBase.html
│   ├── manager.html
│   ├── register.html
│   ├── resultBase.html
│   └── shareBase.html
├── tp.py
└── user.py
```

## Usage

1. 建议使用`virtualenv` 配置python3运行虚拟环境：

   `virtualenv venv -p {your python3 path}`

2. 使用配置文件安装依赖：

   `pip install -r require.ini`

3. 修改数据库文件 `example.db` 为 `data.db`

4. 使用`uwsgi`部署`flask`应用：

   `uwsgi -i xxx.ini`

   ```ini
   [uwsgi]
   socket=127.0.0.1:{{ socket_port }}
   chdir=path
   wsgi-file=main.py
   callable=app
   stats=127.0.0.1:{{ stats_port }} 
   ```

##  Change log

### v0.1.0 Beta (2018/4/3)

第一个版本上线，开始正式测试

### v0.2.0 Beta (2018/4/4)

1. 修复若干bug
2. 添加数据处理生成图表功能

### v0.3.0 Beta (2018/4/5)

1. 修复若干bug
2. 添加二维码分享功能

## TODO

1. 添加邮箱验证功能
2. ~~添加二维码分享功能~~
3. 美化投票界面
