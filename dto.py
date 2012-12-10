__author__ = 'horimislime'

class MainDto:
    '''
    Manages information required when rendering main page
    '''
    def __init__(self):
        pass
    def set_alert_message(self,message):
        self.message=message
    def get_alert_message(self):
        return self.message

    def set_pagination(self,pagination):
        self.pagination=pagination
    def get_pagination(self):
        return self.pagination

    def set_page_no(self,page_no):
        self.page_no=page_no
    def get_page_no(self):
        return self.page_no

    def set_datasets(self,datasets):
        self.datasets=datasets
    def get_datasets(self):
        return self.datasets