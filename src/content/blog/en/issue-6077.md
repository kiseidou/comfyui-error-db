### How to fix 'TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'' in ComfyUI

---

title: "How to fix 'TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'' in ComfyUI"
description: "Step-by-step fix for TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'"
pubDate: "2026-01-15"

---

### Body

The error `TypeError: forward_orig() got an unexpected keyword argument 'attn_mask'` in ComfyUI typically occurs when there is a mismatch between the version of the model or library you are using and the expected input parameters. Specifically, this issue usually arises due to outdated dependencies or changes in API versions.

#### Cause

The error message suggests that `forward_orig()` function does not accept an argument called `'attn_mask'`. This can happen if there were recent updates to ComfyUI or related libraries (like Transformers) and these updates might have deprecated certain features or changed the interface of some functions.

#### Solution Steps for Beginners

1. **Backup Your Work**: Before making any changes, it's a good practice to back up your project files in case something goes wrong during the update process.

2. **Check ComfyUI Version**:
   - Open a terminal and navigate to your ComfyUI directory.
   - Run `python -c "import comfy; print(comfy.__version__)"` to check which version of ComfyUI you are currently running.
   - Compare this with the latest stable release available on GitHub or PyPI.

3. **Update ComfyUI**:
   - To update ComfyUI, follow these steps:
     ```sh
     pip uninstall comfyui  # Uninstall current installation if any
     git clone https://github.com/your-comfyui-repo.git  # Clone the latest version from GitHub
     cd your-comfyui-repo
     pip install .  # Install the updated package
     ```

4. **Update Dependencies**:
   - Sometimes, updating ComfyUI alone isn't enough due to changes in dependencies.
   - Check for updates in related libraries such as `transformers` or others by running:
     ```sh
     pip list --outdated
     ```
   - Update these libraries if necessary:
     ```sh
     pip install transformers==<latest_version>  # Replace <latest_version> with the latest version number
     ```

5. **Review Configuration Files**:
   - If you have configuration files that set specific parameters like `'attn_mask'`, review them to ensure they are compatible with the updated versions.
   - Remove or adjust any deprecated arguments based on the documentation.

6. **Test Your Workflow**:
   - After updating, test your workflow using a simpler or known-working node setup first to see if issues persist.
   - Gradually reintroduce complex setups like FLUX Redux + Pull ID Image to Image Face Swap and monitor for errors.

7. **Report Back If Issues Persist**:
   - If you continue experiencing issues after the update process, it’s advisable to report back with detailed error messages, steps taken so far, and any relevant logs or files (like JSON configurations).

#### Example Commands

Here are some example commands that might help in resolving the issue:

- Uninstalling old version of ComfyUI:
  ```sh
  pip uninstall comfyui
  ```
  
- Installing latest ComfyUI from GitHub:
  ```sh
  git clone https://github.com/your-comfyui-repo.git
  cd your-comfyui-repo
  pip install .
  ```

- Updating Transformers to the latest version (if needed):
  ```sh
  pip install transformers --upgrade
  ```

By following these steps, you should be able to resolve the issue with the unexpected keyword argument error and get ComfyUI running smoothly again.