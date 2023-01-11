
function resolveAfter2Seconds() {
    return new Promise(resolve => {
      setTimeout(() => {
        resolve('resolved');
      }, 500);
    });
  }

const async_count = async () => { 
    for (let i = 0; i < 3; i++) {
        console.log(i);
        await resolveAfter2Seconds();

    }
    return [0, 5]
}

const count = (i) => {
    console.log(i)
}

async function main() {
    async_count()
        .then((x) => { console.log(`Done ${x[0]} ${x[1]}`); return 3 })
        .then((x) => { console.log("thanks for using ", x)})


    async_count()

}

main()