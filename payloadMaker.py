with open('books/cailanBook.txt', 'r') as file:
    file_contents = file.read()
    print('Total words:   ', len(file_contents.split('.')))
    print('total stops:    ', file_contents.count('.'))

file = open('books/cailanBook.txt', 'r')
file = file.read().replace('\n', '')
sentences = file.split('.')

count = 0
fileCount = 0
for lines in sentences:
    if count == 0:
        writeFile = open('payload/cailan/payload{}.txt'.format(fileCount), 'w')
    lines += '.'
    count += 1
    if count == 7:
        fileCount += 1
        count = 0
    print(lines, file=writeFile)

with open("books/testingBook.txt", "r") as fileTest:
    lines = fileTest.readlines()
with open("books/newFormat.txt", "w") as fileFormat:
    for line in lines:
        if line.find("Albert Camus") == -1:
                fileFormat.write(line)

fileTest.close()
fileFormat.close()

with open("books/newFormat.txt","r",encoding='utf-8') as finishing:
    lines2 = finishing.readlines()

payloadCount = 0
lineCounter = 0

for line2 in lines2:

    if lineCounter == 0:
        payload = open("payload/test/payload{}.txt".format(payloadCount),"w",encoding='utf8')

    if line2 == "" or line2 == "\n":
        continue
    if len(line2) == 2 or len(line2) == 3:
        continue
    elif len(line2) > 80 and len(line2[80:len(line2)]) > 50:
        payload.write("{}-\n".format(line2[0:80]))
        payload.write("-{}".format(line2[81:len(line2)]))
        #print("{}-".format(line2[0:80]))
        #print("-{}".format(line2[81:len(line2)]))
        lineCounter += 2
    else:
        payload.write(line2)
        lineCounter += 1
    if lineCounter > 6:
        payloadCount +=1
        lineCounter = 0
        payload.close()
payload.close()
