##  Dynamic Currency  matrix & analyser
A high-performance python financial tool that live exchange rates via API and calculates  conversions across multiple currencies simultaneously using NumPy matrix multiplication. 

## PROJECT OVERVIEW 
this project goes beyond standard for loops by leveraging linear algebra to convert an array of base prices (USD) into multiple golbal currencies (EUR,GBP,INR,JPY,CAD) instantly. It is designed to demonstrate API integeration , robust error handling , and the power of vectorization and broadcasting in mathematical computing.

## KEY FEATURES
--> Live API Integeration : Utilizes the requests library to fetch real-time exchange rates from the Frankfuter API.

--> Resilient Architecture : Implements robust try/except blocks to handle connection errors ,timeouts ,  and HTTP errors ,automatically falling back to a hardcoded Numpy array to rates if the API fails.

--> Matrix Multiplication : Uses Numpy's dot product ( @ operator) to instantly calculate an n x m grid of exchanges rates , completely eliminating slow python loops for the core math.

--> Advanced NumPy Filtering : Features Boolean Masking to Filter and extract specific data points (e.g. , automatically isolating all converted values over 1000).

--> Data Analystics : Uses np.where() to map filtered values back to their original Usd price and target currency , and np.argmax() to programatically identify the highest resulting value in specific price tiers.

