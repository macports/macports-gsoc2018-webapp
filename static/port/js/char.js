window.onload = function () {
	    var chart = new CanvasJS.Chart("chartContainer",
	    {

	      title:{
	      text: "Installations"
	      },
	      axisX: {
	        title:"Months",
	        valueFormatString: "MMM",
	        interval:1,
	        intervalType: "month"
	      },
	      axisY:{ title:"Number of Installations",
	        includeZero: false

	      },
	      data: [
	      {
	        type: "line",

	        dataPoints: [
	        { x: new Date(2012, 00, 1), y: 450 },
	        { x: new Date(2012, 01, 1), y: 414},
	          { x: new Date(2012, 02, 1), y: 520},
	        { x: new Date(2012, 03, 1), y: 460 },
	        { x: new Date(2012, 04, 1), y: 450 },
	        { x: new Date(2012, 05, 1), y: 500 },
	        { x: new Date(2012, 06, 1), y: 480 },
	        { x: new Date(2012, 07, 1), y: 480 },
	        { x: new Date(2012, 08, 1), y: 410 },
	        { x: new Date(2012, 09, 1), y: 500 },
	        { x: new Date(2012, 10, 1), y: 480 },
	        { x: new Date(2012, 11, 1), y: 510 }
	        ]
	      }
	      ]
	    });

	    chart.render();
	  }