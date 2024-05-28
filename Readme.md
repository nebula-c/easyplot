# Usage
> ./easyplot.py jsondata/ex.json

## how to write Json
### data
	"data": [
		{
		"xdata": [1, 2, 3, 4, 5],
		"ydata": [2, 3, 5, 7, 11],
		"label": "data1"
		},
		{
		"xdata": [1, 2, 3, 4, 5],
		"ydata": [3, 5, 1, 2, 8],
		"label": "data2"
		},
		{
		"xdata": [1, 2, 3, 4, 5],
		"ydata": [1, 3, 8, 5, 2],
		"label": "data3"
		}
	],

"xdata" and "ydata" shoulde be same size, but each xdata or ydata don't neet to be same size.
Each label could be set using "label" tag.
### Axis label
	"xlabel": "X-axis title",
	"ylabel": "Y-axis title",

### Axis scale
	"xscale": "linear",
	"yscale": "linear",
Scale of each axis could be set. (ex: linear, log, symlog, logit)

### Axis limit
	"xlimit": [0,10],
	"ylimit": [0,100]
Set limit of axis by using min & max.
