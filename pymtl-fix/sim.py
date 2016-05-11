#=========================================================================
# Unit Test: DecodeUnit
#=========================================================================

import pytest

from pymtl      import *

from pclib.test import mk_test_case_table, run_sim
from pclib.test import TestSource, TestSink

from modAll     import *

#-------------------------------------------------------------------------
# Test harness
#-------------------------------------------------------------------------

class TestHarness( Model ):

  # Constructor

  def __init__( s, dut, test_verilog ):

    # Instantiate units

    s.dut   = dut

    # Translation

    if test_verilog:
      s.dut = TranslationTool(s.dut)

    s.counter = 0

  def done(s):
    s.counter = s.counter + 1
    return s.counter > 100

def run_test( dut, test_params, dump_vcd = False, test_verilog = False, max_cycles=5000 ):

  # Setup the model

  testHarness = TestHarness(dut, test_verilog)

  # Run the simulation
  run_sim(testHarness, False, max_cycles = max_cycles)

#-------------------------------------------------------------------------
# Test case: all
#-------------------------------------------------------------------------

all_msgs  = [
               # inst                    ex_id          ex_fn           v0 p0 tag0 data0 v1 p1 tag1 data1   wen wtag
]

#-------------------------------------------------------------------------
# Test case table
#-------------------------------------------------------------------------

test_case_table = mk_test_case_table([
  (             ),
  [ "default"   ],
])

#-------------------------------------------------------------------------
# Test cases
#-------------------------------------------------------------------------

@pytest.mark.parametrize( **test_case_table )
def test( test_params, dump_vcd, test_verilog ):
  run_test( modAll(), test_params, dump_vcd, test_verilog )
