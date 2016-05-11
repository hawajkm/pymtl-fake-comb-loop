from pymtl import *

from modA  import *
from modB  import *

class modAll( Model ):
  def __init__(s):
    s.modA = modA()
    s.modB = modB()

    s.connect(s.modA.a, s.modB.a)
    s.connect(s.modB.b, s.modA.b)
