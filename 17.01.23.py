def perevod(v, os):
    if v > 1:
        perevod(v//os,os)
    print(v%os)
perevod(12,2)
       