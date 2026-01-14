### How to fix 'Add --use-flash-attention flag.' in ComfyUI

---

title: "How to fix 'Add --use-flash-attention flag.' in ComfyUI"
description: "Step-by-step guide on how to resolve the issue of adding the '--use-flash-attention' flag for AMD systems."
pubDate: "2026-01-14"

---

## Introduction

Flash Attention (FA) is a feature that can significantly speed up computations in models like Stable Diffusion XL (SDXL), especially on AMD GPUs. Flash Attention optimizes the cross-attention mechanism, making it faster than traditional PyTorch implementations. If you encounter an issue requiring you to add the `--use-flash-attention` flag when running ComfyUI, follow this guide to fix it.

## What Causes This Issue?

The error typically occurs because your system is missing the necessary Flash Attention package or dependencies required for efficient cross-attention calculations. For AMD systems, using Flash Attention can offer a performance boost over regular PyTorch cross-attention implementations. 

However, integrating Flash Attention into ComfyUI may require additional Python packages and setup steps.

## Step-by-Step Fix Guide

### 1. Install the Required Dependencies
First, ensure you have all necessary dependencies installed in your environment. You will need to install `flash-attn` and other related packages.

#### Open a Terminal or Command Prompt:
```bash
pip install flash-attn==2.0.2
```

This command installs the latest stable version of Flash Attention. Check for any updates at [Flash Attention GitHub](https://github.com/HazyResearch/flash-attention) if needed.

### 2. Modify ComfyUI Configuration (Optional)
If you are running ComfyUI directly from a script or repository, make sure to include the `--use-flash-attention` flag when starting the application. This step is optional and depends on how your system is set up:

```bash
python main.py --use-flash-attention
```

Or if you’re modifying a `.sh` script:
Replace any existing line that starts with `python` or calls ComfyUI with the above command.

### 3. Verify Installation
To verify that Flash Attention has been successfully installed and is recognized by your system, you can run a simple check:

```bash
python -c "import flash_attn"
```

This should not return any errors if everything was set up correctly.

## Performance Optimization

After adding the `--use-flash-attention` flag, you might notice improvements in performance. For instance, running SDXL on an AMD system can see a reduction from 5.5 seconds to around 5 seconds for operations such as rendering images at 1024x1024 resolution.

### Additional Notes:
- Ensure your Python environment is properly configured and isolated.
- If you encounter any issues with Flash Attention, check the compatibility of your AMD GPU drivers and operating system with the latest `flash-attn` version.
  
By following these steps, you should be able to resolve the issue of needing to add the `--use-flash-attention` flag in ComfyUI. This will enable better performance on AMD systems for tasks like running SDXL efficiently.

If problems persist or new issues arise, refer to the Flash Attention GitHub repository and ComfyUI documentation for further guidance.