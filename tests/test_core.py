import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import re
import time


@allure.story("Тест наличия картины Трамвайный путь в списке, Chrome")
@allure.severity("critical")
def test_tram_track_chrome():
    with allure.step("Создаем драйвер, открываем окно на полный экран, переходим на сайт"):
        try:
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://artnow.ru")
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Открываем выпадающий список"):
        try:
            drop_down_list = driver.find_element(
                By.CSS_SELECTOR,
                "#left_container > div > ul:nth-child(2) > li.menu-group.gids > div")
            drop_down_list.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Переходим в вышитые картины"):
        try:
            paintings = driver.find_element(By.CSS_SELECTOR,
                                            "#left_container > div > ul:nth-child(2) > li:nth-child(8) > a")
            paintings.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Выбираем жанр Городской пейзаж"):
        try:
            city_landscape = driver.find_element(By.CSS_SELECTOR,
                                                 "#genrebox > div > label:nth-child(2)")
            city_landscape.click()
            city_landscape.send_keys(Keys.ENTER)
            time.sleep(3)
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Ищем Трамвайный путь среди картин"):
        try:
            response = re.findall(r'<meta itemprop="description" content="(.*)">', str(driver.page_source))
            flag = False
            for item in response:
                if "Трамвайный путь" in item:
                    flag = True
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()

    try:
        assert flag
    except AssertionError("Указанной картины нет в списке"):
        with allure.step("Делаем скриншот ошибки"):
            allure.attach(driver.get_screenshot_as_png(), name="chrome_error", attachment_type=AttachmentType.PNG)
        driver.close()
        driver.quit()

    with allure.step("Закрываем драйвер"):
        try:
            driver.close()
            driver.quit()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()


@allure.story("Тест жанра картины Трамвайный путь - реализм, Chrome")
@allure.severity("critical")
def test_tram_track_specs_chrome():
    with allure.step("Создаем драйвер, открываем окно на полный экран, переходим на сайт"):
        try:
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://artnow.ru")
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Открываем выпадающий список"):
        try:
            drop_down_list = driver.find_element(
                By.CSS_SELECTOR,
                "#left_container > div > ul:nth-child(2) > li.menu-group.gids > div")
            drop_down_list.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Переходим в вышитые картины"):
        try:
            paintings = driver.find_element(By.CSS_SELECTOR,
                                            "#left_container > div > ul:nth-child(2) > li:nth-child(8) > a")
            paintings.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Выбираем жанр Городской пейзаж"):
        try:
            city_landscape = driver.find_element(By.CSS_SELECTOR,
                                                 "#genrebox > div > label:nth-child(2)")
            city_landscape.click()
            city_landscape.send_keys(Keys.ENTER)
            time.sleep(3)
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Открываем картину трамвайный путь"):
        try:
            tram_track = driver.find_element(By.CSS_SELECTOR, "#sa_container > div:nth-child(5) > a > div")
            tram_track.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Проверяем жанр картины на реализм"):
        try:
            response = str(re.search(r'Стиль: (.*?)\.', str(driver.page_source)).group())
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    try:
        assert "реализм" in response
    except AssertionError("Жанр картины - не реализм"):
        with allure.step("Делаем скриншот ошибки"):
            allure.attach(driver.get_screenshot_as_png(), name="chrome_error", attachment_type=AttachmentType.PNG)
        driver.close()
        driver.quit()
    with allure.step("Закрываем драйвер"):
        try:
            driver.close()
            driver.quit()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()


@allure.story("Тест добавления товара в избранное, Chrome")
@allure.severity("critical")
def test_add_to_favorites_chrome():
    with allure.step("Создаем драйвер, открываем окно на полный экран, переходим на сайт"):
        try:
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://artnow.ru")
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Открываем выпадающий список"):
        try:
            drop_down_list = driver.find_element(
                By.CSS_SELECTOR,
                "#left_container > div > ul:nth-child(2) > li.menu-group.gids > div")
            drop_down_list.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Переходим в батик"):
        try:
            paintings = driver.find_element(By.CSS_SELECTOR,
                                            "#left_container > div > ul:nth-child(2) > li:nth-child(3) > a")
            paintings.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Выбираем первую картину и открываем ее"):
        try:
            chosen_painting = driver.find_element(By.CSS_SELECTOR,
                                                  "#sa_container > div:nth-child(3) > a:nth-child(1) > div")
            chosen_painting.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), nname="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Добавляем ее в избранное, сохранив название"):
        try:
            response1 = str(re.findall('<title>«(.*?)» ', str(driver.page_source))[0])
            heart = driver.find_element(By.CSS_SELECTOR,
                                        "#main_container > div:nth-child(3) > div.infocontainer > div.sale-span > span")
            heart.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Переходим в избранное"):
        try:
            favorites = driver.find_element(By.CSS_SELECTOR, "body > div.topheader > span.fvtico > img")
            favorites.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Ищем название картины в избранном"):
        try:
            fav_painting = driver.find_element(By.CSS_SELECTOR, "#sa_container > div.post > a:nth-child(1) > div")
            fav_painting.click()
            response2 = str(re.findall(r'<title>«(.*?)» ', str(driver.page_source))[0])
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    try:
        assert response1 == response2
    except AssertionError("В избранном другая картина"):
        with allure.step("Делаем скриншот ошибки"):
            allure.attach(driver.get_screenshot_as_png(), name="chrome_error", attachment_type=AttachmentType.PNG)
        driver.close()
        driver.quit()
    with allure.step("Закрываем драйвер"):
        try:
            driver.close()
            driver.quit()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()


@allure.story("Тест поиска по слову Жираф, Chrome")
@allure.severity("critical")
def test_giraffe_chrome():
    with allure.step("Создаем драйвер, открываем окно на полный экран, переходим на сайт"):
        try:
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://artnow.ru")
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Открываем строку поиска и вводим туда Жираф"):
        try:
            find_bar = driver.find_element(By.CSS_SELECTOR,
                                           "#MainSearchForm > div > div:nth-child(1) > input.inp.scLarge")
            find_bar.click()
            find_bar.send_keys('Жираф')
            find_bar.send_keys(Keys.ENTER)
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Ищем Жираф в выдаче"):
        try:
            response = re.search(r'<meta itemprop="description" content="(.*?)">',
                                 str(driver.page_source)).group()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    try:
        assert "Жираф" in response
    except AssertionError("Картины Жираф нет в списке"):
        with allure.step("Делаем скриншот ошибки"):
            allure.attach(driver.get_screenshot_as_png(), name="chrome_error", attachment_type=AttachmentType.PNG)
        driver.close()
        driver.quit()
    with allure.step("Закрываем драйвер"):
        try:
            driver.close()
            driver.quit()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()


@allure.story("Тест добавления товара в корзину и сравнения цены, Chrome")
@allure.severity("critical")
def test_jewelry_art_chrome():
    with allure.step("Создаем драйвер, открываем окно на полный экран, переходим на сайт"):
        try:
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://artnow.ru")
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Открываем выпадающий список"):
        try:
            drop_down_list = driver.find_element(
                By.CSS_SELECTOR,
                "#left_container > div > ul:nth-child(2) > li.menu-group.gids > div")
            drop_down_list.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Переходим в ювелирные работы"):
        try:
            works = driver.find_element(By.CSS_SELECTOR, "#left_container > div > ul:nth-child(2) > li:nth-child(5) > a")
            works.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Выбриаем первую работу, сохраняем ее цену"):
        try:
            chosen_work = driver.find_element(By.CSS_SELECTOR, "#sa_container > div:nth-child(3) > a:nth-child(1) > div")
            chosen_work.click()
            price1 = int(re.findall(r'<b>Цена</b> <b>(.*?) руб', str(driver.page_source))[0])
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Добавляем работу в корзину; переходим туда"):
        try:
            add_to_basket = driver.find_element(By.CSS_SELECTOR, "#CartButton1127052")
            add_to_basket.click()
            time.sleep(2)
            to_basket = driver.find_element(By.CSS_SELECTOR, "#cmodal > div > p > button.ok-button")
            to_basket.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    try:
        assert not "В вашей корзине пока нет товаров" in str(driver.page_source)
    except AssertionError("Жанр картины - не реализм"):
        with allure.step("Делаем скриншот ошибки"):
            allure.attach(driver.get_screenshot_as_png(), name="chrome_error", attachment_type=AttachmentType.PNG)

    with allure.step("Ищем цену товара в корзине"):
       try:
           price2 = re.findall(r'class="price">(.*?) руб', str(driver.page_source))[0]
       except Exception as e:
           print(e)
           with allure.step("Делаем скриншот ошибки"):
               allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                                 attachment_type=AttachmentType.PNG)
           driver.close()
           driver.quit()
    try:
        assert int(str(price2)) == price1
    except AssertionError("Цена не совпадает"):
        with allure.step("Делаем скриншот ошибки"):
            allure.attach(driver.get_screenshot_as_png(), name="chrome_error", attachment_type=AttachmentType.PNG)
        driver.close()
        driver.quit()
    with allure.step("Закрываем драйвер"):
        try:
            driver.close()
            driver.quit()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()


@allure.story("Тест наличия картины Трамвайный путь в списке, Firefox")
@allure.severity("critical")
def test_tram_track_firefox():
    with allure.step("Создаем драйвер, открываем окно на полный экран, переходим на сайт"):
        try:
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get("https://artnow.ru")
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Открываем выпадающий список"):
        try:
            drop_down_list = driver.find_element(
                By.CSS_SELECTOR,
                "#left_container > div > ul:nth-child(2) > li.menu-group.gids > div")
            drop_down_list.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Переходим в вышитые картины"):
        try:
            paintings = driver.find_element(By.CSS_SELECTOR,
                                            "#left_container > div > ul:nth-child(2) > li:nth-child(8) > a")
            paintings.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Выбираем жанр Городской пейзаж"):
        try:
            city_landscape = driver.find_element(By.CSS_SELECTOR,
                                                 "#genrebox > div > label:nth-child(2)")
            city_landscape.click()
            time.sleep(3)
            use = driver.find_element(By.CSS_SELECTOR, "#applymsg")
            use.click()
            time.sleep(3)
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Ищем Трамвайный путь среди картин"):
        try:
            response = re.findall(r'<meta itemprop="description" content="(.*)">', str(driver.page_source))
            flag = False
            for item in response:
                if "Трамвайный путь" in item:
                    flag = True
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()

    try:
        assert flag
    except AssertionError("Указанной картины нет в списке"):
        with allure.step("Делаем скриншот ошибки"):
            allure.attach(driver.get_screenshot_as_png(), name="firefox_error", attachment_type=AttachmentType.PNG)
        driver.close()
        driver.quit()

    with allure.step("Закрываем драйвер"):
        try:
            driver.close()
            driver.quit()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()


@allure.story("Тест жанра картины Трамвайный путь - реализм, Firefox")
@allure.severity("critical")
def test_tram_track_specs_firefox():
    with allure.step("Создаем драйвер, открываем окно на полный экран, переходим на сайт"):
        try:
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get("https://artnow.ru")
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Открываем выпадающий список"):
        try:
            drop_down_list = driver.find_element(
                By.CSS_SELECTOR,
                "#left_container > div > ul:nth-child(2) > li.menu-group.gids > div")
            drop_down_list.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Переходим в вышитые картины"):
        try:
            paintings = driver.find_element(By.CSS_SELECTOR,
                                            "#left_container > div > ul:nth-child(2) > li:nth-child(8) > a")
            paintings.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Выбираем жанр Городской пейзаж"):
        try:
            city_landscape = driver.find_element(By.CSS_SELECTOR,
                                                 "#genrebox > div > label:nth-child(2)")
            city_landscape.click()
            time.sleep(3)
            use = driver.find_element(By.CSS_SELECTOR, "#applymsg")
            use.click()
            time.sleep(3)
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Открываем картину трамвайный путь"):
        try:
            tram_track = driver.find_element(By.CSS_SELECTOR, "#sa_container > div:nth-child(5) > a > div")
            tram_track.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Проверяем жанр картины на реализм"):
        try:
            response = str(re.search(r'Стиль: (.*?)\.', str(driver.page_source)).group())
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    try:
        assert "реализм" in response
    except AssertionError("Жанр картины - не реализм"):
        with allure.step("Делаем скриншот ошибки"):
            allure.attach(driver.get_screenshot_as_png(), name="firefox_error", attachment_type=AttachmentType.PNG)
        driver.close()
        driver.quit()
    with allure.step("Закрываем драйвер"):
        try:
            driver.close()
            driver.quit()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()


@allure.story("Тест добавления товара в избранное, Firefox")
@allure.severity("critical")
def test_add_to_favorites_firefox():
    with allure.step("Создаем драйвер, открываем окно на полный экран, переходим на сайт"):
        try:
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get("https://artnow.ru")
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Открываем выпадающий список"):
        try:
            drop_down_list = driver.find_element(
                By.CSS_SELECTOR,
                "#left_container > div > ul:nth-child(2) > li.menu-group.gids > div")
            drop_down_list.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Переходим в батик"):
        try:
            paintings = driver.find_element(By.CSS_SELECTOR,
                                            "#left_container > div > ul:nth-child(2) > li:nth-child(3) > a")
            paintings.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Выбираем первую картину и открываем ее"):
        try:
            chosen_painting = driver.find_element(By.CSS_SELECTOR,
                                                  "#sa_container > div:nth-child(3) > a:nth-child(1) > div")
            chosen_painting.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Добавляем ее в избранное, сохранив название"):
        try:
            response1 = str(re.findall('<title>«(.*?)» ', str(driver.page_source))[0])
            heart = driver.find_element(By.CSS_SELECTOR,
                                        "#main_container > div:nth-child(3) > div.infocontainer > div.sale-span > span")
            heart.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(),name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Переходим в избранное"):
        try:
            favorites = driver.find_element(By.CSS_SELECTOR, "body > div.topheader > span.fvtico > img")
            favorites.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Ищем название картины в избранном"):
        try:
            fav_painting = driver.find_element(By.CSS_SELECTOR, "#sa_container > div.post > a:nth-child(1) > div")
            fav_painting.click()
            response2 = str(re.findall(r'<title>«(.*?)» ', str(driver.page_source))[0])
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    try:
        assert response1 == response2
    except AssertionError("В избранном другая картина"):
        with allure.step("Делаем скриншот ошибки"):
            allure.attach(driver.get_screenshot_as_png(), name="firefox_error", attachment_type=AttachmentType.PNG)
        driver.close()
        driver.quit()
    with allure.step("Закрываем драйвер"):
        try:
            driver.close()
            driver.quit()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()


@allure.story("Тест поиска по слову Жираф, Firefox")
@allure.severity("critical")
def test_giraffe_firefox():
    with allure.step("Создаем драйвер, открываем окно на полный экран, переходим на сайт"):
        try:
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get("https://artnow.ru")
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Открываем строку поиска и вводим туда Жираф"):
        try:
            find_bar = driver.find_element(By.CSS_SELECTOR,
                                           "#MainSearchForm > div > div:nth-child(1) > input.inp.scLarge")
            find_bar.click()
            find_bar.send_keys('Жираф')
            use = driver.find_element(By.CSS_SELECTOR, "button.control")
            use.click()
            time.sleep(3)
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Ищем Жираф в выдаче"):
        try:
            response = re.search(r'<meta itemprop="description" content="(.*?)">',
                                 str(driver.page_source)).group()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    try:
        assert "Жираф" in response
    except AssertionError("Картины Жираф нет в списке"):
        with allure.step("Делаем скриншот ошибки"):
            allure.attach(driver.get_screenshot_as_png(), name="firefox_error", attachment_type=AttachmentType.PNG)
        driver.close()
        driver.quit()
    with allure.step("Закрываем драйвер"):
        try:
            driver.close()
            driver.quit()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()


@allure.story("Тест добавления товара в корзину и сравнения цены, Firefox")
@allure.severity("critical")
def test_jewelry_art_firefox():
    with allure.step("Создаем драйвер, открываем окно на полный экран, переходим на сайт"):
        try:
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get("https://artnow.ru")
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Открываем выпадающий список"):
        try:
            drop_down_list = driver.find_element(
                By.CSS_SELECTOR,
                "#left_container > div > ul:nth-child(2) > li.menu-group.gids > div")
            drop_down_list.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Переходим в ювелирные работы"):
        try:
            works = driver.find_element(By.CSS_SELECTOR, "#left_container > div > ul:nth-child(2) > li:nth-child(5) > a")
            works.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Выбриаем первую работу, сохраняем ее цену"):
        try:
            chosen_work = driver.find_element(By.CSS_SELECTOR, "#sa_container > div:nth-child(3) > a:nth-child(1) > div")
            chosen_work.click()
            price1 = int(re.findall(r'<b>Цена</b> <b>(.*?) руб', str(driver.page_source))[0])
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Добавляем работу в корзину; переходим туда"):
        try:
            add_to_basket = driver.find_element(By.CSS_SELECTOR, "#CartButton1127052")
            add_to_basket.click()
            time.sleep(2)
            to_basket = driver.find_element(By.CSS_SELECTOR, "#cmodal > div > p > button.ok-button")
            to_basket.click()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    try:
        assert not "В вашей корзине пока нет товаров" in str(driver.page_source)
    except AssertionError("Жанр картины - не реализм"):
        with allure.step("Делаем скриншот ошибки"):
            allure.attach(driver.get_screenshot_as_png(), name="firefox_error", attachment_type=AttachmentType.PNG)

    with allure.step("Ищем цену товара в корзине"):
       try:
           price2 = re.findall(r'class="price">(.*?) руб', str(driver.page_source))[0]
       except Exception as e:
           print(e)
           with allure.step("Делаем скриншот ошибки"):
               allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                                 attachment_type=AttachmentType.PNG)
           driver.close()
           driver.quit()
    try:
        assert int(str(price2)) == price1
    except AssertionError("Цена не совпадает"):
        with allure.step("Делаем скриншот ошибки"):
            allure.attach(driver.get_screenshot_as_png(), name="firefox_error", attachment_type=AttachmentType.PNG)
        driver.close()
        driver.quit()
    with allure.step("Закрываем драйвер"):
        try:
            driver.close()
            driver.quit()
        except Exception as e:
            print(e)
            with allure.step("Делаем скриншот ошибки"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()

