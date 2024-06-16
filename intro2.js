let str = "aabcd";
let arr = str.split()

const remover = (str) => {
    for (let i = 0; i < str.length; i++) {
        let char = str[i];
        for (let j = i + 1; j < str.length; j++){
            if (char == str[j]) {
                str.split(j, j);
            }

            
        }
       
    }
    console.log(str);
}

remover(str);
