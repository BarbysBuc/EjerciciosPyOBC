import pandas as pd

read_file = pd.read_excel(r'C:\Users\Barbys\Desktop\OpenBootCamp\Python\Ejercicios\20220604.xlsx')
read_file.to_csv(r'C:\Users\Barbys\Desktop\OpenBootCamp\Python\Ejercicios\nuevo.csv', index = None, header = True)

