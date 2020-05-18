import os

#
# os.chdir('..')
# print(os.getcwd())
#
# print(os.listdir('.'))
#
# roots = next(os.walk('.'))[0]
# print("Roots = %s" %roots)
#
# dirs = next(os.walk('.'))[1]
# print("Dir = %s" %dirs)
#
#
# files = next(os.walk('.'))[2]
# print("Files = %s" %files)

os.chdir('..')
print(os.getcwd())

os.chdir('Week-4')
print(os.getcwd())

print(os.listdir('.'))

# try:
#     os.mkdir('temp')
# except FileExistsError:
#     pass

try:
    os.removedirs('temp')
except FileNotFoundError:
    pass



print(os.listdir('.'))





