import React from 'react';

export default class Counter extends React.Component {
    constructor(props) {
        super();
        this.state = {
            count: 0
        }
    }

    onClick(e) {
        if (e === 0 && this.state.count === 0) return;
        if (e === 1 && this.state.count === 9) return;
        this.setState({
            count: e === 1 ? this.state.count + 1: this.state.count - 1
        });
    }

    render() {
        return (
            <div>
                <h1>{this.state.count}</h1>
                <button className="easier" onClick={() => this.onClick(0)}>Easier</button>
                <button className="harder" onClick={() => this.onClick(1)}>Harder</button>
            </div>
        )
    }
}

// React.render(
//     <Counter/>,
//     document.getElementById('app-container')
// );