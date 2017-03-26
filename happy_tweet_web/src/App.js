import React, {Component} from 'react';
import logo from './JRBB_logo.png';
import Radar from 'react-chartjs';
import './App.css';

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            chartData: {}
        };

        this.getData = this.getData().bind(this);
    }

    componentDidMount() {
        this.getData();
    }

    getData() {
        let labels = ["anger", "joy", "fear", "sadness", "surprise"];
        let data = [65, 59, 90, 81, 56];
        return {
            'labels': labels,
            'data': [data],
        };
    }

    render() {
        return (
            <div className="App">
                <div className="App-header">
                    <img src={logo} className="App-logo" alt="logo"/>
                    <UsernameBox />
                </div>
                <p className="App-intro">
                    This is the emotion of Boston
                    <Radar data={this.getData()}/>
                </p>
            </div>
        );
    }
}

class Chart extends Component {

}

class UsernameBox extends Component {
    render() {
        return (<div><input></input></div>);
    }
}

export default App;
