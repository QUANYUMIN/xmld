import numpy as np
import matplotlib.pyplot as plt

# 定义时间轴
t = np.linspace(0, 1, 500)  # 连续信号的时间轴
n = np.arange(0, 10)        # 离散信号的时间轴

# 定义信号
continuous_signal = np.sin(2 * np.pi * 5 * t)  # 连续信号：5Hz的正弦波
discrete_signal = np.sin(2 * np.pi * 0.2 * n)  # 离散信号：0.2Hz的正弦波

# 绘制连续信号
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, continuous_signal)
plt.title('Continuous Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# 绘制离散信号
plt.subplot(2, 1, 2)
plt.stem(n, discrete_signal)
plt.title('Discrete Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

# 显示图形
plt.tight_layout()
plt.show()