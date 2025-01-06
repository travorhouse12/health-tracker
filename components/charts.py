import streamlit as st

def line_chart(data, x_axis, y_axis, series):
    """
    Create a multi-line chart with filled dots. Each series gets
    an automatically assigned color that applies to both the line
    and its dots.
    """
    chart_spec = {
        "mark": {
            "type": "line",
            "interpolate": "monotone",
            "point": {
                "filled": True,   # Ensure dots are filled
                "size": 50
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
                    "tickCount": 6,
                    "values": [0, 20, 40, 60, 80, 100]
                }
            },
            "color": {
                "field": series,      # Assign a color per series
                "type": "nominal"
            }
        }
    }

    st.vega_lite_chart(data, chart_spec, use_container_width=True)