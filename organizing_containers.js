let container = [[1, 4],[2,3]];
function organizingContainers(container) {
    const length_container = container.length;

    let balls_count = Array(length_container).fill(0);
    let container_length = [];

    for (let i = 0; i < length_container; i++) {
        for (let y = 0; y < length_container; y++) {
            balls_count[y] += container[i][y];
        }       
    }

    for (let i = 0; i < container.length; i++) {
        const sum = container[i].reduce((acc, curr) => acc + curr, 0);
        container_length.push(sum);
        
    }

    container_length.sort();
    balls_count.sort();
    

    if (JSON.stringify(container_length) === JSON.stringify(balls_count)) {
        return "Possible";
    } else {
        return "Impossible";
    }

}


console.log(organizingContainers(container));

