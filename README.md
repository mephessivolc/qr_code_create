# Gerador de QR Codes em imagens em extensão padrão .png

## Instalação 

```bash 
python3 -m venv dev

source dev/bin/activate

pip install -U pip
pip install -r requirements.txt
```
## Execução
```bash
python main.py
```

O algoritmo irá pedir para inserir a URL e um nome para o arquivo gerando o arquivo. Se colocar uma extensão de imagem junto com o nome irá ser criado a imagem com a extensão desejada.

### Exemplo de uso sem extensão
```python
>>> python main.py

Entre com a url: https://bitbucket.org/ccaface/create_qrcode/src/master/
Entre com o nome do arquivo: teste
```

Será gerado uma imagem com extensão **.png** denominada _teste_

### Exemplo de uso com extensão
```python
>>> python main.py

Entre com a url: https://bitbucket.org/ccaface/create_qrcode/src/master/
Entre com o nome do arquivo: teste.jpg
```

Será gerado uma imagem com extensão **.jpg** denominada _teste_

