  
$(document).ready(function() {
	$(chart_id).highcharts({
		chart: chart,
		title: title,
		series: series,
		tooltip: tooltip,
		plotOptions: plotOptions
	});
});