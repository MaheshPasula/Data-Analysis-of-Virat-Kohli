import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("virat_data.csv")
print(data.head())

print(data.isnull().sum())

def get_runs_scored_chart(data):
    matches = data.index
    figure = px.line(data, x=matches, y="Runs", 
                    title='Runs Scored by Virat Kohli Between 18-Aug-08 - 22-Jan-17')
    return (figure.show())

def get_batting_chart(data):
    # Batting Positions
    data["Pos"] = data["Pos"].map({3.0: "Batting At 3", 4.0: "Batting At 4", 2.0: "Batting At 2", 
                                1.0: "Batting At 1", 7.0:"Batting At 7", 5.0:"Batting At 5", 
                                6.0: "batting At 6"})

    Pos = data["Pos"].value_counts()
    label = Pos.index
    counts = Pos.values
    colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]



    fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
    fig.update_layout(title_text='Number of Matches At Different Batting Positions')
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                    marker=dict(colors=colors, line=dict(color='black', width=3)))
    return fig.show()


def get_batting_at_different_chart(data):
    label = data["Pos"]
    counts = data["Runs"]
    colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

    fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
    fig.update_layout(title_text='Runs By Virat Kohli At Different Batting Positions')
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                    marker=dict(colors=colors, line=dict(color='black', width=3)))
    return fig.show()


def get_centuries_chart(data):
    centuries = data.query("Runs >= 100")
    figure = px.bar(centuries, x=centuries["Inns"], y = centuries["Runs"], 
                    color = centuries["Runs"],
                    title="Centuries By Virat Kohli in First Innings Vs. Second Innings")
    return figure.show()


def get_dismissals_chart(data):
    # Dismissals of Virat Kohli
    dismissal = data["Dismissal"].value_counts()
    label = dismissal.index
    counts = dismissal.values
    colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]



    fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
    fig.update_layout(title_text='Dismissals of Virat Kohli')
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                    marker=dict(colors=colors, line=dict(color='black', width=3)))
    return fig.show()


def get_each_opp_runs_chart(data):
    figure = px.bar(data, x=data["Opposition"], y = data["Runs"], color = data["Runs"],
                title="Most Runs Against Teams")
    return figure.show()

def get_each_centuries_runs_chart(data):
    centuries = data.query("Runs >= 100")
    figure = px.bar(centuries, x=centuries["Opposition"], y = centuries["Runs"], 
                    color = centuries["Runs"],
                    title="Most Centuries Against Teams")
    return figure.show()


def get_high_strike_1st_2nd_inngs_chart(data):
    strike_rate = data.query("SR >= 120")
    figure = px.bar(strike_rate, x = strike_rate["Inns"], 
                    y = strike_rate["SR"], 
                    color = strike_rate["SR"],
                title="Virat Kohli's High Strike Rates in First Innings Vs. Second Innings")
    return figure.show()


def get_all_charts(data):
    res = list()
    res1 = get_batting_chart(data)
    res.append(res1)
    res2 = get_batting_at_different_chart(data)
    res.append(res2)
    res3 = get_centuries_chart(data)
    res.append(res3)
    res4 = get_dismissals_chart(data)
    res.append(res4)
    res5 = get_each_centuries_runs_chart(data)
    res.append(res5)
    res6 = get_each_opp_runs_chart(data)
    res.append(res6)
    res7 = get_runs_scored_chart(data)
    res.append(res7)
    res8 = get_high_strike_1st_2nd_inngs_chart(data)
    res.append(res8)


    return res

(get_all_charts(data))