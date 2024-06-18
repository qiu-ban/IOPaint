import base64
from volcengine.visual.VisualService import VisualService
from config import config_map


def image_to_base64(file_path):
    with open(file_path, 'rb') as image:
        encode_string = base64.b64encode(image.read())
        return encode_string.decode('utf-8')


if __name__ == "__main__":
    visual_service = VisualService()
    visual_service.set_ak(config_map.get('ak'))
    visual_service.set_sk(config_map.get('sk'))
    form = {
        'req_key': 'i2i_inpainting',
        'image_urls':[
            "https://pri.pm.qq.com/3045141795/AA015F5E61AB9AEA328B86C208F04E5522625AFE..jpg?sign=UsWyKiW4+/l26B5hnWZJlO6EwpRhPTEwMDQ1MTkxJmI9c2hvdWd1YW40cHJpJms9QUtJRDcwWjhXb3FTeXEzQ2Y4eDZUc1JpbVpXOEZ2Nm9laXU2JmU9MTcxODcyNzQ4NyZ0PTE3MTg2NDEwODcmcj0zOTk4MDY1MDkzJnU9MCZmPQ==&imageMogr2/auto-orient/thumbnail/x670/interlace/1",
            "https://pri.pm.qq.com/3045141795/610B94CEE444D19C8DC6883BF3782645E18D38A8..png?sign=UsWyKiW4+/l26B5hnWZJlO6EwpRhPTEwMDQ1MTkxJmI9c2hvdWd1YW40cHJpJms9QUtJRDcwWjhXb3FTeXEzQ2Y4eDZUc1JpbVpXOEZ2Nm9laXU2JmU9MTcxODcyNzQ4NyZ0PTE3MTg2NDEwODcmcj0zOTk4MDY1MDkzJnU9MCZmPQ==&imageMogr2/auto-orient/thumbnail/x670/interlace/1"
        ]
    }
    resp = visual_service.img2img_inpainting(form)
    result = resp['data']['binary_data_base64'][0]
    decode_data = base64.b64decode(result)
    file_name = '../result.png'
    with open(file_name, 'wb') as f:
        f.write(decode_data)