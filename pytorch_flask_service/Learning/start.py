from flask import Flask, jsonify

app = Flask(__name__)
import io
import torchvision.transforms as transforms
from PIL import Image
from torchvision import models
import json

@app.route('/predict', method=['POST'])
def predict():
    return jsonify({'class_id': 'image_xx', 'class_name': 'Cat'})


# 处理图像
def transform_image(image_bytes):
    my_transform = transforms.Compose([transforms.Resize(255),
                                       transforms.CenterCrop(224),
                                      transforms.ToTensor(),
                                      transforms.Normalize(
                                          [0.485, 0.456, 0.406],
                                          [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    # unsqueeze(0) 方法在返回的Tensor前面增加一个维度，使其形状从 [C, H, W] 变为 [1, C, H, W]
    # 这是因为在PyTorch中，批量处理图像时，通常需要一个额外的维度来表示批量大小（batch size）
    return my_transform(image).unsqueeze(0)

# 测试方法 transform_image()
with open("../static/img/郁金香.jpg", 'rb') as f:
    image_bytes = f.read()
    tensor = transform_image(image_bytes=image_bytes)
    print(tensor)


# predict
model = models.densenet121(weights='IMAGENET1K_V1')
model.eval()

'''def get_prediction(img_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    inputs = model.forward(tensor)
    _, y_hat = inputs.max(1)
    return y_hat'''

imagenet_class_index = json.load(open('../static/imagenet_class_index.json'))

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _,y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return imagenet_class_index[predicted_idx]

with open("../static/img/郁金香.jpg", 'rb') as f:
    image_bytes = f.read()
    print(get_prediction(image_bytes=image_bytes))