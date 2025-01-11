# SPDX-FileCopyrightText: © 2024 Jimmy Fitzpatrick <jcfitzpatrick12@gmail.com>
# This file is part of SPECTRE
# SPDX-License-Identifier: GPL-3.0-or-later

from enum import Enum

class PanelName(Enum):
    """Defined panel names, each with a corresponding fully implemented `BasePanel` subclass.
    
    :ivar SPECTROGRAM: Plot a spectrogram.
    :ivar FREQUENCY_CUTS: Line-plot spectrums in some spectrogram.
    :ivar TIME_CUTS: Line-plot spectral component time series in some spectrogram.
    :ivar INTEGRAL_OVER_FREQUENCY: Line-plot spectrograms numerically integrated over frequency.
    """
    SPECTROGRAM             = "spectrogram"
    FREQUENCY_CUTS          = "frequency_cuts"
    TIME_CUTS               = "time_cuts"
    INTEGRAL_OVER_FREQUENCY = "integral_over_frequency"