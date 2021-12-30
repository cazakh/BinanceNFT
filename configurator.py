print("Welcome to bot configurator \nDeveloped by Fedor Cazakh Sokolov with love")

print("\nСколько боксов купить?")
amount = str(int(input()))

print("Теперь вставь сюда ID аукциона")
productId = str(int(input()))
print("Теперь вставь ID самого дешевого аукциона, который не закончится до начала дропа")
product_Id = str(int(input()))

print("Теперь укажи время аукциона в системе Unix (можно через сайт)")
saleTime = str(int(input()))

print("Теперь укажи количество запросов. Больше - лучше, но я рекомендую 1000")
requestsNumber = str(int(input()))

print("Сейчас я сгенерирую файл, в котором будет вся информация.")
f= open("conf.cazakhBot","w+")
print("Файл conf.cazakhBot создан")
f.write(amount)
f.write(" ")
f.write(productId)
f.write(" ")
f.write(product_Id)
f.write(" ")
f.write(saleTime)
f.write(" ")
f.write(requestsNumber)
f.close()
print("Файл успешно сгенерирован, перекиньте его в папку где лежит бот и запустите бота!")

