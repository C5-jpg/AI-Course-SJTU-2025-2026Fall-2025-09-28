<div align="center">

# 🤖 SJTU 深度学习课程 2025-2026 秋季学期

**上海交通大学 · 完整学期课程资料 · 9 个专题 · 实战 Notebook**

[![MindSpore](https://img.shields.io/badge/MindSpore-2.0+-FF6F00.svg)](https://www.mindspore.cn/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C.svg)](https://pytorch.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**从线性回归到 Transformer，覆盖深度学习核心知识体系**

</div>

---

## 📋 课程概述

本仓库包含**上海交通大学 2025-2026 学年秋季学期深度学习课程**的完整学习资料，涵盖 9 个专题（Episode），从基础的线性回归到前沿的 Transformer 与 BERT，配合丰富的 Jupyter Notebook 实战练习。

### 📚 课程专题

| 专题 | 主题 | 核心内容 | 实战项目 |
|:---:|------|------|------|
| **E01** | 深度学习概论 | AI 概述、Anaconda 环境、Python 实践 | Python 基础练习 × 2 |
| **E02** | 回归分析 | 线性回归、逻辑回归、集成学习 | NumPy 教程 + Adaboost/RF/Stacking |
| **E03-04** | 神经网络 | 前向传播、反向传播 | 神经网络 Demo |
| **E05-06** | CNN & ResNet | 卷积网络、ResNet50、Inception、优化器 | ResNet50 (CIFAR-10) + OpenCV |
| **E07** | 分割与检测 | FCN、YOLO、SAM | FCN-8s (PASCAL VOC) + YOLO 训练 |
| **E08** | RNN & LSTM | 序列建模、情感分析、序列标注 | LSTM (IMDB) + Emojify |
| **E09** | Transformer | 自注意力机制、BERT 预训练 | Transformer 理论 + BERT |

---

## 🏗️ 课程知识体系

```
┌─────────────────────────────────────────────────────────────────┐
│                    SJTU 深度学习课程体系                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  基础层                                                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────────┐                  │
│  │ E01 概论  │  │ E02 回归  │  │ E03-04 NN    │                  │
│  │ Python   │  │ 线性/逻辑 │  │ 前向/反向传播 │                  │
│  └──────────┘  └──────────┘  └──────────────┘                  │
│                                                                  │
│  视觉层                                                          │
│  ┌──────────────┐  ┌──────────────────────────────────────┐    │
│  │ E05-06 CNN   │  │ E07 分割与检测                        │    │
│  │ ResNet50     │  │ FCN-8s · YOLO · SAM                  │    │
│  │ Inception    │  │ 语义分割 · 目标检测 · 零样本分割      │    │
│  └──────────────┘  └──────────────────────────────────────┘    │
│                                                                  │
│  序列层                                                          │
│  ┌──────────────────┐  ┌──────────────────────────────────┐    │
│  │ E08 RNN & LSTM   │  │ E09 Transformer & BERT            │    │
│  │ 情感分析 · 序列标注│  │ 自注意力 · 预训练语言模型         │    │
│  └──────────────────┘  └──────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📁 项目结构

```
AI-Course-SJTU-2025-2026Fall/
│
├── 📚 课程专题
│   ├── E01 深度学习概论/
│   │   ├── Python 练习 I & II.ipynb
│   │   └── AI提纲.pdf
│   ├── E02 Regression/
│   │   ├── 线性回归 & 逻辑回归.pdf
│   │   ├── NumPy教程.ipynb
│   │   ├── Homework_NumpyLR/
│   │   └── 集成学习/ (Adaboost, Bagging, Stacking, RandomForest)
│   ├── E03-04 Neural Network/
│   │   ├── 前向传播.pdf
│   │   ├── 反向传播.pdf
│   │   └── demo_code.zip
│   ├── E05-06 CNN、ResNet/
│   │   ├── CNN练习/ (TakePhotos, MindSpore, PyTorch)
│   │   ├── ResNet50.ipynb (CIFAR-10, MindSpore)
│   │   ├── OpenCV基础.ipynb
│   │   └── Inception/ResNet/Optimizer.pdf
│   ├── E07 Segmentation and Detection/
│   │   ├── FCN8s.ipynb (PASCAL VOC, MindSpore)
│   │   ├── YOLO训练测试.ipynb (Ultralytics)
│   │   ├── SAM.ipynb (Segment Anything)
│   │   └── YOLO.pdf
│   ├── E08 RNN/
│   │   ├── 情感分析.ipynb (LSTM + GloVe, IMDB)
│   │   ├── 序列标注.ipynb
│   │   └── Emojify/
│   └── E09 Transformer/
│       ├── Transformer.pdf
│       └── BERT.pdf
│
├── 🖼️ course_image/                    # 课程封面图片
│
└── 📝 Git大文件问题解决方案.md           # Git LFS 使用指南
```

---

## 🚀 快速开始

### 环境要求

| 组件 | 版本 |
|:---:|:---:|
| Python | 3.8+ |
| MindSpore | 2.0+ (主要框架) |
| PyTorch | 2.0+ (部分练习) |
| Jupyter Notebook | 6.0+ |

### 安装

```bash
# MindSpore (CPU 版)
pip install mindspore

# MindSpore (GPU 版)
pip install mindspore-gpu

# PyTorch (部分练习)
pip install torch torchvision

# 其他依赖
pip install numpy opencv-python ultralytics
```

### 运行 Notebook

```bash
jupyter notebook
# 打开对应专题目录下的 .ipynb 文件
```

---

## 🔬 实战项目详解

### ResNet50 图像分类 (E05-06)

基于 MindSpore 实现完整 ResNet50 在 CIFAR-10 上的训练：

- 数据加载与增强
- ResNet50 网络搭建
- 模型训练与评估
- 支持 CPU / GPU / Ascend NPU

### FCN-8s 语义分割 (E07)

基于 MindSpore 实现经典 FCN-8s 语义分割网络：

- PASCAL VOC 数据集
- 编码器-解码器结构
- 跳跃连接
- 像素级预测

### YOLO 目标检测 (E07)

基于 Ultralytics 框架的 YOLO 训练与测试：

- 数据集准备
- 模型训练
- 推理与可视化

### LSTM 情感分析 (E08)

基于 PyTorch 的 IMDB 电影评论情感分析：

- GloVe 词向量
- LSTM 序列编码
- 二分类情感判断

---

## 🛠️ 技术栈

<div align="center">

| 类别 | 技术 |
|:---:|:---:|
| 主要框架 | ![MindSpore](https://img.shields.io/badge/MindSpore-2.0+-FF6F00) (华为昇腾) |
| 辅助框架 | ![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C) |
| 数据集 | CIFAR-10 · PASCAL VOC · IMDB |
| 工具 | NumPy · OpenCV · Ultralytics · GloVe |
| 平台 | 华为 ModelArts / 本地 GPU / CPU |

</div>

---

<div align="center">

**⭐ 如果这个课程资料对您有帮助，请给个 Star！**

</div>
