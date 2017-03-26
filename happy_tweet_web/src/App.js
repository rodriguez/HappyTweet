import React, {Component} from 'react';
import logo from './JRBB_logo.png';
import {Radar} from 'react-chartjs';
import Chart from 'chart.js';
var request = require('request');
import 'isomorphic-fetch';
import 'es6-promise';
import './App.css';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import TextField from 'material-ui/TextField';
import {Router, Route, Link, IndexRoute, hashHistory, browserHistory} from 'react-router';

class A extends Component {
    render() {
        return (
            <Router history={hashHistory}>
                <div>
                    <Route path='/' component={App}/>
                    <Route path='/address' component={Address}/>
                </div>
            </Router>
        )
    }
}

const Address = () => <h1>We are located at 555 Jackson St.</h1>

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            'chartData': {
                'labels': ["anger", "joy", "fear", "sadness", "surprise"],
                'datasets': [
                    {
                        data: [65, 59, 90, 81, 56]
                    }
                ]
            },
            'chartOptions': {
                //Boolean - Whether to show lines for each scale point
                scaleShowLine: true,

                //String - Colour of the scale line
                scaleLineColor: "#000000",

                //Number - Pixel width of the scale line
                scaleLineWidth: 1,

                //Boolean - Whether to show labels on the scale
                scaleShowLabels: true,

                //Interpolated JS string - can access value
                scaleLabel: "<%=value%>",

                //String - Scale label font declaration for the scale label
                scaleFontFamily: "'Arial'",

                //Number - Scale label font size in pixels
                scaleFontSize: 12,

                //String - Scale label font weight style
                scaleFontStyle: "normal",

                //String - Scale label font colour
                scaleFontColor: "#000000",

                //Boolean - Show a backdrop to the scale label
                scaleShowLabelBackdrop: true,

                //String - The colour of the label backdrop
                scaleBackdropColor: "#afeeee",

                //Number - The backdrop padding above & below the label in pixels
                scaleBackdropPaddingY: 1,

                //Number - The backdrop padding to the side of the label in pixels
                scaleBackdropPaddingX: 1,

                //Boolean - Whether we show the angle lines out of the radar
                angleShowLineOut: true,

                //String - Colour of the angle line
                angleLineColor: "rgba(255,255,255,0.3)",

                //Number - Pixel width of the angle line
                angleLineWidth: 1,

                //String - Point label font declaration
                pointLabelFontFamily: "'Arial'",

                //String - Point label font weight
                pointLabelFontStyle: "normal",

                //Number - Point label font size in pixels
                pointLabelFontSize: 30,

                //String - Point label font colour
                pointLabelFontColor: "#30449a",


                //Boolean - Whether to show a dot for each point
                pointDot: true,

                //Number - Radius of each point dot in pixels
                pointDotRadius: 3,

                //Number - Pixel width of point dot stroke
                pointDotStrokeWidth: 1,

                //Boolean - Whether to show a stroke for datasets
                datasetStroke: true,

                //Number - Pixel width of dataset stroke
                datasetStrokeWidth: 1,

                //Boolean - Whether to fill the dataset with a colour
                datasetFill: true,

                //Boolean - Whether to animate the chart
                animation: true,

                //Number - Number of animation steps
                animationSteps: 200,

                //String - Animation easing effect
                animationEasing: "easeOutQuart",

                //Function - Fires when the animation is complete
                onAnimationComplete: null

            },
            'username': 'Boston',
        };
        this.loadData = this.loadData.bind(this);
        this.setData = this.setData.bind(this);
        this.changeSubject = this.changeSubject.bind(this);
    }

    loadData() {
        let labels = ["anger", "joy", "fear", "sadness", "surprise"];
        let options = {
            url: 'http://localhost:5000/region/average/boston',
            method: 'GET',
        };
        request(options, function (error, resp, body) {
            if (!error && resp.statusCode == 200) {
                console.log(body);
                let jsonData = JSON.parse(body);
                this.setData({
                    'chartData': {
                        'labels': labels,
                        'datasets': [
                            {
                                data: [7, 7, 7, 7, 7],
                            }
                        ]
                    }
                });
            }
            else
                console.log(error);
        });

    }

    setData(json) {
        let jsonData = json;
        console.log(jsonData);
    }

    componentDidMount() {
        // this.loadData();
        fetch("http://localhost:5000/region/average/boston")
            .then(resp => resp.json())
            .then(json => {
                let r = json;
                this.setState({
                    "chartData": {
                        "labels": ["anger", "joy", "fear", "sadness", "surprise"],
                        "datasets": [
                            {
                                'data': [r['anger'], r['joy'], r['fear'], r['sadness'], r['surprise']]
                            }
                        ]
                    }
                });
            });
    }

    changeSubject(username) {
        this.setState({
            'username': username,
        });
        fetch("http://localhost:5000/analyze/average/" + username)
            .then(resp => resp.json())
            .then(json => {
                let r = json;
                this.setState({
                    "chartData": {
                        "labels": ["anger", "joy", "fear", "sadness", "surprise"],
                        "datasets": [
                            {
                                'data': [r['anger'], r['joy'], r['fear'], r['sadness'], r['surprise']]
                            }
                        ]
                    }
                });
            });
    }

    render() {
        return (
            <div className="App">
                <div className="App-header">
                    <img src={logo} className="App-logo" alt="logo"/>
                    <UsernameBox changeSubject={this.changeSubject}/>
                </div>
                <p className="App-intro">
                    <h2>This is the emotion of {this.state.username}</h2>
                    <div className="chart">
                        <Radar data={this.state.chartData} options={this.state.chartOptions} width="666px"
                               height="666px"/>
                    </div>
                </p>
            </div>
        );
    }
}

class UsernameBox extends Component {
    constructor(props) {
        super(props);
        this.state = {
            "username": "",
        };
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
        event.preventDefault();
        this.props.changeSubject(this.state.username);
    }

    handleInputChange(event) {
        this.setState({
            "username": event.target.value,
        });
    }

    render() {
        return (<div className="username-box">
            <form onSubmit={this.handleSubmit} style={{flex: 1}}>
                <MuiThemeProvider>
                    <TextField placeholder="@" value={this.state.username} onChange={this.handleInputChange}/>
                </MuiThemeProvider></form>
        </div>);
    }
}

export default App;
