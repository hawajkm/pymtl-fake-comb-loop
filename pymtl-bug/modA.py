from pymtl import *

class modA( Model ):
  def __init__(s):
    s.a = OutPort(32)
    s.b = InPort(8)

    s.regB = Wire(8)
    s.next_regB = Wire(8)

    @s.combinational
    def setA():
      s.a.value = 0

      # Combinational Stuff
      if(s.a == 2):
        s.a.value = 10
      else:
        s.a.value = 2

      s.next_regB.value = s.b

    @s.tick_rtl
    def seq():
      s.regB.next = s.next_regB
