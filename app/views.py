from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
from flask_appbuilder.actions import action
from flask import redirect

from . import appbuilder, db
from .models import Folders, Urls
from .scraping import Scraping

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""
class UrlsView(ModelView):
    datamodel = SQLAInterface(Urls)

    label_columns = {'folders':'豆列名','title':'标题','url_a':'收藏链接','url':'收藏链接','des':'摘要','top_image_url':"缩略图"}
    list_columns = ['title','url_a','top_image_url_img']

    @action("getContent", "抓取内容", "确定要抓取网页内容么?", "fa-rocket", multiple=False)
    def getContent(self, item):
        article = Scraping.goose_get_title(item.url)
        #试着把得到的title更新到数据库里去
        item.title = article.title
        item.des   = article.meta_description
        if article.top_image is None:
            item.top_image_url = ""
        else:
            item.top_image_url = article.top_image.src.split('/')[-1]
        self.datamodel.edit(item)
        return redirect(self.get_redirect())


class FoldersView(ModelView):
    datamodel = SQLAInterface(Folders)
    label_columns = {'name':'豆列名'}

    related_views = [UrlsView]



db.create_all()
appbuilder.add_view(
    FoldersView,
    "豆列",
    icon = "fa-folder-open-o",
    category = "豆列",
    category_icon = "fa-envelope"
)
appbuilder.add_view(
    UrlsView,
    "链接",
    icon = "fa-envelope",
    category = "豆列"
)

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


