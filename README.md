# Traducao-Com-Python
Esse exemplo mostra como traduzir um text usando python e a biblioteca googletrans.

  instalação: $ 
  ```pip3 install googletrans```

  No caso, foi usado a versão 3.1.0a0, para
  usar esta ou outra, coloque o operador < == >
    exp: 
    ```pip3 install googletrans==3.1.0a0```
                                                                  

  Obs: O VSCode não reconheceu a biblioteca,rodou sem problemas
  escrevendo da maneira correda as linhas de código.
  
  Adicionando ao projeto
  
```python
from googletrans import Translator
translator = Translator()
```

  .translate().text -> tradução mais usada

```python
print(
  translator.translate('dog', src='en', dest='pt').text
)  #  -> cão
```

  .translate().extra_data -> Um conjundo de informações
  como, verbos, adjetivos... exemplos de uso...
  
```python
print(
  translator.translate('Like', src='en', dest='pt').extra_data
) #  -> {'translation': [['Gostar', 'Like', None, None, 10]], 'all-translations': [['verbo', ['gostar', 'desejar', ...
```


  .detect()             -> Detecta o idioma de algum texto.
  .detect().lang        -> Para retornar somente o idioma.
  .detect().confidence  -> Taxa de confiança que vai de 0-1
  
```python
print(
  translator.detect('marron') 
) # -> Detected(lang=fr, confidence=0.8203125)  Perceba que marron foi indentificado  na lingua francesa com uma descrepancia.
```

```python
print(
  translator.detect('Agora quero que me retorne apenas o idioma').lang # Usar o .lang para retornar o idioma 
) #  -> pt
```


  Para se aprofundar mais, recomedo a documentação oficial.
  Googletrans: Free and Unlimited Google translate API for Python : 
    https://py-googletrans.readthedocs.io/en/latest/#
