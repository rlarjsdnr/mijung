"""
propane(프로판, 프로페인):C3H8
프로판을 연소 시킬 경우

반응물 : C3H8 , O2
생성물 : H2O , CO2 

C3H8 + O2 -> H2O + CO2

계수를 맞춰야곘는데 계수를 맞추기가 어려우므로
a,b,c,d를 불러옵니다.

여기서 반응물과 생성물의 탄소, 수소, 산소의 
원자 수가 같아지도록 관계식을 세워봅시다.

탄소: 3a=d
수소: 8a=2c
산소: 2b=c+2d

a를 1로 가정하고 풀어보면, d는 3이 되고, c는 4가 됩니다.
그리고, b=5가 됩니다.

이제 이 수를 화학반응식에 넣어봅시다.
C3H8+5O2 -> 4H2O + 3CO2
"""

from re import split #정규식 split 함수 

atom=\
(
    'H','He',  
    'Li','Be','B','C','N','O','F','Ne',
    'Na','Mg','Al','Si','P','S','Cl','Ar',
    'K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr',
    'Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe',
    'Cs','Ba',
    #란타넘족
    'La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu',
    'Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn',
    'Fr','Ra',
    #악티늄족
    'Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr',
    'Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og',
    'Uue','Ubn','Ubu','Ubb','Ubt','Ubq','Ubp','Ubh','Ubs'
)

print("="*40)
"""
reactants: 반응물 리스트
products:  생성물 리스트
"""
reactants=split(r"[\W']+",input("반응물을 입력하세요: "))
products=split(r"[\W']+",input("생성물을 입력하세요: "))
print("="*40)

#오류로 들어갈만한 공백, '' 삭제
for x in range(len(reactants)):
    if reactants[x]==' ' or reactants[x]=='':
        del reactants[x]

for x in range(len(products)):
    if products[x]==' ' or products[x]=='':
        del products[x]

#원소 리스트 
reactants_dict=list()
products_dict=list()

for x in range(len(reactants)):
    reactants_dict.append(dict())
for x in range(len(products)):
    products_dict.append(dict())

#원자 추출
for x in range(len(reactants)):
    for i in range(len(reactants[x])):
        #만약 숫자라면
        if reactants[x][i].isdigit():
            reactants_dict[x][reactants[x][i-1]]=int(reactants[x][i])
            try:
                if reactants[x][i+1].isupper():
                    continue
            except IndexError:
                continue        
        #만약 소문자라면  
        if reactants[x][i].lower():
            reactants_dict[x][reactants[x][i]]=1

for x in range(len(products)):
    for i in range(len(products[x])):
     #만약 숫자라면
        if products[x][i].isdigit():
            products_dict[x][products[x][i-1]]=int(products[x][i])
            try:
                if products[x][i+1].isupper():
                    continue
            except IndexError:
                continue        
        #만약 소문자라면  
        if products[x][i].lower():
            products_dict[x][products[x][i]]=1

print(reactants)
print(products)
print(reactants_dict)
print(products_dict)


