<div align=center>
<img src="https://github.com/Hwenshuo/IRCSD/blob/main/assets/IRCSD.png" width="180" height="105"> width="180" height="105"/>
</div>


#### Interactive Rapid Climate Signal Detection Software

The Interactive Rapid Climate Signal Detection Software (IRCSD) is a fast climate signal detection tool developed using Dash and Python. For unknown climate signals as input, IRCSD integrates various climate statistical methods, including selecting time ranges, standard preprocessing, detrending, and employing different filtering methods and types, to compute the correlation between the signal and common climate indices (such as atmospheric, oceanic, and sea ice indices). It utilizes parallel computing to enhance detection speed and outputs interactive detection results (autocorrelation coefficients, correlation coefficients, lead-lag correlation coefficients, and responses of common air-sea fields). IRCSD is aimed at students and researchers in atmospheric science, particularly in the field of climatology, as well as the public interested in meteorology, with the goal of helping to quickly identify potential source regions of anomalous signals, improving the efficiency of climate change research and reducing data processing time.

The following indices are provided:

-[PNA](https://www.psl.noaa.gov/data/correlation/pna.data),
Pacific North American Index  
-[EP/NP](https://www.psl.noaa.gov/data/correlation/epo.data),
East Pacific/North Pacific Oscillation  
-[WP](https://www.psl.noaa.gov/data/correlation/wp.data),
Western Pacific Index  
-[EA/WR](https://www.psl.noaa.gov/data/correlation/ea.data),
Eastern Atlantic/Western Russia  
-[NAO](https://www.psl.noaa.gov/data/correlation/nao.data),
North Atlantic Oscillation  
-[NAO_Jones](https://www.psl.noaa.gov/data/correlation/jonesnao.data),
North Atlantic Oscillation (Jones)  
-[SOI](https://www.psl.noaa.gov/data/correlation/soi.data),
Southern Oscillation Index  
-[SOI_1866](https://climatedataguide.ucar.edu/sites/default/files/2024-04/darwin.anom_.txt),
Southern Oscillation Index 1866  
-[Niño 3](https://www.psl.noaa.gov/data/correlation/nina3.anom.data),
Eastern Tropical Pacific SST (5N-5S, 150W-90W)  
-[BEST](https://www.psl.noaa.gov/data/correlation/censo.long.data),
Bivariate ENSO Timeseries  
-[TNA](https://www.psl.noaa.gov/data/correlation/tna.data),
Tropical Northern Atlantic Index  
-[TSA](https://www.psl.noaa.gov/data/correlation/tsa.data),
Tropical Southern Atlantic Index  
-[WHWP](https://www.psl.noaa.gov/data/correlation/whwp.data),
Western Hemisphere Warm Pool  
-[ONI](https://www.psl.noaa.gov/data/correlation/oni.data),
Oceanic Niño Index  
-[MEI_V2](https://www.psl.noaa.gov/enso/mei/data/meiv2.data),
Multivariate ENSO Index (MEI V2)  
-[Niño 1+2](https://www.psl.noaa.gov/data/correlation/nina1.anom.data),
Extreme Eastern Tropical Pacific SST (0-10S, 90W-80W)  
-[Niño 4](https://www.psl.noaa.gov/data/correlation/nina4.anom.data),
Central Tropical Pacific SST (5N-5S, 160E-150W)  
-[Niño 3.4](https://www.psl.noaa.gov/data/correlation/nina34.anom.data),
East Central Tropical Pacific SST (5N-5S, 170-120W)  
-[PDO](https://www.psl.noaa.gov/data/correlation/pdo.data),
Pacific Decadal Oscillation  
-[IPO](https://www.psl.noaa.gov/data/timeseries/IPOTPI/ipotpi.hadisst2.data),
Tripole Index for the Interdecadal Pacific Oscillation  
-[NOI](https://www.psl.noaa.gov/data/correlation/noi.data),
Northern Oscillation Index  
-[NP](https://www.psl.noaa.gov/data/correlation/np.data),
North Pacific Pattern  
-[TNI](https://www.psl.noaa.gov/data/correlation/tni.data),
Trans-Niño Index (Indices of El Niño Evolution)  
-[AO](https://www.psl.noaa.gov/data/correlation/ao.data),
Arctic Oscillation  
-[AAO](https://www.psl.noaa.gov/data/correlation/aao.data),
Antarctic Oscillation  
-[Pacific Warm Pool Region](https://www.psl.noaa.gov/data/correlation/pacwarm.data),
Pacific Warm Pool Area Average  
-[Tropical Pacific SST EOF](https://psl.noaa.gov/data/correlation/eofpac.data),
Tropical Pacific SST EOF  
-[Atlantic Tripole SST EOF](https://www.psl.noaa.gov/data/correlation/atltri.data),
Atlantic Tripole SST EOF  
-[AMO_US](https://www.psl.noaa.gov/data/correlation/amon.us.data),
Atlantic Multidecadal Oscillation Long Version, unsmoothed  
-[AMM](https://www.psl.noaa.gov/data/timeseries/monthly/AMM/ammsst.data),
Atlantic Meridional Mode  
-[NTA](https://www.psl.noaa.gov/data/correlation/NTA_ersst.data),
North Tropical Atlantic SST Index  
-[CAR](https://www.psl.noaa.gov/data/correlation/CAR_ersst.data),
Caribbean SST Index  
-[AMO_S](https://www.psl.noaa.gov/data/correlation/amon.sm.data),
Atlantic Multidecadal Oscillation Smoothed  
-[QBO](https://www.psl.noaa.gov/data/correlation/qbo.data),
Quasi-Biennial Oscillation  
-[GAM](https://www.psl.noaa.gov/data/correlation/glaam.data.scaled),
Globally Integrated Angular Momentum  
-[ENSO_Pr_Index](https://www.psl.noaa.gov/data/correlation/espi.data),
ENSO Precipitation Index  
-[CI_Pr](https://www.psl.noaa.gov/data/correlation/indiamon.data),
Central Indian Precipitation  
-[Sahel_Pr](https://www.psl.noaa.gov/data/correlation/sahelrain.data),
Sahel Standardized Rainfall  
-[SWM_Pr](https://www.psl.noaa.gov/data/correlation/swmonsoon.data),
SW Monsoon Region Rainfall  
-[NMB_Pr](https://www.psl.noaa.gov/data/correlation/brazilrain.data),
Northeast Brazil Rainfall Anomaly  
-[Solar_Flux](https://www.psl.noaa.gov/data/correlation/solar.data),
Solar Flux (10.7cm)  
-[NAO_MetOffice](https://crudata.uea.ac.uk/cru/data/nao/nao_3dp.dat),
North Atlantic Oscillation Index  
-[NCC_ATM1](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM1  
-[NCC_ATM2](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM2  
-[NCC_ATM3](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM3  
-[NCC_ATM4](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM4  
-[NCC_ATM5](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM5  
-[NCC_ATM6](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM6  
-[NCC_ATM7](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM7  
-[NCC_ATM8](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM8  
-[NCC_ATM9](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM9  
-[NCC_ATM10](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM10  
-[NCC_ATM11](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM11  
-[NCC_ATM12](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM12  
-[NCC_ATM13](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM13  
-[NCC_ATM14](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM14  
-[NCC_ATM15](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM15  
-[NCC_ATM16](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM16  
-[NCC_ATM17](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM17  
-[NCC_ATM18](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM18  
-[NCC_ATM19](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM19  
-[NCC_ATM20](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM20  
-[NCC_ATM21](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM21  
-[NCC_ATM22](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM22  
-[NCC_ATM23](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM23  
-[NCC_ATM24](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM24  
-[NCC_ATM25](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM25  
-[NCC_ATM26](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM26  
-[NCC_ATM27](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM27  
-[NCC_ATM28](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM28  
-[NCC_ATM29](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM29  
-[NCC_ATM30](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM30  
-[NCC_ATM31](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM31  
-[NCC_ATM32](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM32  
-[NCC_ATM33](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM33  
-[NCC_ATM34](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM34  
-[NCC_ATM35](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM35  
-[NCC_ATM36](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM36  
-[NCC_ATM37](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM37  
-[NCC_ATM38](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM38  
-[NCC_ATM39](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM39  
-[NCC_ATM40](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM40  
-[NCC_ATM41](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM41  
-[NCC_ATM42](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM42  
-[NCC_ATM43](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM43  
-[NCC_ATM44](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM44  
-[NCC_ATM45](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM45  
-[NCC_ATM46](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM46  
-[NCC_ATM47](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM47  
-[NCC_ATM48](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM48  
-[NCC_ATM49](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM49  
-[NCC_ATM50](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM50  
-[NCC_ATM51](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM51  
-[NCC_ATM52](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM52  
-[NCC_ATM53](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM53  
-[NCC_ATM54](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM54  
-[NCC_ATM55](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM55  
-[NCC_ATM56](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM56  
-[NCC_ATM57](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM57  
-[NCC_ATM58](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM58  
-[NCC_ATM59](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM59  
-[NCC_ATM60](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM60  
-[NCC_ATM61](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM61  
-[NCC_ATM62](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM62  
-[NCC_ATM63](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM63  
-[NCC_ATM64](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM64  
-[NCC_ATM65](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM65  
-[NCC_ATM66](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM66  
-[NCC_ATM67](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM67  
-[NCC_ATM68](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM68  
-[NCC_ATM69](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM69  
-[NCC_ATM70](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM70  
-[NCC_ATM71](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM71  
-[NCC_ATM72](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM72  
-[NCC_ATM73](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM73  
-[NCC_ATM74](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM74  
-[NCC_ATM75](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM75  
-[NCC_ATM76](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM76  
-[NCC_ATM77](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM77  
-[NCC_ATM78](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM78  
-[NCC_ATM79](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM79  
-[NCC_ATM80](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM80  
-[NCC_ATM81](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM81  
-[NCC_ATM82](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM82  
-[NCC_ATM83](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM83  
-[NCC_ATM84](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM84  
-[NCC_ATM85](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM85  
-[NCC_ATM86](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM86  
-[NCC_ATM87](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM87  
-[NCC_ATM88](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_ATM88  
-[NCC_OCE1](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE1  
-[NCC_OCE2](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE2  
-[NCC_OCE3](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE3  
-[NCC_OCE4](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE4  
-[NCC_OCE5](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE5  
-[NCC_OCE6](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE6  
-[NCC_OCE7](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE7  
-[NCC_OCE8](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE8  
-[NCC_OCE9](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE9  
-[NCC_OCE10](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE10  
-[NCC_OCE11](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE11  
-[NCC_OCE12](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE12  
-[NCC_OCE13](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE13  
-[NCC_OCE14](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE14  
-[NCC_OCE15](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE15  
-[NCC_OCE16](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE16  
-[NCC_OCE17](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE17  
-[NCC_OCE18](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE18  
-[NCC_OCE19](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE19  
-[NCC_OCE20](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE20  
-[NCC_OCE21](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE21  
-[NCC_OCE22](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE22  
-[NCC_OCE23](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE23  
-[NCC_OCE24](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE24  
-[NCC_OCE25](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE25  
-[NCC_OCE26](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_OCE26  
-[NCC_EXT1](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_EXT1  
-[NCC_EXT2](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_EXT2  
-[NCC_EXT3](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_EXT3  
-[NCC_EXT4](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_EXT4  
-[NCC_EXT5](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_EXT5  
-[NCC_EXT6](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_EXT6  
-[NCC_EXT7](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_EXT7  
-[NCC_EXT8](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_EXT8  
-[NCC_EXT9](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_EXT9  
-[NCC_EXT10](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_EXT10  
-[NCC_EXT11](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_EXT11  
-[NCC_EXT12](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_EXT12  
-[NCC_EXT13](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_EXT13  
-[NCC_EXT14](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_EXT14  
-[NCC_EXT15](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_EXT15  
-[NCC_EXT16](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php),
NCC_EXT16  


