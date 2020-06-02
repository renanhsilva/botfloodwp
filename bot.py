from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = "Mensagem"
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos_ou_pessoas = ["Contato"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)
        self.driver.get('https://web.whatsapp.com')
        time.sleep(20)

    def EnviarMensagens(self):
	    for grupo_ou_pessoa in self.grupos_ou_pessoas:
	        campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo_ou_pessoa}']")
	        campo_grupo.click()
	        chat_box = self.driver.find_element_by_class_name('_1Plpp')
	        chat_box.click()
	        chat_box.send_keys(self.mensagem)
	        botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
	        botao_enviar.click()

bot = WhatsappBot()
i = 1
while i < 1000:
    bot.EnviarMensagens()
    i +=1