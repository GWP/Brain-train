import _ from 'lodash';
import React from 'react';
import { genProblem } from './problem-generator';


export default class ProblemPageButtonSet extends React.Component {
    constructor(props) {
        super();
        this.state = {
            current: null,
            problems: props.problems, // contains ptypes as strings e.g "add"
            problemsToDo: props.problems,
            difficulties: props.difficulties, // key: ptype, value: difficulty
            questions: {}, // key: ptype, value: [probString, answer]
            solved: {}, // key: ptype, value: question and answer e.g `41 + 54 = 95`,
            startTime: Date.now(),
            userAnswer: null,
            correct: null,
            allDone: props.allDone,
        }
    }

    renderProblem(ptype) {
        if (!_.includes(this.state.problems, ptype)) {
            return <div className="problem_button null_prob">{ptype}</div>;
        } else if (this.state.solved[ptype]) {
            return <div className="problem_button null_prob">{this.state.solved[ptype]}</div>;
        } else if (this.state.current !== ptype) {
            return <div className="problem_button pending">pending</div>;
        } else {
            console.log("questions: ", this.state.questions);
            return <div className="problem_button">{this.state.questions[ptype][0]}</div>;
        }

    }

    handleUserInput(event) {
        this.setState({
            userAnswer: event.target.value,
        });
    }

    checkAnswer() {
        console.log('checking answer');
        const answer = this.state.questions[this.state.current][1];
        console.log('User Answer: ', this.state.userAnswer);
        const userAttempt = this.state.current === 'hex' ? this.state.userAnswer.toUpperCase() : parseFloat(this.state.userAnswer, 10);

        if (userAttempt === answer) {
            // find how long it took
            const endTime = Date.now();
            const timeToCorrectAnswer = endTime - this.state.startTime;

            // add the problem to the solved collection with well formed string to display
            const solvedString = this.state.questions[this.state.current][0] + ' = ' + this.state.questions[this.state.current][1];
            const newSolved = _.cloneDeep(this.state.solved);
            newSolved[this.state.current] = solvedString;

            this.setState({
                correct: true,
                solved: newSolved,
            });

            // Construct and send the HTTP request with the problem data
            const probForm = new FormData();
            probForm.append('question', this.state.questions[this.state.current][0]);
            probForm.append('answer', this.state.questions[this.state.current][1]);
            probForm.append('time', timeToCorrectAnswer);
            probForm.append('ptype', this.state.current);

            fetch('/question_and_answer', {
                credentials: 'same-origin',
                method: 'POST',
                body: probForm,
            }).then((response) => {
                setTimeout(() => {
                    if (this.state.problemsToDo == false) {
                        return this.state.allDone();
                    } else {
                        this.setState(nextProblem);
                    }}, 1000);
            })
        } else {
            this.setState({
                correct: false,
            });
            setTimeout(() => {this.setState({
                correct: null,
                userAnswer: null,
            })}, 1000);
        }
    }

    /**
     * An answer box accompanies every question, and is merely hidden if the question is not currently being worked on.
     * 
     * @param {String} ptype 
     */
    renderAnswerBox(ptype) {
        const hiddenAnswerBox = (<div className="inner_problem hidden"></div>);

        const answerBoxAfterUserGuess = (
            <div className="answer_box">
                <input type="text" onChange={null} value={this.state.userAnswer}/>
                <div className="problem_button" onClick={() => this.checkAnswer()}>{(this.state.correct === true ? 'Correct!' : 'Incorrect! Try again!')}</div>
            </div>
        );

        const answerBoxBeforeUserGuess = (
            <div className="answer_box">
                <form onSubmit={() => this.checkAnswer()}>
                    <input type="text" onChange={this.handleUserInput.bind(this)}/>
                    <button type="submit" className="answer_btn">Check</button>
                </form>
            </div>
        );

        if (this.state.current !== ptype) {
            return hiddenAnswerBox;
        } else if (this.state.correct !== null) {
            return answerBoxAfterUserGuess;
        } else {
            return answerBoxBeforeUserGuess;
        }
    }

    /**
     * This is called only once, when the problem set begins.
     */
    initialProb() {
        const ptype = this.state.problemsToDo[0];
        const difficulty = _.get(this.state.difficulties, `${ptype}`);
        const [question, answer] = genProblem(ptype, difficulty);

        this.setState(initQuestion(ptype, question, answer));
        this.setState(addQuestion(ptype, question, answer));
    }


    render() {
        console.log("questions are: ", this.state.questions);
        console.log("problems are: ", this.state.problems);
        console.log("problemsToDo are: ", this.state.problemsToDo);
        console.log("solved is: ", this.state.solved);

        if (this.state.current === null) {
            this.initialProb();
            return null;
        }

        return (
            <div id="whetstone_body">
                <div className="problem_buttons">
                    <div className="prob_button">
                        <div className="inner_problem">
                            {this.renderProblem('Addition')}                   
                        </div>
                        <div className="inner_problem">
                            {this.renderAnswerBox('Addition')}
                        </div>
                    </div>
                    <div className="prob_button">
                        <div className="inner_problem">
                            {this.renderProblem('Subtraction')}                   
                        </div>
                        <div className="inner_problem">
                            {this.renderAnswerBox('Subtraction')}
                        </div>
                    </div>
                    <div className="prob_button">
                        <div className="inner_problem">
                            {this.renderProblem('Multiplication')}                   
                        </div>
                        <div className="inner_problem">
                            {this.renderAnswerBox('Multiplication')}
                        </div>
                    </div>
                    <div className="prob_button">
                        <div className="inner_problem">
                            {this.renderProblem('Division')}                   
                        </div>
                        <div className="inner_problem">
                            {this.renderAnswerBox('Division')}
                        </div>
                    </div>
                    <div className="prob_button">
                        <div className="inner_problem">
                            {this.renderProblem('Hexadecimal')}                   
                        </div>
                        <div className="inner_problem">
                            {this.renderAnswerBox('Hexadecimal')}
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

function initQuestion(ptype, question, answer) {
    return function update(state, props) {
        const newCurrent = ptype;
        const newProblemsToDo = state.problemsToDo.slice(1);

        const newQuestions = {};
        newQuestions[ptype] = [question, answer];

        return {
            current: newCurrent,
            problemsToDo: newProblemsToDo,
            questions: newQuestions,
        }
    }
}

function addQuestion(ptype, question, answer) {
    return function update(state, props) {
        const updated = _.cloneDeep(state.questions);
        updated[ptype] = [question, answer];

        return {
            questions: updated,
        }
    }
}

function nextProblem(state, props) {
    const newCurrent = state.problemsToDo[0];
    const difficulty = _.get(state, `difficulties.${newCurrent}`);
    const [question, answer] = genProblem(newCurrent, difficulty);

    const newQuestions = state.questions;
    newQuestions[newCurrent] = [question, answer];

    return {
        current: newCurrent,
        problemsToDo: state.problemsToDo.slice(1),
        questions: newQuestions,
        startTime: Date.now(),
        correct: null,
        userAnswer: null,
    }
}