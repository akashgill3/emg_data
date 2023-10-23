import csv
import math

# Function to calculate the Root Mean Square (RMS) of a list of numbers
def rms(row):
    n = len(row)
    if n > 0:
        ms = sum(float(num) ** 2 for num in row) / n
        return math.sqrt(ms)

# Function to convert CSV data into a list of lists, excluding the first column
def csv_to_list(fileName):
    with open(fileName, newline='') as csvFile:
        reader = csv.reader(csvFile, delimiter=';')
        r = [row[1:] for row in reader]
    return r

# Function to write a list of values to a CSV file
def write_to_csv(listName, fileName='answer.csv'):
    with open(fileName, 'w', newline='') as ans:
        writer = csv.writer(ans)
        writer.writerows([[ans] for ans in listName])

# Main function to orchestrate the execution flow of the program
def main(fileName):
    list_of_data = csv_to_list(fileName)
    answer = [rms(row) for row in list_of_data]
    write_to_csv(answer)

# Execute the main function with the desired CSV file name
main('post101.csv')
