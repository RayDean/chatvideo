import dbm 
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


class MetaServerBase(object):

    def get_meta(self,ids):
        raise NotImplementedError


class ImgMetaServer(MetaServerBase):

    def __init__(self,db_path) -> None:
        """
        图像元信息服务器
        :param db_path:
        """
        logging.info('db_path: {}'.format(db_path))
        self.db_path = db_path
        self.db = dbm.open(self.db_path,'r')
        
    def get_meta(self,ids):
        """
        从db中获取索引为ids的url元信息
        :param ids:
        :return:
        """
        ids = str(ids)
        url = self.db[ids].decode('utf-8')
        return url
    
    def batch_get_meta(self, ids_list):
        """
        批次方式从db中获取ids_list的urls
        :param ids_list:
        :return:
        """
        urls = [self.db[str(idx)].decode('utf-8') for idx in ids_list]
        return urls 


#TODO: 这个类和上面类功能一模一样，可以合并为1个
class VideoMetaServer(MetaServerBase):

    def __init__(self,db_path) -> None:
        """
        视频元信息服务器
        :param db_path:
        """
        logging.info('db_path: {}'.format(db_path))
        self.db_path = db_path
        self.db = dbm.open(self.db_path,'r')
        
    def get_meta(self,ids):
        """
        从db中获取索引为ids的url元信息
        :param ids:
        :return:
        """
        ids = str(ids)
        url = self.db[ids].decode('utf-8')
        return url
    
    def batch_get_meta(self,ids_list):
        urls = [self.db[str(idx)].decode('utf-8') for idx in ids_list]
        return urls
