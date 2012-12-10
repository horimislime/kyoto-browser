__author__ = 'horimislime'

import tornado.ioloop
import tornado.web
import tornado.escape
import tornado.template
from kyoto import Kyoto
from dto import MainDto
from utils.pagination import Pagination

PAGE_LIMIT=10

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.loader=tornado.template.Loader("./view")
        self.kyoto=Kyoto()

class MainHandler(BaseHandler):
    '''
    Index page handler
    '''
    def get(self):
        page_no=int(self.get_argument('pageNo',default='1'))

        raw_message=self.get_argument('message',default=None)
        if raw_message is not None:
            message=eval(tornado.escape.url_unescape(raw_message))
        else:
            message=None

        dto=MainDto()
        datasets=self.kyoto.get_datasets()
        begin=PAGE_LIMIT*(page_no-1)+1
        end=begin+PAGE_LIMIT
        pagination= Pagination(page_no,PAGE_LIMIT,len(datasets))

        dto.set_alert_message(message)
        dto.set_page_no(page_no)
        dto.set_pagination(pagination)
        dto.set_datasets(datasets[begin:end])

        self.write(self.loader.load("index.html").generate(dto=dto))

class KyotoModificationHandler(BaseHandler):
    '''
    Handles modification action to kyototycoon records
    '''
    def post(self, *args, **kwargs):
        delete_key=self.get_argument('key')
        message=''

        if self.kyoto.delete(self.get_argument('key')):
            message=str(dict(success=delete_key+' is successfully deleted!'))

        else:
            message=str(dict(error='Failed to delete record for key '+delete_key))

        self.redirect('/?message='+tornado.escape.url_escape(message))

class SettingsHandler(BaseHandler):
    '''
    Used to render settings page
    '''
    def get(self):
        host,port=self.kyoto.get_settings()
        self.write(self.loader.load('settings.html').generate(host=host,port=port))

    def post(self):
        try:
            host=self.get_argument('host')
            port=self.get_argument('port')
            self.kyoto.set_configs(host,port)

            message=str(dict(success='settings successfully saved!'))
        except:
            message=str(dict(error='Saving settings failed.'))

        self.redirect('/?message='+tornado.escape.url_escape(message))

if __name__ == "__main__":

    application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/settings",SettingsHandler),
    (r"/delete",KyotoModificationHandler),
    (r"/static/(.*)",tornado.web.StaticFileHandler,dict(path='view'))
    ])

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
