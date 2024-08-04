'''
Author: combofish 
Date: 2024-08-04 10:02:59
LastEditors: combofish 35629257+combofish@users.noreply.github.com
LastEditTime: 2024-08-04 10:45:36
FilePath: \script-collection\bin\clipboard_listener\clipboard_listener.py
Description: 监听剪切板，并通过内容触发动作
'''
import sys
from PyQt5.QtWidgets import QApplication
import re
from open_webbrower import open_chrome_with_url
from icecream import ic


pattern = r'^https://365\.kdocs\.cn/'
pattern_2 = r'^https://kdocs\.cn/'

cnt = 0
prev_text = ''


def filter_content(text: str):
    # print(f'text2_{text}')

    global cnt

    if re.match(pattern, text.strip()) or re.match(pattern_2, text.strip()):
        # print(f"The website {text} starts with 'https://365.kdocs.cn/'")
        print(f"Matched. Run with {cnt}")
        open_chrome_with_url(text)
        cnt = cnt + 1
    else:
        # print(f"not error: {text}")
        pass


def on_clipboard_changed():
    global prev_text

    clipboard = QApplication.clipboard()
    mime_data = clipboard.mimeData()

    if mime_data.hasText():
        text = mime_data.text()
        if text != prev_text:
            prev_text = text
            print("\nDetected text on clipboard:", text)

            filter_content(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    clipboard = QApplication.clipboard()
    clipboard.dataChanged.connect(on_clipboard_changed)

    sys.exit(app.exec_())
