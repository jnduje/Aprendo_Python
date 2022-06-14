from playwright.sync_api import Playwright, sync_playwright, expect
from skimage import color
from skimage import io



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

    img = io.imread('firstprint.jpg')
    imgGray = color.rgb2gray(img)

with sync_playwright() as playwright:
    run(playwright)


