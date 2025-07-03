
# str = "BIT SINDRI mein sab" 
# # f.write(str)
# data = f.readlines()
# print(data)
# f.close()

# f = open("file.txt")
# line = f.readline()
# while(line != ""):
#     print(line)
#     line = f.read()
# f.close()

# AMAR = 'studying in asus tuf a15'
# f = open('xyzfile.txt', 'a')
# print (f.read())
# f.close()

# with open('file.txt') as f:
#     info = f.read()
# if 'AMAR kumar' in info:
#    print('present')
# else: print('not present')
           
       
                         # --------GAME PROJECT-------------
# import random
# def file():
#     print('GAME IS STARTING: ')
#     score = random.randint(1,100)
#     with open('file.txt') as f:
#         highscore = f.read()
#         if(highscore != ''):
#             highscore = int(highscore)
#         else: highscore =0 

#     print(f'YOUR SCORE: {score}')
#     if(score > highscore):
#         with open ('file.txt', 'w') as f:
#             f.write(str(score))
#     return score
# file()      
 
  
                            # -------TABLE FROM 2-20 ---------------
# def pahada(a):
#     table = ""
#     for i in range (1,11):
#        line = f'{a} * {i}= {a*i}\n'
#        print(line.strip())
#        table += line

#     table += '------next table------\n'

#     with open('file.txt', 'a') as f:
#         f.write(table)

# for i in range(2,21):
#     pahada(i)
              

                           # -------REPLACING WITH @@@@@ -------------
# word = 'fuck'
# with open('file.txt') as f:
#     content = f.read()
# new  = content.replace(word, '@@@@')
# with open('file.txt', 'w') as f:
#    f.write(new)

# words = ['amar','karna','sumit']
# with open('file.txt','r') as f:
#     content = f.read()
# for word in words:
#    content  = content.replace(word, '*'*len(word))
# with open('file.txt','w') as f:
#     f.write(content)


with open('log.txt') as f:
    a = f.read()
if('amar' in a ):
    print('present')
else: print('not present')

with open('py.txt') as f:
    lines = f.readlines()
lineno = 1
for a in lines:
        if('python'in a):
              print(f'python is present in lineno: {lineno}')
              break
        lineno += 1
else: print('python not present')

