# printing even numbers from 0 to 100
even_num=[i for i in range(0,100) if i%2==0]
print("even_numbers from 0 to 100:\n",even_num,"\n")
# Printing even number square from 0 to 100
even_squ=[i*i for i in even_num]
print("\neven_numbers squares from 0 to 100:\n",even_squ)