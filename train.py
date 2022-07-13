import torch
from resent import resnet34
import argparse

from torchvision.datasets import CIFAR100
import torchvision.transforms as transforms

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--batch_size', default=128, type=int)
    parser.add_argument('--lr', default=0.1, type=float)
    parser.add_argument('--epoch', default=50, type=int)
    parser.add_argument('--log-dir', help='tensorboard directory')
    
    args = parser.parse_args()
    