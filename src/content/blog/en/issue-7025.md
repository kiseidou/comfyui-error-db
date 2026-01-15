---
title: "How to fix '[Announcement] The frontend will no longer be shipped in the main ComfyUI repo, it will be a separate pip package instead.'"
description: "Step-by-step guide for fixing issues related to the change where the ComfyUI frontend is now a separate pip package."
pubDate: "2026-01-15"
---

### Introduction

The ComfyUI project has undergone an important update: the frontend codebase will no longer be part of the main repository. Instead, it will be managed as a separate Python package that can be installed via `pip`. This change helps streamline the development process and keeps the main repo leaner.

If you encounter issues after this change is implemented, particularly if you use manual updates with `git pull`, follow these steps to ensure your environment stays up-to-date.

### Understanding the Change

The ComfyUI frontend was previously included in the main repository. However, now it's maintained separately as a pip package. This means that when updating via Git, you must also update this separate frontend component manually using pip commands.

### Steps to Fix the Issue

#### Step 1: Ensure You Have Python and Pip Installed
Before proceeding, make sure your environment has both Python and `pip` installed.

```bash
python --version
pip --version
```

If these commands do not work or show outdated versions, you may need to install or update Python and pip on your system. See the official documentation for instructions tailored to your operating system.

#### Step 2: Update ComfyUI as Usual (For Manual Git Users)

If you manually pull updates from the main repository using `git`, after the frontend separation is implemented, follow these steps:

1. **Update the Main Repository**:
   First, update the main ComfyUI codebase via git.

   ```bash
   cd path/to/ComfyUI
   git pull origin main
   ```

2. **Install Frontend Dependencies**:
   After updating the repository, you will need to install or upgrade the frontend dependencies using pip. Navigate to your project directory and run:

   ```bash
   pip install -r requirements.txt
   ```

   This command installs all necessary packages specified in `requirements.txt`, which now includes the standalone ComfyUI frontend package.

#### Step 3: Verify Installation

After running these commands, verify that everything is working correctly by starting your ComfyUI application and checking if the frontend loads as expected. If you encounter any issues, check for error messages related to missing dependencies or incorrect paths and resolve accordingly.

### Summary

By following these steps, you ensure that both the main ComfyUI codebase and its newly separated frontend are updated properly when using manual Git updates. The key is remembering to install or update frontend dependencies via pip after updating the core repository.

For users relying on the automatic update scripts (`update/update_comfyui.bat`), no changes should be necessary as these tools have been adjusted to handle this new structure seamlessly.

### Conclusion

This change simplifies maintenance and reduces bloat in the main ComfyUI repository. By installing the frontend via pip, you benefit from an optimized development workflow. If you encounter any issues or need further assistance, consider reaching out to the community or checking out the official documentation for more detailed guidance.

Happy coding!