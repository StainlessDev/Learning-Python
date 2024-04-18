def gto_value(year):
    if year >= 1962 and year <= 1964:
        return "18,500"
    elif year >= 1965 and year <= 1968:
        return "6,000"
    elif year >= 1969 and year <= 1971:
        return "12,000"
    elif year >= 1972 and year <= 1975:
        return "48,000"
    elif year >= 1976 and year <= 1980:
        return "200,000"
    elif year >= 1981 and year <= 1985:
        return "650,000"
    elif year >= 1986 and year <= 2012:
        return "35,000,000"
    elif year >= 2013 and year <= 2014:
        return "52,000,000"
    else:
        return "Value not available"

year = int(input("Enter a year: "))
approximate_value = gto_value(year)

if approximate_value == "Value not available":
    print(f"The value of a Ferrari GTO in {year} is not available.")
else:
    print(f"The approximate value of a Ferrari GTO in {year} is ${approximate_value}.")