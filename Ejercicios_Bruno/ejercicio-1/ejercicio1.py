from pickle import FALSE, TRUE
from playwright.sync_api import Playwright, sync_playwright, expect
from PIL import Image
from datetime import datetime, date, time, timezone
from pytz import utc
import gzip
import shutil
from os import remove, path
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

    #Comprimo la imagen  
    with open('IMG_' + name_print + '.jpg', 'rb') as f_in:
        with gzip.open('IMG_' + name_print + '.jpg.gz', "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)

    #Verifico si existe la carpeta sino la creo
    if path.exists('BACKUP_' + backup_name) == False:
        os.makedirs('BACKUP_' + backup_name)
   
    source = 'IMG_' + name_print + '.jpg.gz'
    destination = 'BACKUP_' + backup_name + '\\' + 'IMG_' + name_print + '.jpg.gz'
    shutil.move(source,destination)

    #Elimino los archivos sobrantes
    os.remove('firstprint.jpg')
    os.remove('IMG_' + name_print + '.jpg')
   
    
with sync_playwright() as playwright:
    run(playwright)


