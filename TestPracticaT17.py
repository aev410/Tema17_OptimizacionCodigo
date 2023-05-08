from PracticaT17 import Media
from unittest.mock import patch

def test_add():
    media = Media()
    assert len(media.array_numeros) == 0
    media.add(1)
    assert len(media.array_numeros) == 1
    
def test_media():
    media = Media()
    media.array_numeros.clear()
    media.add(2)
    media.add(2)
    assert media.media() == 2

def test_array():
    meida = Media()
    assert meida.array() == [2,2]


