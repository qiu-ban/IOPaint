import base64
from io import BytesIO
import tos
from PIL import Image
from tos import HttpMethodType

from config import config_map


tos_ak = config_map.get('tos-ak')
tos_sk = config_map.get('tos-sk')
tos_endpoint = "tos-cn-beijing.volces.com"
tos_region = "cn-beijing"
tos_bucket_name = "iopaint"
tos_client = tos.TosClientV2(tos_ak, tos_sk, tos_endpoint, tos_region)


def put_image_2_tos(image_id, image_base64, content_type):
    '''
    上传图片到TOS
    '''
    try:
        resp = tos_client.put_object(tos_bucket_name, image_id, content=BytesIO(base64.b64decode(image_base64)),
                                     content_type=content_type)
        return True
    except tos.exceptions.TosClientError as e:
        # 操作失败，捕获客户端异常，一般情况为非法请求参数或网络异常
        print('fail with client error, message:{}, cause: {}'.format(e.message, e.cause))
    except tos.exceptions.TosServerError as e:
        # 操作失败，捕获服务端异常，可从返回信息中获取详细错误信息
        print('fail with server error, code: {}'.format(e.code))
        # request id 可定位具体问题，强烈建议日志中保存
        print('error with request id: {}'.format(e.request_id))
        print('error with message: {}'.format(e.message))
        print('error with http code: {}'.format(e.status_code))
        print('error with ec: {}'.format(e.ec))
        print('error with request url: {}'.format(e.request_url))
    except Exception as e:
        print('fail with unknown error: {}'.format(e))


def get_tos_access_url(image_id, expire_minutes=1):
    return tos_client.pre_signed_url(HttpMethodType.Http_Method_Get, tos_bucket_name, image_id,
                                                      expires=expire_minutes*60)


def delete_image_2_oss(image_id):
    '''
    删除TOS的图片
    '''
    try:
        resp = tos_client.delete_object(tos_bucket_name, image_id)
        return True
    except tos.exceptions.TosClientError as e:
        # 操作失败，捕获客户端异常，一般情况为非法请求参数或网络异常
        print('fail with client error, message:{}, cause: {}'.format(e.message, e.cause))
    except tos.exceptions.TosServerError as e:
        # 操作失败，捕获服务端异常，可从返回信息中获取详细错误信息
        print('fail with server error, code: {}'.format(e.code))
        # request id 可定位具体问题，强烈建议日志中保存
        print('error with request id: {}'.format(e.request_id))
        print('error with message: {}'.format(e.message))
        print('error with http code: {}'.format(e.status_code))
        print('error with ec: {}'.format(e.ec))
        print('error with request url: {}'.format(e.request_url))
    except Exception as e:
        print('fail with unknown error: {}'.format(e))


def compress_image(image_base64, format, target_size=(3000, 2000)):
    with Image.open(BytesIO(base64.b64decode(image_base64))) as image:
        # 如果图片尺寸已经是1080p或更小，则不做任何处理直接返回
        if image.size[0] <= target_size[0] and image.size[1] <= target_size[1]:
            print(f"Image is already smaller than or equal to 1080p. Skipping compression.")
            return

        # 按比例调整尺寸
        ratio = min(target_size[0] / image.size[0], target_size[1] / image.size[1])
        new_size = (int(image.size[0] * ratio), int(image.size[1] * ratio))

        # 重新调整尺寸并保存
        image = image.resize(new_size, Image.ANTIALIAS)
        buffered = BytesIO()
        image.save(buffered, format=format)
        image_base64=base64.b64encode(buffered.getbuffer()).decode("utf-8")
        return image_base64


if __name__ == '__main__':
    with open('./assets/manga.png', 'rb') as f:
        image_id = "123.png"
        delete_image_2_oss(image_id)