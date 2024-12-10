import matplotlib.pyplot as plt
from torchvision import datasets

ds_train = datasets.FashionMNIST(
    root='data',
    train=True,
    download=True,
)
print(f'numbers of datasets:{len(ds_train)}')

image, target = ds_train[0]
print(type(image), target)