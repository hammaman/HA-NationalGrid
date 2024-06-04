# Code for an Apex-Charts card to show the National Grid carbon intensity forecast

The National Grid Carbon Intensity forecast data is held in the attributes of the carbon_intensity_forecast sensor; and this can be accessed and shown as a chart by adding an Apex-Chart card with the following configuration.


```
type: custom:apexcharts-card
update_delay: 5s
graph_span: 2d
span:
  start: hour
header:
  show: true
  title: National Grid Carbon Intensity Forecast
  show_states: true
  colorize_states: true
series:
  - entity: sensor.national_grid_carbon_intensity_forecast
    type: line
    color: red
    name: Future Carbon Intensity
    data_generator: |
      return entity.attributes.forecast.map((entry) => {
        return [new Date(entry.start_time), entry.carbon_intensity]
        });
```

