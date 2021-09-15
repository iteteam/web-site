illustrations = ['illustration-1.svg', 'illustration-2.svg', 'illustration-3.svg', 'illustration-4.svg',
                 'illustration-5.svg', 'illustration-6.svg', 'illustration-7.svg', 'illustration-8.svg',
                 'illustration-9.svg', 'illustration-10.svg', 'illustration-11.svg', 'illustration-12.svg',
                 'illustration-13.svg', 'illustration-14.svg', 'illustration-15.svg'
                 ]
# width="1350px" height="1140px"
for i in illustrations:
    file = open(i).read()
    content = file[:file.find('width')] + 'width="1350px" height="1140px" ' + file[file.find('viewBox'):]
    new_file = open('result/' + str(i), 'w')
    new_file.write(content)
    new_file.close()
