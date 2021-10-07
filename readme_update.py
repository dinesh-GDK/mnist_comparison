import re

with open('mnist_comparison.ipynb', 'r') as f:
    read = str(f.read())

time_taken = re.findall(r'(Time taken to train: )(.*?)( minutes)', read)
time_taken = [min[1] for min in time_taken if '60' not in min[1]]
print('Time data:', time_taken)

accuracy = re.findall(r'(accuracy on test set: )(.*?)(%)', read)
accuracy = [acc[1] for acc in accuracy if '100' not in acc[1]]
print('Accuracy data:', accuracy)

with open('README.md', 'r') as f:
    read = f.read()

pickup = re.findall(r'(model)(.*\|)', read)
pickup = [re.findall('\d+.\d+', pic[1]) for pic in pickup]
print('Replace data: ', pickup)

for i in range(len(pickup)):
    read = read.replace(pickup[i][0], accuracy[i])
    read = read.replace(pickup[i][1], time_taken[i])

with open('README.md', 'w') as f:
    f.write(read)
