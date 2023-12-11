from math import *

neopred_ascii = log2(255)

neopred_hartli = log2(50)

razryad_ascii = round(neopred_ascii)

razryad_hartli = round(neopred_hartli)

absolute_ascii = razryad_ascii - neopred_ascii

absolute_hartli = razryad_hartli - neopred_hartli

otnos_ascii = (neopred_ascii-absolute_ascii) / neopred_ascii

otnos_hartli = (neopred_hartli - absolute_hartli) / neopred_hartli

