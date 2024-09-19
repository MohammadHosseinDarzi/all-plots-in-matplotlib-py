import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a line plot
plt.plot(x, y)

# Add titles and labels
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show the plot
plt.show()

########################################################################################################################################
plt.plot(x, y, color='red', linestyle='--', marker='x')
plt.title("Customized Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)  # Add a grid

plt.show()
########################################################################################################################################

categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 2]
#plt.barh(categories, values, color='orange')

plt.bar(categories, values, color='orange')
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

######################################################################################################################################################

#We have lots of Markers 
plt.scatter(x, y, color='green', marker='*' , s=209)
plt.title("Scatter Plot")
plt.xlabel("India")
plt.ylabel("Y-axis")
plt.show()

###########################################################################################################################################

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

plt.hist(data, bins=5, color='purple', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

#########################################################################################################################################

x = [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
a = [8 , 1 , 3 , 4, 7 , 1 , 9 , 4 , 7]
b = [2 , 4, 6,8,9,7,5 , 5 , 9]

plt.scatter(x , a , marker="." , c = 'g' , s=100)
plt.scatter(x , b , marker="*" , c = 'r' , s=150)

plt.show()

#########################################################################################################################################\

x = [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
a = [8 , 1 , 3 , 4, 7 , 1 , 9 , 4 , 7]
b = [2 , 4, 6,8,9,7,5 , 5 , 9]

plt.subplot(1,2,1)
plt.scatter(x , a , marker='.' , s=100 , c='red')

plt.subplot(1,2,2)
plt.scatter(x , a , marker='o' , s=101 , c='orange')

plt.title("grouped figure")
plt.xlabel("hello")
plt.ylabel("how are you??")

plt.show()

#########################################################################################################################################

data = [9 , 1 , 2 , 4 , 3, 8 , 9 , 4 , 10]

plt.xlabel("data is in the 'x'")

plt.hist(data , edgecolor = 'black')
plt.show()

#########################################################################################################################################

one = [1,2,3,4,5,6,7,8,9]
two = [3,5,6,8,3,1,3,4,5]
three=[1,3,4,5,6,7,3,5,6]

data = list([one , two , three])
plt.boxplot(data)

plt.show()

#########################################################################################################################################

one = [1,2,3,4,5,6,7,8,9]
two = [3,5,6,8,3,1,3,4,5]
three=[1,3,4,5,6,7,3,5,6]

data = list([one,two,three])

plt.violinplot(data , showmedians=True)
plt.show()

#########################################################################################################################################

frute = ['Apple' , 'Orange' , 'Mango']
q = [30 , 35 , 35]

plt.pie(q , labels=frute , autopct='%0.1f%%' , colors=['white' , 'black' , 'red'])
plt.show()

#########################################################################################################################################

frute = ['Apple' , 'Orange' , 'Mango']
q = [30 , 35 , 35]

plt.pie(q , labels=frute , radius=1)
plt.pie([1] , colors=["w"] , radius=2)

plt.show()

######################################################################################################################################
