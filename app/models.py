from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_appbuilder.models.decorators import renders
from flask import Markup

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class Folders(Model):
	id = Column(Integer, primary_key=True)
	name = Column(String(50))

	def __repr__(self):
		return self.name


class Urls(Model):
    id = Column(Integer, primary_key=True)
    url =  Column(String(512), default='https://')
    title = Column(String(256), default='')
    des   = Column(String(512), default='')
    top_image_url = Column(String(512), default='https://')
    folder_id = Column(Integer, ForeignKey('folders.id'))
    folders = relationship("Folders")

    def __repr__(self):
        return self.url

    @renders('url')
    def url_a(self):
    # will render this columns as <a> on ListWidget
        return Markup('<a target=\'_blank\' href=\''+ self.url +'\'>' + self.url + '</a>')

    @renders('top_image_url')
    def top_image_url_img(self):
    # will render this columns as <a> on ListWidget
        return Markup('<img width=200 src=\'/static/uploads/'+ self.top_image_url +'\'></img>')