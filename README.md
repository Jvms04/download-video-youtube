# 🎬 Python YouTube Downloader (pytubefix)

Este é um projeto Python simples e funcional para baixar vídeos do YouTube. Ele utiliza a biblioteca `pytubefix` e foi configurado para rodar facilmente em qualquer ambiente.

## ✨ 1. Pré-requisitos (O que você precisa)

Para executar este script, você precisa ter o Python 3 instalado e a biblioteca `pytubefix` configurada:

1.  **Instale o Python:** Certifique-se de ter o Python 3.x instalado em seu sistema.
2.  **Instale a Biblioteca:** Use o `pip` no seu terminal para adicionar a dependência necessária ao seu ambiente:

    ```bash
    pip install pytubefix
    ```

## ⚙️ 2. Como Clonar o Repositório

Para trazer o código para a sua máquina, você deve clonar este repositório:

1.  **Abra o Terminal** (Prompt de Comando ou PowerShell).
2.  **Clone o Projeto:** Execute o comando `git clone`, usando a URL HTTPS deste repositório:

    ```bash
    git clone [https://github.com/Jvms04/download-video-youtube.git](https://github.com/Jvms04/download-video-youtube.git)
    ```
3.  **Entre na Pasta:** Navegue para o diretório do projeto:

    ```bash
    cd download-video-youtube
    ```

## 💻 3. Tutorial de Uso (main.py)

Abaixo está o código completo do arquivo `main.py` para referência:

```python
from pytubefix import YouTube

link = ""
link = input("Cole o link do video aqui: ")

yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()
print("Download concluído com sucesso!")
```

### Explicação Passo a Passo

Entenda como o código funciona linha por linha:

| Linha | Código | Ação (O que a linha faz) |
| :--- | :--- | :--- |
| **Linha 1** | `from pytubefix import YouTube` | Importa a classe principal `YouTube` da biblioteca para que possamos criar um objeto de vídeo. |
| **Linha 2** | `link = ""` | **Ação do Usuário:** Esta é a variável que armazena o URL do vídeo que você deseja baixar. |
| **Linha 3** | `link = input("Cole o link do video aqui: ")` | Solicita que o usuário cole o link do YouTube diretamente no terminal durante a execução do script. |
| **Linha 4** | `yt = YouTube(link)` | **Cria o Objeto:** Passa o link do usuário para a classe `YouTube`, inicializando o objeto do vídeo. |
| **Linha 5** | `stream = yt.streams.get_highest_resolution()` | **Define a Qualidade:** Acessa a lista de streams disponíveis para o vídeo e seleciona a opção com a melhor resolução de áudio e vídeo combinados. |
| **Linha 6** | `stream.download()` | **Baixa o Vídeo:** Executa o download real do vídeo selecionado. O arquivo `.mp4` é salvo na mesma pasta do `main.py`. |
| **Linha 7** | `print("Download concluído com sucesso!")` | Exibe uma mensagem de sucesso no terminal após o término do download. |

### 🚀 Para Executar:

1.  **Edite o `main.py`** (ou use a função `input()` no terminal).
2.  **Execute o Script:**
    ```bash
    python main.py
    ```

## 🧑‍💻 Autor

Este projeto foi criado por **João Vítor Moço Santos**.
