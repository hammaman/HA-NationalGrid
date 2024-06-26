from datetime import datetime
from typing import TypedDict


class NationalGridGeneration(TypedDict):
    gas_mwh: int  # ccgt + ocgt
    oil_mwh: int  # oil
    coal_mwh: int  # coal
    biomass_mwh: int  # biomass
    nuclear_mwh: int  # nuclear
    wind_mwh: int  # wind
    solar_mwh: int  # solar
    national_wind_mwh: int  # wind plugged into national transmission network
    embedded_wind_mwh: int  # wind plugged into local distribution networks
    pumped_storage_mwh: int  # ps - pumped storage
    hydro_mwh: int  # npshyd - non pumped storage hydro plant
    other_mwh: int  # other - undefined
    france_mwh: int  # intfr ( IFA ) + intelec ( ElecLink ) + intifa2 ( IFA2 )
    ireland_mwh: int  # intirl ( Moyle ) + intew ( East-West )
    netherlands_mwh: int  # intned ( Brit Ned )
    belgium_mwh: int  # intnem ( Nemo )
    norway_mwh: int  # intnsl ( North Sea Link )
    denmark_mw: int  # intvkl (Viking Link)
    total_generation_mwh: int  # total generation
    fossil_fuel_percentage_generation: int  # Counts gas, oil, coal
    renewable_percentage_generation: int  # Counts solar, wind, hydro
    low_carbon_percentage_generation: int  # Counts renewable, nuclear
    low_carbon_with_biomass_percentage_generation: int  # Counts renewable, nuclear, biomass
    other_percentage_generation: int  # Counts nuclear, biomass
    grid_collection_time: datetime


class NationalGridWindData(TypedDict):
    today_peak: float
    tomorrow_peak: float
    today_peak_time: datetime
    tomorrow_peak_time: datetime


class NationalGridWindForecastItem(TypedDict):
    start_time: datetime
    generation: int


class NationalGridWindForecast(TypedDict):
    current_value: int
    forecast: list[NationalGridWindForecastItem]


class NationalGridWindForecastLongTerm(TypedDict):
    forecast: list[NationalGridWindForecastItem]


class NationalGridSolarForecastItem(TypedDict):
    start_time: datetime
    generation: int


class NationalGridSolarForecast(TypedDict):
    current_value: int
    forecast: list[NationalGridSolarForecastItem]


class NationalGridDemandDayAheadForecastItem(TypedDict):
    start_time: datetime
    transmission_demand: int
    national_demand: int


class NationalGridDemandDayAheadForecast(TypedDict):
    current_value: int
    forecast: list[NationalGridDemandDayAheadForecastItem]


class NationalGridDemandForecastItem(TypedDict):
    start_time: datetime
    national_demand: int


class NationalGridDemandForecast(TypedDict):
    current_value: int
    forecast: list[NationalGridDemandForecastItem]

# New classes for Carbon Intensity Forecast
class NationalGridCarbonIntensityForecastItem(TypedDict):
    start_time: datetime
    carbon_intensity: int

class NationalGridCarbonIntensityForecast(TypedDict):
    current_value: int
    forecast: list[NationalGridCarbonIntensityForecastItem]

# End of new classes

class DFSRequirementItem(TypedDict):
    start_time: datetime
    end_time: datetime
    required_mw: int
    requirement_type: str
    despatch_type: str
    participants_eligible: list[str]


class DFSRequirements(TypedDict):
    requirements: list[DFSRequirementItem]


class NationalGridData(TypedDict):
    sell_price: float
    carbon_intensity: int
    # Added
    carbon_intensity_forecast: NationalGridCarbonIntensityForecast

    grid_frequency: float

    wind_data: NationalGridWindData
    wind_forecast: NationalGridWindForecast
    wind_forecast_earliest: NationalGridWindForecast

    now_to_three_wind_forecast: NationalGridWindForecastLongTerm
    fourteen_wind_forecast: NationalGridWindForecastLongTerm
    long_term_wind_forecast: tuple[
        NationalGridWindForecastLongTerm,
        NationalGridWindForecastLongTerm,
    ]

    solar_forecast: NationalGridSolarForecast

    three_embedded_solar: NationalGridSolarForecast
    fourteen_embedded_solar: NationalGridSolarForecast

    three_embedded_wind: NationalGridWindForecast
    fourteen_embedded_wind: NationalGridWindForecast

    long_term_embedded_wind_and_solar_forecast: tuple[
        NationalGridSolarForecast,
        NationalGridSolarForecast,
        NationalGridWindForecast,
        NationalGridWindForecast,
    ]

    grid_generation: NationalGridGeneration

    grid_demand_day_ahead_forecast: NationalGridDemandDayAheadForecast

    grid_demand_three_day_forecast: NationalGridDemandForecast
    grid_demand_fourteen_day_forecast: NationalGridDemandForecast
    three_day_demand_and_fourteen_day_demand: tuple[
        NationalGridDemandForecast,
        NationalGridDemandForecast,
    ]

    total_demand_mwh: int
    total_transfers_mwh: int

    dfs_requirements: DFSRequirements
