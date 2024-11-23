from fastapi import FastAPI
# from fastapi.responses import HTMLResponse // com o jinja2 não foi necessário usar essa biblioteca
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Configurar o Jinja2Templates para apontar ao diretório templates
templates = Jinja2Templates(directory='templates')
# Configuração para poder usar metodos dinamicos na aplicação
# Aponta para a pasta static onde esta o css, js e images
app.mount('/static', StaticFiles(directory='static'), name='static')

# Rota para acessar a pagina inicial
@app.get('/')
async def index(request: Request, usuario: str = "Renan Clemonini"):
    context = {
        'request': request,
        'usuario': usuario
    }

    return templates.TemplateResponse('index.html', context=context)

# Rota para acessar a página serviços
@app.get('/servicos')
async def servicos(request: Request):
    context = {
        'request': request
    }

    return templates.TemplateResponse('servicos.html', context=context)

# Rota para realizar o envio de dados via POST
@app.post('/servicos')
async def cadastrar_servico(request: Request):
    # O metodo form de request herda caracteristicas da classe Awaitable 
    # e neste caso deve se usar await
    form = await request.form() 

    email: str = form.get('email')
    pwd: str = form.get('pwd')
    remember: any = form.get('remember')

    body_form = {
        'email': email,
        'pwd': pwd,
        'remember': remember
    }

    print(body_form)

    context = {
        'request': request,
    }

    return templates.TemplateResponse('servicos.html', context=context)
