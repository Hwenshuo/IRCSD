<div align=center>
<img src="https://github.com/Hwenshuo/IRCSD/blob/main/assets/IRCSD.png" width="246" height="251"> 
</div>


## Introduction

The Interactive Rapid Climate Signal Detection Software (IRCSD) is a fast climate signal detection tool developed using Dash and Python. For unknown climate signals as input, IRCSD integrates various climate statistical methods, including selecting time ranges, standard preprocessing, detrending, and employing different filtering methods and types, to compute the correlation between the signal and common climate indices (such as atmospheric, oceanic, and sea ice indices). It utilizes parallel computing to enhance detection speed and outputs interactive detection results (autocorrelation coefficients, correlation coefficients, lead-lag correlation coefficients, and responses of common air-sea fields). IRCSD is aimed at students and researchers in atmospheric science, particularly in the field of climatology, as well as the public interested in meteorology, with the goal of helping to quickly identify potential source regions of anomalous signals, improving the efficiency of climate change research and reducing data processing time.

## Climate Indices List
The following indices are provided (Total number: 271)

-[PNA](https://www.psl.noaa.gov/data/correlation/pna.data) (1948-2024), 
Pacific North American Index  
-[EP/NP](https://www.psl.noaa.gov/data/correlation/epo.data) (1948-2024), 
East Pacific/North Pacific Oscillation  
-[WP](https://www.psl.noaa.gov/data/correlation/wp.data) (1948-2024), 
Western Pacific Index  
-[EA/WR](https://www.psl.noaa.gov/data/correlation/ea.data) (1948-2024), 
Eastern Atlantic/Western Russia  
-[NAO](https://www.psl.noaa.gov/data/correlation/nao.data) (1948-2024), 
North Atlantic Oscillation  
-[NAO_Jones](https://www.psl.noaa.gov/data/correlation/jonesnao.data) (1948-2022), 
North Atlantic Oscillation (Jones)  
-[SOI](https://www.psl.noaa.gov/data/correlation/soi.data) (1948-2024), 
Southern Oscillation Index  
-[SOI_1866](https://climatedataguide.ucar.edu/sites/default/files/2024-04/darwin.anom_.txt) (1866-2024), 
Southern Oscillation Index 1866  
-[Niño 3](https://www.psl.noaa.gov/data/correlation/nina3.anom.data) (1948-2024), 
Eastern Tropical Pacific SST (5N-5S, 150W-90W)  
-[BEST](https://www.psl.noaa.gov/data/correlation/censo.long.data) (1871-2003), 
Bivariate ENSO Timeseries  
-[TNA](https://www.psl.noaa.gov/data/correlation/tna.data) (1948-2024), 
Tropical Northern Atlantic Index  
-[TSA](https://www.psl.noaa.gov/data/correlation/tsa.data) (1948-2024), 
Tropical Southern Atlantic Index  
-[WHWP](https://www.psl.noaa.gov/data/correlation/whwp.data) (1948-2024), 
Western Hemisphere Warm Pool  
-[ONI](https://www.psl.noaa.gov/data/correlation/oni.data) (1950-2024), 
Oceanic Niño Index  
-[MEI_V2](https://www.psl.noaa.gov/enso/mei/data/meiv2.data) (1979-2024), 
Multivariate ENSO Index (MEI V2)  
-[Niño 1+2](https://www.psl.noaa.gov/data/correlation/nina1.anom.data) (1948-2024), 
Extreme Eastern Tropical Pacific SST (0-10S, 90W-80W)  
-[Niño 4](https://www.psl.noaa.gov/data/correlation/nina4.anom.data) (1948-2024), 
Central Tropical Pacific SST (5N-5S, 160E-150W)  
-[Niño 3.4](https://www.psl.noaa.gov/data/correlation/nina34.anom.data) (1948-2024), 
East Central Tropical Pacific SST (5N-5S, 170-120W)  
-[PDO](https://www.psl.noaa.gov/data/correlation/pdo.data) (1948-2022), 
Pacific Decadal Oscillation  
-[IPO](https://www.psl.noaa.gov/data/timeseries/IPOTPI/ipotpi.hadisst2.data) (1870-2010), 
Tripole Index for the Interdecadal Pacific Oscillation  
-[NOI](https://www.psl.noaa.gov/data/correlation/noi.data) (1948-2024), 
Northern Oscillation Index  
-[NP](https://www.psl.noaa.gov/data/correlation/np.data) (1948-2020), 
North Pacific Pattern  
-[TNI](https://www.psl.noaa.gov/data/correlation/tni.data) (1948-2023), 
Trans-Niño Index (Indices of El Niño Evolution)  
-[AO](https://www.psl.noaa.gov/data/correlation/ao.data) (1950-2024), 
Arctic Oscillation  
-[AAO](https://www.psl.noaa.gov/data/correlation/aao.data) (1979-2023), 
Antarctic Oscillation  
-[Pacific Warm Pool Region](https://www.psl.noaa.gov/data/correlation/pacwarm.data) (1948-2024), 
Pacific Warm Pool Area Average  
-[Tropical Pacific SST EOF](https://psl.noaa.gov/data/correlation/eofpac.data) (1948-2008), 
Tropical Pacific SST EOF  
-[Atlantic Tripole SST EOF](https://www.psl.noaa.gov/data/correlation/atltri.data) (1948-2008), 
Atlantic Tripole SST EOF  
-[AMO_US](https://www.psl.noaa.gov/data/correlation/amon.us.data) (1948-2023), 
Atlantic Multidecadal Oscillation Long Version, unsmoothed  
-[AMM](https://www.psl.noaa.gov/data/timeseries/monthly/AMM/ammsst.data) (1948-2024), 
Atlantic Meridional Mode  
-[NTA](https://www.psl.noaa.gov/data/correlation/NTA_ersst.data) (1950-2020), 
North Tropical Atlantic SST Index  
-[CAR](https://www.psl.noaa.gov/data/correlation/CAR_ersst.data) (1950-2020), 
Caribbean SST Index  
-[AMO_S](https://www.psl.noaa.gov/data/correlation/amon.sm.data) (1948-2017), 
Atlantic Multidecadal Oscillation Smoothed  
-[QBO](https://www.psl.noaa.gov/data/correlation/qbo.data) (1948-2024), 
Quasi-Biennial Oscillation  
-[GAM](https://www.psl.noaa.gov/data/correlation/glaam.data.scaled) (1958-2014), 
Globally Integrated Angular Momentum  
-[ENSO_Pr_Index](https://www.psl.noaa.gov/data/correlation/espi.data) (1979-2023), 
ENSO Precipitation Index  
-[CI_Pr](https://www.psl.noaa.gov/data/correlation/indiamon.data) (1948-1999), 
Central Indian Precipitation  
-[Sahel_Pr](https://www.psl.noaa.gov/data/correlation/sahelrain.data) (1948-2017), 
Sahel Standardized Rainfall  
-[SWM_Pr](https://www.psl.noaa.gov/data/correlation/swmonsoon.data) (1948-2010), 
SW Monsoon Region Rainfall  
-[NMB_Pr](https://www.psl.noaa.gov/data/correlation/brazilrain.data) (1948-2000), 
Northeast Brazil Rainfall Anomaly  
-[Solar_Flux](https://www.psl.noaa.gov/data/correlation/solar.data) (1948-2024), 
Solar Flux (10.7cm)  
-[NAO_MetOffice](https://crudata.uea.ac.uk/cru/data/nao/nao_3dp.dat) (1821-2024), 
North Atlantic Oscillation Index  
-[NCC_ATM1](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Northern Hemisphere Subtropical High Area Index  
-[NCC_ATM2](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North African Subtropical High Area Index  
-[NCC_ATM3](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North African-North Atlantic-North American Subtropical High Area Index  
-[NCC_ATM4](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Indian Subtropical High Area Index  
-[NCC_ATM5](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Western Pacific Subtropical High Area Index  
-[NCC_ATM6](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Eastern Pacific Subtropical High Area Index  
-[NCC_ATM7](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North American Subtropical High Area Index  
-[NCC_ATM8](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Atlantic Subtropical High Area Index  
-[NCC_ATM9](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
South China Sea Subtropical High Area Index  
-[NCC_ATM10](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North American-Atlantic Subtropical High Area Index  
-[NCC_ATM11](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Pacific Subtropical High Area Index  
-[NCC_ATM12](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Northern Hemisphere Subtropical High Intensity Index  
-[NCC_ATM13](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North African Subtropical High Intensity Index  
-[NCC_ATM14](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North African-North Atlantic-North American Subtropical High Intensity Index  
-[NCC_ATM15](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Indian Subtropical High Intensity Index  
-[NCC_ATM16](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Western Pacific Subtropical High Intensity Index  
-[NCC_ATM17](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Eastern Pacific Subtropical High Intensity Index  
-[NCC_ATM18](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North American Subtropical High Intensity Index  
-[NCC_ATM19](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North Atlantic Subtropical High Intensity Index  
-[NCC_ATM20](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
South China Sea Subtropical High Intensity Index  
-[NCC_ATM21](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North American-North Atlantic Subtropical High Intensity Index  
-[NCC_ATM22](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Pacific Subtropical High Intensity Index  
-[NCC_ATM23](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Northern Hemisphere Subtropical High Ridge Position Index  
-[NCC_ATM24](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North African Subtropical High Ridge Position Index  
-[NCC_ATM25](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North African-North Atlantic-North American Subtropical High Ridge Position Index  
-[NCC_ATM26](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Indian Subtropical High Ridge Position Index  
-[NCC_ATM27](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Western Pacific Subtropical High Ridge Position Index  
-[NCC_ATM28](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Eastern Pacific Subtropical High Ridge Position Index  
-[NCC_ATM29](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North American Subtropical High Ridge Position Index  
-[NCC_ATM30](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Atlantic Sub Tropical High Ridge Position Index  
-[NCC_ATM31](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
South China Sea Subtropical High Ridge Position Index  
-[NCC_ATM32](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North American-North Atlantic Subtropical High Ridge Position Index  
-[NCC_ATM33](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Pacific Subtropical High Ridge Position Index  
-[NCC_ATM34](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Northern Hemisphere Subtropical High Northern Boundary Position Index  
-[NCC_ATM35](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North African Subtropical High Northern Boundary Position Index  
-[NCC_ATM36](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North African-North Atlantic-North American Subtropical High Northern Boundary Position Index  
-[NCC_ATM37](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Indian Subtropical High Northern Boundary Position Index  
-[NCC_ATM38](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Western Pacific Subtropical High Northern Boundary Position Index  
-[NCC_ATM39](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Eastern Pacific Subtropical High Northern Boundary Position Index  
-[NCC_ATM40](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North American Subtropical High Northern Boundary Position Index  
-[NCC_ATM41](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Atlantic Subtropical High Northern Boundary Position Index  
-[NCC_ATM42](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
South China Sea Subtropical High Northern Boundary Position Index  
-[NCC_ATM43](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North American-Atlantic Subtropical High Northern Boundary Position Index  
-[NCC_ATM44](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Pacific Subtropical High Northern Boundary Position Index  
-[NCC_ATM45](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Western Pacific Sub Tropical High Western Ridge Point Index  
-[NCC_ATM46](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Asia Polar Vortex Area Index  
-[NCC_ATM47](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Pacific Polar Vortex Area Index  
-[NCC_ATM48](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North American Polar Vortex Area Index  
-[NCC_ATM49](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Atlantic-European Polar Vortex Area Index  
-[NCC_ATM50](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Northern Hemisphere Polar Vortex Area Index  
-[NCC_ATM51](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Asia Polar Vortex Intensity Index  
-[NCC_ATM52](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Pacific Polar Vortex Intensity Index  
-[NCC_ATM53](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North American Polar Vortex Intensity Index  
-[NCC_ATM54](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Atlantic-European Polar Vortex Intensity Index  
-[NCC_ATM55](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Northern Hemisphere Polar Vortex Intensity Index  
-[NCC_ATM56](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Northern Hemisphere Polar Vortex Central Longitude Index  
-[NCC_ATM57](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Northern Hemisphere Polar Vortex Central Latitude Index  
-[NCC_ATM58](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Northern Hemisphere Polar Vortex Central Intensity Index  
-[NCC_ATM59](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Eurasian Zonal Circulation Index  
-[NCC_ATM60](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Eurasian Meridional Circulation Index  
-[NCC_ATM61](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Asian Zonal Circulation Index  
-[NCC_ATM62](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Asian Meridional Circulation Index  
-[NCC_ATM63](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
East Asian Trough Position Index  
-[NCC_ATM64](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
East Asian Trough Intensity Index  
-[NCC_ATM65](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Tibet Plateau Region 1 Index  
-[NCC_ATM66](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Tibet Plateau Region 2 Index  
-[NCC_ATM67](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
India-Burma Trough Intensity Index  
-[NCC_ATM68](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Arctic Oscillation, AO  
-[NCC_ATM69](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Antarctic Oscillation, AAO  
-[NCC_ATM70](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North Atlantic Oscillation , NAO  
-[NCC_ATM71](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Pacific/ North American Pattern , PNA  
-[NCC_ATM72](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
East Atlantic Pattern, EA  
-[NCC_ATM73](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
West Pacific Pattern , WP  
-[NCC_ATM74](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
North Pacific Pattern , NP  
-[NCC_ATM75](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
East Atlantic-West Russia Pattern , EA/WR  
-[NCC_ATM76](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Tropical-Northern Hemisphere Pattern, TNH  
-[NCC_ATM77](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Polar-Eurasia Pattern , POL  
-[NCC_ATM78](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Scandinavia Pattern , SCA  
-[NCC_ATM79](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Pacific Transition Pattern, PT  
-[NCC_ATM80](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
30hPa zonal wind Index  
-[NCC_ATM81](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
50 hPa zonal wind Index  
-[NCC_ATM82](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Mid-Eastern Pacific 200mb Zonal Wind Index  
-[NCC_ATM83](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
West Pacific 850mb Trade Wind Index  
-[NCC_ATM84](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Central Pacific 850mb Trade Wind Index  
-[NCC_ATM85](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
East Pacific 850mb Trade Wind Index  
-[NCC_ATM86](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Atlantic-European Circulation W Pattern Index  
-[NCC_ATM87](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Atlantic-European Circulation C Pattern Index  
-[NCC_ATM88](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Atlantic-European Circulation E Pattern Index  
-[NCC_OCE1](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NINO 1+2 SSTA Index  
-[NCC_OCE2](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NINO 3 SSTA Index  
-[NCC_OCE3](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NINO 4 SSTA Index  
-[NCC_OCE4](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NINO 3.4 SSTA Index  
-[NCC_OCE5](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NINO W SSTA Index  
-[NCC_OCE6](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NINO C SSTA Index  
-[NCC_OCE7](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NINO A SSTA Index  
-[NCC_OCE8](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NINO B SSTA Index  
-[NCC_OCE9](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NINO Z SSTA Index  
-[NCC_OCE10](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Tropical Northern Atlantic SST Index  
-[NCC_OCE11](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Tropical Southern Atlantic SST Index  
-[NCC_OCE12](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Western Hemisphere Warm Pool Index  
-[NCC_OCE13](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Indian Ocean Warm Pool Area Index  
-[NCC_OCE14](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Indian Ocean Warm Pool Strength Index  
-[NCC_OCE15](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Western Pacific Warm Pool Area Index  
-[NCC_OCE16](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Western Pacific Warm Pool Strength index  
-[NCC_OCE17](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Atlantic Multi-decadal Oscillation Index  
-[NCC_OCE18](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Oyashio Current SST Index  
-[NCC_OCE19](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
West Wind Drift Current SST Index  
-[NCC_OCE20](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Kuroshio Current SST Index  
-[NCC_OCE21](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
ENSO Modoki Index  
-[NCC_OCE22](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Warm-pool ENSO Index  
-[NCC_OCE23](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Cold-tongue ENSO Index  
-[NCC_OCE24](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Indian Ocean Basin-Wide Index  
-[NCC_OCE25](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
Tropic Indian Ocean Dipole Index  
-[NCC_OCE26](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
South Indian Ocean Dipole Index  
-[NCC_EXT1](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
Cold Air Activity Index  
-[NCC_EXT2](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
Western North Pacific Typhoon number  
-[NCC_EXT3](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
Number of Landing Typhoon on China  
-[NCC_EXT4](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
Total Sunspot Number Index  
-[NCC_EXT5](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
Southern Oscillation Index  
-[NCC_EXT6](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
Tropical Pacific Outgoing Long Wave Radiation Index  
-[NCC_EXT7](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
Multivariate ENSO Index  
-[NCC_EXT8](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
Pacific Decadal Oscillation Index  
-[NCC_EXT9](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
Atlantic Meridional Mode SST Index  
-[NCC_EXT10](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
Quasi-Biennial Oscillation Index  
-[NCC_EXT11](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
Globally Integrated Angular Momentum Index  
-[NCC_EXT12](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
Solar Flux Index  
-[NCC_EXT13](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
Equatorial Pacific 130°E-80°W Upper 300m temperature averaged anomaly index  
-[NCC_EXT14](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
Equatorial Pacific 160°E-80°W Upper 300m temperature Average anomaly index  
-[NCC_EXT15](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
Equatorial Pacific 180º-100ºW Upper 300m temperature Average anomaly index  
-[NCC_EXT16](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
North Atlantic Triple index  