import subprocess
import pytest

from ..helpers import BaseACS


class TestSinkcorr(BaseACS):
    """
    Process a single fullframe and a single subarray WFC dataset 
    using all standard calibration steps with the sink pixel flagging 
    and no PCTE correction.
    """
    detector = 'wfc'

    @pytest.mark.xfail
    def test_fullframe_sinkcorr(self):
        """Ported from ``wfc_sinkcorr``, routine test_sinkcorr_fullframe."""
        raw_file = 'jd1y03r5q_raw.fits'

        # Prepare input file.
        self.get_input_file(raw_file)

        # Run CALACS
        subprocess.call(['calacs.e', raw_file, '-v'])

        # Compare results
        outputs = [('jd1y03r5q_flt.fits', 'jd1y03r5q_flt_ref.fits')]
        self.compare_outputs(outputs)

    @pytest.mark.xfail
    def test_subarray_sinkcorr(self):
        """Ported from ``wfc_sinkcorr``, routine test_sinkcorr_subarr."""
        raw_file = 'jd0q13ktq_raw.fits'

        # Prepare input file.
        self.get_input_file(raw_file)

        # Run CALACS
        subprocess.call(['calacs.e', raw_file, '-v'])

        # Compare results
        outputs = [('jd0q13ktq_flt.fits', 'jd0q13ktq_flt_ref.fits')]
        self.compare_outputs(outputs)
