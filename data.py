# https://en.wikipedia.org/wiki/2016_Summer_Olympics_Parade_of_Nations

# https://www.olympic.org/national-olympic-committees
# The mission of these committees is to develop, promote and protect the Olympic Movement
# in their respective countries. Today there are 206 NOCs.

# https://en.wikipedia.org/wiki/National_Olympic_Committee

# cannonical name is the first in the list
national_olympic_committees = {
    "GRE": ["Greece"],
    "AFG": ["Afghanistan"],
    "ALB": ["Albania"],
    "GER": ["Germany"],
    "AND": ["Andorra"],
    "ANG": ["Angola"],
    "KSA": ["Saudi Arabia"],
    "ALG": ["Algeria"],
    "ARG": ["Argentina"],
    "ARM": ["Armenia"],
    "ARU": ["Aruba"],
    "AUS": ["Australia"],
    "AUT": ["Austria"],
    "AZE": ["Azerbaijan"],
    "BAH": ["Bahamas"],
    "BRN": ["Bahrain"],
    "BAN": ["Bangladesh"],
    "BAR": ["Barbados"],
    "BLR": ["Belarus"],
    "BEL": ["Belgium"],
    "BIZ": ["Belize"],
    "BEN": ["Benin"],
    "BER": ["Bermuda"],
    "BOL": ["Bolivia"],
    "BOT": ["Botswana"],
    "BRU": ["Brunei Darussalam"],
    "BUL": ["Bulgaria"],
    "BUR": ["Burkina Faso"],
    "BDI": ["Burundi"],
    "BHU": ["Bhutan"],
    "CPV": ["Cape Verde"],
    "CMR": ["Cameroon"],
    "CAM": ["Cambodia"],
    "CAN": ["Canada"],
    "QAT": ["Qatar"],
    "KAZ": ["Kazakhstan"],
    "CHA": ["Chad"],
    "CHI": ["Chile"],
    "CYP": ["Cyprus"],
    "SIN": ["Singapore"],
    "COL": ["Colombia"],
    "COM": ["Comoros"],
    "CIV": ["Ivory Coast"],
    "CRC": ["Costa Rica"],
    "CRO": ["Croatia"],
    "CUB": ["Cuba"],
    "DEN": ["Denmark"],
    "DJI": ["Djibouti"],
    "EGY": ["Egypt"],
    "ESA": ["El Salvador"],
    "ECU": ["Ecuador"],
    "ERI": ["Eritrea"],
    "SVK": ["Slovakia"],
    "SLO": ["Slovenia"],
    "ESP": ["Spain"],
    "EST": ["Estonia"],
    "ETH": ["Ethiopia"],
    "FIJ": ["Fiji"],
    "PHI": ["Philippines"],
    "FIN": ["Finland"],
    "FRA": ["France"],
    "GAB": ["Gabon"],
    "GAM": ["Gambia"],
    "GHA": ["Ghana"],
    "GEO": ["Georgia"],
    "GRN": ["Grenada"],
    "GUM": ["Guam"],
    "GUA": ["Guatemala"],
    "GUY": ["Guyana"],
    "HAI": ["Haiti"],
    "HON": ["Honduras"],
    "HUN": ["Hungary"],
    "YEM": ["Yemen"],
    "IND": ["India"],
    "INA": ["Indonesia"],
    "IRQ": ["Iraq"],
    "IRL": ["Ireland"],
    "ISL": ["Iceland"],
    "ISR": ["Israel"],
    "ITA": ["Italy"],
    "JAM": ["Jamaica"],
    "JPN": ["Japan"],
    "JOR": ["Jordan"],
    "KIR": ["Kiribati"],
    "KOS": ["Kosovo"],
    "KUW": ["Kuwait"],
    "LES": ["Lesotho"],
    "LAT": ["Latvia"],
    "LIB": ["Lebanon"],
    "LBR": ["Liberia"],
    "LBA": ["Libya"],
    "LIE": ["Liechtenstein"],
    "LTU": ["Lithuania"],
    "LUX": ["Luxembourg"],
    "MAD": ["Madagascar"],
    "MAS": ["Malaysia"],
    "MAW": ["Malawi"],
    "MDV": ["Maldives"],
    "MLI": ["Mali"],
    "MLT": ["Malta"],
    "MAR": ["Morocco"],
    "MRI": ["Mauritius"],
    "MTN": ["Mauritania"],
    "MEX": ["Mexico"],
    "MOZ": ["Mozambique"],
    "MON": ["Monaco"],
    "MGL": ["Mongolia"],
    "MNE": ["Montenegro"],
    "MYA": ["Myanmar"],
    "NAM": ["Namibia"],
    "NRU": ["Nauru"],
    "NEP": ["Nepal"],
    "NCA": ["Nicaragua"],
    "NIG": ["Niger"],
    "NGR": ["Nigeria"],
    "NOR": ["Norway"],
    "NZL": ["New Zealand"],
    "OMA": ["Oman"],
    "NED": ["Netherlands"],
    "PLW": ["Palau"],
    "PLE": ["Palestine"],
    "PAN": ["Panama"],
    "PAK": ["Pakistan"],
    "PAR": ["Paraguay"],
    "PER": ["Peru"],
    "POL": ["Poland"],
    "PUR": ["Puerto Rico"],
    "POR": ["Portugal"],
    "KEN": ["Kenya"],
    "KGZ": ["Kyrgyzstan"],
    "CZE": ["Czech Republic"],
    "ROU": ["Romania"],
    "RWA": ["Rwanda"],
    "SAM": ["Samoa"],
    "ASA": ["American Samoa"],
    "SMR": ["San Marino"],
    "LCA": ["Saint Lucia"],
    "SEN": ["Senegal"],
    "SLE": ["Sierra Leone"],
    "SRB": ["Serbia"],
    "SEY": ["Seychelles"],
    "SYR": ["Syria"],
    "SOM": ["Somalia"],
    "SRI": ["Sri Lanka"],
    "SWZ": ["Swaziland"],
    "SWE": ["Sweden"],
    "SUI": ["Switzerland"],
    "SUR": ["Suriname"],
    "THA": ["Thailand"],
    "TJK": ["Tajikistan"],
    "TAN": ["Tanzania"],
    "TLS": ["Timor-Leste"],
    "TOG": ["Togo"],
    "TGA": ["Tonga"],
    "TUN": ["Tunisia"],
    "TKM": ["Turkmenistan"],
    "TUR": ["Turkey"],
    "TUV": ["Tuvalu"],
    "UKR": ["Ukraine"],
    "UGA": ["Uganda"],
    "URU": ["Uruguay"],
    "UZB": ["Uzbekistan"],
    "VAN": ["Vanuatu"],
    "VEN": ["Venezuela"],
    "VIE": ["Vietnam"],
    "ZAM": ["Zambia"],
    "ZIM": ["Zimbabwe"],
    "BRA": ["Brazil"],
    "RSA": ["South Africa"],
    "CAF": ["Central African Republic"],
    "DMA": ["Dominica"],
    "DOM": ["Dominican Republic"],

    # Special Cases

    "BIH": ["Bosnia and Herzegovina", "Bosnia", "Herzegovina"],
    "UAE": ["United Arab Emirates", "UAE"],
    "RUS": ["Russia", "Russian Federation"],
    "FSM": ["Federated States of Micronesia", "Micronesia"],
    "USA": ["United States", "United States of America", "America", "US"],
    "HKG": ["Hong Kong, China", "Hong Kong"],
    "GBR": ["Britain", "Great Britain", "United Kingdom", "England", "UK"],
    "CAY": ["Cayman Islands", "Cayman"],
    "COK": ["Cook Islands", "Cook"],
    "MHL": ["Marshall Islands"],
    "SOL": ["Solomon Islands", "Solomon"],
    "MDA": ["Republic of Moldova", "Moldova"],
    "IRI": ["Islamic Republic of Iran", "Iran"],
    "CHN": ["People's Republic of China", "China"],
    "LAO": ["Lao People's Democratic Republic", "Laos"],
    "SKN": ["Saint Kitts and Nevis", "Saint Kitts", "Kitts"],
    "VIN": ["Saint Vincent and the Grenadines", "Saint Vincent", "Grenadines"],
    "TPE": ["Taiwan", "Chinese Taipei"],
    "TTO": ["Trinidad and Tobago", "Trinidad", "Tobago"],
    "MKD": ["Former Yugoslav Republic of Macedonia", "Yugoslav", "Macedonia"],
    "ANT": ["Antigua and Barbuda", "Antigua", "Barbuda"],
    "ROA": ["Refugee Olympic Athletes", "Refugee"],

    # Edge Cases

    "STP": ["São Tomé and Príncipe"],

    "KOR": ["Republic of Korea", "South Korea", "Korea"],
    "PRK": ["Democratic People's Republic of Korea", "North Korea"],

    "GUI": ["Guinea"],
    "GBS": ["Guinea-Bissau"],
    "GEQ": ["Equatorial Guinea"],
    "PNG": ["Papua New Guinea"],

    "SUD": ["Sudan"],
    "SSD": ["South Sudan"],

    "CGO": ["Congo"],
    "COD": ["Democratic Republic of the Congo", "Democratic Congo", "Republic of Congo", "Republic Congo"],

    "ISV": ["Virgin Islands"],
    "IVB": ["British Virgin Islands"],
}

reversed_national_olympic_committees = {}

for abbreviation, names in national_olympic_committees.items():
    abbreviation = abbreviation.lower()
    for name in names:
        name = name.lower()
        if name in reversed_national_olympic_committees:
            raise Exception("conflict! %s is already in dict. it is currently mapped to %s and was going to be mapped to %s" % (
                name, reversed_national_olympic_committees[name], abbreviation))
        else:
            reversed_national_olympic_committees[name] = abbreviation
    reversed_national_olympic_committees[abbreviation] = abbreviation
