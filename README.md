## Dataset Acquisition

### Snack Box Dataset

Download link:  
https://drive.google.com/file/d/1q8ADmzlx0v_DcgkVKSn5sjA1ZDqhoqtP/view?usp=drive_link

### LLVIP Dataset

Download link:  
https://drive.google.com/file/d/1VTlT3Y7e1h-Zsne4zahjx5q0TK2ClMVv/view?usp=sharing
## Dataset Structure
```
├── datasets/
    ├── SnackBox/
    │   ├── train/
    │   │   ├── image/
    │   │   └── depth/
    │   ├── val/
    │   │   ├── image/
    │   │   └── depth/
    │   └── test/
    │       ├── image/
    │       └── depth/
    └── LLVIP/
        ├── train/
        │   ├── image/
        │   ├── IR/
        ├── val/
        │   ├── image/
        │   ├── IR/
        └── test/
            ├── image/
            └── IR/
```
### Environment
Python3.9 and Pytorch 1.12.1
Install torch
```conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.6 -c pytorch -c conda-forge
```
### Train
```python train.py
```
