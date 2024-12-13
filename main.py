# 12.12.2024    4 OY 7 Dars
# Mavzu: Iterators & iterables, Generators
# iterables -> litst , str, range, dict, set, taple


#-------------------------------------------------------------

# user = ["Asilbek", "Bakir", "Ali"]
# inter_user = iter(user)
# print(next(inter_user))
# print(next(inter_user))
# print(next(inter_user))
#
# for i in user:
#     print(i)

#-------------------------------------------------------------

# from typing import Iterable
#
# users = ["Toxir", "Sobir", "Bakir", "Jalil"]
#
# class CustomIterator:
#     def __init__(self, users: Iterable):
#         self.__users = users
#         self.__index = -1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.__index += 1
#         if self.__index >= len(self.__users):
#             raise StopIteration("Boshqa element qolmadi !!!!")
#         return self.__users[self.__index]
# a = CustomIterator(users)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


#-------------------------------------------------------------

# def costum_generator():
#     yield "salom"
# print(list(costum_generator()))
#
# for user in costum_generator():
#     print(user)


#-------------------------------------------------------------

# def generate_number():
#     for i in range(10000000):
#         yield i
# print(generate_number().__sizeof__())
#
# nums = [i for i in range(10000000)]
# print(nums.__sizeof__())


#-------------------------------------------------------------

#===============================================UYGA VAZIFA==================================================

# 4 OY 7 Dars UYGA VAZIFASI

# 1 vazifa

# class SimpleIterator:
#     def __init__(self):
#         self.current = 1
#         self.limit = 10
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current <= self.limit:
#             value = self.current
#             self.current += 1
#             return value
#         else:
#             raise StopIteration
# iterator = SimpleIterator()
# for number in iterator:
#     print(number)


#--------------------------------------------------------------------------------------------------

# 2 vazifa

# from typing import Iterable
#
# users = ["Asilbek", "Rustamov", "Azizbek ", "O'gli"]
#
# class CustomIterator:
#     def __init__(self, users: Iterable):
#         self.__users = users
#         self.__index = -1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.__index += 1
#         if self.__index >= len(self.__users):
#             raise StopIteration("Boshqa element qolmadi !!!!")
#         return self.__users[self.__index]
# a = CustomIterator(users)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


#--------------------------------------------------------------------------------------------------

# 3 vazifa

# from typing import Iterable
#
# users = ["Asilbek", "Rustamov", "Azizbek ", "O'gli"]
#
# class CustomIterator:
#     def __init__(self, users: Iterable):
#         self.__users = users
#         self.__index = 4
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.__index -= 1
#         if self.__index >= len(self.__users):
#             raise StopIteration("Boshqa element qolmadi !!!!")
#         return self.__users[self.__index]
# a = CustomIterator(users)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


#--------------------------------------------------------------------------------------------------

# 4 vazifa

# from typing import Iterable
#
# users = "PYTHON"
#
# class CustomIterator:
#     def __init__(self, users: Iterable):
#         self.__users = users
#         self.__index = -1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.__index += 1
#         if self.__index >= len(self.__users):
#             raise StopIteration("Boshqa element qolmadi !!!!")
#         return self.__users[self.__index]
# a = CustomIterator(users)
# for i in range(6):
#     print(next(a))


#--------------------------------------------------------------------------------------------------

# 5 vazifa

# class SimpleIterator:
#     def __init__(self, num):
#         self.current = 0
#         self.limit = num
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current <= self.limit:
#             value = self.current
#             self.current += 2
#             return value
#         else:
#             raise StopIteration
# num = int(input("Raqam kiriting: "))
# iterator = SimpleIterator(num)
# for number in iterator:
#     print(number)


#--------------------------------------------------------------------------------------------------

# 6 vazifa

# class SimpleIterator:
#     def __init__(self, num):
#         self.current = 1
#         self.limit = num
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current <= self.limit:
#             value = self.current
#             self.current += 1
#             return value
#         else:
#             raise StopIteration
# num = int(input("Raqam kiriting: "))
# iterator = SimpleIterator(num)
# total_sum = sum(iterator)
# print(f"Elementlarning yig'indisi: {total_sum}")


#--------------------------------------------------------------------------------------------------

# 7 vazifa

# def find_in_list(target, items):
#     """
#         Bu funksiya foydalanuvchidan ism qabul qiladi agar u ism bo'lsa ha bu ism bor ask holda bu ismdi royxatga qo'shib bu ism yoq dib chiqaradi!
#         doimiy ishlashdi tohtatish uchun stop sozini sizdan ism soraganda yozishingiz kerak!
#     """
#     if target in items:
#         return True
#     return False
# names = ["Ali", "Vali", "Olim", "Zarina", "Malika", "Asilbek"]
# while True:
#     search_target = input("Qanday ismni qidiraylik(Toxtatish -> stop): ")
#     if search_target == "stop":
#         break
#     elif find_in_list(search_target, names):
#         print(f"Ha, {search_target} ro'yxatda bor.")
#     else:
#         print(f"Kechirasiz, {search_target} ro'yxatda yo'q.")
#         names.append(search_target)


#--------------------------------------------------------------------------------------------------

#================================Generatorlarga oid====================================

# 1 vazifa

# def custom_range(start, stop, step=1):
#     """
#     range oringa qollansa boladiga funksiya !
#     bunda ham range oxshab statr va stop qiymatlarini kiritish kerak va hohlasa qancha qadamdan yurishini ham aytishi mumkin
#     """
#     current = start
#     while current < stop:
#         yield current
#         current += step
#
# for num in custom_range(1, 10, 1):
#     print(num)


#--------------------------------------------------------------------------------------------------

# 2 vazifa
#
# def custom_range(start, stop, step=1):
#     current = start
#     while current < stop:
#         yield current
#         current += step
# def word_lengths(text):
#     for word in text.split():
#         yield len(word)
# sample_text = input("Matn kiriting: ")
# for length in word_lengths(sample_text):
#     print(length)

#--------------------------------------------------------------------------------------------------

# 3 vazifa

# def custom_range(start, stop, step=2):
#
#     current = start
#     while current < stop:
#         yield current
#         current += step
#
# for num in custom_range(1, 10, 2):
#     print(num)


#--------------------------------------------------------------------------------------------------

# 4 vazifa

# def custom_range(start, stop, step=1):
#
#     current = start
#     while current < stop:
#         yield current
#         current += step
#
# for num in custom_range(0, 10, 2):
#     print(num)


#--------------------------------------------------------------------------------------------------

# 5 vazifa

# def infinite_sequence():
#     current = 1
#     while True:
#         yield current
#         current += 1
# print("Cheksiz ketma-ketlik:")
# for i, num in enumerate(infinite_sequence()):
#     if i >= 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
#         break
#     print(num)


#--------------------------------------------------------------------------------------------------

# 6 vazifa

# def infinite_sequence():
#     current = 1
#     while True:
#         yield current
#         current += 1
# print("Cheksiz ketma-ketlik:")
# for i, num in enumerate(infinite_sequence()):
#     if i >= 10:
#         break
#     print(num, ":", num ** 2)


#--------------------------------------------------------------------------------------------------

# 7 vazifa

# def yigindi_generator(sonlar):
#     summa = 0
#     for son in sonlar:
#         summa += son
#         yield summa
# sonlar = [1, 2, 3, 4, 5]
# yigindi = yigindi_generator(sonlar)
# for summa in yigindi:
#     print(f"RO'yxatdagi sonlar yegindisi {summa} ga yetdi")


#--------------------------------------------------------------------------------------------------

# 8 vazifa

# def ijobiy_sonlar_generator(ketma_ketlik):
#     for son in ketma_ketlik:
#         if son > 0:
#             yield son
# sonlar = [1, -2, 3, 0, -4, 5, -6]
# generator = ijobiy_sonlar_generator(sonlar)
# musbat_sonlar = []
# for son in generator:
#     musbat_sonlar.append(son)
# print("Musbat sonlar royxati: ", musbat_sonlar)


#--------------------------------------------------------------------------------------------------

# 9 vazifa

# import random
#
# def tasodifiy_sonlar_generator(chegaralar, soni=None):
#     """
#     Tasodifiy sonlar generatori.
#      (min, max) ko'rinishidagi chegaralar.
#      Qaytariladigan tasodifiy sonlar soni (None bo'lsa, cheksiz generator).
#     """
#     min_chegara, max_chegara = chegaralar
#     hisoblagich = 0
#     while soni is None or hisoblagich < soni:
#         yield random.randint(min_chegara, max_chegara)
#         hisoblagich += 1
# generator = tasodifiy_sonlar_generator((1, 10000000), 1)
# for son in generator:
#     print(son)


#--------------------------------------------------------------------------------------------------

# 10 vazifa

# def prime_generator(n):
#     """Birinchi N ta tub sonni hosil qiladigan generator."""
#     count = 0
#     num = 2
#     while count < n:
#         if is_prime(num):
#             yield num
#             count += 1
#         num += 1
# def is_prime(num):
#     """Berilgan son tub ekanligini tekshirish."""
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# n = int(input("Birinchi nechta tub sonni ko'rishni xohlaysiz: "))
# print(f"Birinchi {n} ta tub son:")
# for prime in prime_generator(n):
#     print(prime, end=" ")



#--------------------------------------------------------------------------------------------------

# 11 vazifa

# def reverse_string_generator(s):
#     for char in reversed(s):
#         yield char
# original_string = input("Matnni kiriting: ")
# reversed_string = ''.join(reverse_string_generator(original_string))
#
# print(f"Teskari matn: {reversed_string}")


#--------------------------------------------------------------------------------------------------

# 12 vazifa

# def product_generator(n):
#     """1 dan N gacha bo‘lgan sonlarning ketma-ket ko‘paytmasini hosil qiluvchi generator."""
#     product = 1
#     for i in range(1, n + 1):
#         product *= i
#         yield product
# n = int(input("Qaysi N gacha bo‘lgan sonlarning ko‘paytmasini hosil qilishni xohlaysiz: "))
# print(f"1 dan {n} gacha bo‘lgan sonlarning ketma-ket ko‘paytmasi:")
# for result in product_generator(n):
#     print(result, end=" ")

# Bajaruvchi : Rustamov Asilbek
#--------------------------------------------------------------------------------------------------
