import base64
from io import BytesIO
from PIL import Image


def compress_image(image_base64, format, target_size=1080):
    with Image.open(BytesIO(base64.b64decode(image_base64))) as image:
        # 如果图片尺寸已经是1080p或更小，则不做任何处理直接返回
        if image.size[0] <= target_size:
            print(f"Image is already smaller than or equal to 1080p. Skipping compression.")
            return

        # 按比例调整尺寸
        ratio = target_size / image.size[0]
        new_size = (int(image.size[0] * ratio), int(image.size[1] * ratio))

        # 重新调整尺寸并保存
        image = image.resize(new_size)
        buffered = BytesIO()
        image.save(buffered, format=format)
        image_base64=base64.b64encode(buffered.getbuffer()).decode("utf-8")
        return image_base64


def shift_image_if_need(image, mask):
    image_image = Image.open(BytesIO(base64.b64decode(image)))
    mask_image = Image.open(BytesIO(base64.b64decode(mask)))

    if image_image.size[0] == mask_image.size[1] and image_image.size[1] == mask_image.size[0]:
        # mask左转90度
        image_image = image_image.rotate(270, expand=True)
    buffered = BytesIO()
    image_image.save(buffered, format='png')
    image_base64 = base64.b64encode(buffered.getbuffer()).decode("utf-8")
    return image_base64