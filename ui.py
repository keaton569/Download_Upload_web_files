import tkinter as tk
from tkinter import filedialog, Text
import os
import urllib.request
import os
import csv
import time
import wx
import selenium
from os import listdir
from os.path import isfile, join
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import autoit



def addATCSV():
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\kbenning\\Desktop\\thumbnails\\script", title="Load CSV file", filetypes=(("CSV", "*.csv"), ("All Files", "*.*")))
    app = wx.App()
    with open(f'{filename}') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            driver = webdriver.Chrome()
            driver.set_page_load_timeout(4)
            driver.fullscreen_window()
            PROXY = "smartadv:picklestone@142.93.170.17"
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f'--proxy-server={PROXY}')
            webdriver.Chrome(options=chrome_options)

            for row in csv_reader:
                if line_count == 0:
                    print(f'Processed {row} lines.')
                    line_count += 1
                else:
                    try:
                        driver.get(f'{row[1]}')
                        driver.execute_script("document.body.style.zoom='70%'")
                        screen = wx.ScreenDC()
                        size = screen.GetSize()
                        bmp = wx.Bitmap(size[0], size[1])
                        mem = wx.MemoryDC(bmp)
                        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
                        del mem  # Release bitmap
                        bmp.SaveFile(f'C:\\Users\\kbenning\\Desktop\\savedImages\\{row[0]}.jpeg', wx.BITMAP_TYPE_JPEG)
                        count = 0
                        line_count += 1
                        print(f"{row[0]}: Successful")
                        time.sleep(2)
                    except urllib.error.HTTPError as e:
                        print(f'{row[0]}: '"error: ", e)
                    except TimeoutException as f:
                        print(f"{row[0]}: Page load Timeout Occured")
                    except selenium.common.exceptions.UnexpectedAlertPresentException as g:
                        print(f"{row[0]}: Alert Text Scam")
                    except selenium.common.exceptions.InvalidArgumentException as h:
                        print(f"{row[0]}: Invlaid Argument")
            print(f'Processed {line_count} lines.')

def addAUCSV():
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\kbenning\\Desktop\\thumbnails\\script", title="Load CSV file", filetypes=(("CSV", "*.csv"), ("All Files", "*.*")))
    app = wx.App()
    with open(f'{filename}') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            driver = webdriver.Chrome()
            driver.set_page_load_timeout(4)
            driver.fullscreen_window()
            PROXY = "119.252.16.207"
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f'--proxy-server={PROXY}')
            webdriver.Chrome(options=chrome_options)

            for row in csv_reader:
                if line_count == 0:
                    print(f'Processed {row} lines.')
                    line_count += 1
                else:
                    try:
                        driver.get(f'{row[1]}')
                        driver.execute_script("document.body.style.zoom='70%'")
                        screen = wx.ScreenDC()
                        size = screen.GetSize()
                        bmp = wx.Bitmap(size[0], size[1])
                        mem = wx.MemoryDC(bmp)
                        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
                        del mem  # Release bitmap
                        bmp.SaveFile(f'C:\\Users\\kbenning\\Desktop\\savedImages\\{row[0]}.jpeg', wx.BITMAP_TYPE_JPEG)
                        count = 0
                        line_count += 1
                        print(f"{row[0]}: Successful")
                        time.sleep(2)
                    except urllib.error.HTTPError as e:
                        print(f'{row[0]}: '"error: ", e)
                    except TimeoutException as f:
                        print(f"{row[0]}: Page load Timeout Occured")
                    except selenium.common.exceptions.UnexpectedAlertPresentException as g:
                        print(f"{row[0]}: Alert Text Scam")
                    except selenium.common.exceptions.InvalidArgumentException as h:
                        print(f"{row[0]}: Invlaid Argument")
            print(f'Processed {line_count} lines.')

def addBECSV():
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\kbenning\\Desktop\\thumbnails\\script", title="Load CSV file", filetypes=(("CSV", "*.csv"), ("All Files", "*.*")))
    app = wx.App()
    with open(f'{filename}') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            driver = webdriver.Chrome()
            driver.set_page_load_timeout(4)
            driver.fullscreen_window()
            PROXY = "82.102.19.69"
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f'--proxy-server={PROXY}')
            webdriver.Chrome(options=chrome_options)

            for row in csv_reader:
                if line_count == 0:
                    print(f'Processed {row} lines.')
                    line_count += 1
                else:
                    try:
                        driver.get(f'{row[1]}')
                        driver.execute_script("document.body.style.zoom='70%'")
                        screen = wx.ScreenDC()
                        size = screen.GetSize()
                        bmp = wx.Bitmap(size[0], size[1])
                        mem = wx.MemoryDC(bmp)
                        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
                        del mem  # Release bitmap
                        bmp.SaveFile(f'C:\\Users\\kbenning\\Desktop\\savedImages\\{row[0]}.jpeg', wx.BITMAP_TYPE_JPEG)
                        count = 0
                        line_count += 1
                        print(f"{row[0]}: Successful")
                        time.sleep(2)
                    except urllib.error.HTTPError as e:
                        print(f'{row[0]}: '"error: ", e)
                    except TimeoutException as f:
                        print(f"{row[0]}: Page load Timeout Occured")
                    except selenium.common.exceptions.UnexpectedAlertPresentException as g:
                        print(f"{row[0]}: Alert Text Scam")
                    except selenium.common.exceptions.InvalidArgumentException as h:
                        print(f"{row[0]}: Invlaid Argument")
            print(f'Processed {line_count} lines.')

def addCACSV():
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\kbenning\\Desktop\\thumbnails\\script", title="Load CSV file", filetypes=(("CSV", "*.csv"), ("All Files", "*.*")))
    app = wx.App()
    with open(f'{filename}') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            driver = webdriver.Chrome()
            driver.set_page_load_timeout(4)
            driver.fullscreen_window()
            PROXY = "107.6.27.129"
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f'--proxy-server={PROXY}')
            webdriver.Chrome(options=chrome_options)

            for row in csv_reader:
                if line_count == 0:
                    print(f'Processed {row} lines.')
                    line_count += 1
                else:
                    try:
                        driver.get(f'{row[1]}')
                        driver.execute_script("document.body.style.zoom='70%'")
                        screen = wx.ScreenDC()
                        size = screen.GetSize()
                        bmp = wx.Bitmap(size[0], size[1])
                        mem = wx.MemoryDC(bmp)
                        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
                        del mem  # Release bitmap
                        bmp.SaveFile(f'C:\\Users\\kbenning\\Desktop\\savedImages\\{row[0]}.jpeg', wx.BITMAP_TYPE_JPEG)
                        count = 0
                        line_count += 1
                        print(f"{row[0]}: Successful")
                        time.sleep(2)
                    except urllib.error.HTTPError as e:
                        print(f'{row[0]}: '"error: ", e)
                    except TimeoutException as f:
                        print(f"{row[0]}: Page load Timeout Occured")
                    except selenium.common.exceptions.UnexpectedAlertPresentException as g:
                        print(f"{row[0]}: Alert Text Scam")
                    except selenium.common.exceptions.InvalidArgumentException as h:
                        print(f"{row[0]}: Invlaid Argument")
            print(f'Processed {line_count} lines.')

def addDECSV():
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\kbenning\\Desktop\\thumbnails\\script", title="Load CSV file", filetypes=(("CSV", "*.csv"), ("All Files", "*.*")))
    app = wx.App()
    with open(f'{filename}') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            driver = webdriver.Chrome()
            print("created driver")
            driver.set_page_load_timeout(4)
            print("load tim at 4")
            driver.fullscreen_window()
            print("full screen")
            PROXY = "142.93.170.17"
            print("proxy")
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f'--proxy-server=http://{PROXY}')
            chrome_options.set_capability("PROXY", PROXY)
            webdriver.Chrome(options=chrome_options)

            for row in csv_reader:
                if line_count == 0:
                    print(f'Processed {row} lines.')
                    line_count += 1
                else:
                    try:
                        driver.get(f'{row[1]}')
                        driver.execute_script("document.body.style.zoom='70%'")
                        screen = wx.ScreenDC()
                        size = screen.GetSize()
                        bmp = wx.Bitmap(size[0], size[1])
                        mem = wx.MemoryDC(bmp)
                        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
                        del mem  # Release bitmap
                        bmp.SaveFile(f'C:\\Users\\kbenning\\Desktop\\savedImages\\{row[0]}.jpeg', wx.BITMAP_TYPE_JPEG)
                        count = 0
                        line_count += 1
                        print(f"{row[0]}: Successful")
                        time.sleep(2)
                    except urllib.error.HTTPError as e:
                        print(f'{row[0]}: '"error: ", e)
                    except TimeoutException as f:
                        print(f"{row[0]}: Page load Timeout Occured")
                    except selenium.common.exceptions.UnexpectedAlertPresentException as g:
                        print(f"{row[0]}: Alert Text Scam")
                    except selenium.common.exceptions.InvalidArgumentException as h:
                        print(f"{row[0]}: Invlaid Argument")
            print(f'Processed {line_count} lines.')

def addFRCSV():
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\kbenning\\Desktop\\thumbnails\\script", title="Load CSV file", filetypes=(("CSV", "*.csv"), ("All Files", "*.*")))
    app = wx.App()
    with open(f'{filename}') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            driver = webdriver.Chrome()
            driver.set_page_load_timeout(4)
            driver.fullscreen_window()
            PROXY = "46.226.105.208"
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f'--proxy-server={PROXY}')
            webdriver.Chrome(options=chrome_options)

            for row in csv_reader:
                if line_count == 0:
                    print(f'Processed {row} lines.')
                    line_count += 1
                else:
                    try:
                        driver.get(f'{row[1]}')
                        driver.execute_script("document.body.style.zoom='70%'")
                        screen = wx.ScreenDC()
                        size = screen.GetSize()
                        bmp = wx.Bitmap(size[0], size[1])
                        mem = wx.MemoryDC(bmp)
                        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
                        del mem  # Release bitmap
                        bmp.SaveFile(f'C:\\Users\\kbenning\\Desktop\\savedImages\\{row[0]}.jpeg', wx.BITMAP_TYPE_JPEG)
                        count = 0
                        line_count += 1
                        print(f"{row[0]}: Successful")
                        time.sleep(2)
                    except urllib.error.HTTPError as e:
                        print(f'{row[0]}: '"error: ", e)
                    except TimeoutException as f:
                        print(f"{row[0]}: Page load Timeout Occured")
                    except selenium.common.exceptions.UnexpectedAlertPresentException as g:
                        print(f"{row[0]}: Alert Text Scam")
                    except selenium.common.exceptions.InvalidArgumentException as h:
                        print(f"{row[0]}: Invlaid Argument")
            print(f'Processed {line_count} lines.')

def addITCSV():
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\kbenning\\Desktop\\thumbnails\\script", title="Load CSV file", filetypes=(("CSV", "*.csv"), ("All Files", "*.*")))
    app = wx.App()
    with open(f'{filename}') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            driver = webdriver.Chrome()
            driver.set_page_load_timeout(4)
            driver.fullscreen_window()
            PROXY = "192.121.46.225"
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f'--proxy-server={PROXY}')
            webdriver.Chrome(options=chrome_options)

            for row in csv_reader:
                if line_count == 0:
                    print(f'Processed {row} lines.')
                    line_count += 1
                else:
                    try:
                        driver.get(f'{row[1]}')
                        driver.execute_script("document.body.style.zoom='70%'")
                        screen = wx.ScreenDC()
                        size = screen.GetSize()
                        bmp = wx.Bitmap(size[0], size[1])
                        mem = wx.MemoryDC(bmp)
                        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
                        del mem  # Release bitmap
                        bmp.SaveFile(f'C:\\Users\\kbenning\\Desktop\\savedImages\\{row[0]}.jpeg', wx.BITMAP_TYPE_JPEG)
                        count = 0
                        line_count += 1
                        print(f"{row[0]}: Successful")
                        time.sleep(2)
                    except urllib.error.HTTPError as e:
                        print(f'{row[0]}: '"error: ", e)
                    except TimeoutException as f:
                        print(f"{row[0]}: Page load Timeout Occured")
                    except selenium.common.exceptions.UnexpectedAlertPresentException as g:
                        print(f"{row[0]}: Alert Text Scam")
                    except selenium.common.exceptions.InvalidArgumentException as h:
                        print(f"{row[0]}: Invlaid Argument")
            print(f'Processed {line_count} lines.')

def addNLCSV():
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\kbenning\\Desktop\\thumbnails\\script", title="Load CSV file", filetypes=(("CSV", "*.csv"), ("All Files", "*.*")))
    app = wx.App()
    with open(f'{filename}') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            driver = webdriver.Chrome()
            driver.set_page_load_timeout(4)
            driver.fullscreen_window()
            PROXY = "191.101.21.160"
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f'--proxy-server={PROXY}')
            webdriver.Chrome(options=chrome_options)

            for row in csv_reader:
                if line_count == 0:
                    print(f'Processed {row} lines.')
                    line_count += 1
                else:
                    try:
                        driver.get(f'{row[1]}')
                        driver.execute_script("document.body.style.zoom='70%'")
                        screen = wx.ScreenDC()
                        size = screen.GetSize()
                        bmp = wx.Bitmap(size[0], size[1])
                        mem = wx.MemoryDC(bmp)
                        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
                        del mem  # Release bitmap
                        bmp.SaveFile(f'C:\\Users\\kbenning\\Desktop\\savedImages\\{row[0]}.jpeg', wx.BITMAP_TYPE_JPEG)
                        count = 0
                        line_count += 1
                        print(f"{row[0]}: Successful")
                        time.sleep(2)
                    except urllib.error.HTTPError as e:
                        print(f'{row[0]}: '"error: ", e)
                    except TimeoutException as f:
                        print(f"{row[0]}: Page load Timeout Occured")
                    except selenium.common.exceptions.UnexpectedAlertPresentException as g:
                        print(f"{row[0]}: Alert Text Scam")
                    except selenium.common.exceptions.InvalidArgumentException as h:
                        print(f"{row[0]}: Invlaid Argument")
            print(f'Processed {line_count} lines.')

def addNOCSV():
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\kbenning\\Desktop\\thumbnails\\script", title="Load CSV file", filetypes=(("CSV", "*.csv"), ("All Files", "*.*")))
    app = wx.App()
    with open(f'{filename}') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            driver = webdriver.Chrome()
            driver.set_page_load_timeout(4)
            driver.fullscreen_window()
            PROXY = "185.243.217.100"
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f'--proxy-server={PROXY}')
            webdriver.Chrome(options=chrome_options)

            for row in csv_reader:
                if line_count == 0:
                    print(f'Processed {row} lines.')
                    line_count += 1
                else:
                    try:
                        driver.get(f'{row[1]}')
                        driver.execute_script("document.body.style.zoom='70%'")
                        screen = wx.ScreenDC()
                        size = screen.GetSize()
                        bmp = wx.Bitmap(size[0], size[1])
                        mem = wx.MemoryDC(bmp)
                        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
                        del mem  # Release bitmap
                        bmp.SaveFile(f'C:\\Users\\kbenning\\Desktop\\savedImages\\{row[0]}.jpeg', wx.BITMAP_TYPE_JPEG)
                        count = 0
                        line_count += 1
                        print(f"{row[0]}: Successful")
                        time.sleep(2)
                    except urllib.error.HTTPError as e:
                        print(f'{row[0]}: '"error: ", e)
                    except TimeoutException as f:
                        print(f"{row[0]}: Page load Timeout Occured")
                    except selenium.common.exceptions.UnexpectedAlertPresentException as g:
                        print(f"{row[0]}: Alert Text Scam")
                    except selenium.common.exceptions.InvalidArgumentException as h:
                        print(f"{row[0]}: Invlaid Argument")
            print(f'Processed {line_count} lines.')

def addNZCSV():
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\kbenning\\Desktop\\thumbnails\\script", title="Load CSV file", filetypes=(("CSV", "*.csv"), ("All Files", "*.*")))
    app = wx.App()
    with open(f'{filename}') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            driver = webdriver.Chrome()
            driver.set_page_load_timeout(4)
            driver.fullscreen_window()
            PROXY = "119.252.16.207"
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f'--proxy-server={PROXY}')
            webdriver.Chrome(options=chrome_options)

            for row in csv_reader:
                if line_count == 0:
                    print(f'Processed {row} lines.')
                    line_count += 1
                else:
                    try:
                        driver.get(f'{row[1]}')
                        driver.execute_script("document.body.style.zoom='70%'")
                        screen = wx.ScreenDC()
                        size = screen.GetSize()
                        bmp = wx.Bitmap(size[0], size[1])
                        mem = wx.MemoryDC(bmp)
                        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
                        del mem  # Release bitmap
                        bmp.SaveFile(f'C:\\Users\\kbenning\\Desktop\\savedImages\\{row[0]}.jpeg', wx.BITMAP_TYPE_JPEG)
                        count = 0
                        line_count += 1
                        print(f"{row[0]}: Successful")
                        time.sleep(2)
                    except urllib.error.HTTPError as e:
                        print(f'{row[0]}: '"error: ", e)
                    except TimeoutException as f:
                        print(f"{row[0]}: Page load Timeout Occured")
                    except selenium.common.exceptions.UnexpectedAlertPresentException as g:
                        print(f"{row[0]}: Alert Text Scam")
                    except selenium.common.exceptions.InvalidArgumentException as h:
                        print(f"{row[0]}: Invlaid Argument")
            print(f'Processed {line_count} lines.')

def addSECSV():
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\kbenning\\Desktop\\thumbnails\\script", title="Load CSV file", filetypes=(("CSV", "*.csv"), ("All Files", "*.*")))
    app = wx.App()
    with open(f'{filename}') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            driver = webdriver.Chrome()
            driver.set_page_load_timeout(4)
            driver.fullscreen_window()
            PROXY = "185.86.149.109"
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f'--proxy-server={PROXY}')
            webdriver.Chrome(options=chrome_options)

            for row in csv_reader:
                if line_count == 0:
                    print(f'Processed {row} lines.')
                    line_count += 1
                else:
                    try:
                        driver.get(f'{row[1]}')
                        driver.execute_script("document.body.style.zoom='70%'")
                        screen = wx.ScreenDC()
                        size = screen.GetSize()
                        bmp = wx.Bitmap(size[0], size[1])
                        mem = wx.MemoryDC(bmp)
                        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
                        del mem  # Release bitmap
                        bmp.SaveFile(f'C:\\Users\\kbenning\\Desktop\\savedImages\\{row[0]}.jpeg', wx.BITMAP_TYPE_JPEG)
                        count = 0
                        line_count += 1
                        print(f"{row[0]}: Successful")
                        time.sleep(2)
                    except urllib.error.HTTPError as e:
                        print(f'{row[0]}: '"error: ", e)
                    except TimeoutException as f:
                        print(f"{row[0]}: Page load Timeout Occured")
                    except selenium.common.exceptions.UnexpectedAlertPresentException as g:
                        print(f"{row[0]}: Alert Text Scam")
                    except selenium.common.exceptions.InvalidArgumentException as h:
                        print(f"{row[0]}: Invlaid Argument")
            print(f'Processed {line_count} lines.')

def addUKCSV():
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\kbenning\\Desktop\\thumbnails\\script", title="Load CSV file", filetypes=(("CSV", "*.csv"), ("All Files", "*.*")))
    app = wx.App()
    with open(f'{filename}') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            driver = webdriver.Chrome()
            driver.set_page_load_timeout(4)
            driver.fullscreen_window()
            PROXY = "77.81.107.159"
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f'--proxy-server={PROXY}')
            webdriver.Chrome(options=chrome_options)

            for row in csv_reader:
                if line_count == 0:
                    print(f'Processed {row} lines.')
                    line_count += 1
                else:
                    try:
                        driver.get(f'{row[1]}')
                        driver.execute_script("document.body.style.zoom='70%'")
                        screen = wx.ScreenDC()
                        size = screen.GetSize()
                        bmp = wx.Bitmap(size[0], size[1])
                        mem = wx.MemoryDC(bmp)
                        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
                        del mem  # Release bitmap
                        bmp.SaveFile(f'C:\\Users\\kbenning\\Desktop\\savedImages\\{row[0]}.jpeg', wx.BITMAP_TYPE_JPEG)
                        count = 0
                        line_count += 1
                        print(f"{row[0]}: Successful")
                        time.sleep(2)
                    except urllib.error.HTTPError as e:
                        print(f'{row[0]}: '"error: ", e)
                    except TimeoutException as f:
                        print(f"{row[0]}: Page load Timeout Occured")
                    except selenium.common.exceptions.UnexpectedAlertPresentException as g:
                        print(f"{row[0]}: Alert Text Scam")
                    except selenium.common.exceptions.InvalidArgumentException as h:
                        print(f"{row[0]}: Invlaid Argument")
            print(f'Processed {line_count} lines.')

def addUSCSV():
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\kbenning\\Desktop\\thumbnails\\script", title="Load CSV file", filetypes=(("CSV", "*.csv"), ("All Files", "*.*")))
    app = wx.App()
    with open(f'{filename}') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            driver = webdriver.Chrome()
            driver.set_page_load_timeout(4)
            driver.fullscreen_window()

            for row in csv_reader:
                if line_count == 0:
                    print(f'Processed {row} lines.')
                    line_count += 1
                else:
                    try:
                        driver.get(f'{row[1]}')
                        driver.execute_script("document.body.style.zoom='70%'")
                        time.sleep(2)
                        screen = wx.ScreenDC()
                        size = screen.GetSize()
                        bmp = wx.Bitmap(size[0], size[1])
                        mem = wx.MemoryDC(bmp)
                        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
                        del mem  # Release bitmap
                        bmp.SaveFile(f'C:\\Users\\kbenning\\Desktop\\uploadMe\\{row[0]}.jpeg', wx.BITMAP_TYPE_JPEG)
                        count = 0
                        line_count += 1
                        print(f"{row[0]}: Successful")
                        time.sleep(2)
                    except urllib.error.HTTPError as e:
                        print(f'{row[0]}: '"error: ", e)
                    except TimeoutException as f:
                        print(f"{row[0]}: Page load Timeout Occured")
                    except selenium.common.exceptions.UnexpectedAlertPresentException as g:
                        print(f"{row[0]}: Alert Text Scam")
                    except selenium.common.exceptions.InvalidArgumentException as h:
                        print(f"{row[0]}: Invlaid Argument")
            print(f'Processed {line_count} lines.')

def uploadImages():
    savedDir = filedialog.askdirectory(initialdir="\\Desktop", title="Load Directory")
    fileNames = [f for f in listdir(f"{savedDir}") if isfile(join(f"{savedDir}", f))]
    print(fileNames)
    fileNamesFinal = ([s.strip('.jpg') for s in fileNames])


    driver = webdriver.Chrome()
    driver.get(f'https://portal.smartadv.com/')
    username = driver.find_element_by_id("email")
    username.clear()
    username.send_keys("{nope}")
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("{also nope}")
    driver.find_element_by_xpath("//*[@id='login']/div[2]/div[2]/div/form/button").click()
    time.sleep(5)
    count = 0

    for file in fileNamesFinal:
        count += 1
        driver.get(f'https://portal.smartadv.com/offers/{file}/edit?tab=creatives')
        time.sleep(7)
        try:
            driver.find_element_by_xpath("//*[@id='tabs-container']/div[7]/ef-offer-creative-form/form/div[1]/div[2]/ef-file-uploader/div/div[1]/div[3]/i").click()
            driver.find_element_by_xpath("//*[@id='tabs-container']/div[7]/ef-offer-creative-form/form/div[1]/div[2]/ef-file-uploader/div/div[1]/ef-input/input").click()
            autoit.win_wait("[CLASS:#32770;TITLE:Open]", 2)
            path = os.path.join('C:\\Users\\kbenning\\Desktop\\uploadMe\\done', "{}.jpg".format(file))
            print(path)
            print(count)
            autoit.control_set_text("[CLASS:#32770;TITLE:Open]", "Edit1", os.path.join('C:\\Users\\kbenning\\Desktop\\uploadMe\\done', "{}.jpg".format(file)))
            autoit.control_click("[CLASS:#32770;TITLE:Open]", "Button1")
            time.sleep(3)
            driver.find_element_by_xpath("//*[@id='app-tmpl']/div[1]/ef-app-layout/div[1]/div/div/ui-view/ui-view/ef-offer-form/div/ef-form-action-bar/div/div/div[2]/ef-button[2]/ef-tooltip/div/div[1]/button").click()
            time.sleep(3)
        except selenium.common.exceptions.NoSuchElementException as e:
            driver.find_element_by_xpath("//*[@id='tabs-container']/div[7]/ef-offer-creative-form/form/div[1]/div[2]/ef-file-uploader/div/div[1]/ef-input/input").click()
            autoit.win_wait("[CLASS:#32770;TITLE:Open]", 2)
            path = os.path.join('C:\\Users\\kbenning\\Desktop\\uploadMe\\done', "{}.jpg".format(file))
            print(path)
            print(count)
            autoit.control_set_text("[CLASS:#32770;TITLE:Open]", "Edit1", os.path.join('C:\\Users\\kbenning\\Desktop\\uploadMe\\done', "{}.jpg".format(file)))
            autoit.control_click("[CLASS:#32770;TITLE:Open]", "Button1")
            time.sleep(3)
            driver.find_element_by_xpath("//*[@id='app-tmpl']/div[1]/ef-app-layout/div[1]/div/div/ui-view/ui-view/ef-offer-form/div/ef-form-action-bar/div/div/div[2]/ef-button[2]/ef-tooltip/div/div[1]/button").click()
            time.sleep(3)





root = tk.Tk()
canvas = tk.Canvas(root, height=700, width=700, bg="#091040")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=".9", relheight=".9", relx=".05", rely=".05")

AT = tk.Button(frame, text="AT sites", padx=10, pady=5, fg="black", bg="#45a0c4", command=addATCSV, font="lato", width="300")
AT.pack()

AU = tk.Button(frame, text="AU sites", padx=10, pady=5, fg="black", bg="#45a0c4", command=addAUCSV, font="lato", width="300")
AU.pack()

BE = tk.Button(frame, text="BE sites", padx=10, pady=5, fg="black", bg="#45a0c4", command=addBECSV, font="lato", width="300")
BE.pack()

CA = tk.Button(frame, text="CA sites", padx=10, pady=5, fg="black", bg="#45a0c4", command=addCACSV, font="lato", width="300")
CA.pack()

DE = tk.Button(frame, text="DE sites", padx=10, pady=5, fg="black", bg="#45a0c4", command=addDECSV, font="lato", width="300")
DE.pack()

FR = tk.Button(frame, text="FR sites", padx=10, pady=5, fg="black", bg="#45a0c4", command=addFRCSV, font="lato", width="300")
FR.pack()

IT = tk.Button(frame, text="IT sites", padx=10, pady=5, fg="black", bg="#45a0c4", command=addITCSV, font="lato", width="300")
IT.pack()

NL = tk.Button(frame, text="NL sites", padx=10, pady=5, fg="black", bg="#45a0c4", command=addNLCSV, font="lato", width="300")
NL.pack()

NO = tk.Button(frame, text="NO sites", padx=10, pady=5, fg="black", bg="#45a0c4", command=addNOCSV, font="lato", width="300")
NO.pack()

NZ = tk.Button(frame, text="NZ sites", padx=10, pady=5, fg="black", bg="#45a0c4", command=addNZCSV, font="lato", width="300")
NZ.pack()

SE = tk.Button(frame, text="SE sites", padx=10, pady=5, fg="black", bg="#45a0c4", command=addSECSV, font="lato", width="300")
SE.pack()

UK = tk.Button(frame, text="UK sites", padx=10, pady=5, fg="black", bg="#45a0c4", command=addUKCSV, font="lato", width="300")
UK.pack()

US = tk.Button(frame, text="US sites UPDATE BEFORE ALL USES", padx=10, pady=5, fg="black", bg="#45a0c4", command=addUSCSV, font="lato", width="300")
US.pack()

UPLOAD = tk.Button(frame, text="UPLOAD", padx=10, pady=5, fg="black", bg="#45a0c4", command=uploadImages, font="lato", width="300")
UPLOAD.pack()




root.mainloop()
