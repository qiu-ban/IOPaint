import json

config_map = json.load('./conf.json')
ak = config_map.get('tos-ak')
sk = config_map.get('tos-sk')


def put_image_2_oss(image):
    '''
    上传图片到OSS
    '''
    return 'xxx'


def delete_image_2_oss(url):
    '''
    删除OSS的图片
    '''
    return 'xxx'