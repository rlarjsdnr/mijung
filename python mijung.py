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

#주기율표 1~127
atoms=(
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

#반응물과 생성물 입력
print("="*40)
"""
reactants: 반응물 리스트
products:  생성물 리스트
"""
reactants=split(r"[\W']+",input("반응물을 입력하세요: "))
products=split(r"[\W']+",input("생성물을 입력하세요: "))
print("="*40)

#reacntans, 오류로 들어갈만한 공백, '' 삭제
for x in range(len(reactants)):
    if reactants[x]==' ' or reactants[x]=='':
        del reactants[x]
#product 공백 오류 제거 
for x in range(len(products)):
    if products[x]==' ' or products[x]=='':
        del products[x]

#==============================================================================================
#원소 리스트 ex.
#[['O', 'H2'], ['O2', 'C']]
#[['H4', 'C'], ['H4', 'C']]

reactants_list=[list() for x in range(len(reactants))]
products_list=[list() for x in range(len(products))]

#원자 추출
#reactants
for x in range(len(reactants)): #reactants의 원소 길이
    str_direction=len(reactants[x]) #reactants의 원소의 문자열 길이
    for i in range(len(reactants[x])-1,-1,-1): #문자열 맨 끝부터 0까지 -1씩 줄이면서 반복
        if reactants[x][i].isupper(): #만약 대문자라면 
            reactants_list[x].append(reactants[x][i:str_direction])
            str_direction=i
#products
for x in range(len(products)): #products의 원소 길이
    str_direction=len(products[x]) #products의 원소의 문자열 길이
    for i in range(len(products[x])-1,-1,-1): #문자열 맨 끝부터 0까지 -1씩 줄이면서 반복
        if products[x][i].isupper(): #만약 대문자라면 
            products_list[x].append(products[x][i:str_direction])
            str_direction=i
#==============================================================================================
#딕셔너리형으로 변환 
reactants_dict=[dict() for x in range(len(reactants))] #생성물 원소 공간 
products_dict=[dict() for x in range(len(products))] #반응물 원소 공간

for x in range(len(reactants_list)):
    for j in range(len(reactants_list[x])):
        var=reactants_list[x][j] # O, H2, O2, C
        try:
            if var[-1].isalpha(): #맨 뒷 글자가 문자라면
                reactants_dict[x][var]=1 if reactants_dict[x].get(var)==None else  reactants_dict[x][var]+1
            else: #만약 아니라면
                for k in range(len(var)):
                    if var[k].isdigit():
                        reactants_dict[x][var[:k]]=int(var[k:]) if reactants_dict[x].get(var[:k])==None else reactants_dict[x][var[:k]]+int(var[k:])
                        break
        except KeyError:
            print("문제 발생: 입력 부분을 확인하고 다시 하시길 바랍니다.")
            pass
    
#products
for x in range(len(products_list)):
    for j in products_list[x]:
        try:
            if j[-1].isdigit():
                products_dict[x][j[:-1]]=int(j[-1]) if products_dict[x].get(j[:-1])==None else products_dict[x][j[:-1]]+int(x[-1])
            else:
                products_dict[x][j]=1 if products_dict[x].get(j)==None else  products_dict[x][j]+1
        except KeyError:
            print("문제 발생: 입력 부분을 확인하고 다시 하시길 바랍니다.")
            pass


print(reactants_dict)
print(products_dict)
#==============================================================================================
#실제로 존재하는 원소인지 


