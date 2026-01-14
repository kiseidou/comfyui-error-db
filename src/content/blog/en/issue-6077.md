### How to fix 'TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'' in ComfyUI

---

title: "How to fix 'TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'' in ComfyUI"
description: "Step-by-step fix for TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'"
pubDate: "2026-01-14"

---

### Introduction

The error `TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'` typically occurs when there is a mismatch between the version of ComfyUI and its dependencies. This can happen after updating ComfyUI or one of its libraries.

This guide provides a step-by-step solution to fix this issue for both beginners and advanced users.

### Cause

The error usually happens because `attn_mask` is being passed as an argument to `forward_orig()`, which does not expect such an argument. This often results from an outdated version of a dependency or a mismatch between ComfyUI versions and the versions of its dependencies, particularly in how attention mechanisms are implemented.

### Solution

To fix this issue, follow these steps:

#### Step 1: Backup Your Work
Before making any changes, it's always wise to back up your project files. This ensures that you have everything needed if something goes wrong during the update process.

#### Step 2: Check for Updates and Dependencies
Ensure that all of ComfyUI’s dependencies are up-to-date. The error might be due to a library incompatibility between versions. To update, use pip:

```bash
pip install --upgrade comfyui
```

If you are using specific packages or libraries (like transformers), make sure they are also updated to the latest version compatible with ComfyUI:

```bash
pip install --upgrade transformers
```

#### Step 3: Verify ComfyUI Version Compatibility
Check if there is a known issue related to your current versions of ComfyUI and its dependencies. Look for any documentation or GitHub issues related to this specific error.

#### Step 4: Manually Adjust the Code (Advanced)
If updating does not resolve the issue, you may need to manually adjust the code where the error occurs. In this case, it is within `nodes_custom_sampler.py` in ComfyUI's extras directory.

Locate the file:

```bash
F:\StabilityMatrix\Data\Packages\ComfyUI\comfy_extras\nodes_custom_sampler.py
```

Find the line causing the issue (around line 633 based on your logs):

```python
samples = guider.sample(noise.generate_noise(latent), latent)
```

Check if `guider.sample` method accepts an `attn_mask`. If it does not, and you are passing `attn_mask`, adjust the call to remove or handle `attn_mask` appropriately.

For example:

```python
if hasattr(guider.sample, 'attn_mask'):
    samples = guider.sample(noise.generate_noise(latent), latent, attn_mask=some_value)
else:
    samples = guider.sample(noise.generate_noise(latent), latent) # Remove or adjust the attn_mask argument here
```

#### Step 5: Re-run Your Workflow
After making these changes, try running your workflow again to see if the error is resolved.

### Conclusion

By following this guide, you should be able to resolve the `TypeError` related to unexpected arguments in ComfyUI. Always make sure that all components are compatible and up-to-date before running workflows to avoid similar issues.

If problems persist, consider reaching out to the ComfyUI community or checking for more detailed documentation on version compatibility and updates.