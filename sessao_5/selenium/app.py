from pip._internal.commands import search
from selenium import webdriver
from time import sleep
import pyautogui as pg

from selenium.webdriver import Keys


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user_data_dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()
    def clica_sign_in(self):
        try:
            btn_signi_in = self.chrome.find_element_by_link_text('Sign in')
            btn_signi_in.click()

        except Exception as e:
            print("Ero ao clicar em sign in", e)
    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')

            input_login.send_keys('diego_carlos110@hotmail.com')
            input_password.send_keys('Diego110@')
            sleep(3)
            btn_login.click()


        except Exception as e:
            print("Erro ao fazer login", e)

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary > img')
            perfil.click()
        except Exception as e:
            print("Erro ao clicar no perfil", e)

    def faz_logout(self):
        try:
            log_out = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            log_out.click()
        except Exception as e:
            print("Erro ao fazer logout", e)
    def verifica_usuario(self, usuario):
        profile_link = self.chrome.find_element_by_class_name('user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html
        print(profile_link_html)



if __name__ == '__main__':
    chrome = ChromeAuto()
    sleep(3)
    pg.hotkey('win', 'up')
    sleep(3)
    chrome.acessa('https://github.com/')

    sleep(3)
    chrome.clica_perfil()
    sleep(2)
    chrome.faz_logout()
    sleep(3)
    chrome.clica_sign_in()
    sleep(3)
    chrome.faz_login()
    sleep(3)


    chrome.verifica_usuario('dcarll')

    sleep(3)
    chrome.sair


    """
    versão do curso
    
    
    
    from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sign_in.click()
        except Exception as e:
            print('Erro ao clicar em Sign in:', e)

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details')
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no perfil:', e)

    def faz_logout(self):
        try:
            perfil = self.chrome.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > details-menu > form > button')
            perfil.click()
        except Exception as e:
            print('Erro fazer logout:', e)

    def verifica_usuario(self, usuario):
        profile_link = self.chrome.find_element_by_class_name(
            'user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')

            input_login.send_keys('')
            input_password.send_keys('')
            sleep(3)
            btn_login.click()

        except Exception as e:
            print('Erro ao fazer login:', e)


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')

    chrome.clica_perfil()
    chrome.faz_logout()

    chrome.clica_sign_in()
    chrome.faz_login()

    chrome.clica_perfil()
    chrome.verifica_usuario('otaviomirandabr')

    sleep(5)
    chrome.sair()

    
    
    """