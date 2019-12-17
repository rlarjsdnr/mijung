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

물질의 상태

고체(s)
액체(l)
기체(g)
수용액(aq)

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
reactants=split("\W+",input("반응물을 입력하세요: "))
products=split("\W+",input("생성물을 입력하세요: "))
print("="*40)

#실제로 존재하는 원소인지 판별
for x in range(len(reactants)):
    for i in range(len(reactants[x]))
        if reactants[x][i].isdigit() or reactants[x][i].islower():
            reactants
"""
for x in reactants:
    if x in atom:
        print("원소 있음")
    else:
        print("프로그램 종료")
        exit(1)

for x in products:
    if x in atom:
        print("원소 있음")
    else:
        print("프로그램 종료")
        exit(1)
"""
