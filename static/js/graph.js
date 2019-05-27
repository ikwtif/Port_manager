  
$(document).ready(function() {
	$(chart_id1).highcharts({
		chart: chart1,
		title: title1,
		series: series1,
		tooltip: tooltip1,
		plotOptions: plotOptions1
	});
});

$(document).ready(function() {
	$(chart_id2).highcharts({
		chart: chart2,
		title: title2,
		series: series2,
		tooltip: tooltip2,
		plotOptions: plotOptions2
	});
});