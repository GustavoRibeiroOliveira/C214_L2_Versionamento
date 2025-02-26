# Projeto de Criptografia Simples

Este projeto realiza a criptografia e descriptografia de um texto predefinido. Ele utiliza a biblioteca `cryptography` para a encriptação e desencriptação e pode ser empacotado em um executável utilizando o `pyinstaller`. Além disso, emprega `black`, `isort` e `flake8` para garantir a padronização e qualidade do código.

## Dependências

As dependências do projeto estão listadas abaixo:

```
altgraph==0.17.4
black==25.1.0
cffi==1.17.1
click==8.1.8
colorama==0.4.6
cryptography==44.0.1
flake8==7.1.1
isort==6.0.0
mccabe==0.7.0
mypy-extensions==1.0.0
packaging==24.2
pathspec==0.12.1
pefile==2023.2.7
platformdirs==4.3.6
pycodestyle==2.12.1
pycparser==2.22
pyflakes==3.2.0
pyinstaller==6.12.0
pyinstaller-hooks-contrib==2025.1
pywin32-ctypes==0.2.3
setuptools==75.8.0
```

## Como Usar

1. Instale as dependências do projeto:
   ```sh
   pip install -r requirements.txt
   ```

2. Execute o script para criptografar e descriptografar o texto:
   ```sh
   python main.py
   ```

3. Para gerar um executável usando PyInstaller:
   ```sh
   pyinstaller --onefile main.py
   ```

4. O executável gerado estará na pasta `dist/`.

## Padronização de Código

Para manter um código organizado e limpo, utilize os seguintes comandos:

- Formatar o código com `black`:
  ```sh
  black .
  ```
- Ordenar as importações com `isort`:
  ```sh
  isort .
  ```
- Verificar problemas no código com `flake8`:
  ```sh
  flake8
  ```