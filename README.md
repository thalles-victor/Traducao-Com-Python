# Traducao-Com-Python
Esse exemplo mostra como traduzir um usando python e a biblioteca googletrans

  instalação: $ pip3 install googletrans

  No caso, foi usado a versão 3.1.0a0, para
  usar está ou outra, coloque o operador < == >
    exp: pip3 install googletrans==3.1.0a0
                                                                  

  Obs: O VSCode não reconheceu a biblioteca, porém ele
  funcionou escrevendo da maneira correda as linhas de código.
  
Adicionando ao projeto
```
from googletrans import Translator
translator = Translator()
```

  .translate().text -> tradução mais usada

print(
  translator.translate('Undefined', src='en', dest='pt').text
)




  .translate().extra_data -> Um conjundo de informações
  como, varbos, adjetivos... exemplos de uso...

print(
  translator.translate('Like', src='en', dest='pt').extra_data
)
