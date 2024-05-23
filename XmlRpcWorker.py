from xmlrpc.client import ServerProxy, Fault, Binary
import os
import xml
import mimetypes


class XmlRpcWorker:
    def __init__(self, url, username, password) -> None:
        self.proxy = ServerProxy(url, verbose=False)
        self.username = username
        self.password = password
    

    def get_recent_blogs(self, count: int = -1):
        try:
            posts = self.proxy.metaWeblog.getRecentPosts(1, self.username, self.password, count)
            return posts
        except Fault as f:
            print(f)
        return None

    def new_category(self, category, slug='', description=''):
        try:
            _category = {
                'name': category,
                'slug': slug,
                'description': description
            }
            category_ = self.proxy.wp.newCategory(1, self.username, self.password, _category)
            return category_
        except Fault as f:
            print(f)
        return None
    
    def get_categories(self):
        try:
            categories_ = self.proxy.metaWeblog.getCategories(1, self.username, self.password)
            return categories_
        except Fault as f:
            print(f)
        return None
    
    def get_post(self, post_id):
        try:
            post = self.proxy.metaWeblog.getPost(post_id, self.username, self.password)
            return post
        except Fault as f:
            print(f)
        return None
    
    def upload_media_object(self, path, name, type=None):
        try:
            content = None
            with open(path, 'rb') as f:
                content = Binary(f.read())
                if type is None:
                    _, suffix = os.path.splitext(path)
                    type = mimetypes.guess_type(path)[0]
            _file = {
                'name': name,
                'type': type,
                'bits': content
            }
            
            url = self.proxy.metaWeblog.newMediaObject(1, self.username, self.password, _file)
            return url
        except Fault as f:
            print(f)
        except xml.parsers.expat.ExpatError as e:
            print(e)
        return None

    def new_post(self, post, publish=True):
        try:
            id = self.proxy.metaWeblog.newPost(1, self.username, self.password, post, publish)
            return id
        except Fault as f:
            print(f)
        except xml.parsers.expat.ExpatError as e:
            print(e)
        return None