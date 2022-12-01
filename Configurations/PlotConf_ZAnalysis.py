config = {
#"Luminosity": 547, #period A
#"Luminosity": 1949, #period B
#"Luminosity": 2884, #period C
#"Luminosity": 4684, #period D
"Luminosity": 10064, #period A-D
"InputDirectory": "resultsZ",

# What Histograms are being produced?

"Histograms" : {
    "etmiss"          : {"rebin" : 1},
    "invMassZ"          : {"rebin" : 1},
    #"lep_n"          : {"rebin" : 1},
    #"mass_four_lep_ext"       : {},
    #"invMassZ1"       : {"rebin" : 3},
    #"invMassZ2"       : {"rebin" : 3},
    #"lep_n"           : {"y_margin" : 0.4},
    #"lep_pt"          : {"y_margin" : 0.4, "rebin" : 4},
    #"lep_eta"         : {"y_margin" : 0.5, "rebin" : 3},
    #"lep_E"           : {"rebin" : 3},
    #"lep_phi"         : {"y_margin" : 0.6, "rebin" : 4,},
    #"lep_charge"      : {"y_margin" : 0.6},
    #"lep_type"        : {"y_margin" : 0.5,},
    #"lep_ptconerel30" : {"y_margin" : 0.3, "rebin" : 4},
    #"lep_etconerel20" : {"y_margin" : 0.3, "rebin" : 4},

},



# Histogram Design


"Paintables": {
    "Stack": {
        "Order": ["Zee", "Zmumu"], # "ttbar", "Zee", "Zmumu", "Ztautau", "HZZ", "ZZ", "Other"
        "Processes" : {
#            "ttbar" : {
#                "Color"         : "#ff9900",
#                "Contributions" : ["ttbar_lep"]},
            "Zee" : {
                "Color"         : "#0000ff",
                "Contributions" : ["Zee"]},  
            "Zmumu" : {
                "Color"         : "#006666",
                "Contributions" : ["Zmumu"]},
#            "Ztautau" : {
#                "Color"         : "#660066",
#                "Contributions" : ["Ztautau"]},
#            "HZZ" : {
#                "Color"         : "#ff0000",
#                "Contributions" : ["ggH125_WW2lep", "VBFH125_WW2lep"]},
#            "ZZ" : {
#                "Color"         : "#00cdff",
#                "Contributions" : ["llll"
#                                   ,"ZqqZll"
#                                   ,"llvv"
#                                  ]},
#            "Other": {       
#                "Color"         : "#6b59d3",
#                "Contributions" : ["WqqZll", "lllv"]},
        }
    },
    "data" : {
        "Contributions": ["data_A", "data_B", "data_C", "data_D"]}
},

"Depictions": {
    "Order": ["Main", "Data/MC"],
    "Definitions" : {
        "Data/MC": {
            "type"       : "Agreement",
            "Paintables" : ["data", "Stack"]
        },
        
        "Main": {
            "type"      : "Main",
            "Paintables": ["Stack", "data"],
            
            #Configure Fit
            #Parameters not necessary for ROOT pre-defined functions ("fitfunction": gaus, pol2, landau, or expo)
            
            "Fits" : {
                "invMassZ"          : {"fitfunction" : "[0]*(2.0*(2)**(1/2)*[1]*[2]*(([1]**2*([1]**2 + [2]**2))**(1/2))/((3.1415)*([1]**2 + (([1]**2*([1]**2 + [2]**2))**(1/2)))**(1/2)))/((x**2 - [1]**2)**2 + [1]**2*[2]**2)", "range" : [80,100], "parameters" : [1166*100, 9.07*10, 10], "background" : "none"},
                
                #"etmiss"          : {"fitfunction" : "gaus", "range" : [80,100], "parameters" : [], "background" : "none"},
                #"lep_n"          : {"fitfunction" : "gaus", "range" : [80,100], "parameters" : [], "background" : "none"},
                #"invMassZ2"       : {"fitfunction" : "gaus", "range" : [80,100], "parameters" : [], "background" : "none"},

                

            },
        },
    }
},
}
