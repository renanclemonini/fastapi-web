from fastapi import FastAPI
# from fastapi.responses import HTMLResponse // com o jinja2 não foi necessário usar essa biblioteca
from fastapi.requests import Request
# Para utilizar o template engine Jinja2
from fastapi.templating import Jinja2Templates
# Para utilizar metodos dinamicos para acessar a pasta static
from fastapi.staticfiles import StaticFiles
# Para realizar upload de arquivos: 2 classes e uma função
from fastapi import UploadFile
from pathlib import Path
from aiofile import async_open
# Função para gerar nomes aleatorios 
from uuid import uuid4

app = FastAPI()

# Configurar o Jinja2Templates para apontar ao diretório templates
templates = Jinja2Templates(directory='templates')
# Configuração para poder usar metodos dinamicos na aplicação
# Aponta para a pasta static onde esta o css, js e images
app.mount('/static', StaticFiles(directory='static'), name='static')
# Para o conteudo da pasta media ficar acessível precisa montar igual ao static
app.mount('/media', StaticFiles(directory='media'), name='media')
# criar uma variável media que será um objeto da classe Path
media = Path('media')


# Rota para acessar a pagina inicial
@app.get('/')
async def index(request: Request, usuario: str = "Renan Clemonini"):
    context = {
        'request': request,
        'usuario': usuario
    }

    return templates.TemplateResponse('index.html', context=context)

# Rota para acessar a página login


@app.get('/login')
async def login(request: Request):
    context = {
        'request': request
    }

    return templates.TemplateResponse('login.html', context=context)

# Rota para realizar o envio de dados via POST


@app.post('/login')
async def login(request: Request):
    # O metodo form de request herda caracteristicas da classe Awaitable
    # e neste caso deve se usar await
    form = await request.form()

    email: str = form.get('email')
    pwd: str = form.get('pwd')
    remember: str | None = form.get('remember')

    context = {
        'request': request,
        'email': email,
        'pwd': pwd,
        'remember': remember
    }

    return templates.TemplateResponse('login.html', context=context)


@app.get('/servicos')
async def servicos(request: Request):
    context = {
        'request': request
    }

    return templates.TemplateResponse('servicos.html', context=context)


@app.post('/servicos')
async def cad_servico(request: Request):
    form = await request.form()

    servico: str = form.get('servico')
    print(f"Serviço: {servico}")

    arquivo: UploadFile = form.get('arquivo')
    print(f"Nome Arquivo: {arquivo.filename}")
    print(f"Tamanho Arquivo: {arquivo.size}")
    print(f"Tipo Arquivo: {arquivo.content_type}")

    # nome_arquivo = arquivo.filename
    tipo_arquivo = arquivo.content_type

    # Gerar Nome aleatório para o arquivo
    arquivo_ext: str = arquivo.filename.split(".")[1]
    novo_nome = f"{str(uuid4())}.{arquivo_ext}"

    if tipo_arquivo.__contains__('pdf'):
        tipo = "PDF"
    else:
        tipo = tipo_arquivo

    upload: str | None = None
    if not arquivo.filename == "":
        nome_arquivo = f"{servico}_{novo_nome}"
        async with async_open(f"{media}/{nome_arquivo}", "wb") as afile:
            await afile.write(arquivo.file.read())
            upload = "ok"

    mensagem: str = f"Arquivo enviado com sucesso como {nome_arquivo}" if upload is not None else "Erro ao Enviar"

    context = {
        'request': request,
        'nome': nome_arquivo,
        'tipo': tipo,
        'mensagem': mensagem,
        'imagem': nome_arquivo
    }

    return templates.TemplateResponse('servicos.html', context=context)
