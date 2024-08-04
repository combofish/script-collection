'''
Author: combofish 
Date: 2024-08-04 10:06:30
LastEditors: combofish 35629257+combofish@users.noreply.github.com
LastEditTime: 2024-08-04 10:53:14
FilePath: \script-collection\bin\clipboard_listener\open_webbrower.py
Description: 让浏览器打开指定网址
'''
import subprocess
import os


def open_chrome_with_url(url="https://www.example.com"):
    print(f"Start to open >>> {url}", end='')

    # browser_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # 指定浏览器路径
    browser_path = r'~\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe'
    browser_path = browser_path.replace('\\\\', '\\')
    browser_path = os.path.expanduser(browser_path)
    browser_path = browser_path.replace('\\', '\\\\')

    # print(browser_path)

    subprocess.Popen([browser_path, url])

    print(" <<< Down!")


if __name__ == '__main__':
    open_chrome_with_url()
