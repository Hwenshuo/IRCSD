<div align=center>
<img src="https://github.com/Hwenshuo/IRCSD/blob/main/assets/IRCSD.png" width="246" height="251"> 
</div>


## Introduction

The Interactive Rapid Climate Signal Detection Software (IRCSD) is a fast climate signal detection tool developed using Dash and Python. For unknown climate signals as input, IRCSD integrates various climate statistical methods, including selecting time ranges, data preprocessing, detrending, and employing different filtering methods and types, to compute the correlation between the signal and over 250 common climate indices (such as atmospheric, oceanic, and sea ice indices). It utilizes parallel computing to accelerate detection speed and outputs interactive detection results (signal time series, correlation, lead-lag correlation, and sliding correlation). IRCSD is designed for students and researchers in atmospheric science, particularly those in the field of climatology, as well as for the public interested in climate change. The goal of IRCSD is to assist in quickly identifying potential source regions of anomalous signals and to enhance the efficiency of climate change research.

Author: Wenshuo Huang (huangwenshuo21@mails.ucas.ac.cn)   
Version: 1.1 (Last updated: 2024.11.06)  
Source Code/Indices Infos: https://github.com/Hwenshuo/IRCSD  

## Functions

### Calculate correlation
#### Sort by absolute value of correlation coefficient from large to small
<div align="center">
  <video 
    width="400"
    style="max-width: 100%; display: block; margin: 10px auto;"
    src="https://github.com/user-attachments/assets/09187ee9-87e4-4a00-9419-afb5ac50a929"
    controls
    playsinline
  >
  </video>
</div>

### Calculate lead-lagged correlation
#### Sort by the largest absolute value of lead-lagged correlation coefficient from large to small
<div align="center">
  <video 
    width="400"
    style="max-width: 100%; display: block; margin: 10px auto;"
    src="https://github.com/user-attachments/assets/d4805da6-9674-429f-9d97-173338fcbc50"
    controls
    playsinline
  >
  </video>
</div>

### Calculate sliding correlation
<div align="center">
  <video 
    width="400"
    style="max-width: 100%; display: block; margin: 10px auto;"
    src="https://github.com/user-attachments/assets/07d241f3-67ee-4658-8d05-188b0dd4e526"
    controls
    playsinline
  >
  </video>
</div>

## Climate Indices List
The following indices are provided (Total number: 258):

-[Niño 1+2 (HadISST) ](https://psl.noaa.gov/data/timeseries/month/DS/Nino12/) (1870-2024), 
Niño 1+2 (HadISST)   
-[Niño 1+2 (ERSSTv5) ](https://psl.noaa.gov/data/timeseries/month/DS/Nino12_CPC/) (1948-2024), 
Niño 1+2 (ERSSTv5)   
-[Niño 3 (HadISST)](https://psl.noaa.gov/data/timeseries/month/DS/Nino3/) (1870-2024), 
Niño 3 (HadISST)  
-[Niño 3 (ERSSTv5)](https://psl.noaa.gov/data/timeseries/month/DS/Nino3_CPC/) (1948-2024), 
Niño 3 (ERSSTv5)  
-[Niño 3.4 (HadISST)](https://psl.noaa.gov/data/timeseries/month/DS/Nino34/) (1870-2024), 
Niño 3.4 (HadISST)  
-[Niño 3.4 (ERSSTv5)](https://psl.noaa.gov/data/timeseries/month/DS/Nino34_CPC/) (1948-2024), 
Niño 3.4 (ERSSTv5)  
-[Niño 4 (HadISST)](https://psl.noaa.gov/data/timeseries/month/DS/Nino4/) (1870-2024), 
Niño 4 (HadISST)  
-[Niño 4 (ERSSTv5)](https://psl.noaa.gov/data/timeseries/month/DS/Nino4_CPC/) (1948-2024), 
Niño 4 (ERSSTv5)  
-[MEI_Extended](https://psl.noaa.gov/data/timeseries/month/DS/MEI_EXTENDED/) (1871-2005), 
Multivariate ENSO Index (MEI Extended)  
-[MEI_V2](https://psl.noaa.gov/data/timeseries/month/DS/MEIV2/) (1979-2024), 
Multivariate ENSO Index V2  
-[ONI](https://psl.noaa.gov/data/timeseries/month/DS/ONI/) (1950-2024), 
Oceanic Niño Index  
-[OLR_CTP](https://psl.noaa.gov/data/timeseries/month/DS/OLR/ ) (1974-2024), 
Central Tropical Pacific OLR Index  
-[WH_WP](https://psl.noaa.gov/data/climateindices/list/) (1948-2024), 
Western Hemisphere Warm Pool  
-[PAC_WP](https://psl.noaa.gov/data/climateindices/list/) (1948-2024), 
Pacific Warm Pool Area Average  
-[PAC_WP_Long](https://psl.noaa.gov/data/timeseries/month/DS/PACWARM/ ) (1854-2024), 
Pacific Warm Pool  
-[TNI](https://psl.noaa.gov/data/climateindices/list/) (1948-2023), 
Trans-Niño Index  
-[TNI_Long](https://psl.noaa.gov/data/timeseries/month/DS/TNI/) (1870-2023), 
Trans-Niño Index Long  
-[HeatCentraPac](https://psl.noaa.gov/data/timeseries/month/DS/HEATCENTRA/) (1979-2024), 
Equatorial Central Pacific Heat Content: 160E-80W  
-[BEST_long](http://psl.noaa.gov/data/climateindices/list/) (1871-2003), 
Bivariate ENSO Time-series  
-[BEST](https://psl.noaa.gov/data/timeseries/month/DS/BEST/) (1948-2023), 
Bivariate ENSO Time-series  
-[AMM_WIND](https://psl.noaa.gov/data/timeseries/month/DS/AMM/ ) (1948-2023), 
Atlantic Meridional Mode Wind  
-[AMM_SST](https://psl.noaa.gov/data/timeseries/month/DS/AMM/ ) (1948-2024), 
Atlantic Meridional Mode SST  
-[PMM_WIND](https://psl.noaa.gov/data/timeseries/month/DS/PMM/ ) (1948-2019), 
Pacific Meridional Mode Wind  
-[PMM_SST](https://psl.noaa.gov/data/timeseries/month/DS/PMM/ ) (1948-2024), 
Pacific Meridional Mode SST  
-[DMI/IOD](https://psl.noaa.gov/data/timeseries/month/DS/DMI/) (1870-2022), 
Dipole Mode Index (DMI or IOD)  
-[DMI/IOD EAST](https://psl.noaa.gov/data/timeseries/month/DS/DMI/) (1870-2024), 
Dipole Mode Index (DMI or IOD) EAST  
-[TC-NE Pacific Days](https://psl.noaa.gov/data/timeseries/month/DS/HURRICANE_NEPAC_DAYS/) (1971-2021), 
Hurricane: NE Pacific Days  
-[TC-Atlantic Days](https://psl.noaa.gov/data/timeseries/month/DS/HURRICANE_ATL_DAYS/) (1851-2022), 
Hurricane : Atlantic Days  
-[TC-NW Pacific Days](https://psl.noaa.gov/data/timeseries/month/DS/HURRICANE_NWPAC_DAYS/) (1950-2021), 
Hurricane: NW Pacific Days  
-[TC-NE Pacific ACE](https://psl.noaa.gov/data/timeseries/month/DS/HURRICANE_NEPAC_ACE/) (1971-2021), 
Hurricane: NE Pacific ACE  
-[TC-Atlantic ACE](https://psl.noaa.gov/data/timeseries/month/DS/HURRICANE_ATL_ACE/) (1851-2022), 
Hurricane: Atlantic ACE  
-[TC-NW Pacific ACE](https://psl.noaa.gov/data/timeseries/month/DS/HURRICANE_NWPAC_ACE/) (1950-2021), 
Hurricane: NW Pacific ACE  
-[NPGO](https://psl.noaa.gov/data/timeseries/month/DS/NPGO/) (1950-2024), 
North Pacific Gyre Oscillation  
-[PDO_ENS](https://psl.noaa.gov/pdo/) (1870-2024), 
Pacific Decadal Oscillation calculate from Ensemble Mean  
-[PDO_ERSSTv5](https://psl.noaa.gov/pdo/) (1854-2024), 
Pacific Decadal Oscillation calculate from ERSSTv5  
-[PDO_HadISST_1.1](https://psl.noaa.gov/pdo/) (1870-2024), 
Pacific Decadal Oscillation calculate from HadISST 1.1  
-[PDO_COBE2](https://psl.noaa.gov/pdo/) (1850-2024), 
Pacific Decadal Oscillation calculate from COBE2  
-[PDO_CPC](https://psl.noaa.gov/data/timeseries/month/DS/PDO/) (1948-2022), 
Pacific Decadal Oscillation from CPC  
-[TPI_HadISST_2](https://psl.noaa.gov/data/timeseries/month/DS/PDOUW/) (1870-2010), 
Tripole Index for the Interdecadal Pacific Oscillation  
-[TPI_ERSSTv5](https://psl.noaa.gov/data/timeseries/IPOTPI/) (1854-2024), 
TPI (IPO) Tripole Index for the Interdecadal Pacific Oscillation from ERSSTv5  
-[TPI_HadISST_1.1](https://psl.noaa.gov/data/timeseries/IPOTPI/) (1870-2024), 
TPI (IPO) Tripole Index for the Interdecadal Pacific Oscillation from HadISST 1.1  
-[TPI_COBE](https://psl.noaa.gov/data/timeseries/IPOTPI/) (1891-2023), 
TPI (IPO) Tripole Index for the Interdecadal Pacific Oscillation from COBE2  
-[Tropical Pacific SST EOF](http://psl.noaa.gov/data/climateindices/list/) (1948-2008), 
Tropical Pacific SST EOF  
-[Atlantic Tripole SST EOF](http://psl.noaa.gov/data/climateindices/list/) (1948-2008), 
Atlantic Tripole SST EOF  
-[AMO_us](http://psl.noaa.gov/data/climateindices/list/) (1948-2023), 
Atlantic Multidecadal Oscillation, unsmoothed  
-[AMO_sm](http://psl.noaa.gov/data/climateindices/list/) (1948-2023), 
Atlantic Multidecadal Oscillation Smoothed  
-[AMO_us_long](https://psl.noaa.gov/data/timeseries/AMO/) (1856-2023), 
Atlantic Multidecadal Oscillation, unsmoothed, long  
-[AMO_sm_long](https://psl.noaa.gov/data/timeseries/AMO/) (1856-2023), 
Atlantic Multidecadal Oscillation, Smoothed, long  
-[GSL](https://psl.noaa.gov/data/timeseries/month/DS/SEALEVEL/) (1900-2018), 
Global Sea Level  
-[AAO](https://psl.noaa.gov/data/timeseries/month/DS/AAO_CPC/) (1979-2023), 
Antarctic Oscillation from NOAA/CPC  
-[AO](https://psl.noaa.gov/data/timeseries/month/DS/AO/) (1948-2022), 
Arctic Oscillation  
-[EA/WR](https://psl.noaa.gov/data/timeseries/month/EA/) (1948-2024), 
Eastern Atlantic/Western Russia: From NOAA Climate Prediction Center (CPC)  
-[AO_20CRv3](https://psl.noaa.gov/data/timeseries/month/AO20CR/) (1871-2012), 
Arctic Oscillation from the 20CRv3  
-[Madras-SLP](https://psl.noaa.gov/data/timeseries/month/DS/MADRAS/) (1796-2005), 
Madras reconstructed SLP  
-[NJ-SLP](https://psl.noaa.gov/data/timeseries/month/DS/NAGASAKI/) (1818-2000), 
Nakasaki Japan reconstructed SLP  
-[NAO_AZO](https://psl.noaa.gov/data/timeseries/month/DS/NAO_AZO/) (1865-2002), 
Azores Sea Level Pressure (SLP)  
-[NAO](http://psl.noaa.gov/data/climateindices/list/) (1948-2022), 
North Atlantic Oscillation  
-[NAO_ICE](http://psl.noaa.gov/data/climateindices/list/) (1821-2024), 
North Atlantic Oscillation: Iceland SLP(NAO ICE)  
-[NAO_GIB](http://psl.noaa.gov/data/climateindices/list/) (1821-2024), 
North Atlantic Oscillation: Gibralter SLP(NAO GIB)  
-[NAO_Jones](http://psl.noaa.gov/data/climateindices/list/) (1948-2022), 
North Atlantic Oscillation (Jones)  
-[NAO_CRU_Long](https://psl.noaa.gov/data/timeseries/month/DS/NAO/) (1821-2024), 
North Atlantic Oscillation from CRU  
-[RNAO](https://psl.noaa.gov/data/timeseries/month/DS/RNAO/) (1658-2001), 
Reconstructed North Atlantic Oscillation  
-[EP/NP](http://psl.noaa.gov/data/climateindices/list/) (1948-2024), 
East Pacific/North Pacific Oscillation  
-[NOI](https://psl.noaa.gov/data/timeseries/month/DS/NOI/) (1948-2024), 
Northern Oscillation Index  
-[NP](http://psl.noaa.gov/data/climateindices/list/) (1948-2020), 
North Pacific Pattern  
-[NP/NPI](https://psl.noaa.gov/data/timeseries/month/NP/) (1899-2022), 
North Pacific Index  
-[NP_20CRV3](https://psl.noaa.gov/data/timeseries/month/NP20CR/) (1836-2015), 
North Pacific Index from the 20CRV3  
-[TNA](http://psl.noaa.gov/data/climateindices/list/) (1948-2024), 
Tropical Northern Atlantic Index  
-[TSA](http://psl.noaa.gov/data/climateindices/list/) (1948-2024), 
Tropical Southern Atlantic Index  
-[NTA](http://psl.noaa.gov/data/climateindices/list/) (1950-2020), 
North Tropical Atlantic SST Index  
-[CAR](http://psl.noaa.gov/data/climateindices/list/) (1950-2020), 
Caribbean SST Index  
-[PNA](https://psl.noaa.gov/data/timeseries/month/PNA/) (1948-2024), 
Pacific North American Index  
-[SCAND](https://psl.noaa.gov/data/timeseries/month/SCAND/) (1950-2024), 
Scandinavian Index  
-[SOI_CRU_1866](https://psl.noaa.gov/data/timeseries/month/SOI/) (1866-2024), 
Southern Oscillation Index  
-[SOI](http://psl.noaa.gov/data/climateindices/list/) (1948-2024), 
Southern Oscillation Index  
-[SOI_20CRV3](https://psl.noaa.gov/data/timeseries/month/SOI20CR/) (1836-2015), 
Southern Oscillation Index from the 20CRV3  
-[WP](https://psl.noaa.gov/data/timeseries/month/DS/WP/) (1948-2024), 
West Pacific Index  
-[CO2-Loa](https://psl.noaa.gov/data/timeseries/month/DS/CO2ML) (1958-2024), 
CO2 at Mauna Loa  
-[CO2-GlobalAve](https://psl.noaa.gov/data/timeseries/month/DS/CO2/) (1979-2024), 
CO2: Global Average  
-[GBI_long](https://psl.noaa.gov/data/timeseries/month/GBI_UL/) (1851-2023), 
Greenland Blocking Index Long  
-[GBI](https://psl.noaa.gov/data/timeseries/month/GBI/) (1948-2015), 
Greenland Blocking Index (GBI)  
-[GLAAM](https://psl.noaa.gov/data/timeseries/month/DS/GLAAM/) (1958-2014), 
Global Angular Momentum  
-[MDR](https://psl.noaa.gov/data/timeseries/month/DS/MDR/) (1854-2024), 
Atlantic Main Development Region  
-[QBO-30mb](https://psl.noaa.gov/data/timeseries/month/DS/QBO/) (1948-2024), 
Quasi-biennial Oscillation 30mb  
-[QBO-50mb](https://psl.noaa.gov/data/timeseries/month/DS/QBO50/) (1948-2024), 
Quasi-biennial Oscillation 50mb  
-[uwnd_200_troppac](https://psl.noaa.gov/data/timeseries/month/DS/TROPPACU200/) (1948-2024), 
Tropical Pacific 200mb averaged zonal winds.  
-[Brazil_Pr](https://psl.noaa.gov/data/timeseries/month/DS/BRAZILRAIN/) (1948-2000), 
Northeast Brazil Rainfall Anomaly  
-[ENSO_Pr](https://psl.noaa.gov/data/timeseries/month/DS/ESPI/) (1979-2023), 
ENSO Precipitation Index  
-[Sahel_Pr_Long](https://psl.noaa.gov/data/timeseries/month/DS/SAHELRAIN/) (1901-2017), 
Sahel Standardized Rainfall Long  
-[Sahel_Pr](https://psl.noaa.gov/data/timeseries/month/DS/SAHELRAIN/) (1948-2017), 
Sahel Standardized Rainfall  
-[NSierra8_Pr](https://psl.noaa.gov/data/timeseries/month/DS/NSIERRA/) (1920-2024), 
N. Sierra 8 station precipitation time-series  
-[NSierra5_Pr](https://psl.noaa.gov/data/timeseries/month/DS/CSIERRA/) (1913-2024), 
C. Sierra 5 station precipitation time-series  
-[NSierra6_Pr](https://psl.noaa.gov/data/timeseries/month/DS/SSIERRA/) (1923-2024), 
S. Sierra 6 station precipitation time-series  
-[SWM_Pr](http://psl.noaa.gov/data/climateindices/list/) (1948-2010), 
SW Monsoon Region Rainfall  
-[SWUSM_Pr_Long](https://psl.noaa.gov/data/timeseries/month/DS/SWMONSOON/) (1895-2024), 
SW US Monsoon Region precipitation  
-[CI_Pr](http://psl.noaa.gov/data/climateindices/list/) (1948-1999), 
Central Indian Precipitation  
-[UCB_Pr](https://psl.noaa.gov/data/timeseries/month/DS/UpperCOP/) (1895-2019), 
Upper Colorado Basin precipitation  
-[NASA_Land_T](https://psl.noaa.gov/data/timeseries/month/DS/NASAGLBLT/) (1880-2024), 
NASA Global Land Temperature  
-[NASA_Comb_T](https://psl.noaa.gov/data/timeseries/month/DS/NASAGLBCOMT/) (1880-2024), 
NASA Global Land/Ocean Temperature  
-[Berk_Land_T](https://psl.noaa.gov/data/timeseries/month/DS/BERKELEYGLBLT/) (1750-2024), 
Berkeley Global Land Temperature  
-[Berk_Comb_T](https://psl.noaa.gov/data/timeseries/month/DS/BERKELEYGLBCOMT/) (1850-2024), 
Berkeley Global Land/Ocean Temperature  
-[CRU_Land_T](https://psl.noaa.gov/data/timeseries/month/DS/CRUGLBLT/) (1850-2022), 
CRU Global Land Temperature  
-[CRU_Comb_T](https://psl.noaa.gov/data/timeseries/month/DS/CRUGLBCOMT/) (1850-2024), 
CRU Global Land/Ocean Temperature  
-[NOAA_Land_T](https://psl.noaa.gov/data/timeseries/month/DS/NOAAGLBLT/) (1850-2024), 
NOAA Global Land Temperature  
-[NOAA_Comb_T](https://psl.noaa.gov/data/timeseries/month/DS/NOAAGLBCOMT/) (1850-2024), 
NOAA Global Land/Ocean Temperature  
-[NH_Ice_Area](https://psl.noaa.gov/data/timeseries/month/DS/NHICE/) (1978-2024), 
Northern Hemisphere Ice Area  
-[NH_Ice_Extent](https://psl.noaa.gov/data/timeseries/month/DS/NHICE/) (1978-2024), 
Northern Hemisphere Ice Extent  
-[NH_Snow_Extent](https://psl.noaa.gov/data/timeseries/month/DS/SNOWNH/) (1966-2024), 
Northern Hemisphere Snow Cover Extent  
-[SH_Ice_Area](https://psl.noaa.gov/data/timeseries/month/DS/SHICE/) (1978-2024), 
Southern Hemisphere Ice Area  
-[SH_Ice_Extent](https://psl.noaa.gov/data/timeseries/month/DS/SHICE/) (1978-2024), 
Southern Hemisphere Ice Extent  
-[Sunspot_Count](https://psl.noaa.gov/data/timeseries/month/DS/SUNSPOT/) (1749-2024), 
Sunspot Count  
-[Solar Flux](https://psl.noaa.gov/data/timeseries/month/DS/SOLAR/) (1948-2024), 
Solar Flux (10.7cm)  
-[US_Tornado_Count](https://psl.noaa.gov/data/timeseries/month/DS/TORNADO/) (1950-2024), 
US Tornado Count  
-[UCB_T](https://psl.noaa.gov/data/timeseries/month/DS/UpperCOT/) (1895-2019), 
Upper Colorado Basin Temperature  
-[LeesFerryNatlFlow](https://psl.noaa.gov/data/timeseries/month/DS/LeesFerryFlow/ ) (1905-2017), 
Lee's Ferry Natural Streamflow (upper CO Basin Streamflow)  
-[NCC_ATM1](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM1  
-[NCC_ATM2](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM2  
-[NCC_ATM3](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM3  
-[NCC_ATM4](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM4  
-[NCC_ATM5](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM5  
-[NCC_ATM6](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM6  
-[NCC_ATM7](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM7  
-[NCC_ATM8](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM8  
-[NCC_ATM9](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM9  
-[NCC_ATM10](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM10  
-[NCC_ATM11](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM11  
-[NCC_ATM12](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM12  
-[NCC_ATM13](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM13  
-[NCC_ATM14](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM14  
-[NCC_ATM15](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM15  
-[NCC_ATM16](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM16  
-[NCC_ATM17](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM17  
-[NCC_ATM18](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM18  
-[NCC_ATM19](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM19  
-[NCC_ATM20](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM20  
-[NCC_ATM21](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM21  
-[NCC_ATM22](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM22  
-[NCC_ATM23](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM23  
-[NCC_ATM24](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM24  
-[NCC_ATM25](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM25  
-[NCC_ATM26](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM26  
-[NCC_ATM27](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM27  
-[NCC_ATM28](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM28  
-[NCC_ATM29](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM29  
-[NCC_ATM30](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM30  
-[NCC_ATM31](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM31  
-[NCC_ATM32](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM32  
-[NCC_ATM33](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM33  
-[NCC_ATM34](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM34  
-[NCC_ATM35](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM35  
-[NCC_ATM36](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM36  
-[NCC_ATM38](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM38  
-[NCC_ATM39](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM39  
-[NCC_ATM40](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM40  
-[NCC_ATM41](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM41  
-[NCC_ATM43](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM43  
-[NCC_ATM44](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM44  
-[NCC_ATM45](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM45  
-[NCC_ATM46](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM46  
-[NCC_ATM47](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM47  
-[NCC_ATM48](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM48  
-[NCC_ATM49](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM49  
-[NCC_ATM50](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM50  
-[NCC_ATM51](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM51  
-[NCC_ATM52](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM52  
-[NCC_ATM53](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM53  
-[NCC_ATM54](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM54  
-[NCC_ATM55](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM55  
-[NCC_ATM56](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM56  
-[NCC_ATM57](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM57  
-[NCC_ATM58](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM58  
-[NCC_ATM59](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM59  
-[NCC_ATM60](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM60  
-[NCC_ATM61](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM61  
-[NCC_ATM62](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM62  
-[NCC_ATM63](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM63  
-[NCC_ATM64](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM64  
-[NCC_ATM65](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM65  
-[NCC_ATM66](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM66  
-[NCC_ATM67](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM67  
-[NCC_ATM68](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM68  
-[NCC_ATM69](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM69  
-[NCC_ATM70](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM70  
-[NCC_ATM71](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM71  
-[NCC_ATM72](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM72  
-[NCC_ATM73](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM73  
-[NCC_ATM74](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM74  
-[NCC_ATM75](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM75  
-[NCC_ATM76](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM76  
-[NCC_ATM77](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM77  
-[NCC_ATM78](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM78  
-[NCC_ATM80](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM80  
-[NCC_ATM81](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM81  
-[NCC_ATM82](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM82  
-[NCC_ATM83](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM83  
-[NCC_ATM84](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM84  
-[NCC_ATM85](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM85  
-[NCC_ATM86](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM86  
-[NCC_ATM87](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM87  
-[NCC_ATM88](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_ATM88  
-[NCC_OCE1](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE1  
-[NCC_OCE2](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE2  
-[NCC_OCE3](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE3  
-[NCC_OCE4](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE4  
-[NCC_OCE5](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE5  
-[NCC_OCE6](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE6  
-[NCC_OCE7](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE7  
-[NCC_OCE8](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE8  
-[NCC_OCE9](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE9  
-[NCC_OCE10](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE10  
-[NCC_OCE11](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE11  
-[NCC_OCE12](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE12  
-[NCC_OCE13](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE13  
-[NCC_OCE14](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE14  
-[NCC_OCE15](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE15  
-[NCC_OCE16](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE16  
-[NCC_OCE17](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE17  
-[NCC_OCE18](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE18  
-[NCC_OCE19](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE19  
-[NCC_OCE20](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE20  
-[NCC_OCE21](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE21  
-[NCC_OCE22](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE22  
-[NCC_OCE23](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE23  
-[NCC_OCE24](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE24  
-[NCC_OCE25](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE25  
-[NCC_OCE26](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2023), 
NCC_OCE26  
-[NCC_EXT2](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
NCC_EXT2  
-[NCC_EXT3](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
NCC_EXT3  
-[NCC_EXT4](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
NCC_EXT4  
-[NCC_EXT5](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
NCC_EXT5  
-[NCC_EXT6](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
NCC_EXT6  
-[NCC_EXT7](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
NCC_EXT7  
-[NCC_EXT9](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
NCC_EXT9  
-[NCC_EXT10](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
NCC_EXT10  
-[NCC_EXT11](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
NCC_EXT11  
-[NCC_EXT12](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
NCC_EXT12  
-[NCC_EXT13](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
NCC_EXT13  
-[NCC_EXT14](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
NCC_EXT14  
-[NCC_EXT15](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
NCC_EXT15  
-[NCC_EXT16](http://cmdp.ncc-cma.net/Monitoring/cn_index_130.php) (1951-2021), 
NCC_EXT16  
-[amoc_mean](http://marine.copernicus.eu) (1993-2019), 
ocean_meridional_overturning_streamfunction  
-[amoc_std](http://marine.copernicus.eu) (1993-2019), 
ocean_meridional_overturning_streamfunction  
-[amoc_cglo](http://marine.copernicus.eu) (1993-2019), 
ocean_meridional_overturning_streamfunction  
-[amoc_glos](http://marine.copernicus.eu) (1993-2019), 
ocean_meridional_overturning_streamfunction  
-[amoc_glor](http://marine.copernicus.eu) (1993-2019), 
ocean_meridional_overturning_streamfunction  
-[amoc_oras](http://marine.copernicus.eu) (1993-2019), 
ocean_meridional_overturning_streamfunction  
-[SAM_Station](https://climatedataguide.ucar.edu/climate-data/marshall-southern-annular-mode-sam-index-station-based) (1957-2024), 
Marshall Southern Annular Mode (SAM) Index (Station-based)  
-[SAM_20CRV3](https://psl.noaa.gov/data/20thC_Rean/timeseries/monthly/SAM/) (1836-2015), 
Southern Annular Mode (SAM) Index (20CRV3-based)  
-[SAM_20crv2c](https://psl.noaa.gov/data/20thC_Rean/timeseries/monthly/SAM/) (1851-2011), 
Southern Annular Mode (SAM) Index (20crv2c-based)  
-[PJ_huang04](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023GL106982) (1940-2023), 
Pacific-Japan teleconnection index defined by Huang04  
-[PJ_noh21](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023GL106982) (1940-2023), 
Pacific-Japan teleconnection index defined by Noh21  
-[PJ_ling22](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023GL106982) (1940-2023), 
Pacific-Japan teleconnection index defined by ling21  
-[SINTEX_ATL3](https://www.jamstec.go.jp/aplinfo/sintexf/e/seasonal/data_download.html) (1982-2024), 
the Atlantic Niño index (ATL3)  
-[SINTEX_CNI](https://www.jamstec.go.jp/aplinfo/sintexf/e/seasonal/data_download.html) (1982-2024), 
the California Niño index (CNI)  
-[SINTEX_DNI](https://www.jamstec.go.jp/aplinfo/sintexf/e/seasonal/data_download.html) (1982-2024), 
the Dakar Ninño index (DNI)  
-[SINTEX_NNI](https://www.jamstec.go.jp/aplinfo/sintexf/e/seasonal/data_download.html) (1982-2024), 
he Ningaloo Niño index (NNI)  
-[SINTEX_SASD](https://www.jamstec.go.jp/aplinfo/sintexf/e/seasonal/data_download.html) (1982-2024), 
the Southern Atlantic Subtropical Dipole index (SASD)  
-[SINTEX_SIOD](https://www.jamstec.go.jp/aplinfo/sintexf/e/seasonal/data_download.html) (1982-2024), 
the Indian Ocean Subtropical Dipole index (SIOD)  
