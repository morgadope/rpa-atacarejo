from selenium.webdriver import Chrome
from time import sleep, time
from selenium.webdriver.common.keys import Keys
from datetime import timedelta, datetime
from selenium.webdriver.support.expected_conditions import frame_to_be_available_and_switch_to_it
from selenium.webdriver.support.wait import WebDriverWait


driver = Chrome()

locais = ["alvo","dom","o bom"]

for local in locais:
        driver.find_element_by_xpath('//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/button/span').click()
        for n in range(0,2):
                driver.find_element_by_xpath('//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/ul/li[2]/a/label/input').click()
        driver.find_element_by_xpath('//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/ul/li[1]/div/input').click()
        driver.find_element_by_xpath('//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/ul/li[1]/div/input').clear()
        driver.find_element_by_xpath('//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/ul/li[1]/div/input').send_keys(local)
        sleep(2)
        if local == ('dom'):
            driver.find_element_by_xpath('//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/ul/li[3]/a/label/input').click() #checkbox dom
        if local== ('o bom'):
            driver.find_element_by_xpath('//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/ul/li[3]/a/label/input').click() #checkbox  o bom
        driver.find_element_by_xpath('//*[@id="btnFilter"]').click()
        if local == ('alvo'):
            driver.find_element_by_xpath('//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/ul/li[3]/a/label') #
        sleep(3)
        
        driver.find_element_by_xpath('//*[@id="select_photo"]').click()  # selecionar todas as fotos
        sleep(3)
        try:
            selecionar_todas = driver.find_element_by_xpath('//*[@id="select_all_images"]/a')
        except Exception:
            print("Elemento não localizado!")

        
        
        print(selecionar_todas.text)
        
        bufQuantidadeImagens = str(selecionar_todas.text).split(" ")
        if len(bufQuantidadeImagens) == 8:
            texto = (str(selecionar_todas.text).split(" "))
            quantidadeImagens = int(texto[6])
            print (quantidadeImagens)
            if (quantidadeImagens > 10):
                selecionar_todas.click()
        else:
            raise Exception("")
        
        
        driver.find_element_by_xpath('//*[@id="photo"]/div[2]/div[3]/div/div/button').click()
        sleep(2)
        driver.back()  # volta para pagina anterior
        wdw.until(frame_to_be_available_and_switch_to_it)
        driver.switch_to.frame(0)
        sleep(1)



    filtros 

     driver.switch_to.frame(0)  # select
     driver.find_element_by_xpath('//*[@id="filterPanel"]/div[1]/div[2]/div[2]/div/button').click()  # clicar no filtro
     driver.find_element_by_xpath( '//*[@id="filterPanel"]/div[1]/div[2]/div[2]/div/ul/li/a/label/input').click()  # Selecionar o filtro
