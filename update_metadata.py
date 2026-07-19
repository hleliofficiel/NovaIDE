import os
def update_file(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except Exception:
        return
    original = content
    content = content.replace("AndroidIDE", "NovaIDE")
    content = content.replace("androidide", "novaide")
    content = content.replace("com.itsaky.novaide", "com.itsaky.androidide")
    if original != content:
        with open(filepath, 'w') as f:
            f.write(content)

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'build' in root:
        continue
    for file in files:
        if file.endswith('.yml') or file.endswith('.yaml') or 'fastlane' in root:
            update_file(os.path.join(root, file))
