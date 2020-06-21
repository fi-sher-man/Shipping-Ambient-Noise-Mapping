# Shipping-Ambient-Noise-Mapping
This does the spatiotemporal shipping ambient noise mapping using Wittekind model for estimating the Source Level(SL) and 2D PE-RAM model for estimating the Transmission Loss(TL)

AIS_Old3.csv has the AIS data of 2209 ships.

area has max depths at each of refrence coordinates.

Etopo1v2.xlsx has the Bathtmetry data which is used as one the inputs for total_TL.

Reference Coordinates has the coordinates which we take as reference. The total TL and SL after running the total_TL.py and total_SL.py will get appendend to this.

Wittekind_Inputs.csv has all data required for computing SL from total_SL.py

book1.csv has the row indexes of the ships that contriubute to the ambient noise in 0.5 latitude range.

extractbathy.py is a function to obtain bathymetry data from area.xlsx in the format required for PE RAM model.

extractspeeds.py is a function to obtain speed data from the area.xlsx in the speeds folder in the format required for PE RAM model.

findships.py updates the book1 for which ships are to be considered in the given range.

mywittekind.py has the wittekind function.

total_SL.py calculates the cumulative SL contributed by the ships for each reference coordinate.

total_TL.py calculates the cumulative TL to be accounted for by the ships for each reference coordinate.
