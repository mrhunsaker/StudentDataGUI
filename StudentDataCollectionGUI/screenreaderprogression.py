import pandas as pd
import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os
import argparse
import numpy as np
import kaleido

# To use as command line argument python skillsprogression.py -i <pathToFile>
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
args = vars(ap.parse_args())
df = pd.read_csv(args["image"],sep=',',index_col=[0],parse_dates=[0])
df = df.sort_values(by="Date")
#print(df)

# To use as within python 
#df = pd.read_csv("C:\\Users\\Ryan\\OneDrive\\Documents\\DSDSTUDENTS\\PMDATA\\ScreenreaderSkillsProgression.csv",sep=',',index_col=[0],parse_dates=[0])
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
    rows=5, cols=2,
    specs=[[{}, {"rowspan": 2}],
           [{}, None],
           [{"rowspan": 2},{}],
           [None,{}],
           [{}, {}]],
    subplot_titles=("Phase 1a: Reading", "Phase 2: Writing", "Phase 1b: Reading", "Phase 3a: Internet", "Phase 3b: Internet", "Phase 3c: Internet", "Phase 4a: File Management", "Phase 4b: File Management"),
    #print_grid=True
    )

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.1"], mode="lines+markers", name="Turn ON/OFF",legendgroup="Phase 1a", legendgrouptitle_text="Phase 1a"), row=1, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.2"], mode="lines+markers", name="Use Modifier Keys",legendgroup="Phase 1a", legendgrouptitle_text="Phase 1a"), row=1, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.3"], mode="lines+markers", name="Use Reading Commands",legendgroup="Phase 1a", legendgrouptitle_text="Phase 1a"), row=1, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.4"], mode="lines+markers", name="ID Titles",legendgroup="Phase 1b", legendgrouptitle_text=" "), row=2, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.5"], mode="lines+markers", name="Access Documents",legendgroup="Phase 1b", legendgrouptitle_text=" "), row=2, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P1.6"], mode="lines+markers", name="Switch Program Focus",legendgroup="Phase 1b", legendgrouptitle_text=" "), row=2, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.1"], mode="lines+markers", name="Type with all keys",legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.2"], mode="lines+markers", name="Change Screen Reader Settings",legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.3"], mode="lines+markers", name="Write documents",legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P2.4"], mode="lines+markers", name="Copy/Paste Text",legendgroup="Phase 2", legendgrouptitle_text="Phase 2"), row=1, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.4"], mode="lines+markers", name="TAB Navigation",legendgroup="Phase 3a", legendgrouptitle_text="Phase 3a"), row=3, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.5"], mode="lines+markers", name="Quick Key Navigation",legendgroup="Phase 3a", legendgrouptitle_text="Phase 3a"), row=3, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.6"], mode="lines+markers", name="Elements List Navigation",legendgroup="Phase 3a", legendgrouptitle_text="Phase 3a"), row=3, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.7"], mode="lines+markers", name="Justify Navigation Method",legendgroup="Phase 3a", legendgrouptitle_text="Phase 3a"), row=3, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.1"], mode="lines+markers", name="Define HTML Elements",legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.2"], mode="lines+markers", name="ID HTML Elements",legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.3"], mode="lines+markers", name="Navigate to Address Bar",legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.8"], mode="lines+markers", name="ALT-TAB Focus",legendgroup="Phase 3b", legendgrouptitle_text="Phase 3b"), row=3, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.9"], mode="lines+markers", name="Toggle Screen Reader Mode",legendgroup="Phase 3c", legendgrouptitle_text="Phase 3c"), row=4, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.10"], mode="lines+markers", name="Navigate a Table",legendgroup="Phase 3c", legendgrouptitle_text="Phase 3c"), row=4, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P3.11"], mode="lines+markers", name="Navigation Sequence",legendgroup="Phase 3c", legendgrouptitle_text="Phase 3c"), row=4, col=2)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.1"], mode="lines+markers", name="Save and Open Files",legendgroup="Phase 4a", legendgrouptitle_text="Phase 4a"), row=5, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.2"], mode="lines+markers", name="Create Folders",legendgroup="Phase 4a", legendgrouptitle_text="Phase 4a"), row=5, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.3"], mode="lines+markers", name="Navigate Cloud Storage",legendgroup="Phase 4a", legendgrouptitle_text="Phase 4a"), row=5, col=1)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.4"], mode="lines+markers", name="Download from Internet",legendgroup="Phase 4a", legendgrouptitle_text="Phase 4a"), row=5, col=1)

fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.5"], mode="lines+markers", name="UNZIP Folders",legendgroup="Phase 4b", legendgrouptitle_text="Phase 4b"), row=5, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.6"], mode="lines+markers", name="Use Virtual Cursor",legendgroup="Phase 4b", legendgrouptitle_text="Phase 4b"), row=5, col=2)
fig.add_trace(go.Scatter(x=df_noisy.index,y=df_noisy["P4.7"], mode="lines+markers", name="Use Built-In OCR",legendgroup="Phase 4b", legendgrouptitle_text="Phase 4b"), row=5, col=2)

fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=1, col=1)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=2, col=1)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=1, col=2)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=1, col=2)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=1, col=2)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=1, col=2)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=3, col=1)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=3, col=2)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=3, col=2)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=3, col=2)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=3, col=2)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=4, col=2)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=4, col=2)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=4, col=2)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=4, col=2)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=5, col=1)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=5, col=1)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=5, col=1)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=5, col=1)
fig.add_hrect(y0=-.5, y1=.5, line_width=0, fillcolor="red", opacity=0.2, row=5, col=2)
fig.add_hrect(y0=.5, y1=1.5, line_width=0, fillcolor="orange", opacity=0.2, row=5, col=2)
fig.add_hrect(y0=1.5, y1=2.5, line_width=0, fillcolor="yellow", opacity=0.2, row=5, col=2)
fig.add_hrect(y0=2.5, y1=3.5, line_width=0, fillcolor="green", opacity=0.2, row=5, col=2)


fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])], row=1, col=1)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=1, col=2)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=2, col=1)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=3, col=1)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=3, col=1)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=3, col=2)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=4, col=2)
fig.update_xaxes(rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=5, col=1)
fig.update_xaxes( rangebreaks=[dict(values=["2021-12-16","2021-12-17","2021-12-18" ,"2021-12-19","2021-12-20","2021-12-21","2021-12-22","2021-12-23","2021-12-24","2021-12-25","2021-12-26","2021-12-27","2021-12-28","2021-12-29","2021-12-30","2021-12-31","2022-01-01","2022-01-02"])],row=5, col=2)

fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=1, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=2, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=1, col=2)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=3, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=3, col=2)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=4, col=2)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=5, col=1)
fig.update_yaxes(range=[-.5,3.5], fixedrange=True, ticktext=["Unable","Prompted","Hesitated","Independent"], tickvals=[0.1,1,2,3], row=5, col=2)

fig.update_layout(template="simple_white", title_text="Screen Reader Skills Progression")

fig.write_html("C:\\Users\\Ryan\\OneDrive\\Documents\\DSDSTUDENTS\\PMPLOTS\\ScreenReaderSkillsProgression.html")

#fig.show()

