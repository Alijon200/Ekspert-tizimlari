# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17eNDeoP5YeOLQwuyWW8pgDdsSSPquGmB
"""

def kasallik_tashxisi(alomat):
  if alomat=="bosh og'riq, istma":
    return "Sizda grip bor"
  elif alomat=="qorin og'riq":
    return "Sizda spazma bor"
  elif alomat=="tish og'riq":
    return " Kupen yoki Bolnol dorilarini tafsiya qilamiz"
  elif alomat=="Tomoq o'g'rig'i":
    return "mukaltin"
  elif alomat=="oshqozon og'riq":
    return "omez"
  elif alomat=="Bel og'riq":
    return "menovazin"
  elif alomat=="Qon bosimi oshishi":
    return "dipazol"
  elif alomat=="yurak og'riq":
    return "validol"
  elif alomat=="shamolash":
    return "anaferon"
  elif alomat=="bo'g'im og'riq":
    return "fastum gel"
  else:
    return "Noaniq kasallik, Shifokorga murojat qiling"
alomat=input("Alomatni kiriting ")
natija=kasallik_tashxisi(alomat)
print(natija)

def talabalar(bizning_guruh):
  if bizning_guruh=="Boymirzayev Alijon":
    return "bizning guruhdan"
  elif bizning_guruh=="Aminjonov Nurulloh":
    return "bizning guruhdan"
  elif bizning_guruh=="Yusufjonov Muhsinjon":
    return "bizning guruhdan"
  elif bizning_guruh=="To'xtasinov Boynazar":
    return "bizning guruhdan"
  else:
    return "Bu talaba, Bizning guruhdan emas"
bizning_guruh=input("Guruh talabalarini kiriting:")
natija=talabalar(bizning_guruh)
print(natija)