import csv

def find_s_algorithm(filename):
  with open(filename, 'r') as file:
    csvreader = csv.reader(file)
    headers = next(csvreader)

    hypothesis = None
    for row in csvreader:
      # Assuming 'Play' (Yes/No) is the second to last column, 
      # and the very last column is an unexpected 'Sunny' as seen in the df output.
      attributes = row[:-2] # All columns except the last two
      target = row[-2].lower() # The second to last column, converted to lowercase

      if target == "yes":
        if hypothesis is None:
          hypothesis = attributes.copy()
        else:
          for i in range(len(hypothesis)):
            if hypothesis[i] != attributes[i]:
              hypothesis[i] = "?"

  return hypothesis

final_hypothesis = find_s_algorithm("Trainingdata.csv")
print("Final Hypothesis:", final_hypothesis)