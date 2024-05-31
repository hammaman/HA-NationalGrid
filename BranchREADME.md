# Additional README for the branch developed by hammaman

Addition of extra sensor to pick up the projected carbon intensity for the next 24 hours,

using API call: GET /intensity/{from}/fw24h

This returns data for each 1/2 hour in the next 24 hours in JSON format:
- from
- to
- intensity:
  - forecast
  - actual (should be null)
  - index (string, e.g. "low")

Also addition of extra sensor to pick up the projected carbon intensity for the next 48 hours,
using API call: GET /intensity/{from}/fw48h

Current sensor to pick up the historic carbon intensity for the last 24 hours,
using API call: GET /intensity/{from}/pt24h

This has the same JSON format as the 24 hour forecast, but the intensity data is populated for both the forecast and actual.

API calls are handled in the national_grid.py

TO DO: Need to create a new object to hold the data for the following 48 projected values (rather than just returning the latest value)