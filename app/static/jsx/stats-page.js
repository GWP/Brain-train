import React from 'react';

function ProblemButton(props) {
    return (
        <button className={(props.clicked === 1 ? "clicked_btn" : "unclicked")} onClick={props.onClick}>
            {props.pt}
        </button>
    );
}

export default class StatsPageButtonSet extends React.Component {
    constructor(props) {
        super();
        this.state = {
            chosenPtype: null,
            chosenQtype: null,
            stats: null,
        };
    }

    onProblemClick(problemOrQuery, value) {
        if (problemOrQuery === 'problem') {
            this.setState({
                chosenPtype: this.state.chosenPtype === value ? null: value,
            });
        } else {
            this.setState({
                chosenQtype: this.state.chosenQtype === value ? null: value,
            });
        }
    }

    renderStatButton(ptype) {
        return <ProblemButton
                    clicked={(this.state.chosenPtype === ptype ? 1 : 0)}
                    pt={ptype}
                    onClick={() => this.onProblemClick('problem', ptype)}
                    />;
    }

    renderQueryButton(qtype) {
        return <ProblemButton
                    clicked={(this.state.chosenQtype === qtype ? 1 : 0)}
                    pt={qtype}
                    onClick={() => this.onProblemClick('query', qtype)}
                    />;
    }

    onCalcStatsClick() {
        const statQueryFrom = new FormData();
        statQueryFrom.append('query_type', this.state.chosenQtype);
        statQueryFrom.append('problem_type', this.state.chosenPtype);

        fetch('/userstats', {
            credentials: 'same-origin',
            method: 'POST',
            body: statQueryFrom,
        })
        .then((response) => {
            console.log('response: ', response.body);
            const parsed = response.text();
            return parsed;
        })
        .then((responseText) => {
            console.log('supposedly succeeded with: ', responseText);
            this.setState({
                stats: responseText,
            });
        })
    }

    render() {
        return (
            <div className="whetstone_body">
                <p>What problem type do you want statistics for?</p>
                <div className="problem_types">
                    <div className="stat_button">
                        {this.renderStatButton('Addition')}
                    </div>
                    <div className="stat_button">
                        {this.renderStatButton('Subtraction')}
                    </div>
                    <div className="stat_button">
                        {this.renderStatButton('Multiplication')}
                    </div>
                    <div className="stat_button">
                        {this.renderStatButton('Division')}
                    </div>
                    <div className="stat_button">
                        {this.renderStatButton('Hexadecimal')}
                    </div>
                </div>
                <br/>
                <p>What type of statistic do you want?</p>
                <div className="query_types">
                    <div className="query_type">
                        {this.renderQueryButton('Average')}
                    </div>
                    <div className="query_type">
                        {this.renderQueryButton('Quickest')}
                    </div>
                </div>
                <br/>
                <div className="generate_problems">
                    <button id="gen_prob" onClick={() => this.onCalcStatsClick()}>Find it for me!</button>
                </div>
                <div className="stats_window">
                    {this.state.stats}
                </div>
            </div>
        )
    }
}