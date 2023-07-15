#pip install countryinfo
from countryinfo import CountryInfo

count= input("Enter your country : ")
country = CountryInfo(count)
print("capital is: ",country.capital())
print("currencies is: ",country.currencies())
print("languaga is: ",country.languages())
print("Borders are: ",country.borders())
print("others names: ",country.alt_spellings())