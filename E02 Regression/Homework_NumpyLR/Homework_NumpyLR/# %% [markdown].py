# %% [markdown]
# # Numpy基础 
# 
# 
# **完成此任务后，你将:**
# - 能够使用numpy函数和numpy矩阵/向量运算
# - 了解“广播”的概念
# - 了解代码“向量化”
# 
# Let's get started!

# %% [markdown]
# ## 1 - 用numpy构建基本函数 ##
# 
# Numpy是Python中科学计算的主要软件包。它由一个大型社区（www.numpy.org)来维护。
# 在本练习中，将学习一些关键的numpy函数，例如np.exp，np.log和np.reshape。
# 同时，将了解如何在以后的任务中使用这些功能。
# 
# ### 1.1 - sigmoid 函数： np.exp() ###
# 在使用np.exp（）之前，我们先使用math.exp（）实现Sigmoid函数。
# 然后，你将知道为什么np.exp（）比math.exp（）更可取。
# 
# **Exercise**: 
# 
# 使用math.exp（x）构建一个参数为x，返回Sigmoid结果的函数。
# 
# 
# **Reminder**:
# $sigmoid(x) = \frac{1}{1+e^{-x}}$ 也称为逻辑函数。它是一种非线性函数，不仅用于机器学习（逻辑回归），而且还用于深度学习。
# 

# %%
# GRADED FUNCTION: basic_sigmoid

import math

def basic_sigmoid(x):
    """
    Compute sigmoid of x.

    Arguments:
    x -- A scalar

    Return:
    s -- sigmoid(x)
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    s = 1/(1+math.exp(-x))
    ### END CODE HERE ###
    
    return s

# %%
basic_sigmoid(3)

# %% [markdown]
# **Expected Output**: 
# <table style = "width:40%">
#     <tr>
#     <td>** basic_sigmoid(3) **</td> 
#         <td>0.9525741268224334 </td> 
#     </tr>
# 
# </table>

# %% [markdown]
# 实际上，我们很少在深度学习中使用“math”库。因为函数的输入是实数，而深度学习中，我们需要使用矩阵和向量。 
# 
# 这就是为什么numpy更有用。

# %%
### 在深度学习中，我们用numpy库代替math库的原因之一 ###
x = [1, 2, 3]
basic_sigmoid(x)  # x是向量，所以此处会报错

# %% [markdown]
# 事实上, 如果 $ x = (x_1, x_2, ..., x_n)$ 是个向量，那么 $np.exp(x)$ 将会把指数函数运算应用于向量中的每一个元素x. 输出将会是: $np.exp(x) = (e^{x_1}, e^{x_2}, ..., e^{x_n})$

# %%
import numpy as np

# np中建立数组的方法np.array()
x = np.array([[1, 2, 3]])

print(np.exp(x)) # 结果将是(exp(1), exp(2), exp(3))

# %% [markdown]
# 而且, 如果 x 是一个向量, 类似 $s = x + 3$ 或 $s = \frac{1}{x}$ 这样的Python计算将会输出一个和x一样大小的向量。

# %%
# example of vector operation
x = np.array([1, 2, 3])
print (x + 3)

# %% [markdown]
# 如果需要有关numpy函数的更多信息，建议查看[官方文档](https://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.exp.html).
# 
# **Exercise**: 使用numpy实现`sigmoid()`。
# 
# **Instructions**: x现在可以是实数、向量或矩阵。而我们在numpy中所使用的来表示这些矢量，矩阵等的数据结构称为numpy数组。
# 
# $$ \text{For } x \in \mathbb{R}^n \text{,     } sigmoid(x) = sigmoid\begin{pmatrix}
#     x_1  \\
#     x_2  \\
#     ...  \\
#     x_n  \\
# \end{pmatrix} = \begin{pmatrix}
#     \frac{1}{1+e^{-x_1}}  \\
#     \frac{1}{1+e^{-x_2}}  \\
#     ...  \\
#     \frac{1}{1+e^{-x_n}}  \\
# \end{pmatrix}\tag{1} $$

# %%
# GRADED FUNCTION: sigmoid

import numpy as np # this means you can access numpy functions by writing np.function() instead of numpy.function()

def sigmoid(x):
    """
    Compute the sigmoid of x

    Arguments:
    x -- A scalar or numpy array of any size

    Return:
    s -- sigmoid(x)
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    
    ### END CODE HERE ###
    
    return s

# %%
x = np.array([1, 2, 3])
sigmoid(x)

# %% [markdown]
# **Expected Output**: 
# <table>
#     <tr> 
#         <td> **sigmoid([1,2,3])**</td> 
#         <td> array([ 0.73105858,  0.88079708,  0.95257413]) </td> 
#     </tr>
# </table> 
# 

# %% [markdown]
# ### 1.2 - Sigmoid gradient
# 
# 正如在基础知识里所提到的，我们将需要计算梯度来实现反向传播，优化损失函数。 
# 
# 
# **Exercise**: 
# 
# 完成`sigmoid_grad（）`函数来计算sigmoid函数对x的梯度。可以使用前面定义好的`sigmoid()`函数。
# 
# sigmoid函数的梯度公式为:
# 
# $$sigmoid\_derivative(x) = \sigma'(x) = \sigma(x) (1 - \sigma(x))\tag{2}$$
# 

# %%
# GRADED FUNCTION: sigmoid_derivative

def sigmoid_derivative(x):
    """
    Arguments:
    x -- A scalar or numpy array

    Return:
    ds -- Your computed gradient.
    """
    
    ### START CODE HERE ### (≈ 2 lines of code)
    
    
    ### END CODE HERE ###
    
    return ds

# %%
x = np.array([1, 2, 3])
print ("sigmoid_derivative(x) = " + str(sigmoid_derivative(x)))

# %% [markdown]
# **Expected Output**: 
# 
# 
# <table>
#     <tr> 
#         <td> **sigmoid_derivative([1,2,3])**</td> 
#         <td> [ 0.19661193  0.10499359  0.04517666] </td> 
#     </tr>
# </table> 
# 
# 

# %% [markdown]
# ### 1.3 - Reshaping arrays ###
# 
# 深度学习中，经常使用的两个numpy函数是[np.shape](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.shape.html) 和 [np.reshape()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html). 
# 
# - X.shape用于获取矩阵/向量X的形状（尺寸）。
# - X.reshape（...）用于将X重塑为其他的形状。
# 
# 举个例子：在计算机科学中，一张图片是由shape$（length，height，dipth=3）$的3D数组来表示。 但当我们读取图片作为算法输入时，会将它转换为shape为$（length * height * 3，1）$的向量。也就是说，我们将3D的array“展开”或reshape为1D的vector。
# 
# <img src="images/image2vector_kiank.png" style="width:500px;height:300;">
# 
# **Exercise**: 完成 `image2vector()`，把输入shape为(length, height, 3)reshape成(length\*height\*3, 1).
# 
# 举个例子，如果我们需要把shape为 (a, b, c) 的输入reshape成 (a*b,c) 你需要使用:
# ``` python
# v = v.reshape((v.shape[0]*v.shape[1], v.shape[2])) # v.shape[0] = a ; v.shape[1] = b ; v.shape[2] = c
# ```
# - 注意：请不要将图片的尺寸设为常数，我们使用`image.shape [0]`索引的方法来查找所需的数量。

# %%
# GRADED FUNCTION: image2vector
def image2vector(image):
    """
    Argument:
    image -- a numpy array of shape (length, height, depth)
    
    Returns:
    v -- a vector of shape (length*height*depth, 1)
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    
    ### END CODE HERE ###
    
    return v

# %%
# This is a 3 by 3 by 2 array, typically images will be (num_px_x, num_px_y,3) where 3 represents the RGB values
image = np.array([[[ 0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]],

       [[ 0.92814219,  0.96677647],
        [ 0.85304703,  0.52351845],
        [ 0.19981397,  0.27417313]],

       [[ 0.60659855,  0.00533165],
        [ 0.10820313,  0.49978937],
        [ 0.34144279,  0.94630077]]])

print ("image2vector(image) = " + str(image2vector(image)))

# %% [markdown]
# **Expected Output**: 
# 
# 
# <table style="width:100%">
#      <tr> 
#        <td> **image2vector(image)** </td> 
#        <td> [[ 0.67826139]
#  [ 0.29380381]
#  [ 0.90714982]
#  [ 0.52835647]
#  [ 0.4215251 ]
#  [ 0.45017551]
#  [ 0.92814219]
#  [ 0.96677647]
#  [ 0.85304703]
#  [ 0.52351845]
#  [ 0.19981397]
#  [ 0.27417313]
#  [ 0.60659855]
#  [ 0.00533165]
#  [ 0.10820313]
#  [ 0.49978937]
#  [ 0.34144279]
#  [ 0.94630077]]</td> 
#      </tr>
#     
#    
# </table>

# %% [markdown]
# ### 1.4 - Broadcasting and softmax ####
# 
# 在numpy中的一个非常重要的概念就是Broadcasting“广播”————它对于执行不同shape数组之间的运算非常有用。
# 有关广播的详细信息，可以阅读[broadcasting documentation](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).
# 

# %% [markdown]
# **Exercise**: 使用numpy实现`softmax()`。softmax常被视为处理多分类问题时的归一化函数。
# 
# **Instructions**: 
# 
# - $ \text{for } x \in \mathbb{R}^{1\times n} \text{,     } softmax(x) = softmax(\begin{bmatrix}
#     x_1  &&
#     x_2 &&
#     ...  &&
#     x_n  
# \end{bmatrix}) = \begin{bmatrix}
#      \frac{e^{x_1}}{\sum_{j}e^{x_j}}  &&
#     \frac{e^{x_2}}{\sum_{j}e^{x_j}}  &&
#     ...  &&
#     \frac{e^{x_n}}{\sum_{j}e^{x_j}} 
# \end{bmatrix} $ 
# 
# - $\text{对于一个矩阵} x \in \mathbb{R}^{m \times n} \text{,  $x_{ij}$ 代表 $i^{th}$ 行  $j^{th}$ 列的元素, 因此我们有: }$  $$softmax(x) = softmax\begin{bmatrix}
#     x_{11} & x_{12} & x_{13} & \dots  & x_{1n} \\
#     x_{21} & x_{22} & x_{23} & \dots  & x_{2n} \\
#     \vdots & \vdots & \vdots & \ddots & \vdots \\
#     x_{m1} & x_{m2} & x_{m3} & \dots  & x_{mn}
# \end{bmatrix} = \begin{bmatrix}
#     \frac{e^{x_{11}}}{\sum_{j}e^{x_{1j}}} & \frac{e^{x_{12}}}{\sum_{j}e^{x_{1j}}} & \frac{e^{x_{13}}}{\sum_{j}e^{x_{1j}}} & \dots  & \frac{e^{x_{1n}}}{\sum_{j}e^{x_{1j}}} \\
#     \frac{e^{x_{21}}}{\sum_{j}e^{x_{2j}}} & \frac{e^{x_{22}}}{\sum_{j}e^{x_{2j}}} & \frac{e^{x_{23}}}{\sum_{j}e^{x_{2j}}} & \dots  & \frac{e^{x_{2n}}}{\sum_{j}e^{x_{2j}}} \\
#     \vdots & \vdots & \vdots & \ddots & \vdots \\
#     \frac{e^{x_{m1}}}{\sum_{j}e^{x_{mj}}} & \frac{e^{x_{m2}}}{\sum_{j}e^{x_{mj}}} & \frac{e^{x_{m3}}}{\sum_{j}e^{x_{mj}}} & \dots  & \frac{e^{x_{mn}}}{\sum_{j}e^{x_{mj}}}
# \end{bmatrix} = \begin{pmatrix}
#     softmax\text{(first row of x)}  \\
#     softmax\text{(second row of x)} \\
#     ...  \\
#     softmax\text{(last row of x)} \\
# \end{pmatrix} $$

# %%
# GRADED FUNCTION: softmax

def softmax(x):
    """Calculates the softmax for each row of the input x.

    Argument:
    x -- A numpy matrix of shape (n,m)

    Returns:
    s -- A numpy matrix equal to the softmax of x, of shape (n,m)
    """
    
    ### START CODE HERE ### (≈ 3 lines of code)
    # Apply exp() element-wise to x. Use np.exp(...).
    

    # Create a vector x_sum that sums each row of x_exp. Use np.sum(..., axis = 1, keepdims = True).
    
    
    # Compute softmax(x) by dividing x_exp by x_sum. It should automatically use numpy broadcasting.
    
    ### END CODE HERE ###
    
    return s

# %%
x = np.array([
    [9, 2, 5, 0, 0],
    [7, 5, 0, 0 ,0]])
print("softmax(x) = " + str(softmax(x)))

# %% [markdown]
# **Expected Output**:
# 
# <table style="width:60%">
#      <tr> 
#        <td> **softmax(x)** </td> 
#        <td> [[  9.80897665e-01   8.94462891e-04   1.79657674e-02   1.21052389e-04
#     1.21052389e-04]
#  [  8.78679856e-01   1.18916387e-01   8.01252314e-04   8.01252314e-04
#     8.01252314e-04]]</td> 
#      </tr>
# </table>
# 

# %% [markdown]
# **Note**:
# - 如果我们打印一下x_exp，x_sum和s的形状，将会看到x_sum的shape为（2,1），而x_exp和s的shape为（2,5）。 正是因为广播功能，x_exp/x_sum才能工作。

# %% [markdown]
# ## 2) Vectorization

# %% [markdown]
# ### 2.1 实现 L1 和 L2 损失函数
# 
# **Exercise**: 完成 L1 损失的 numpy 版本。np.abs(x)函数可用来计算绝对值。np.sum(x)可用于计算和
# 
# **Reminder**:
# - 损失函数用于计算模型的性能，损失越大,说明预测值 ($ \hat{y} $) 距离真实值 ($y$) 越远。在深度学习中，我们常常使用如 Gradient Descent 的优化算法来训练模型，降低损失。 
# - L1 损失函数如下：
# 
# $$\begin{align*} & L_1(\hat{y}, y) = \sum_{i=0}^m|y^{(i)} - \hat{y}^{(i)}| \end{align*}\tag{6}$$

# %%
# GRADED FUNCTION: L1

def L1(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L1 loss function defined above
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    
    ### END CODE HERE ###
    
    return loss

# %%
yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L1 = " + str(L1(yhat,y)))

# %% [markdown]
# **Expected Output**:
# 
# <table style="width:20%">
#      <tr> 
#        <td> **L1** </td> 
#        <td> 1.1 </td> 
#      </tr>
# </table>
# 

# %% [markdown]
# **Exercise**: 完成L2损失的numpy向量化版本。实现方式很多，你可以使用np.dot( )函数。
# 
# 举个例子，如果 $x = [x_1, x_2, ..., x_n]$, 那么 `np.dot(x,x)` = $\sum_{j=0}^n x_j^{2}$. 
# 
# - L2 损失函数如下：
# 
# $$\begin{align*} & L_2(\hat{y},y) = \sum_{i=0}^m(y^{(i)} - \hat{y}^{(i)})^2 \end{align*}\tag{7}$$

# %%
# GRADED FUNCTION: L2

def L2(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L2 loss function defined above
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    
    ### END CODE HERE ###
    
    return loss

# %%
yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L2 = " + str(L2(yhat,y)))

# %% [markdown]
# **Expected Output**: 
# <table style="width:20%">
#      <tr> 
#        <td> **L2** </td> 
#        <td> 0.43 </td> 
#      </tr>
# </table>

# %% [markdown]
# 恭喜你完成Numpy的热身小练习！


