import pandas as pd
import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os
import argparse
import numpy as np


# To use as command line argument python skillsprogression.py -i <pathToFile>
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
args = vars(ap.parse_args())
df = pd.read_csv(args["image"],sep=',',index_col=[0],parse_dates=[0])
df = df.sort_values(by="Date")
#print(df)

# To use as within python 
#df = pd.read_csv("C:\\Users\\Ryan\\OneDrive\\Documents\\DSDSTUDENTS\\PMDATA\\AbacusSkillsProgression.csv",sep=',',index_col=[0],parse_dates=[0])
#df = df.sort_values(by="Date")
#print(df)

# Generate Jitter in Dataframe columns since all data are 0,1,2, or 3
mu, sigma = 0, 0.1 
noise = np.random.normal(mu, sigma, [len(df.index),len(df.columns)])
df_noisy=df + noise
#print(df_noisy) #df_noisy is used for all plotting. Replace df_noisy with df in all fig.add_trace below for unadjusted raw data

###################
# Line Plots
###################

fig = make_subplots(
    rows=4, cols=2,
    subplot_titles=("Phase 1: Foundation", "Phase 2: Addition", "Phase 3: Subtraction", "Phase 4: Multiplication", "Phase 5: Division", "Phase 6: Decimals", "Phase 7: Fractions", "Phase 8: Special Functions"),
    #print_grid=True
    )

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.1"], mode="lines+markers", name="Setting Numbers",legendgroup="Phase 1", legendgrouptitle_text="Phase 1"), row=1, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.2"], mode="lines+markers", name="Clearing Beads",legendgroup="Phase 1", legendgrouptitle_text="Phase 1"), row=1, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.3"], mode="lines+markers", name="Place Value",legendgroup="Phase 1", legendgrouptitle_text="Phase 1"), row=1, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.4"], mode="lines+markers", name="Vocabulary",legendgroup="Phase 1", legendgrouptitle_text="Phase 1"), row=1, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.1"], mode="lines+markers", name="Setting Numbers",legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.2"], mode="lines+markers", name="Clearing Beads",legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.3"], mode="lines+markers", name="Place Value",legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.1"], mode="lines+markers", name="Setting Numbers",legendgroup="Phase 3", legendgrouptitle_text="Phase 3"), row=2, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.2"], mode="lines+markers", name="Clearing Beads",legendgroup="Phase 3", legendgrouptitle_text="Phase 3"), row=2, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.3"], mode="lines+markers", name="Place Value",legendgroup="Phase 3", legendgrouptitle_text="Phase 3"), row=2, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.1"], mode="lines+markers", name="Setting Numbers",legendgroup="Phase 4", legendgrouptitle_text="Phase 4"), row=2, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.2"], mode="lines+markers", name="Clearing Beads",legendgroup="Phase 4", legendgrouptitle_text="Phase 4"), row=2, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P5.1"], mode="lines+markers", name="Place Value",legendgroup="Phase 5", legendgrouptitle_text="Phase 5"), row=3, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P5.2"], mode="lines+markers", name="Vocabulary",legendgroup="Phase 5", legendgrouptitle_text="Phase 5"), row=3, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P6.1"], mode="lines+markers", name="Setting Numbers",legendgroup="Phase 6", legendgrouptitle_text="Phase 6"), row=3, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P6.2"], mode="lines+markers", name="Clearing Beads",legendgroup="Phase 6", legendgrouptitle_text="Phase 6"), row=3, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P6.3"], mode="lines+markers", name="Place Value",legendgroup="Phase 6", legendgrouptitle_text="Phase 6"), row=3, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P6.4"], mode="lines+markers", name="Vocabulary",legendgroup="Phase 6", legendgrouptitle_text="Phase 6"), row=3, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P7.1"], mode="lines+markers", name="Setting Numbers",legendgroup="Phase 7", legendgrouptitle_text="Phase 7"), row=4, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P7.2"], mode="lines+markers", name="Clearing Beads",legendgroup="Phase 7", legendgrouptitle_text="Phase 7"), row=4, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P7.3"], mode="lines+markers", name="Place Value",legendgroup="Phase 7", legendgrouptitle_text="Phase 7"), row=4, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P7.4"], mode="lines+markers", name="Vocabulary",legendgroup="Phase 7", legendgrouptitle_text="Phase 7"), row=4, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P8.1"], mode="lines+markers", name="Setting Numbers",legendgroup="Phase 8", legendgrouptitle_text="Phase 8"), row=4, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P8.2"], mode="lines+markers", name="Clearing Beads",legendgroup="Phase 8", legendgrouptitle_text="Phase 8"), row=4, col=2)

fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=1, col=1)

fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=1, col=2)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=1, col=2)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=1, col=2)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=1, col=2)

fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=2, col=1)

fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=2, col=2)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=2, col=2)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=2, col=2)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=2, col=2)

fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=3, col=1)

fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3, col=2)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=3, col=2)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=3, col=2)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=3, col=2)

fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=4, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=4, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=4, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=4, col=1)

fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=4, col=2)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=4, col=2)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=4, col=2)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=4, col=2)


fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])], row=1, col=1)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=1, col=2)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=2, col=1)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=2, col=2)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=3, col=1)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=3, col=2)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=4, col=1)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=4, col=2)

fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=1, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=1, col=2)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=2, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=2, col=2)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=3, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=3, col=2)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=4, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=4, col=2)

fig.update_layout(template="simple_white", title_text="Abacus Skills Progression")

fig.write_html("C:\\Users\\Ryan\\OneDrive\\Documents\\DSDSTUDENTS\\PMPLOTS\\AbacusSkillsProgression.html")

#fig.show()


