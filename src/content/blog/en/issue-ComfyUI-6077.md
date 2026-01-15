### How to fix 'TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'' in ComfyUI

---

title: "How to fix 'TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'' in ComfyUI"
description: "Step-by-step fix for TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'"
pubDate: "2026-01-15"

---

## Explanation and Solution

This issue typically arises when the version of a library or package you are using does not support certain arguments, such as `attn_mask`. In your case, it appears that an update to ComfyUI or one of its dependencies has introduced this error. Here's how you can resolve it:

### Step 1: Identify Affected Dependencies
The error message suggests a conflict with the `forward_orig` method in the context of sampling operations within ComfyUI.

### Step 2: Check for Library Updates and Compatibility
Check if there are updates available for any libraries that could be causing this issue. Often, developers release patches or minor versions to address such compatibility issues.

- **Identify conflicting library version:** This can often be determined by reviewing the commit history on GitHub, specifically looking at changes around the time you started experiencing this error.
  
### Step 3: Downgrade Dependencies
If a newer version of ComfyUI or one of its dependencies is causing the issue, downgrading to an older version that works might be necessary.

```bash
# Uninstall current conflicting library versions (example)
pip uninstall transformers comfyui

# Install previous working version if available
pip install transformers==X.X.X comfyui==Y.Y.Y
```

### Step 4: Patching the Code
If downgrading is not an option or does not resolve the issue, you might need to patch the ComfyUI code itself. This involves finding where `forward_orig` is defined and ensuring that it correctly handles the `attn_mask` argument.

1. **Locate the Issue:**
   - Navigate to the file mentioned in the stack trace (`nodes_custom_sampler.py`).
   - Find the line number indicated (around 633).

2. **Modify or Comment Out Code:**
   - Temporarily comment out or modify the problematic code segment until a proper fix can be implemented.

```python
# Before modification:
samples = guider.sample(noise.generate_noise(latent), latent)

# Potential modification to handle attn_mask argument if applicable
if 'attn_mask' in inputs:
    samples = guider.sample(noise.generate_noise(latent), latent, attn_mask=inputs['attn_mask'])
else:
    samples = guider.sample(noise.generate_noise(latent), latent)
```

3. **Test Changes:**
   - Save your changes and re-run the ComfyUI workflow to see if the error persists.

### Step 5: Report Issue
If you are unable to resolve the issue through these steps, it's important to report this bug back to the developers of ComfyUI or the relevant library via their GitHub repository. Provide them with:

- The complete stack trace.
- Your current environment setup and versions of all dependencies installed.
- Any modifications you've made to address the problem.

### Conclusion

This guide should help resolve the `TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'` error in ComfyUI by either downgrading problematic libraries or patching your local copy. Always ensure that any changes are tested thoroughly before deploying them in production environments.

For further assistance, consider reaching out to developer communities associated with ComfyUI and related projects on platforms like GitHub Discussions or dedicated forums.