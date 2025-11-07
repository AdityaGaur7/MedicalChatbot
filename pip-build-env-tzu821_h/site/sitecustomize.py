
import os, site, sys

# First, drop system-sites related paths.
original_sys_path = sys.path[:]
known_paths = set()
for path in {'c:\\users\\91884\\favorites\\onedrive\\desktop\\medicalchatbot\\.venv\\lib\\site-packages', 'c:\\users\\91884\\favorites\\onedrive\\desktop\\medicalchatbot\\.venv'}:
    site.addsitedir(path, known_paths=known_paths)
system_paths = set(
    os.path.normcase(path)
    for path in sys.path[len(original_sys_path):]
)
original_sys_path = [
    path for path in original_sys_path
    if os.path.normcase(path) not in system_paths
]
sys.path = original_sys_path

# Second, add lib directories.
# ensuring .pth file are processed.
for path in ['C:\\Users\\91884\\Favorites\\OneDrive\\Desktop\\MedicalChatbot\\Build-a-Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask-AWS-main\\pip-build-env-tzu821_h\\overlay\\Lib\\site-packages', 'C:\\Users\\91884\\Favorites\\OneDrive\\Desktop\\MedicalChatbot\\Build-a-Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask-AWS-main\\pip-build-env-tzu821_h\\normal\\Lib\\site-packages']:
    assert not path in sys.path
    site.addsitedir(path)
