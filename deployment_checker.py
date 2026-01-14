import os
import json
import shutil

def check_file_exists(path):
    return os.path.exists(path)

def check_package_json():
    print("\n🔍 Checking package.json...")
    if not os.path.exists("package.json"):
        print("❌ package.json missing!")
        return
    
    with open("package.json", 'r') as f:
        data = json.load(f)
        
    deps = data.get('dependencies', {})
    devDeps = data.get('devDependencies', {})
    all_deps = {**deps, **devDeps}
    
    # Check for astro-compress
    if "astro-compress" in all_deps:
        print("⚠️ WARNING: 'astro-compress' found. Known to cause build issues on Cloudflare.")
    else:
        print("✅ 'astro-compress' not found (Good).")

    # Check for sharp
    if "sharp" in all_deps:
        print("ℹ️ NOTE: 'sharp' found. Ensure Node 18+ used (Fixed via .node-version).")
        
    # Check scripts
    if "build" not in data.get('scripts', {}):
        print("❌ Missing 'build' script!")
        
    print(f"✅ Engines: {data.get('engines', 'None')}")

def check_astro_config():
    print("\n🔍 Checking astro.config.mjs...")
    if not os.path.exists("astro.config.mjs"):
        print("❌ astro.config.mjs missing!")
        return
        
    with open("astro.config.mjs", 'r') as f:
        content = f.read()
        
    if "cloudflare" in content:
        print("ℹ️ Cloudflare adapter detected.")
        if "nodejs_compat" not in content and "wrangler" not in content:
             print("⚠️ Suggestion: Ensure 'nodejs_compat' flag if using Node built-ins.")
    else:
        print("ℹ️ Standard Astro Config (Static Build).")

def check_wrangler():
    print("\n🔍 Checking wrangler.toml...")
    if os.path.exists("wrangler.toml"):
        print("✅ wrangler.toml exists.")
        with open("wrangler.toml", 'r') as f:
            print(f.read())
    else:
        print("❌ wrangler.toml MISSING! (This is critical for silent failure fix)")

def check_functions():
    print("\n🔍 Checking functions/ directory...")
    if os.path.exists("functions"):
        size = 0
        for root, _, files in os.walk("functions"):
            for f in files:
                fp = os.path.join(root, f)
                size += os.path.getsize(fp)
        print(f"ℹ️ Functions dir exists. Size: {size} bytes.")
        if size > 10 * 1024 * 1024:
            print("❌ Functions bundle might be too large (>10MB).")
    else:
        print("✅ No 'functions' directory (Simpler build).")

def main():
    print("=== Cloudflare Deployment Readiness Checker ===")
    check_package_json()
    check_astro_config()
    check_wrangler()
    check_functions()
    
    # check node version files
    if os.path.exists(".node-version"):
        print(f"\n✅ .node-version: {open('.node-version').read().strip()}")
    else:
        print("\n❌ .node-version missing")

    if os.path.exists(".nvmrc"):
        print(f"✅ .nvmrc: {open('.nvmrc').read().strip()}")
    else:
        print("❌ .nvmrc missing")

if __name__ == "__main__":
    main()
