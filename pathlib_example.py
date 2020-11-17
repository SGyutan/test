from pathlib import Path
import os
import pprint


mypath = Path('.')
print(type(mypath))

pp='./README.md'
base='test'
p_file = Path(pp)

print(p_file)
# 20_03_29_13_15_48.mp4

print(type(p_file))
# <class 'pathlib.PosixPath'>

print(p_file.exists())
#True

print(p_file.resolve())
#D:\github\kerr\20_03_29_13_15_48.mp4

print(p_file.name)
#20_03_29_13_15_48.mp4

print(p_file.stem)
#20_03_29_13_15_48

print(p_file.suffix)
# .mp4

print(p_file.parent)
# .
print(p_file.resolve().parent)
#D:\github\kerr

# p2=p_file.parent/base
# print(str(p2))

# print(p_file.resolve().parent.joinpath('test.txt'))