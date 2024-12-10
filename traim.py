import time

import matplotlib.pyplot as plt

import torch
from torchvision import datasets
import torchvision.transforms.v2 as transforms

import models


# データセットの前処理関数
ds_transforms = transforms.Compose([
    transforms.ToImage(),
    transforms.ToDtype(torch.float32, scale=True)
])

# データセットの読み込み
ds_train = datasets.FashionMNIST(
    root='data',
    train=False,
    download=True,
    transform=ds_transforms 
)

ds_test = datasets.FashionMNIST(
    root='data',
    train=False,
    download=True,
    transform=ds_transforms
)

# ミニバッチのデータローダー
bs = 64
dataloader_train = torch.utils.data.DataLoader(
    ds_test,
    batch_size=bs,
    shuffle=False
)
dataloader_test = torch.utils.data.DataLoader(
    ds_test,
    batch_size=bs,
    shuffle=False
)

for image_batch, label_batch in dataloader_test:
    print(image_batch.shape)
    print(label_batch.shape)
    break

# モデルのインスタンスを作成
model = models.MyModel()

# 損失関数（誤差関数・ロス関数）の選択
loss_fn = torch.nn.CrossEntropyLoss()

# 最適化の方法の選択
learing_rate = 0.003  # 学習率
optimizer = torch.optim.SGD(model.parameters(), lr=learing_rate)
# criterion（基準）とも呼ぶ

# 精度を計算する
acc_test = models.test_accuracy(model, dataloader_test)
print(f'test accuracy: {acc_test*100:.3f}%' )

n_epochs = 5

loss_train_history = []
loss_test_history = []
acc_train_history = []
acc_test_history = []

for k in range(n_epochs):
    print(f'epoch {k+1}/{n_epochs}', end=': ', flush=True)

    # 1 epoch の学習
    loss_train = models.train(model, dataloader_train, loss_fn, optimizer)
    loss_train_history.append(loss_train)
    print(f'train loss: {loss_train}', end=': ')

    loss_test = models.test(model, dataloader_train, loss_fn)
    loss_test_history.append(loss_test)
    print(f'test loss: {acc_test*100:.3f}', end=': ')

    # 精度を計算する
    acc_train = models.test_accuracy(model, dataloader_train)
    acc_train_history.append(loss_train)
    print(f'train accuracy: {acc_train*100:.3f}%', end=', ')
    acc_test = models.test_accuracy(model, dataloader_test)
    acc_test_history.append(loss_train)
    print(f'test accuracy: {acc_test*100:.3f}%')

plt.plot(acc_train_history, label='train')
plt.plot(acc_test_history, label='test')
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend()
plt.grid()
plt.show()

plt.plot(loss_train_history, label='train')
plt.plot(loss_test_history, label='test')
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend()
plt.grid()
plt.show()