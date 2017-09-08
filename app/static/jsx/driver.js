import React from 'react';
import MainPageButtonSet from './main-page';
import ProblemPageButtonSet from './problem-page';
import StatsPageButtonSet from './stats-page';

class WhetstoneDriver extends React.Component {
    constructor() {
        super();
        this.state = {
            problems: [],
            difficulties: {},
            answer: null,
            page: 'mainPage',
        };
    }

    changePage(page) {
        this.setState({
            page: (this.state.page === page ? 'mainPage' : page),
        });
    }

    onGenProbClick(problems, difficulties) {
        this.setState({
            page: 'problemPage',
            problems: problems,
            difficulties: difficulties,
        })
    }

    onGetStatsClick() {
        this.setState({
            page: 'statsPage',
        });
    }

    render() {
        const mainPage = (
            <div className="problem">
                <div className="problem_select">
                    <MainPageButtonSet
                        onGenProbClick={this.onGenProbClick.bind(this)}
                        onGetStatsClick={this.onGetStatsClick.bind(this)}
                        changePage={this.changePage.bind(this)}/>
                </div>
            </div>
        );

        const problemPage = (
            <ProblemPageButtonSet
                problems={this.state.problems}
                difficulties={this.state.difficulties}
                allDone={() => this.changePage('mainPage')}
                changePage={this.changePage.bind(this)}
                />
        );

        const statsPage = (
            <div className="problem">
                <div className="problem_select">
                    <StatsPageButtonSet
                        changePage={this.changePage.bind(this)}/>
                </div>
            </div>
        );

        const pageMap = {
            'mainPage': mainPage,
            'problemPage': problemPage,
            'statsPage': statsPage,
        };

        return pageMap[this.state.page];
    }
}

ReactDOM.render(
    <WhetstoneDriver />,
    document.getElementById('root')
);