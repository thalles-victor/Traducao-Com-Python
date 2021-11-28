"""
  instalação: $ pip3 install googletrans

  No caso, foi usado a versão 3.1.0a0, para
  usar está ou outra, coloque o operador < == >
    exp: pip3 install googletrans==3.1.0a0
                                                                  

  Obs: O VSCode não reconheceu a biblioteca, porém ele
  funcionou escrevendo da maneira correda as linhas de código.
"""

from googletrans import Translator
translator = Translator()

"""
  .translate().text -> tradução mais usada
"""
print(
  translator.translate('dog', src='en', dest='pt').text
)  #  -> cão



"""
  .translate().extra_data -> Um conjundo de informações
  como, verbos, adjetivos... exemplos de uso...
"""

print(
  translator.translate('Like', src='en', dest='pt').extra_data
) #  -> {'translation': [['Gostar', 'Like', None, None, 10]], 'all-translations': [['verbo', ['gostar', 'desejar', ...

"""
  .detect() -> Detecta o idioma de algum texto.
"""

print(
  translator.detect('marron') 
) # -> Detected(lang=fr, confidence=0.8203125)  Perceba que marron foi indentificado  na lingua francesa com uma descrepancia.

print(
  translator.detect('Agora quero que me retorne apénas o idioma').lang # Usar o .lang para retornar o idioma 
) #  -> pt
