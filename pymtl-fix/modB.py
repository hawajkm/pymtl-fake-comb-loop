from pymtl import *

class modB( Model ):
  def __init__(s):
    s.a = InPort(32)
    s.b = OutPort(8)

    s.temp_b = Wire(8)

    s.next_regA = Wire(32)
    s.regA = Wire(32)

    # This kind of blocks seems to cause the issue
    @s.combinational
    def setB():
      s.temp_b.value = 0

      # Combinational Stuff
      if(s.temp_b == 5):
        s.temp_b.value = 1
      else:
        s.temp_b.value = 5

      s.b.value = s.temp_b
      s.next_regA.value = s.a

    @s.tick_rtl
    def seq():
      s.regA.next = s.next_regA
