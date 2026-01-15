### How to fix 'After the last update black images after few steps on Mac mini M2 pro with Sonoma 14.5' in ComfyUI

---

title: "How to fix 'After the last update black images after few steps on Mac mini M2 pro with Sonoma 14.5' in ComfyUI"
description: "Step-by-step fix for After the last update black images after few steps on Mac mini M2 pro with Sonoma 14.5"
pubDate: "2026-01-15"

---

If you're experiencing issues where your images turn black after a few steps in ComfyUI on a Mac mini M2 Pro running macOS Sonoma 14.5, this guide will help you resolve the problem.

### Problem Description

After updating to the latest version of ComfyUI or any dependent packages, many workflows are not functioning as expected. Specifically, when using the "Karras" scheduler, images turn black after a few steps in the workflow.

### Cause

The issue arises due to compatibility problems between your current setup and the updated software. The Karras scheduler might be incompatible with certain configurations or versions of ComfyUI dependencies.

### Solution

To fix this problem, follow these steps:

#### 1. Ensure Python Dependencies Are Up-to-Date
Before addressing specific issues related to the Karras scheduler, make sure all your Python packages are up-to-date and compatible with each other. Open a terminal and run:
```bash
pip install --upgrade pip
```

Then update ComfyUI dependencies:
```bash
pip install -U comfyui
pip install -U torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117  # Ensure CUDA compatibility if you are using a GPU
pip install -U k-diffusion
```

#### 2. Verify Scheduler Compatibility

The Karras scheduler might be causing issues due to version mismatches or bugs in the latest release. You can try switching to another scheduler like "DDIM" to see if it resolves your problem:
- Navigate to your ComfyUI settings.
- Change the default scheduler from Karras to DDIM (or any other available scheduler).

If you still want to use the Karras scheduler, proceed with caution and ensure that all dependencies are correctly installed.

#### 3. Install or Reinstall Specific Dependency
Sometimes reinstalling a specific package can fix issues related to corrupted installs:
```bash
pip uninstall k-diffusion
pip install k-diffusion==<specific_version>  # Replace <specific_version> with the version you previously used that worked well.
```

#### 4. Check for GPU Support

Ensure your setup is properly configured to support GPU acceleration if you are using a CUDA-enabled device like an NVIDIA graphics card:
```bash
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
```
This installs PyTorch with CUDA 11.7 compatibility, which is important for GPU acceleration.

#### 5. Report and Monitor Issues

If the problem persists after trying these steps, consider reaching out to ComfyUI's community or developers by creating a detailed issue report on GitHub:
- Include your current Python version.
- List all installed packages with their versions using `pip freeze > requirements.txt`.
- Mention any error messages you see.

By following these steps, you should be able to resolve the black image issue in ComfyUI after updating. If issues persist or worsen, it might indicate a deeper compatibility problem that requires community input and further debugging.