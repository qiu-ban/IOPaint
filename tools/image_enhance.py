# coding:utf-8
from __future__ import print_function

import base64
import json

from volcengine.visual.VisualService import VisualService


with open('./conf.json', 'r') as f:
    config_map = json.load(f)


def image_to_base64(file_path):
    with open(file_path, 'rb') as image:
        encode_string = base64.b64encode(image.read())
        return encode_string.decode('utf-8')


if __name__ == '__main__':
    visual_service = VisualService()
    visual_service.set_ak(config_map.get('ak'))
    visual_service.set_sk(config_map.get('sk'))

    form = {
        "req_key": "lens_opr",
        "binary_data_base64": [
            image_to_base64('C:/Users/Administrator/Desktop/修图接单/周思琪/20240618/高清_1.jpg')
        ],
        "resolution_boundary": "2k",
        # "enable_hdr": True,
        # "enable_wb": True,
        "result_format": 0,

    }

    resp = visual_service.enhance_photo_v2(form)
    result = resp['data']['binary_data_base64'][0]
    decode_data = base64.b64decode(result)
    file_name = './image_enhance_result.png'
    with open(file_name, 'wb') as f:
        f.write(decode_data)