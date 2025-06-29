'''
Farmer Problem:
Mahesh is a farmer and owns 80 acres of land. His land is equally divided into 5 segments. He grows
tomatoes in the 1st segment, potatoes in the 2nd segment, cabbage in the 3rd segment, sunflower in
the 4th segment and sugarcane in the 5th segment.
He is converting his land from chemical-driven farming to chemical-free farming. Mahesh starts with
the conversion of vegetables into chemical-free produce. He spends the first 6 months doing the same.
He then converts the sunflower land bank into chemical-free farming. This takes him another 4
months. Finally, he converts sugarcane into chemical-free farming over the next 4 months.
He gets a yield of the following for tomatoes. 30% of his tomato land gives him 10 tonne yield per acre.
The remaining 70% of his tomato land gives him 12 tonnes yield per acre. The selling price of tomato
is Rs. 7 per Kg.
The yield of potatoes is 10 tonnes per acre. He sells each kg at Rs. 20.
The yield of cabbage is 14 tonnes per acre. He sells each kg at Rs. 24.
The yield of sunflowers is 0.7 tonnes per acre. He sells each kg at Rs. 200.
The yield of sugarcane is 45 tonnes per acre. He sells each tonne at Rs. 4,000.
All the crops are sowed at the same time. Mahesh gets the above yield at the above-mentioned rate
in one crop cycle across his entire land of 80 acres.
What is
a. The overall sales achieved by Mahesh from the 80 acres of land.
b. Sales realisation from chemical-free farming at the end of 11 months?

Land distribution

Each of the 5 segments = 80 ÷ 5 = 16 acres

Tomatoes (16 acres):

30% of 16 = 4.8 acres → yield = 4.8 * 10 = 48 tonnes

70% of 16 = 11.2 acres → yield = 11.2 * 12 = 134.4 tonnes

Total tomato yield = 48 + 134.4 = 182.4 tonnes = 182,400 kg

Selling price = ₹7/kg → Revenue = 182,400 * 7 = ₹1,276,800

Potatoes (16 acres):

Yield = 10 tonnes/acre * 16 = 160 tonnes = 160,000 kg

Price = ₹20/kg → Revenue = 160,000 * 20 = ₹3,200,000

Cabbage (16 acres):

Yield = 14 tonnes/acre * 16 = 224 tonnes = 224,000 kg

Price = ₹24/kg → Revenue = 224,000 * 24 = ₹5,376,000

Sunflower (16 acres):

Yield = 0.7 tonnes/acre * 16 = 11.2 tonnes = 11,200 kg

Price = ₹200/kg → Revenue = 11,200 * 200 = ₹2,240,000

Sugarcane (16 acres):

Yield = 45 tonnes/acre * 16 = 720 tonnes

Price = ₹4,000/tonne → Revenue = 720 * 4,000 = ₹2,880,000

Total sales from all 80 acres =
₹1,276,800 (tomatoes) + ₹3,200,000 (potatoes) + ₹5,376,000 (cabbage) + ₹2,240,000 (sunflower) + ₹2,880,000 (sugarcane) =
₹14,972,800
'''


def farmer_sales():
    total_land = 80
    segments = 5
    land_per_crop = total_land / segments
    tomato_land = land_per_crop
    tomato_30 = 0.3 * tomato_land * 10 * 1000 * 7 
    tomato_70 = 0.7 * tomato_land * 12 * 1000 * 7 
    tomato_sales = tomato_30 + tomato_70
    potato_sales = land_per_crop * 10 * 1000 * 20
    cabbage_sales = land_per_crop * 14 * 1000 * 24
    sunflower_sales = land_per_crop * 0.7 * 1000 * 200
    sugarcane_sales = land_per_crop * 45 * 4000 

    total_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales

    print(f"A. Total Sales from 80 acres: Rs. {total_sales:,.2f}")
    chemical_free_veggies = tomato_sales + potato_sales + cabbage_sales
    chemical_free_sunflower = sunflower_sales 
    chemical_free_sales = chemical_free_veggies + chemical_free_sunflower

    print(f"B. Chemical-Free Farming Sales (at 11 months): Rs. {chemical_free_sales:,.2f}")

farmer_sales()

