import nose.tools as nt
import numpy as np

from sigfigs import sigFigs

class base_sigFigs(object):
    @nt.raises(ValueError)
    def test_inf(self):
        sigFigs(np.inf, 3)

    @nt.raises(ValueError)
    def test_NaN(self):
        sigFigs(np.nan, 3)

    @nt.raises(ValueError)
    def test_too_few_sig_figs(self):
        sigFigs(1.234, 0)

    def test_7(self):
        nt.assert_equal(sigFigs(self.maininput, 7), self.known_7)

    def test_3(self):
        nt.assert_equal(sigFigs(self.maininput, 3), self.known_3)

    def test_3_roundup(self):
        nt.assert_equal(sigFigs(self.rndup_input, 3), self.known_roundup)

class test_sigFigs_LT1(base_sigFigs):
    def setup(self):
        self.maininput = 0.1234567
        self.rndup_input = 0.1239567
        self.known_3 = '0.123'
        self.known_7 = '0.1234567'
        self.known_roundup = '0.124'

class test_sigFigs_GT1(base_sigFigs):
    def setup(self):
        self.maininput = 1.234567
        self.rndup_input = 1.239567
        self.known_3 = '1.23'
        self.known_7 = '1.234567'
        self.known_roundup = '1.24'

class test_sigFigs_LargeInt(base_sigFigs):
    def setup(self):
        self.maininput = 123456722
        self.rndup_input = 123956789
        self.known_3 = '123,000,000'
        self.known_7 = '123,456,700'
        self.known_roundup = '124,000,000'
