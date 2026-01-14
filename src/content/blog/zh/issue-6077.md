### 【完美解决】ComfyUI 报错 “TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'” 的修复方法

---

title: "【ComfyUI】TypeError: forward_orig() got an unexpected keyword argument 'attn_mask' 完美解决指南"
description: "ComfyUI Error fix for TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'"
pubDate: "2026-01-14"

---

### 正文

#### 问题背景
最近在使用 ComfyUI 进行图像处理时，用户遇到了一个错误信息：“TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'”。这个错误通常发生在某些库或模块更新后，导致接口不兼容的情况。

#### 解决方法
1. **确认环境**
   在尝试任何修复之前，请确保你的 Python 和 ComfyUI 环境是最新的。你可以通过以下命令检查和升级相关包：

   ```bash
   pip install --upgrade stable-diffusion-webui comfy-ui
   ```

2. **查看错误日志**
   根据提供的调试日志，问题发生在 `comfy_extras/nodes_custom_sampler.py` 文件的第 633 行。这表明是在使用自定义采样器时发生的。

3. **修复步骤**

   - 首先，备份原始文件：
     ```bash
     cp F:\StabilityMatrix\Data\Packages\ComfyUI\comfy_extras\nodes_custom_sampler.py F:\StabilityMatrix\Data\Packages\ComfyUI\comfy_extras\nodes_custom_sampler.py.bak
     ```

   - 然后，编辑 `nodes_custom_sampler.py` 文件。找到出错的行（大约在第 633 行），并修改调用方法以删除或替换不必要的参数 `'attn_mask'`。

4. **修复示例**
   如果你发现错误是在传递 `attn_mask` 参数时发生的，可以尝试调整相关代码片段如下：

   ```python
   # 修改前的代码（假设）
   samples = guider.sample(noise.generate_noise(latent), latent, attn_mask=your_attn_mask)

   # 修复后的代码（删除或替换不支持的参数）
   if 'attn_mask' in locals():
       # 处理 attn_mask 参数，例如忽略它
       pass
   else:
       samples = guider.sample(noise.generate_noise(latent), latent)
   ```

5. **重新启动 ComfyUI**
   在进行任何代码修改后，请确保重启 ComfyUI 服务以应用更改。

6. **验证修复**
   - 启动你的项目或测试脚本，看看问题是否已解决。
   - 如果问题仍然存在，尝试查看是否有更多的错误信息，并根据这些信息进一步调整代码或其他设置。

#### 注意事项
- 检查是否有可用的更新版本或补丁可以下载，以避免手动修复可能引入的新问题。
- 始终保持项目的备份，以便在出现问题时可以轻松恢复到已知良好的状态。

通过上述步骤，你应该能够解决由 `'attn_mask'` 参数引起的 `TypeError`。如果有更多问题或需要进一步的帮助，请随时联系社区或查阅官方文档和指南。