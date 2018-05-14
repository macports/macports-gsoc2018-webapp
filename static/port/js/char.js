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
	    var chart1 = new CanvasJS.Chart("chartContainer1",
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
	        { x: new Date(2012, 00, 1), y: 200 },
	        { x: new Date(2012, 01, 1), y: 41},
	        { x: new Date(2012, 02, 1), y: 20},
	        { x: new Date(2012, 03, 1), y: 460 },
	        { x: new Date(2012, 04, 1), y: 450 },
	        { x: new Date(2012, 05, 1), y: 100 },
	        { x: new Date(2012, 06, 1), y: 680 },
	        { x: new Date(2012, 07, 1), y: 980 },
	        { x: new Date(2012, 08, 1), y: 210 },
	        { x: new Date(2012, 09, 1), y: 580 },
	        { x: new Date(2012, 10, 1), y: 120 },
	        { x: new Date(2012, 11, 1), y: 410 }
	        ]
	      }
	      ]
	    });

	    chart1.render();

	    var chart2 = new CanvasJS.Chart("chartContainer2",
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
	        { x: new Date(2012, 00, 1), y: 23 },
	        { x: new Date(2012, 01, 1), y: 41},
	          { x: new Date(2012, 02, 1), y: 52},
	        { x: new Date(2012, 03, 1), y: 46 },
	        { x: new Date(2012, 04, 1), y: 45 },
	        { x: new Date(2012, 05, 1), y: 50 },
	        { x: new Date(2012, 06, 1), y: 480 },
	        { x: new Date(2012, 07, 1), y: 280 },
	        { x: new Date(2012, 08, 1), y: 310 },
	        { x: new Date(2012, 09, 1), y: 800 },
	        { x: new Date(2012, 10, 1), y: 480 },
	        { x: new Date(2012, 11, 1), y: 510 }
	        ]
	      }
	      ]
	    });

	    chart2.render();

	  }


