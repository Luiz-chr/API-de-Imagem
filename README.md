API de Imagens Simples
Uma API RESTful leve para gerenciar uma galeria de imagens, com um frontend HTML simples, sem frameworks externos como React. O projeto prioriza a simplicidade, facilitando a integração entre backend e frontend.

Objetivo
Criar uma API fácil de usar para upload, armazenamento e visualização de imagens, combinando FastAPI no backend com HTML/CSS/JS no frontend, mantendo tudo leve e simples.
 
⚙️ Tecnologias Utilizadas
Python + FastAPI: Backend da API RESTful  
HTML/CSS/JS inline: Frontend simples, sem frameworks externos  
PIL (Python Imaging Library): Para gerar um favicon automático  
Uvicorn: Servidor ASGI para rodar a aplicação  

Como Executar
1. Instale as dependências:
```bash
pip install fastapi python-multipart pillow
pip install uvicorn
pip install python-multipart
pip install pillow
```
Detalhes
•	Frontend separado: Mantive o HTML em static/index.html para não misturar com o código Python, mantendo o projeto organizado.

•	Simplicidade: Nada de frameworks pesados; tudo roda com Python e um HTML básico.

•	Fácil integração: Backend e frontend comunicam-se diretamente via endpoints da API.
