"""Render terminal-friendly bar charts from plain numeric series."""

def analyze(text):
    values=[]
    for part in text.replace(',',' ').split():
        try:values.append(float(part))
        except ValueError:continue
    maximum=max([abs(x) for x in values] or [1]) or 1
    bars=['#'*round(25*abs(value)/maximum) for value in values]
    return {'values':values,'bars':bars,'count':len(values)}
