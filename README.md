# 🏦 ACME Bank Mortgage Calculator  
A Python-based mortgage calculation system that computes monthly payments and generates a full amortization schedule following ACME Bank Ltd. guidelines.

## 📌 Project Overview  
The **ACME Bank Mortgage Calculator** is a two-part Python program that:

1. **Part 1:**  
   - Collects user information  
   - Calculates minimum down payment  
   - Determines mortgage insurance  
   - Computes mortgage principal  
   - Applies interest rate  
   - Outputs monthly mortgage payment  

2. **Part 2:**  
   - Imports Part 1  
   - Generates full amortization schedule  
   - Lists principal/interest/closing balance monthly  

## 📁 Project Structure
```
mortgage_calculator_part1.py
mortgage_calculator_part2.py
```

## 🛠 Features
- Input validation  
- Mortgage formulas  
- Insurance calculation  
- Effective monthly rate  
- Amortization table  

## 💻 Running the Program
```
python mortgage_calculator_part1.py
python mortgage_calculator_part2.py
```

## 🤝 Author
- Ebube Vincent Okutalukwe  


## 📜 License  
SAIT License

📌 SAMPLE  RUN (Program Output)

SAMPLE RUN #1

Enter client name: Anita Howes 
Enter address of property: 19 Condo Circle
Enter Purchase Price: 315000
Enter down payment percentage (minimum5.000): 10
Down payment amount is $31,500
Mortgage insurance price is $8,788
Total mortgage amount is $292,288
Enter Mortgage term(1 , 2, 3, 4, 5, 10): 1
Enter mortgage ammortization period (5, 10, 15, 20, 25): 20
Please enter a vaild choice
Intrest rate for the term bill will be 5.95%
Monthly payment amount is: $2,073
Would you like to see the amortization schedule? (Y/N): y
                      Monthly Amortization Shedule

Month     Opening Bal     Payment   Principal    Interest    Closing Bal
    1       292288.50     2073.45      641.83     1431.62      291646.67
    2       291646.67     2073.45      644.98     1428.48      291001.69
    3       291001.69     2073.45      648.14     1425.32      290353.56
    4       290353.56     2073.45      651.31     1422.14      289702.25
    5       289702.25     2073.45      654.50     1418.95      289047.75
    6       289047.75     2073.45      657.71     1415.75      288390.04
    7       288390.04     2073.45      660.93     1412.52      287729.11
    8       287729.11     2073.45      664.16     1409.29      287064.95
    9       287064.95     2073.45      667.42     1406.03      286397.53
   10       286397.53     2073.45      670.69     1402.77      285726.84
   11       285726.84     2073.45      673.97     1399.48      285052.87
   12       285052.87     2073.45      677.27     1396.18      284375.60
========================================================================
Total                                 7912.90    16968.52


SAMPLE RUN #2

Enter client name: Min Downey 
Enter address of property: 1904 Duplex Drive 
Enter Purchase Price: 500500
Enter down payment percentage (minimum5.005): 5
Please enter a value bewtween the minimum and 100
Enter down payment percentage (minimum5.005): 101.5
Please enter a value bewtween the minimum and 100
Enter down payment percentage (minimum5.005): 5.005
Down payment amount is $25,050
Mortgage insurance price is $19,018
Total mortgage amount is $494,468
Enter Mortgage term(1 , 2, 3, 4, 5, 10): 10
Enter mortgage ammortization period (5, 10, 15, 20, 25): 25
Please enter a vaild choice
Intrest rate for the term bill will be 6.00%
Monthly payment amount is: $3,164
Would you like to see the amortization schedule? (Y/N): n

SAMPLE RUN #3

Enter client name: Peyton Quick
Enter address of property: 65 Bungalow Blvd
Enter Purchase Price: 670000
Enter down payment percentage (minimum6.269): 30
Down payment amount is $201,000
Mortgage insurance price is $0
Total mortgage amount is $469,000
Enter Mortgage term(1 , 2, 3, 4, 5, 10): 5
Enter mortgage ammortization period (5, 10, 15, 20, 25): 5
Please enter a vaild choice
Intrest rate for the term bill will be 5.29%
Monthly payment amount is: $8,901
Would you like to see the amortization schedule? (Y/N): Y
                      Monthly Amortization Shedule

Month     Opening Bal     Payment   Principal    Interest    Closing Bal
    1       469000.00     8900.68     6855.60     2045.08      462144.40
    2       462144.40     8900.68     6885.49     2015.19      455258.92
    3       455258.92     8900.68     6915.51     1985.17      448343.40
    4       448343.40     8900.68     6945.67     1955.01      441397.73
    5       441397.73     8900.68     6975.96     1924.72      434421.78
    6       434421.78     8900.68     7006.37     1894.31      427415.40
    7       427415.40     8900.68     7036.93     1863.75      420378.48
    8       420378.48     8900.68     7067.61     1833.07      413310.87
    9       413310.87     8900.68     7098.43     1802.25      406212.44
   10       406212.44     8900.68     7129.38     1771.30      399083.06
   11       399083.06     8900.68     7160.47     1740.21      391922.59
   12       391922.59     8900.68     7191.69     1708.99      384730.89
   13       384730.89     8900.68     7223.05     1677.63      377507.84
   14       377507.84     8900.68     7254.55     1646.13      370253.29
   15       370253.29     8900.68     7286.18     1614.50      362967.11
   16       362967.11     8900.68     7317.95     1582.73      355649.16
   17       355649.16     8900.68     7349.86     1550.82      348299.29
   18       348299.29     8900.68     7381.91     1518.77      340917.38
   19       340917.38     8900.68     7414.10     1486.58      333503.28
   20       333503.28     8900.68     7446.43     1454.25      326056.84
   21       326056.84     8900.68     7478.90     1421.78      318577.94
   22       318577.94     8900.68     7511.51     1389.17      311066.43
   23       311066.43     8900.68     7544.27     1356.41      303522.16
   24       303522.16     8900.68     7577.16     1323.51      295945.00
   25       295945.00     8900.68     7610.21     1290.47      288334.79
   26       288334.79     8900.68     7643.39     1257.29      280691.40
   27       280691.40     8900.68     7676.72     1223.96      273014.68
   28       273014.68     8900.68     7710.19     1190.49      265304.49
   29       265304.49     8900.68     7743.81     1156.87      257560.67
   30       257560.67     8900.68     7777.58     1123.10      249783.09
   31       249783.09     8900.68     7811.50     1089.18      241971.60
   32       241971.60     8900.68     7845.56     1055.12      234126.04
   33       234126.04     8900.68     7879.77     1020.91      226246.27
   34       226246.27     8900.68     7914.13      986.55      218332.14
   35       218332.14     8900.68     7948.64      952.04      210383.51
   36       210383.51     8900.68     7983.30      917.38      202400.21
   37       202400.21     8900.68     8018.11      882.57      194382.10
   38       194382.10     8900.68     8053.07      847.61      186329.03
   39       186329.03     8900.68     8088.19      812.49      178240.84
   40       178240.84     8900.68     8123.46      777.22      170117.38
   41       170117.38     8900.68     8158.88      741.80      161958.50
   42       161958.50     8900.68     8194.46      706.22      153764.05
   43       153764.05     8900.68     8230.19      670.49      145533.86
   44       145533.86     8900.68     8266.08      634.60      137267.78
   45       137267.78     8900.68     8302.12      598.56      128965.66
   46       128965.66     8900.68     8338.32      562.36      120627.34
   47       120627.34     8900.68     8374.68      526.00      112252.66
   48       112252.66     8900.68     8411.20      489.48      103841.46
   49       103841.46     8900.68     8447.88      452.80       95393.58
   50        95393.58     8900.68     8484.71      415.97       86908.87
   51        86908.87     8900.68     8521.71      378.97       78387.16
   52        78387.16     8900.68     8558.87      341.81       69828.29
   53        69828.29     8900.68     8596.19      304.49       61232.09
   54        61232.09     8900.68     8633.68      267.00       52598.42
   55        52598.42     8900.68     8671.32      229.36       43927.10
   56        43927.10     8900.68     8709.13      191.55       35217.96
   57        35217.96     8900.68     8747.11      153.57       26470.85
   58        26470.85     8900.68     8785.25      115.43       17685.60
   59        17685.60     8900.68     8823.56       77.12        8862.04
   60         8862.04     8900.68     8862.04       38.64          -0.00
========================================================================
Total                               469000.00    65040.77

SAMPLE RUN #4

Enter client name: Plenty Childs
Enter address of property: 200 Park View
Enter Purchase Price: 999999
Enter down payment percentage (minimum 7.500): 10
Down payment amount is $100,000
Mortgage insurance price is $27,900
Total mortgage amount is $927,899
Enter Mortgage term(1 , 2, 3, 4, 5, 10): 3
Enter mortgage ammortization period (5, 10, 15, 20, 25): 17
Please enter a vaild choice
Enter mortgage ammortization period (5, 10, 15, 20, 25): 15
Intrest rate for the term bill will be 5.60%
Monthly payment amount is: $7,599
Would you like to see the amortization schedule? (Y/N): N

SAMPLE RUN #5

Enter client name: H. I. Falutin 
Enter address of property: 8 Swanky Lane 
Enter Purchase Price: 1420000
Enter down payment percentage (minimum 20.000): 20
Down payment amount is $284,000
Mortgage insurance price is $0
Total mortgage amount is $1,136,000
Enter Mortgage term(1, 2, 3, 5, 10): 22
Please enter a valid choice
Enter Mortgage term(1, 2, 3, 5, 10): 2
Enter mortgage ammortization period (5, 10, 15, 20, 25): 10
Intrest rate for the term bill will be 5.90%
Monthly payment amount is: $12,514
Would you like to see the amortization schedule? (Y/N): Y
                      Monthly Amortization Shedule

Month     Opening Bal     Payment   Principal    Interest    Closing Bal
    1      1136000.00    12514.46     6996.57     5517.89     1129003.43
    2      1129003.43    12514.46     7030.55     5483.91     1121972.88
    3      1121972.88    12514.46     7064.70     5449.76     1114908.17
    4      1114908.17    12514.46     7099.02     5415.44     1107809.15
    5      1107809.15    12514.46     7133.50     5380.96     1100675.65
    6      1100675.65    12514.46     7168.15     5346.31     1093507.50
    7      1093507.50    12514.46     7202.97     5311.49     1086304.53
    8      1086304.53    12514.46     7237.96     5276.51     1079066.57
    9      1079066.57    12514.46     7273.11     5241.35     1071793.46
   10      1071793.46    12514.46     7308.44     5206.02     1064485.02
   11      1064485.02    12514.46     7343.94     5170.52     1057141.08
   12      1057141.08    12514.46     7379.61     5134.85     1049761.47
   13      1049761.47    12514.46     7415.46     5099.01     1042346.01
   14      1042346.01    12514.46     7451.48     5062.99     1034894.54
   15      1034894.54    12514.46     7487.67     5026.79     1027406.87
   16      1027406.87    12514.46     7524.04     4990.42     1019882.83
   17      1019882.83    12514.46     7560.59     4953.88     1012322.24
   18      1012322.24    12514.46     7597.31     4917.15     1004724.93
   19      1004724.93    12514.46     7634.21     4880.25      997090.72
   20       997090.72    12514.46     7671.29     4843.17      989419.43
   21       989419.43    12514.46     7708.56     4805.91      981710.87
   22       981710.87    12514.46     7746.00     4768.46      973964.87
   23       973964.87    12514.46     7783.62     4730.84      966181.25
   24       966181.25    12514.46     7821.43     4693.03      958359.82
========================================================================
Total                               177640.18   122706.92
