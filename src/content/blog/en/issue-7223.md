# How to fix 'Add --use-flash-attention flag.' in ComfyUI

---

title: "How to fix 'Add --use-flash-attention flag.' in ComfyUI"
description: "Step-by-step fix for Add --use-flash-attention flag."
pubDate: "2026-01-15"

---

## Introduction

Flash Attention (FA) is a technique that can significantly speed up the attention mechanism used in transformers, especially beneficial on AMD systems. The improvement comes from optimizing memory access and reducing redundant computations compared to traditional PyTorch implementations.

When you encounter an error or notice a recommendation like "Add --use-flash-attention flag" while using ComfyUI, this guide will walk you through how to properly set up the environment to support Flash Attention for improved performance.

## Understanding the Error

The message "Add --use-flash-attention flag" typically indicates that your system can benefit from enabling Flash Attention, a specialized implementation of attention mechanisms that offers better performance on AMD GPUs. This recommendation is usually seen when running large models like SDXL (Stable Diffusion XL), especially when working with high-resolution images.

## Solution Guide

### Prerequisites
Ensure you have Python and pip installed. If not, install them using your package manager or download the latest version from [Python's official site](https://www.python.org/downloads/).

### Step 1: Install Dependencies

First, ensure that your environment has the necessary dependencies for Flash Attention:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 -U
```

This command installs PyTorch and its related libraries. Make sure to use the correct CUDA version if you're using NVIDIA GPUs; adjust `cu118` accordingly.

For AMD GPUs, you'll need ROCm (Radeon Open Compute), which is less commonly used but can be installed following AMD's official documentation: [ROCm Installation Guide](https://rocmdocs.amd.com/en/latest/Installation_Guide/index.html).

### Step 2: Install Flash Attention

Flash Attention requires a specific version of the `flash-attn` package. The installation process involves cloning the repository and building it from source:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/HazyResearch/flash-attention.git
    cd flash-attention
    ```

2. **Install Flash Attention**

   - If using ROCm, use this command:
   
     ```bash
     pip install --no-build-isolation --editable .
     ```
   
   - For CUDA-enabled GPUs (NVIDIA), ensure you have the correct version of PyTorch installed before proceeding with the above command.

### Step 3: Update ComfyUI Configuration

To enable Flash Attention in ComfyUI, you need to start it with a specific flag. Assuming your ComfyUI executable is named `run_comfyui.py`, run it as follows:

```bash
python run_comfyui.py --use-flash-attention
```

This command starts ComfyUI and instructs it to use the Flash Attention implementation for better performance.

### Step 4: Verify Installation

Once installed, you can verify that Flash Attention is being used by checking your model's inference time. A noticeable decrease in processing times for tasks such as Stable Diffusion XL on high-resolution images (like 1024x1024) should indicate successful setup and optimization.

## Conclusion

By following these steps, you've set up ComfyUI to utilize Flash Attention, optimizing performance especially on AMD GPUs. This guide provided a step-by-step process from installing dependencies through to launching the application with the necessary flag for improved attention mechanism processing.

---

For more detailed documentation or troubleshooting, refer to the [Flash Attention GitHub Repository](https://github.com/HazyResearch/flash-attention) and the official [ComfyUI Documentation](https://comfyui.github.io/).