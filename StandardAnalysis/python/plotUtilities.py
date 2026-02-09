# Note: these imports are necessary for plot styling, however importing them in a CMSSW framework
#       configuration causes a segfault when saving skims. The ROOT modules seem to not play nicely
#       with CMSSW, so be sure to only use this for plot-making scripts.

import warnings

from OSUT3Analysis.Configuration.histogramUtilities import *
from DisappTrks.StandardAnalysis.tdrstyle import *
from DisappTrks.StandardAnalysis.utilities import *

from ctypes import c_double # see https://root-forum.cern.ch/t/issue-with-using-integralanderror-with-pyroot/53182/2


def get_hist(file_path, channel, hist):
    """Retrieve a histogram from a ROOT file.

    Args:
        file_path: Full path to the ROOT file.
        channel: Directory path within the ROOT file.
        hist: Name of the histogram.

    Returns:
        A cloned histogram detached from the file.

    Raises:
        FileNotFoundError: If the ROOT file cannot be opened.
        KeyError: If the histogram is not found in the file.
    """
    input_file = TFile(file_path)
    if not input_file or input_file.IsZombie():
        raise FileNotFoundError(f"Could not open ROOT file: {file_path}")

    hist_path = f"{channel}/{hist}"
    h0 = input_file.Get(hist_path)
    if not h0:
        input_file.Close()
        raise KeyError(f"Histogram '{hist_path}' not found in file: {file_path}")

    h = h0.Clone()
    h.SetDirectory(0)
    input_file.Close()
    return h

def setStyle(h, color = 1):
    h.SetLineColor(color)
    h.SetLineStyle(1)
    h.SetLineWidth(2)
    h.SetMarkerColor(color)
    h.SetMarkerStyle(20)
    h.SetMarkerSize(1.5)
    h.SetTitle("")

def setCanvasStyle(canvas):
    canvas.SetHighLightColor(2)
    canvas.SetFillColor(0)
    canvas.SetBorderMode(0)
    canvas.SetBorderSize(2)
    canvas.SetTickx(1)
    canvas.SetTicky(1)
    canvas.SetLeftMargin(0.128141)
    canvas.SetRightMargin(0.12782)
    canvas.SetBottomMargin(0.0971503)
    canvas.SetTopMargin(0.0712435)
    canvas.SetFrameFillStyle(0)
    canvas.SetFrameBorderMode(0)
    canvas.SetFrameFillStyle(0)
    canvas.SetFrameBorderMode(0)

def setAxisStyle(h, xTitle = "", yTitle = "", xRange = (0, 0), yRange = (0, 0)):
    h.GetXaxis().SetNdivisions(505)
    h.GetXaxis().SetLabelOffset(0.005)
    h.GetXaxis().SetLabelSize(0.04)
    h.GetXaxis().SetTitleOffset(1.0)
    h.GetXaxis().SetTitleSize(0.04)
    if xTitle != "":
        h.GetXaxis().SetTitle(xTitle)
    if xRange[0] != 0 or xRange[1] != 0:
        h.GetXaxis().SetRangeUser(xRange[0], xRange[1])
    h.GetYaxis().SetNdivisions(505)
    h.GetYaxis().SetLabelOffset(0.005)
    h.GetYaxis().SetLabelSize(0.04)
    h.GetYaxis().SetTitleOffset(1.5)
    h.GetYaxis().SetTitleSize(0.04)
    if yTitle != "":
        h.GetYaxis().SetTitle(yTitle)
    if yRange[0] != 0 or yRange[1] != 0:
        h.GetYaxis().SetRangeUser(yRange[0], yRange[1])

def getHist(sample, condor_dir, channel, hist, quietFailure = False):
    """Deprecated: Use get_hist(file_path, channel, hist) instead."""
    warnings.warn(
        "getHist is deprecated and will be removed in a future release. "
        "Use get_hist(file_path, channel, hist) instead.",
        DeprecationWarning,
        stacklevel=2
    )
    dataset_file = "condor/%s/%s.root" % (condor_dir, sample)
    try:
        return get_hist(dataset_file, channel, hist)
    except (FileNotFoundError, KeyError) as e:
        if not quietFailure:
            print(f"ERROR [getHist]: {e}")
        return 0

def get_hist_from_projection_z(file_path, channel, hist, fiducial_electron_sigma_cut, fiducial_muon_sigma_cut, alternate_1d_hist="", verbose=False):
    """Retrieve a histogram from a 3D projection with fiducial cuts.

    Args:
        file_path: Full path to the ROOT file.
        channel: Directory path within the ROOT file.
        hist: Name of the 3D histogram.
        fiducial_electron_sigma_cut: Upper bound for electron sigma cut.
        fiducial_muon_sigma_cut: Upper bound for muon sigma cut.
        alternate_1d_hist: Fallback 1D histogram if 3D not found.
        verbose: If True, print warning when using fallback.

    Returns:
        The projected histogram, or None if not found.

    Raises:
        KeyError: If neither the 3D histogram nor alternate is found.
    """
    count_projections = 0 if not hasattr(get_hist_from_projection_z, "count_projections") else getattr(get_hist_from_projection_z, "count_projections")

    try:
        h3d = get_hist(file_path, channel, hist)
    except (FileNotFoundError, KeyError):
        h3d = None

    if not h3d:
        if alternate_1d_hist:
            if verbose:
                print("WARNING: not applying fiducial cuts via projections.")
            return get_hist(file_path, channel, alternate_1d_hist)
        return None

    h = h3d.ProjectionZ(hist + "_pz" + str(count_projections),
                        0, h3d.GetXaxis().FindBin(fiducial_electron_sigma_cut) - 1,
                        0, h3d.GetYaxis().FindBin(fiducial_muon_sigma_cut) - 1, "e")

    count_projections += 1
    setattr(get_hist_from_projection_z, "count_projections", count_projections)
    return h


def getHistFromProjectionZ(sample, condor_dir, channel, hist, fiducialElectronSigmaCut, fiducialMuonSigmaCut, alternate1DHist="", verbose=False):
    """Deprecated: Use get_hist_from_projection_z(file_path, ...) instead."""
    warnings.warn(
        "getHistFromProjectionZ is deprecated and will be removed in a future release. "
        "Use get_hist_from_projection_z(file_path, channel, hist, ...) instead.",
        DeprecationWarning,
        stacklevel=2
    )
    dataset_file = "condor/%s/%s.root" % (condor_dir, sample)
    try:
        return get_hist_from_projection_z(dataset_file, channel, hist, fiducialElectronSigmaCut, fiducialMuonSigmaCut, alternate_1d_hist=alternate1DHist, verbose=verbose)
    except (FileNotFoundError, KeyError) as e:
        print(f"ERROR [getHistFromProjectionZ]: {e}")
        return None


def get_hist_integral_from_projection_z(file_path, channel, fiducial_electron_sigma_cut, fiducial_muon_sigma_cut):
    """Get the yield from a 3D histogram projection with fiducial cuts.

    Args:
        file_path: Full path to the ROOT file.
        channel: Directory path within the ROOT file.
        fiducial_electron_sigma_cut: Upper bound for electron sigma cut.
        fiducial_muon_sigma_cut: Upper bound for muon sigma cut.

    Returns:
        Tuple of (yield, statistical_error).

    Raises:
        KeyError: If the histogram is not found.
    """
    hist = "Track-met Plots/metNoMuMinusOnePtVsMaxSigmaForFiducialTracks"
    h = get_hist_from_projection_z(file_path, channel, hist, fiducial_electron_sigma_cut, fiducial_muon_sigma_cut, alternate_1d_hist="Met Plots/metNoMu")
    statError_ = c_double(0.0)
    yield_ = h.IntegralAndError(0, -1, statError_)
    return (yield_, statError_.value)


def getHistIntegralFromProjectionZ(sample, condor_dir, channel, fiducialElectronSigmaCut, fiducialMuonSigmaCut):
    """Deprecated: Use get_hist_integral_from_projection_z(file_path, ...) instead."""
    warnings.warn(
        "getHistIntegralFromProjectionZ is deprecated and will be removed in a future release. "
        "Use get_hist_integral_from_projection_z(file_path, channel, ...) instead.",
        DeprecationWarning,
        stacklevel=2
    )
    dataset_file = "condor/%s/%s.root" % (condor_dir, sample)
    try:
        return get_hist_integral_from_projection_z(dataset_file, channel, fiducialElectronSigmaCut, fiducialMuonSigmaCut)
    except (FileNotFoundError, KeyError) as e:
        print(f"ERROR [getHistIntegralFromProjectionZ]: {e}")
        return (0, 0)

def get_yield(file_path, channel, hist):
    """Get the yield (integral and error) of a histogram.

    Args:
        file_path: Full path to the ROOT file.
        channel: Directory path within the ROOT file.
        hist: Name of the histogram.

    Returns:
        Tuple of (yield, statistical_error).

    Raises:
        FileNotFoundError: If the ROOT file cannot be opened.
        KeyError: If the histogram is not found in the file.
    """
    h = get_hist(file_path, channel, hist)
    statError_ = c_double(0.0)
    yield_ = float(h.IntegralAndError(0, h.GetNbinsX() + 1, statError_))
    return (yield_, statError_.value)


def getYield(sample, condor_dir, channel):
    """Deprecated: Use get_yield(file_path, channel, hist) instead."""
    warnings.warn(
        "getYield is deprecated and will be removed in a future release. "
        "Use get_yield(file_path, channel, hist) instead.",
        DeprecationWarning,
        stacklevel=2
    )
    dataset_file = "condor/%s/%s.root" % (condor_dir, sample)
    try:
        return get_yield(dataset_file, channel, "Met Plots/metPt")
    except (FileNotFoundError, KeyError) as e:
        print(f"ERROR [getYield]: {e}")
        return 0

def getHistFromChannelDict(channel, hist, quietFailure = False):
    """Deprecated: Use get_hist(file_path, channel, hist) instead."""
    warnings.warn(
        "getHistFromChannelDict is deprecated and will be removed in a future release. "
        "Use get_hist(file_path, channel, hist) instead.",
        DeprecationWarning,
        stacklevel=2
    )
    if "sample" not in channel or "condorDir" not in channel or "name" not in channel:
        raise ValueError(f"Bad channel given to getHistFromChannelDict: {channel}")
    dataset_file = "condor/%s/%s.root" % (channel["condorDir"], channel["sample"])
    channel_name = channel["name"] + "Plotter"
    try:
        return get_hist(dataset_file, channel_name, hist)
    except (FileNotFoundError, KeyError) as e:
        if not quietFailure:
            print(f"ERROR [getHistFromChannelDict]: {e}")
        return 0

def addChannelExtensions(histogram, channel, histName):
    if "extensions" in channel:
        for x in channel["extensions"]:
            histogram.Add (getHistFromChannelDict (x, histName))

