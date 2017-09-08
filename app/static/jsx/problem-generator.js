import _ from 'lodash';


function genProblem(ptype, difficulty) {
    const problems = {
        'Addition': addProblem,
        'Subtraction': subProblem,
        'Multiplication': multProblem,
        'Division': divProblem,
        'Hexadecimal': hexProblem,
    }

    return problems[ptype](difficulty);
}

function getDigits(difficulty) {
    const difA = Math.floor(difficulty / 2) + 1;
    const difB = Math.floor((difficulty - 1) / 2) + 1;

    return [difA, difB];
}

function addProblem(difficulty) {
    const firstOperand = Math.round(Math.random() * 100 * 10 ** difficulty);
    const secondOperand = Math.round(Math.random() * 100 * 10 ** difficulty);

    const question = `${firstOperand} + ${secondOperand}`;
    const answer = firstOperand + secondOperand;

    return [question, answer];
}

function subProblem(difficulty) {
    const firstOperand = Math.round(Math.random() * 100 * 10 ** difficulty);
    const secondOperand = Math.round(Math.random() * 100 * 10 ** difficulty);

    const question = `${firstOperand} - ${secondOperand}`;
    const answer = firstOperand - secondOperand;

    return [question, answer];
}

function multProblem(difficulty) {
    const diffs = getDigits(difficulty);
    const firstPlace = Math.round(Math.random());
    const difA = diffs[firstPlace];
    const difB = diffs[1 - firstPlace];
    const firstOperand = Math.round(Math.random() * 10 ** difA);
    const secondOperand = Math.round(Math.random() * 10 ** difB);

    const question = `${firstOperand} * ${secondOperand}`;
    const answer = firstOperand * secondOperand;

    return [question, answer];
}

function divProblem(difficulty) {
    const diffs = getDigits(difficulty);
    const firstPlace = Math.round(Math.random());
    const difA = diffs[firstPlace];
    const difB = diffs[1 - firstPlace];
    const firstOperand = Math.round(Math.random() * 10 ** difA);
    const secondOperand = Math.round(Math.random() * 10 ** difB);

    const question = `${firstOperand} / ${secondOperand}`;
    const answer = Math.round(firstOperand / secondOperand * 1000) / 1000;

    return [question, answer];
}

function hexProblem(difficulty) {
    let num;
    let targetType;
    let answer;
    const hexMap = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'];
    const direction = Math.random();
    
    if (direction > 0.5) {
        num = _.reduce(_.range(difficulty), (result, n) => {
            const randomHex = hexMap[Math.floor(Math.random() * 16)];
            return result + randomHex;
        }, '');

        targetType = 'decimal';
        let power = num.length - 1;
        answer = 0;

        for(let i = 0; i < num.length; i++) {
            const increase = hexMap.indexOf(num[i]) * 16 ** power;
            answer = answer + increase;
            power = power - 1;
        }
        answer = String(answer);
    } else {
        let remainder;
        num = Math.floor(Math.random() * (10 ** (difficulty + 1)));
        let tempNum = num;
        targetType = 'hexadecimal';
        answer = '';
        while (tempNum / 16 >= 1) {
            remainder = tempNum % 16;
            answer = hexMap[remainder] + answer;
            tempNum = Math.floor(tempNum / 16);
        }
        answer = hexMap[tempNum] + answer;
    }

    const question = `convert ${num} to ${targetType}`;

    return [question, answer];
}



export {
    genProblem,
}