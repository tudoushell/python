#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


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




