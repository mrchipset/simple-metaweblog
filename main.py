import yaml
import os
import datetime

from XmlRpcWorker import XmlRpcWorker

def read_config(path):
    with open(path, 'r', encoding='utf-8') as f:
        cfg = f.read()
        d = yaml.load(cfg, Loader=yaml.Loader)
        return d

def read_config_str(str_):
    d = yaml.load(str_, Loader=yaml.Loader)
    return d

def main():
    conf = read_config('conf.yml')

    worker = XmlRpcWorker(url=conf['url'], username=conf['username'], password=conf['password'])
    # TODO add a method to create post
    # TODO add keywords
    print(worker.new_post({
        'title': '测试Post222',
        'dateCreated': datetime.datetime.now(),
        'description': '# AutoMapper可以将多个\n```c\nprintf();\n```',
        'categories': [] 
    }, True))

if __name__ == '__main__':
    main()
