#!/usr/bin/env python
# -*- coding: utf-8 -*-
english_dictionary={ 
	'position':"位置",
	'chaos':"混乱",
	'vain':"没有真正意义的",
	'boligation':"义务",
	'orbit':"轨道",
	'bend':"弯曲",
	'swallow':"吞下"
	}
dic=input("please type you want search word: ")
if dic not in english_dictionary:
	print("this word is not in dictionary,this word is add now")
	dictionary_mean=input("plesase type this word mean: ")
	english_dictionary[dic]=dictionary_mean
	tip=input("is  look up  dictionary ? yes or no ")
	if tip=="yes":
		for i,j in english_dictionary.items():
			print(i+":  "+j)
	else:
		print("Thank you")
else:
	print("this word mean is ")
	print(english_dictionary[dic])
