import tempfile as tmp

temp = tmp.TemporaryFile()

print("Temp:", temp)
print('Temp.name:', temp.name)
temp.close()
