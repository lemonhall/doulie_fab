Base Skeleton to start your application using Flask-AppBuilder
--------------------------------------------------------------

- Install it::

    pip install flask-appbuilder
    git clone https://github.com/dpgaspar/Flask-AppBuilder-Skeleton.git

- Run it::

    $ export FLASK_APP=app
    # Create an admin user
    $ flask fab create-admin
    # Run dev server
    $ flask run


That's it!!

- 安装图形库的依赖::

    那个图形处理库很神经，我这是个Debian的镜像，行吧，不折腾，就这些依赖了

     apt-get install -y libtiff5-dev
     apt-get install -y libjpeg62-turbo-dev
     apt-get install -y libopenjp2-7-dev
     apt-get install -y zlib1g-dev
     apt-get install -y libfreetype6-dev
     apt-get install -y liblcms2-dev
     apt-get install -y libwebp-dev 
     apt-get install -y tcl8.6-dev 
     apt-get install -y tk8.6-dev
     apt-get install -y python3-tk
     apt-get install -y libharfbuzz-dev
     apt-get install -y libfribidi-dev 
     apt-get install -y libxcb1-dev

- 安装pip3本身::
     apt-get -y install python3-pip

- 安装本项目的python包的依赖::
    pip3 install -r requirements.txt

- dev.sh本身，内容如下，直接可以运行，是5000端口的::
    export FLASK_APP=app
    flask run

- 数据库::  
    我已经建立好了，是空的，看以后怎么定时备份？

- docker部署::  
    1、最后部署的工艺流程是这样的，用docker desktop弄了一个ubuntu的镜像，起来一个容器，安装pip3、python3、以及goose3需要的那些依赖库，然后把容器commit为了新的images，之后docker save成了新的images，并且存储成了tar包后放到了nas上，docker load，然后进去git了一把，flask fab create-admin，初始化了一下，最后启动。还有两件事没有做，1、EXPOSE端口号，这样web station才能自动反向。2、应该给容器挂载一个外部目录的

- 增加favicon支持:: 
    1、打开config.py，那个里面的是页面上的，改了也好，好看许多
    2、参考：https://flask.palletsprojects.com/en/2.1.x/patterns/favicon/
    在views.py文件里增加了
    import os
    from flask import send_from_directory

    @appbuilder.app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(appbuilder.app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

    说到底，fab它还是一个flask的程序，所以appbuilder.app的调用是成功了的
