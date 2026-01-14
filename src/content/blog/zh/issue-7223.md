### 【完美解决】ComfyUI 报错 “Add --use-flash-attention flag.” 的修复方法

---

title: "【ComfyUI】Add --use-flash-Attention flag. 完美解决指南"
description: "ComfyUI Error fix for Add --use-flash-attention flag."
pubDate: "2026-01-14"

---

最近在使用 ComfyUI 时，您可能会遇到报错信息提示“Add --use-flash-attention flag.” 这个错误通常出现在需要启用更快注意力机制（flash attention）的场景中。该问题主要影响 AMD 系统上的用户，因为对于这类硬件架构来说，Flash Attention (FA) 的构建仍然比 Pytorch cross-attention 快大约 10%。

#### 解释原因

当使用 ComfyUI 并且希望在模型推理过程中提高性能时（特别是在处理图像生成任务如 Stable Diffusion XL），启用 flash attention 是一个有效的方法。然而，要使用 flash attention 功能，您需要确保已经安装了支持此特性的库和依赖项。

#### 解决步骤

1. **更新 PyTorch 版本**

   确保您的 PyTorch 库是最新版本的，因为某些新功能可能不会在旧版本中可用。您可以通过以下命令来升级：

   ```bash
   pip install torch --upgrade
   ```

2. **安装 Flash Attention 依赖**

   接下来需要单独安装 flash attention 相关的库。这一步骤包括安装 Hugging Face 的 transformers 库和 PyTorch Lightning，以及在某些情况下手动安装 flash_attention。

   首先安装 transformers:

   ```bash
   pip install transformers
   ```

   然后根据您的需求选择安装 flash attention：

   如果您使用的是 CPU 或者没有特殊需求的环境，直接使用现有的库即可。但为了确保兼容性和功能完整性，请考虑手动安装 flash_attention 模块。首先克隆或下载相关仓库到本地：

   ```bash
   git clone https://github.com/HazyResearch/flash-attention.git
   cd flash-attention
   pip install -e .
   ```

3. **运行 ComfyUI 时添加 --use-flash-attention 标志**

   在命令行中启动 ComfyUI 的时候，确保在终端里使用此标志以启用 flash attention 功能。例如：

   ```bash
   comfyui --use-flash-attention
   ```

通过以上步骤，您可以成功解决 "Add --use-flash-attention flag." 这一报错问题，并且充分利用 Flash Attention 优化来提升 ComfyUI 的性能和效率。

---

希望这个指南对您有所帮助！如果您还有其他任何疑问或需要进一步的支持，请随时提问。