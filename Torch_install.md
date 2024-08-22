## Torch install on Jetson with Jetpack 6
### Start from here:


https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048
https://developer.download.nvidia.com/compute/redist/jp/
```shell

python3 -m pip install numpy=='1.26.1'
python3 -m pip install --no-cache https://developer.download.nvidia.com/compute/redist/jp/v60/pytorch/torch-2.4.0a0+07cecf4168.nv24.05.14710581-cp310-cp310-linux_aarch64.whl
```

Test installation:
```python
import torch

print(torch.__version__)
print('CUDA available: ' + str(torch.cuda.is_available()))
print('cuDNN version: ' + str(torch.backends.cudnn.version()))

a = torch.cuda.FloatTensor(2).zero_()
print('Tensor a = ' + str(a))
b = torch.randn(2).cuda()
print('Tensor b = ' + str(b))
c = a + b
print('Tensor c = ' + str(c))
```



Installing Torch on nVidia Jetson Orin NX 16GB
1. Detect Jetpack version apt-cache show nvidia-jetpack —> Version: 5.1.2
```shell
jetson_release
```
2. Set env vars:
```shell
JP_VERSION=512
```
3. Find compatible Torch Version: https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform-release-notes/pytorch-jetson-rel.html#pytorch-jetson-rel
4. Set env var:
```shell
PYT_VERSION=2.1.0a
```
5. Set download URL:
```shell
TORCH_INSTALL=https://developer.download.nvidia.com/compute/redist/jp/v$JP_VERSION/pytorch/$PYT_VERSION

TORCH_INSTALL=https://developer.download.nvidia.com/compute/redist/jp/v512/pytorch/torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl

python3 -m pip install --upgrade pip; python3 -m pip install numpy==’1.26.1’; python3 -m pip install --no-cache $TORCH_INSTALL  
```
5. Install torchvision
```shell
git clone --branch v0.16.1 https://github.com/pytorch/vision torchvision
cd torchvision
python setup.py install
```

6. Install pyserial
```shell
pip install pyserial
sudo usermod -a -G dialout `whoami`
sudo chmod 766 /dev/ttyUSB0
```

7. Install depthai
```shell
pip install depthai
```