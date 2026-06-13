import numpy as np
import requests as rp 


# ______fetch_live_rates__________________________________

def get_live_rates(base="USD" , currencies="None"):
     """Fetch live exchange rates from frankfurter.app (free, no API key needed)."""

     if currencies is None:
        currencies = ["EUR","GBP","INR","JPY","CAD"]

     symbols = ",".join(currencies)
     url = f"https://api.frankfurter.app/latest?base={base}&symbols={symbols}"

     try:
        response = rp.get(url ,timeout=10)
        response.raise_for_status()  # raises error for 4xx/5xx responses
        data = response.json()

        #data = {
       #"date": "2026-06-09",
        #"rates": {          # ← data["rates"] points here
        #"EUR": 0.91,
        #"GBP": 0.78,
       # "INR": 83.10,
       # "JPY": 149.20,
       # "CAD": 1.34
         #}
       #}

        rates = [data["rates"][c] for c in currencies]

     except rp.exceptions.ConnectionError:
         print(" No internet connection.using fallback rates.")
     except rp.exceptions.Timeout:
         print(" Request timeout. using fallback rates.")
     except rp.exceptions.HTTPError as e:
         print(f" HTTPERROR :{e} . using fallback rates.")

         # Fallback →  using original values of array 
     return np.array([0.92, 0.79 , 83.20 , 149.50 , 1.35])       




currencies = ["EUR","GBP","INR","JPY","CAD"]


#1D array of prices in USD
prices_usd=np.array([10,50,100,150,200,250,500])

#1d array of conversion rates: [EUR , GBP , INR , JPY , CAD ]
exchange_rates = get_live_rates(currencies=currencies)
#reshape intom 5*1 column vector 
prices_col = prices_usd.reshape(-1,1)

# reshape rates into a 1x5 row vector 
rates_row = exchange_rates.reshape(1,-1)

#Generate the 2d matrix instantly 
conversion_matrix = prices_col @ rates_row


print("Exchange Rates:",currencies)
print("-" * 45)

# Loop through the rows to print them cleanly alongside the original usd prices 

for i in range(len(prices_usd)):
    usd_val = prices_usd[i]
    converted_vals = np.round(conversion_matrix[i],2) # round to 2 decimals 
    print(f"${usd_val:<5} -> {converted_vals}")


#__________After_Building_Conversion_Matrix______________

#round the full matrix
conversion_matrix=np.round(conversion_matrix,2)

#Boolean masking -> filtering valus > 1000

mask = conversion_matrix > 1000
filtered_values = conversion_matrix[mask]

print(f"\nValues > 1000 in the matrix :\n{filtered_values}")

#  Know exactly which currency & price each value belongs to ─────────
print("\n--- Detailed view (USD price | Currency | Converted Value) ---")

row_indices , column_indices = np.where(mask)  #  Returns (row_indices, col_indices) of every True position

for r , c in zip(row_indices,column_indices):
    print(f" ${prices_usd[r]:<5} | {currencies[c]:<4} | {conversion_matrix[r,c]}")

#___________np.argmax() finds the index of the highest value_____________________

row_500  = conversion_matrix[-1]
max_idx = np.argmax(row_500)
max_currency = currencies[max_idx]
max_value = row_500[max_idx]

print(f"\nHighest value for $500 -> {max_currency} at { max_value}")
