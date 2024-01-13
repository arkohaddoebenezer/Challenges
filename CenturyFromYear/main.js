class Main {
    getCentury(year) {
        return Math.ceil(year / 100);
    }
}

const myObject = new Main();
const year = 2024;
const century = myObject.getCentury(year);

console.log(`Year: ${year} is in the ${century}th century.`);
