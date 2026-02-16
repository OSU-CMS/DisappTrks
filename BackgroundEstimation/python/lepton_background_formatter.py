from dataclasses import dataclass
from tabulate import tabulate

@dataclass
class IntermediateResult:
    label: str
    value: float
    error: float
    formula: str

class LeptonBackgroundFormatter:
    def __init__(self):
        self._results = {}

    def add_result(self, label, value, error, formula=""):
        self._results[label] = IntermediateResult(label, value, error, formula)

    def print_default(self, nlayers, is_verbose):
        rows = [
            self._format_default(self._results["Lumi scale factor"], is_verbose),
            self._format_default(self._results["Lepton trigger eff"], is_verbose),
            self._format_default(self._results["N_tagged (unscaled)"], is_verbose),
            self._format_default(self._results["N_tagged"], is_verbose),
            self._format_default(self._results["P(pass lepton veto)"], is_verbose),
            self._format_default(self._results["P(pass MET cut)"], is_verbose),
            self._format_default(self._results["P(pass MET trigger)"], is_verbose),
            self._format_default(self._results["N_est"], is_verbose)
        ]

        headers = [f"NLayers {nlayers}", "Value"]
        if is_verbose:
            headers.append("Details")

        print(tabulate(rows, headers=headers, tablefmt="simple_outline"))
        print()

    def print_latex(self, nlayers, include_year=False):
        cols = [
            self._format_latex_value(self._results["Lepton trigger eff"].value, self._results["Lepton trigger eff"].error, precision=3),
            self._format_latex_value(self._results["N_tagged"].value, self._results["N_tagged"].error, precision=0),
            self._format_latex_value(self._results["P(pass lepton veto)"].value, self._results["P(pass lepton veto)"].error, precision=2, use_sci_notation=True),
            self._format_latex_value(self._results["P(pass MET cut)"].value, self._results["P(pass MET cut)"].error, precision=3),
            self._format_latex_value(self._results["P(pass MET trigger)"].value, self._results["P(pass MET trigger)"].error, precision=3),
            self._format_latex_value(self._results["N_est"].value, self._results["N_est"].error, precision=2),
        ]
        nlayers_label = r"\geq 6" if nlayers == "6" else nlayers

        if include_year:
            print(r"\multirow{4}{*}{YEAR} & " + f"${nlayers_label}$ & " + " & ".join(cols) + r" \\")
        else:
            print(f"& ${nlayers_label}$ & " + " & ".join(cols) + r" \\")

    def _format_default(self, result, is_verbose):
        value_str = f"{result.value:.8g} +/- {result.error:.8g}"

        row = [result.label, value_str]
        if is_verbose:
            row.append(result.formula)

        return row

    def _format_latex_value(self, value, error, precision=2, use_sci_notation=False):
        use_asymmetric = value < error

        if use_sci_notation:
            if value != 0:
                exponent = int(math.floor(math.log10(abs(value))))
            else:
                exponent = int(math.floor(math.log10(abs(error))))
            mantissa = value / (10 ** exponent)
            err_mantissa = error / (10 ** exponent)

            if use_asymmetric:
                return (f"$({mantissa:.{precision}f}_{{-{mantissa:.{precision}f}}}"
                        f"^{{+{err_mantissa:.{precision}f}}}) \\times 10^{{{exponent}}}$")
            else:
                return f"$({mantissa:.{precision}f} \\pm {err_mantissa:.{precision}f}) \\times 10^{{{exponent}}}$"
        else:
            if use_asymmetric:
                return f"${value:.{precision}f}_{{-{value:.{precision}f}}}^{{+{error:.{precision}f}}}$"
            else:
                return f"${value:.{precision}f} \\pm {error:.{precision}f}$"
