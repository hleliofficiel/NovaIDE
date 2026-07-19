import os
def update_file(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except Exception:
        return
    original = content
    content = content.replace('rootProject.name = "AndroidIDE"', 'rootProject.name = "NovaIDE"')
    # If there are any other branding references like plugin classes, let's keep them as AndroidIDEPlugin because we didn't rename classes.
    if original != content:
        with open(filepath, 'w') as f:
            f.write(content)

update_file('settings.gradle.kts')
update_file('build.gradle.kts')
