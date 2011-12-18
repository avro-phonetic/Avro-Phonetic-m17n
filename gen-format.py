#!/usr/bin/python
# coding: utf-8
"""
Helper script to generate formats
Written By - Md. Enzam Hossain, PROGmaatic Developer Network (http://progmaatic.com)

Copyright (C) 2011 Md. Enzam Hossain <enzam@progmaatic.com>
DO WHATEVER YOU WANT TO PUBLIC LICENSE
(merely same as http://sam.zoy.org/wtfpl/)
TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
0. You just DO WHATEVER YOU WANT TO.
"""

phonetic = ["k", "kh", "g", "gh", "Ng", "c", "ch", "j", "jh", "NG", "T", "Th", "D", "Dh", "N", "t", "th", "d", "dh", "n", "p", "ph", "f", "b", "bh", "v" , "m", "z", "r", "l", "sh", "S", "Sh", "s", "h", "R", "Rh", "y", "Y", "t``", "ng", ":", "^", ",,", ".", "$", ":`", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
bangla   = ["ক" , "খ"  , "গ" , "ঘ"  , "ঙ"  , "চ"  , "ছ"  , "জ" , "ঝ"  , "ঞ" , "ট"  , "ঠ"  , "ড" , "ঢ"  , "ণ"  , "ত" , "থ"  , "দ"  , "ধ"  , "ন" , "প" , "ফ"  , "ফ" , "ব" , "ভ"  , "ভ"  , "ম"  , "য" , "র"  , "ল" , "শ"  , "শ" , "ষ"  , "স"  , "হ" , "ড়" , "ঢ়"  , "য়" , "য়"  , "ৎ"   , "ং" , "ঃ", "ঁ" , "্" , "।" , "৳" , ":" , "০" , "১" , "২" , "৩"  , "৪" , "৫" , "৬" , "৭" , "৮" , "৯"]
for i in range(len(phonetic)):
	print '("'+phonetic[i]+'" "'+bangla[i]+'")'


#vowels below
vowel_phonetic = ["o", "a", "i", "I", "ee", "u", "oo", "U", "rri", "e", "OI", "O", "OU"]
vowel_bangla_full = ["অ", "আ", "ই", "ঈ", "ঈ", "উ", "উ", "ঊ", "ঋ", "এ", "ঐ", "ও", "ঔ"]
vowel_bangla_kar = ["", "া", "ি", "ী", "ী", "ু", "ু", "ূ", "ৃ", "ে", "ৈ", "ো", "ৌ"]

for i in range(len(vowel_phonetic)):
	print '("'+vowel_phonetic[i]+'" "'+vowel_bangla_kar[i]+'")'
