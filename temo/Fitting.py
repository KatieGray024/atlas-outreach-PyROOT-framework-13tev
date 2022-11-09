import ROOT
import scipy.optimize
import numpy as np

def get_hist_content(hist):
    hist_bin = []
    hist_content = []
    hist_uncert = []
    for i in range(0, hist.GetNbinsX()):
        hist_bin.append(hist.GetBinCenter(i + 1))
        hist_content.append(hist.GetBinContent(i + 1))
        hist_uncert.append(hist.GetBinError(i + 1))
    return hist_bin, hist_content, hist_uncert

def add_fit_hist(hist, fit_val):
    for i in range(0, hist.GetNbinsX()):
        hist.SetBinContent(i+1, hist.GetBinContent(i + 1) + fit_val[i])
    return hist

def Fit(self, paintables):
    # list of distribution to fit ('Stack' for MC and 'data' for the data)
    distribution_list = ['Stack']
    # list of distributions to fit
    hist_list = ['mass_four_lep_ext']
    #hist_bkg = paintables['Fit'].getHistogram()
    for distribution in distribution_list:
        # extract the paintable
        print(distribution, paintables[distribution])
        
        hist = paintables[distribution].getHistogram()
        # skip if hist is not in hist_list
        if not hist.GetName() in hist_list:
            continue
        
        hist_bin, hist_content, hist_uncert = get_hist_content(hist)
        #hist_bkg_bin, hist_bkg_content, hist_bkg_uncert = get_hist_content(hist_bkg)

        # print the histogram content
        print(f'{distribution} fit of {hist.GetName()} histogram')
        #print('Bin centers of the Histogram:')
        #print(hist_bin)
        #print('Entries of the Histogram:')
        #print(hist_content)

        # apply the fit
        fit_range = [80, 150]


        # plot the fit
        fit_function = ROOT.TF1("fit_function", "[0]*exp(-0.5*((x-[1])/[2])**2)", fit_range[0], fit_range[1])
        # Parameter: scale
        fit_function.SetParameter(0, 3)
        # Parameter: mean
        fit_function.SetParameter(1, 120)
        # Parameter: sigma
        fit_function.SetParameter(2, 10)

        def gauss(x, a, b, c):
            return a*np.exp(-0.5*((x-b)/c)**2)
        
        fit_val = gauss(np.array(hist_bin), 3, 120, 10)
        
        #hist_bkg = add_fit_hist(hist_bkg, fit_val)
        self.fitFunction.SetLineColor(ROOT.kBlue)
        print('color', ROOT.kBlue)
        self.fitFunction = fit_function
        self.fitFunction.Draw('same')
