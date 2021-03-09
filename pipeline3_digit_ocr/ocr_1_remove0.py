

file = open('training/matrix/data.txt', 'r')
data_rows = file.readlines()
file.close()


file = open('training/window/data.txt', 'r')
window_rows = file.readlines()
file.close()

valid_rows = []
valid_labels = []
counter = 0
for row in window_rows :
    if int(row) != 0 :
        row = row.replace('\n', '')
        valid_rows.append(data_rows[counter].replace('\n', ''))
        valid_labels.append(row)

    counter = counter + 1


# print(len(valid_rows))
file = open('training/matrix/data_processed.txt', 'w')
file.write('\n'.join(valid_rows))
file.close()

file = open('training/window/data_processed.txt', 'w')
file.write('\n'.join(valid_labels))
file.close()
# print(len(valid_labels))
