from playwright.sync_api import Playwright, sync_playwright, expect
from PIL import Image
from datetime import datetime, date, time, timezone
from pytz import utc
import gzip
import shutil
import os




def run(playwright: Playwright) -> None:
    # browser = playwright.chromium.launch(headless=)
    browser = playwright.chromium.launch()
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://dolarhoy.com/
    page.goto("https://dolarhoy.com/")
    page.screenshot(path="firstprint.jpg")

    # ---------------------
    context.close()
    browser.close()

    # Trabajo con las fechas
    datetime_print = datetime.now(tz=timezone.utc)
    name_print = datetime_print.strftime("%d%m%Y_%H%M%S")
    backup_name = datetime_print.strftime("%d%m%Y_%H")
    
    # Abro imagen, convierto a escala de grises y luego la guardo con otro nombre
    img = Image.open('firstprint.jpg')
    imgGray = img.convert('L')
    imgGray.save('IMG_' + name_print + '.jpg')

    #----------------------------------------------------   

    with open('IMG_' + name_print + '.jpg', 'rb') as f_in:
        with gzip.open('backup_' + backup_name + ".jpg.gz", "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    

   # compress(backup_name, data)
    
with sync_playwright() as playwright:
    run(playwright)


