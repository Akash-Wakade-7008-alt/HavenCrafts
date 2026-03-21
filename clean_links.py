import os
import re

ROOT_DIR = "/Users/akashvikaswakade/Desktop/HavenCrafts"

def clean_file(path):
    if not os.path.exists(path): return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Clean up redundant parts
    content = content.replace('css/./css/', 'css/')
    content = content.replace('js/./js/', 'js/')
    content = content.replace('pages/./pages/', 'pages/')
    content = content.replace('pages/./', 'pages/')
    content = content.replace('css/./', 'css/')
    content = content.replace('js/./', 'js/')
    content = content.replace('href=".././css/', 'href="../css/')
    content = content.replace('src=".././js/', 'src="../js/')

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

clean_file(os.path.join(ROOT_DIR, "index.html"))

PAGES_DIR = os.path.join(ROOT_DIR, "pages")
for page in os.listdir(PAGES_DIR):
    if page.endswith(".html"):
        clean_file(os.path.join(PAGES_DIR, page))

JS_DIR = os.path.join(ROOT_DIR, "js")
for js in os.listdir(JS_DIR):
    if js.endswith(".js"):
        clean_file(os.path.join(JS_DIR, js))

print("Cleanup done")
