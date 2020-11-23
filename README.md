## Seja bem vindo ao meu repositório!

#### Programa de automação para Mensagens via Whatsapp. Código comentado.

Linguagens e programas utilizados;

![Python](https://res.cloudinary.com/practicaldev/image/fetch/s--_W3c7FfD--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://d33wubrfki0l68.cloudfront.net/c8827c80d7162a7eeb8a071d9a0c884e3a105a36/a2b46/blog/selenium-python/header_selenium_python.png)

## COMO CRIAR UM BOT NO WHATSAPP DE ENVIO DE MENSAGEM AUTOMÁTICAS

Para todas as vovós, tios e tias, vendedores e amigos de plantão, que gostam de enviar mensagem para os conhecidos todos os dias, eu tenho um segredo para você: aprenda a fazer isso de um jeito mais eficiente, deixando o código trabalhar por você.

Por que fazer um trabalho manual todo dia se podemos, através da programação com Python, criar um robô para o WhatsApp uma vez e depois deixar ele trabalhando incansavelmente por nós?

Você está pronto para montar o nosso “robô WhatsApp”? Ele irá enviar as mensagens que você definir para todos os grupos ou contatos individuais que você quiser.

Se você está pronto para aprender, então bora lá!

## INSTALAÇÃO DAS FERRAMENTAS

### INSTALAÇÃO DO PYTHON

Para que a gente consiga criar nosso bot, iremos fazer a instalação do Python. Para fazer a instalação do Python acesse [https://www.python.org/downloads/](https://www.python.org/downloads/) e faça o download da versão mais atual do Python.

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_651,h_278/https://devaprender.com/wp-content/uploads/2020/03/download-python.png)

Na sequência execute o arquivo de instalação, mas fique atento as duas opções que você precisa marcar, ou o restante do tutorial não irá funcionar. Marque as opções **Add Python to PATH**(ou a tradução disso em português) e **Install Launcher**.

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_600,h_370/https://devaprender.com/wp-content/uploads/2020/03/instala%C3%A7%C3%A3o-python.png)

Se a instalação foi feita corretamente, você deve possuir o Python instalado agora.

Podemos verificar se a instalação funcionou corretamente abrindo o terminal (botão iniciar -> digite cmd no windows) , digitando **_python_** e apertando enter. Você deve receber uma mensagem dizendo qual é a versão atual instalada em seu computador. Algo como a imagem abaixo:

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_1024,h_120/https://devaprender.com/wp-content/uploads/2020/03/python-step-3-1024x120.png)

Caso este comando gere um erro, e não exiba a versão do Python. Volte aos passos anteriores e faça a instalação novamente.

### INSTALAÇÃO DO SELENIUM

Agora temos que fazer a instalação que nos permitirá fazer a automação de tarefas na web.

O nosso exemplo de hoje sendo a automação de envio de mensagens para contatos e grupos no WhatsApp web.

Abra um **novo** **terminal** e digite:

```bash
pip install selenium
```

Ao rodar este comando você estará instalando a biblioteca que utilizaremos para navegar até o whatsapp web.

Caso tenha um erro aqui, é provável que sua instalação do python não foi feita corretamente. Desinstale o python e siga o passo da instalação novamente.

### BAIXANDO O GOOGLE CHROME DRIVER

A seguir temos que fazer o download do **[Google Chrome Driver](https://chromedriver.chromium.org/downloads)** que é um navegador especialmente criado para fazer automação de sites.

Ao acessar o site, você verá algumas versões diferentes para fazer o download. Você deve baixar uma versão igual à versão do Google Chrome que esta instalada em seu computador.

**Como descobrir a sua _versão_ atual do Google Chrome?**

Vá até em configurações, sobre Google Chrome(minha versão está em inglês, mas as imagens devem ajudar)

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_589,h_454/https://devaprender.com/wp-content/uploads/2020/03/python-step-4-min.png)

Após clicar neste menu, seremos levados para uma página onde podemos verificar a versão do Chrome que temos instalado. No meu caso possuo a versão 80, mas é possível que você possua uma versão diferente.

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_553,h_348/https://devaprender.com/wp-content/uploads/2020/03/python-step-5-min-1024x644.png)

Agora temos a informação que precisamos: **nossa versão do Google Chrome**. Com essa informação em mãos, navegue ate [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads). E clique na versão que corresponde a sua versão do Chrome.

No meu caso estarei fazendo o download da versão 80(**baixe a versão do seu Google Chrome**)

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_389,h_206/https://devaprender.com/wp-content/uploads/2020/03/step-6-min.png)

Na página a seguir você deve baixar o arquivo correspondente ao seu sistema operacional. Como uso Windows 10, estarei fazendo o download da versão para o Windows:

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_391,h_237/https://devaprender.com/wp-content/uploads/2020/03/step7-min.png)

Após ter feito o download do driver, extraia o arquivo .zip para que possamos usar ele no próximo passo.

#### CRIANDO UMA PASTA PARA O PROJETO

Navegue até algum lugar no seu computador(área de trabalho, por exemplo) e crie uma nova pasta.

Vamos chamar essa pasta de “bot whatsapp”(o nome não importa). Feito isso copie o **chromedriver.exe** que você acaba de extrair para dentro desta pasta. Estes arquivos serão usados a seguir.

### INSTALAÇÃO DO VS CODE

Navegue até [https://code.visualstudio.com/](https://code.visualstudio.com/) e clique no botão de download.

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_765,h_415/https://devaprender.com/wp-content/uploads/2020/03/download-vs-code-min-1024x556.png)

Após o download, execute o arquivo e faça os seguintes passos para fazer a instalação do VS Code

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_578,h_477/https://devaprender.com/wp-content/uploads/2020/03/step9-min.png)

Clique em Próximo ou _Next_

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_581,h_482/https://devaprender.com/wp-content/uploads/2020/03/step10-min.png)

Marque as opções em vermelho acima, caso ainda não estejam,

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_581,h_475/https://devaprender.com/wp-content/uploads/2020/03/step11-min.png)

Clique em **finalizar** ou **_finish_** para concluir a instalação do Vs Code

O Vs Code deve abrir automaticamente. Caso não abra vá até botão iniciar –> vs code.

### PREPARANDO O VS CODE PARA USO DO PYTHON

Ao abrir o VS Code pela primeira vez, as ferramentas da linguagem de programação Python não estarão instaladas.

Para fazer essa instalação, clique em Python dentro de “_Tools and languages_“(ou o correspondente disso em português) e aguarde até que ele fique cinza, como na imagem abaixo.

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_629,h_423/https://devaprender.com/wp-content/uploads/2020/03/step12-min-1024x689.png)

Clique em _open_ folder(ou “abrir pasta” caso esteja em português) e selecione a pasta”bot whatsapp”, criada no passo anterior.

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_779,h_388/https://devaprender.com/wp-content/uploads/2020/03/step13-min-1024x510.png)

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_501,h_469/https://devaprender.com/wp-content/uploads/2020/03/step14-min.png)

## HORA DO CÓDIGO

Ok, estamos agora dentro da pasta onde iremos colocar nosso código. Para criar um arquivo python, clique com o botão esquerdo em _New File_(ou novo arquivo em português).

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_738,h_407/https://devaprender.com/wp-content/uploads/2020/03/step15.png)

A seguir iremos criar um arquivo chamado **_whatsapp_bot.py_**. Com isso você deve ter o arquivo whatsapp_bot..py aberto, caso ele não tenha aberto automaticamente, faça isso agora.

Caso precise renomear o arquivo, clique em cima dele e **aperte F2** no seu teclado para alterar o nome do arquivo.

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_1024,h_290/https://devaprender.com/wp-content/uploads/2020/03/step16-min-1-1024x290.png)

### CONFIGURANDO NOME DOS GRUPOS E PESSOAS

Copie o código abaixo para dentro do arquivo **_whatsapp bot_**, você deve alterar as mensagens dentro da **Parte 1** e **Parte 2** como visto no código abaixo.

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = "Bom dia pessoal, veja o video que acabou de sair https://www.youtube.com"
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos_ou_pessoas = ["GRUPO DA FAMÍLIA", "GRUPO DE VENDAS"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)
```

A única configuração que você precisa fazer já foi feita no bloco de código do passo anterior. No entanto, ele ainda não está completo, adicione o código abaixo ao arquivo **_whatsapp_bot.py_** .

```python
	def EnviarMensagens(self):
	        self.driver.get('https://web.whatsapp.com')
	        time.sleep(30)
	        for grupo_ou_pessoa in self.grupos_ou_pessoas:
	            campo_grupo = self.driver.find_element_by_xpath(
	                f"//span[@title='{grupo_ou_pessoa}']")
	            time.sleep(3)
	            campo_grupo.click()
	            chat_box = self.driver.find_element_by_class_name('_13mgZ')
	            time.sleep(3)
	            chat_box.click()
	            chat_box.send_keys(self.mensagem)
	            botao_enviar = self.driver.find_element_by_xpath(
	                "//span[@data-icon='send']")
	            time.sleep(3)
	            botao_enviar.click()
	            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagens()
```

Para executar o código acima temos 2 opções.  
Opção 1) Clicar no botao “**Play**” do _VS Code_

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_1024,h_739/https://devaprender.com/wp-content/uploads/2020/03/step17-min-1024x739.png)

Opção 2) Executar o script Python diretamente no terminal.

Para abrir o terminal aperte **CTRL + `** (tecla logo abaixo do _ESC_) no seu teclado e digite py.exe + nome do arquivo que criou.

No nosso caso como criei o arquivo chamado **_whatsapp_bot.py_**, estarei rodando o comando abaixo:

```python
py.exe whatsapp_bot.py
```

![](https://cdn.shortpixel.ai/client/to_avif,q_lossy,ret_img,w_1024,h_574/https://devaprender.com/wp-content/uploads/2020/03/step18-min-1024x574.png)

## ACESSANDO O WHATSAPP WEB

Após ter rodado o arquivo o nosso programa irá abrir o site do WhatsApp Web.

Nele você deverá ler o _QR code_ para que ele possa abrir o whatsapp web.
![WHATSAPP WEB](https://imagens.canaltech.com.br/285719.535215-WhatsApp-web.png)

Agora você não precisa fazer mais nada. Apenas aguarde a veja o nosso bot fazer o trabalho para a gente [😎](https://emojipedia.org/smiling-face-with-sunglasses/) .

**P.S.** – O bot irá enviar mensagem **apenas para contatos que estejam visíveis** quando você abre o Whatsapp Web. Caso o contato ou grupo para o qual está tentando enviar mensagem não esteja visível nessa janela, o bot não irá funcionar, sendo necessário alterar o código para que ele trate essas situações também.

## CONSIDERAÇÕES FINAIS

Isso é apenas um exemplo de um Bot que podemos criar usando o **Python + Selenium**.
Fontes:
https://github.com/Queila-Souto/Whatsautomacao
https://devaprender.com/como-criar-um-bot-no-whatsapp/

# Volte sempre! # 😉

![Foto de UMJS](https://scontent.ffor11-1.fna.fbcdn.net/v/t1.0-9/70713611_2418334764888591_8632977409915748352_o.jpg?_nc_cat=111&ccb=2&_nc_sid=84a396&_nc_eui2=AeFvNFlYmLBYQEJWBySuYIxgmGmpj5pPTMqYaamPmk9MymeSQYuZp-2UpMCEEcPe8PQ15fFd9HeL9uJ4yYFMiaLk&_nc_ohc=e3yzaDzY5yEAX8pcw-Z&_nc_ht=scontent.ffor11-1.fna&oh=7ee6bc0ee465207313b717c85437f4b3&oe=5FE19A8A)
