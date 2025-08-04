import pandas as pd
import plotly.express as px

def generate_correlation_plot():
    # Sample asset returns
    df = pd.DataFrame({
        'AAPL': [0.01, 0.02, 0.015, -0.005, 0.012],
        'MSFT': [0.008, 0.022, 0.012, -0.003, 0.01],
        'GOOG': [-0.002, 0.005, 0.018, 0.007, 0.009]
    })

    corr = df.corr().round(2)

    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale='RdBu_r',
        title='📈 Asset Return Correlation Matrix'
    )
    fig.update_layout(margin=dict(l=40, r=40, t=40, b=40))

    return fig.to_html(full_html=False)

