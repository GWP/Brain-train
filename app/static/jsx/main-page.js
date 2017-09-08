import React from 'react';
import Counter from './counter';
import _ from 'lodash';

function ProblemButton(props) {
        return (
            <button className={(props.clicked === 1 ? "clicked_btn" : "unclicked")} onClick={props.onClick}>
                {props.pt}
            </button>
        );
    }

export default class MainPageButtonSet extends React.Component {
    constructor(props) {
        super();
        this.state = {
            problems: [],
            difficulties: {
                Addition: 0,
                Subtraction: 0,
                Multiplication: 0,
                Division: 0,
                Hexadecimal: 0,
            },
            onGenProbClick: props.onGenProbClick,
            onGetStatsClick: props.onGetStatsClick,
        }
    }

    onEnterPress(e) {
        if (e.key === 'Enter') {
            return this.onGenProbClick();
        }
    }


    renderButtons(ptype) {
        return <ProblemButton
                    clicked={(_.includes(this.state.problems, ptype) ? 1 : 0)}
                    pt={ptype}
                    onClick={() => this.onProblemClick(ptype)}
                    />;
    }

    onProblemClick(ptype) {
        this.setState({
            problems: _.xor(this.state.problems, [ptype]),

        })
    }

    onCounterClick(ptype, e) {
        if (e === -1 && this.state.difficulties[ptype] === 0) return;
        if (e === 1 && this.state.difficulties[ptype] === 9) return;
        this.setState(updateDifficulty(ptype, e));
    }

    renderCounter(ptype) {
        return (
            <div className="counter">
                <div className="difficulty">{this.state.difficulties[ptype]}</div>
                <button className="easier" onClick={() => this.onCounterClick(ptype, -1)}>Easier</button>
                <button className="harder" onClick={() => this.onCounterClick(ptype, 1)}>Harder</button>
            </div>
        )
    }

    render() {
        return (
            <div id="whetstone_body">
                <div className="problem_buttons">
                    <div className="prob_button">
                        <div className="inner_problem">
                            {this.renderButtons('Addition')}                   
                        </div>
                        <div className="inner_problem">
                            {this.renderCounter('Addition')}
                        </div>
                    </div>
                    <div className="prob_button">
                        <div className="inner_problem">
                            {this.renderButtons('Subtraction')}                   
                        </div>
                        <div className="inner_problem">
                            {this.renderCounter('Subtraction')}
                        </div>
                    </div>
                    <div className="prob_button">
                        <div className="inner_problem">
                            {this.renderButtons('Multiplication')}                   
                        </div>
                        <div className="inner_problem">
                            {this.renderCounter('Multiplication')}
                        </div>
                    </div>
                    <div className="prob_button">
                        <div className="inner_problem">
                            {this.renderButtons('Division')}                   
                        </div>
                        <div className="inner_problem">
                            {this.renderCounter('Division')}
                        </div>
                    </div>
                    <div className="prob_button">
                        <div className="inner_problem">
                            {this.renderButtons('Hexadecimal')}                   
                        </div>
                        <div className="inner_problem">
                            {this.renderCounter('Hexadecimal')}
                        </div>
                    </div>
                </div>
                <div className="generate_problems">
                        <button id="gen_prob" onClick={() => this.state.onGenProbClick(this.state.problems, this.state.difficulties)}>Make it happen!</button>
                </div>
                <br/>
                <div className="get_stats">
                        <button id="user_stats" onClick={() => this.state.onGetStatsClick()}>Look at Stats</button>
                </div>
            </div>
        );
    }
}

function updateDifficulty(ptype, e) {
    return function updateD(state, props) {
        const updated = _.cloneDeep(state.difficulties);
        updated[ptype] = updated[ptype] + e;
        return {
            difficulties: updated,
        }
    }
}