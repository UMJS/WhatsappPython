from selenium import webdriver
import time

class WhatsappBot:
    #Agora vamos iniciar nosso método construtor
    def __init__(self):
        #Na linha abaixo é registrado a mensagem que será enviada
        self.mensagem = "Bom dia Pessoal. Testando automação"
        #Na linha abaixo identifica-se a pessoa ou os grupos destinatários. Se atentar para colocar o nome corretamente, conforme descrito no Whatsapp
        self.grupos = ["teste automação"]
        #Nas linhas seguintes cria-se uma opção para definir a linguagem padrão
        options = webdriver.ChromeOptions()
        options.add_argument( 'lang=pt-br' )
        #Na linha a seguir estanciamos o arquivo Chromedriver, indicando seu local no servidor
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def Enviar(self):
    #nome do grupob : <span dir="auto" title="teste automação" class="_3ko75 _5h6Y_ _3Whw5">teste automação</span>
    #caixa de texto : <div tabindex="-1" class="_3uMse">
    #botão enviar: <span data-testid="send" data-icon="send" class="">

        self.driver.get('https://web.whatsapp.com/') #Aqui indicamos o caminho do nosso site, no caso Whatsapp, para que o Chrome driver possa acessa-lo
        time.sleep( 30 ) #Com esse código é possível aplicar uma pausa na programação, evitando erros
        for grupo in self.grupos: #Aqui criamos um laço em for, para que o app continue rodando conforme o numero de grupo ou pessoas cadastrado anteriormente.
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']") #Nessa etapa o programa está localizando o(s) grupo(s) cadastrado
            time.sleep(3)
            grupo.click() #Aqui ele clica sobre o grupo cadastrado
            chat_box = self.driver.find_element_by_class_name('_3uMse') #Aqui ele localiza o elemento caixa de texto
            time.sleep(3)
            chat_box.click() #Nessa etapa o programa clica sobre a caixa de texto
            chat_box.send_keys(self.mensagem) # Nessa etapa o programa escreve a mensagem que solicitamos anteriormente
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']") # Agora o programa está localizando o botão enviar
            time.sleep(3)
            botao_enviar.click() #Aqui o programa clica sobre o botao enviar
            time.sleep(5)

bot = WhatsappBot() # Estanciando a classe
bot.Enviar() # Chamando o método enviar
# O programa irá rodar enquanto durar o laço determinado em for.