/*!
 * Chart.js
 * http://chartjs.org
 *
 * Copyright 2013 Nick Downie
 * Released under the MIT license
 * https://github.com/nnnick/Chart.js/blob/master/LICENSE.md
 */

var radarOptions = {
    //Boolean - Whether to show lines for each scale point
	scaleShowLine : true,

	//String - Colour of the scale line
	scaleLineColor : "#999",

	//Number - Pixel width of the scale line
	scaleLineWidth : 1,

	//Boolean - Whether to show labels on the scale
	scaleShowLabels : true,

	//Interpolated JS string - can access value
	scaleLabel : "<%=value%>",

	//String - Scale label font declaration for the scale label
	scaleFontFamily : "'Arial'",

	//Number - Scale label font size in pixels
	scaleFontSize : 12,

	//String - Scale label font weight style
	scaleFontStyle : "normal",

	//String - Scale label font colour
	scaleFontColor : "#666",

	//Boolean - Show a backdrop to the scale label
	scaleShowLabelBackdrop : true,

	//String - The colour of the label backdrop
	scaleBackdropColor : "rgba(0,200,255,0.75)",

	//Number - The backdrop padding above & below the label in pixels
	scaleBackdropPaddingY : 1,

	//Number - The backdrop padding to the side of the label in pixels
    scaleBackdropPaddingX : 1,

	//Boolean - Whether we show the angle lines out of the radar
	angleShowLineOut : true,

	//String - Colour of the angle line
	angleLineColor : "rgba(255,255,255,0.3)",

	//Number - Pixel width of the angle line
	angleLineWidth : 1,

	//String - Point label font declaration
	pointLabelFontFamily : "'Arial'",

	//String - Point label font weight
	pointLabelFontStyle : "normal",

	//Number - Point label font size in pixels
	pointLabelFontSize : 12,

	//String - Point label font colour
	pointLabelFontColor : "#EFEFEF",

	//Boolean - Whether to show a dot for each point
	pointDot : true,

	//Number - Radius of each point dot in pixels
	pointDotRadius : 3,

	//Number - Pixel width of point dot stroke
	pointDotStrokeWidth : 1,

	//Boolean - Whether to show a stroke for datasets
	datasetStroke : true,

	//Number - Pixel width of dataset stroke
	datasetStrokeWidth : 1,

	//Boolean - Whether to fill the dataset with a colour
	datasetFill : true,

	//Boolean - Whether to animate the chart
	animation : true,

	//Number - Number of animation steps
	animationSteps : 200,

	//String - Animation easing effect
	animationEasing : "easeOutQuart",

	//Function - Fires when the animation is complete
	onAnimationComplete : null

}
// Radar Data



var data = {
  labels: ['12/12/2013','13/12/2013','14/12/2013','14/12/2013','15/12/2013','16/12/2013','17/12/2013'],
   datasets: [
     { data: [100,210,220,300,200,190,192], fillColor: 'rgba(31,200,248,0.1)', strokeColor: '#1fc8f8', pointColor: '#1fc8f8', pointStrokeColor: '#1fc8f8' },
     { data: [130,200,190,150,140,210,0], fillColor: 'rgba(118,163,70,0.1)', strokeColor: '#76a346', pointColor: '#76a346', pointStrokeColor: '#76a346' },
     { data: [130,200,190,150,140,210,0], fillColor: 'rgba(118,163,70,0.1)', strokeColor: '#76a346', pointColor: '#76a346', pointStrokeColor: '#76a346' },
     { data: [130,200,190,150,140,210,0], fillColor: 'rgba(118,163,70,0.1)', strokeColor: '#76a346', pointColor: '#76a346', pointStrokeColor: '#76a346' },
     { data: [130,200,190,150,140,210,0], fillColor: 'rgba(118,163,70,0.1)', strokeColor: '#76a346', pointColor: '#76a346', pointStrokeColor: '#76a346' }

    ]
};

var line = document.getElementById('line');
var lineCtx = line.getContext('2d');
var chart1 = new Chart(lineCtx).Line(data);

