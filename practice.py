# from bs4 import BeautifulSoup
# import requests
# url = "https://aeon.co/essays/why-you-need-your-whole-body-from-head-to-toes-to-think"
# r = requests.get(url)

# soup = BeautifulSoup(r.content,'html.parser')
# # print(soup.prettify())

# article = soup.find('div',class_ = 'article-body')
# # print(article.get_text(strip=True))

# print(soup.title.string)

# for h in soup.find_all(['h1','h2','h3','h4','h5','h6']):
#     print(h.get_text(strip=True))

# for link in soup.find_all('a'):
#     print(link.get('href'))

# links = [a['href'] for a in soup.find_all('a',href = True)]
# print(links)    


import practice as np

# choice = int(input("enter an how many numbers you want in array:-\n"))

# numbers = []

# for i in range(choice):
#   num = int(input(f"Enter number {i+1}:-"))
#   numbers.append(num)


# arr = numpy.array(numbers) 

# print(arr)
# print(numpy.__version__)

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr.ndim)

print(arr[-1,-1,-3])
print(arr[1,0,:3])

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.flatten()
print(newarr)
print(newarr.base)

newarr = np.ravel(arr)
newarr[1]=90
print(newarr)
print(newarr.base)

flipp_rows=np.flip(arr,axis=0)
print(flipp_rows)

print("\n\n")

flipp_cols=np.flip(arr,axis=1)
print(flipp_cols)


lr_flipped=np.fliplr(arr)
print(lr_flipped)

ud_flipped=np.flipud(arr)
print(ud_flipped)

#rotating counter clockwise

rotated_once=np.rot90(arr)
print(rotated_once)

rotated_twice = np.rot90(arr,k=2)
print(rotated_twice)

print("\n\n")

rolled_flat = np.roll(arr,2)
print(rolled_flat)

print("\n")

rolled_rows=np.roll(arr,1,axis=1)
print(rolled_rows)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print("x represents the 2-D array:")
  print(x)

print("The numbers are:-\n")
for x in arr:
  for y in x:
     for z in y:
      print(z)


print("\n\n")
print("numbers after using nditer:-\n")
for x in np.nditer(arr):
    print(x)
    
print("\n\n")
for x in np.nditer(arr,flags=["buffered"],op_dtypes=["U"]):
   print(x)

   