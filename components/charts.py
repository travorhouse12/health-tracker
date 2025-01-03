import streamlit as st

def area_line_chart(data, x_axis, y_axis, color='#FFDC1E'):
    chart_spec = {
        "mark": {
            "type": "area",
            "interpolate": "monotone",
            "line": {"color": color},
            "color": {
                "gradient": "linear",
                "x1": 1,
                "y1": 1,
                "x2": 1,
                "y2": 0,
                "stops": [
                    {"offset": 0, "color": "#1d1d1d"},
                    {"offset": 1, "color": color}
                ]
            }
        },
        "encoding": {
            "x": {
                "field": x_axis,
                "type": "temporal",
                "axis": {
                    "grid": False,
                    "title": None
                }
            },
            "y": {
                "field": y_axis,
                "type": "quantitative",
                "axis": {
                    "grid": True,
                    "title": None,
                    "tickCount": 6,  # Ensure 6 ticks (e.g., 0, 20, 40, 60, 80, 100)
                    "values": [0, 20, 40, 60, 80, 100]  # Set explicit tick values
                }
            }
        }
    }

    # Display the chart
    st.vega_lite_chart(data, chart_spec, use_container_width=True)